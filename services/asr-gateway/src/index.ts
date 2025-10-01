import http from 'http';
import express from 'express';
import cors from 'cors';
import { Server } from 'socket.io';
import client from 'prom-client';
import { ASRPipeline } from './pipelines/asrPipeline';
import { logger } from './utils/logger';

const app = express();
app.use(cors());
app.use(express.json({ limit: '2mb' }));

const register = new client.Registry();
client.collectDefaultMetrics({ register });

const partialHistogram = new client.Histogram({
  name: 'asr_partial_latency_ms',
  help: 'Latency for emitting ASR partials',
  buckets: [50, 100, 150, 200, 400]
});
register.registerMetric(partialHistogram);

const sessionGauge = new client.Gauge({
  name: 'asr_active_sessions',
  help: 'Active ASR sessions'
});
register.registerMetric(sessionGauge);

const httpServer = http.createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: '*'
  },
  path: '/webrtc'
});

app.get('/health', (_req, res) => {
  res.json({ status: 'ok', mode: process.env.FWHISPER_PATH ? 'gpu' : 'stub' });
});

app.get('/metrics', async (_req, res) => {
  res.setHeader('Content-Type', register.contentType);
  res.send(await register.metrics());
});

const sessionPipelines = new Map<string, ASRPipeline>();

io.of('/ingress').on('connection', socket => {
  const sessionId = socket.handshake.query.sessionId?.toString() ?? socket.id;
  logger.info({ sessionId }, 'WebRTC ingress connection');
  const pipeline = new ASRPipeline(sessionId);
  sessionPipelines.set(sessionId, pipeline);
  sessionGauge.inc();

  const lastEmit = new Map<string, number>();

  const emitSegment = (type: 'partial' | 'final', payload: any) => {
    const now = Date.now();
    const key = `${type}-${payload.id}`;
    if (!lastEmit.has(key)) {
      partialHistogram.observe(now - payload.end);
    }
    lastEmit.set(key, now);
    socket.emit(type, payload);
  };

  pipeline.on('partial', segment => emitSegment('partial', segment));
  pipeline.on('final', segment => emitSegment('final', segment));
  pipeline.on('diarization', speakerMap => socket.emit('diarization', speakerMap));
  pipeline.on('error', err => {
    logger.error({ err, sessionId }, 'ASR pipeline error');
    socket.emit('error', { message: err.message });
  });

  socket.on('audio-chunk', (payload: { pcm16: number[]; timestamp: number }) => {
    const frameStart = Date.now();
    try {
      const frame = {
        pcm16: Int16Array.from(payload.pcm16),
        timestamp: payload.timestamp
      };
      pipeline.acceptFrame(frame);
      const latency = Date.now() - frameStart;
      if (latency > 200) {
        socket.emit('lag-warning', { latency });
      }
    } catch (err) {
      logger.error({ err, sessionId }, 'Failed to process audio chunk');
      socket.emit('error', { message: 'ASR processing failed' });
    }
  });

  socket.on('disconnect', reason => {
    logger.info({ sessionId, reason }, 'WebRTC ingress disconnected');
    pipeline.close();
    sessionPipelines.delete(sessionId);
    sessionGauge.dec();
  });

  socket.emit('ready', {
    diarization: pipeline.listenerCount('diarization') > 0,
    vadThreshold: process.env.VAD_THRESHOLD ?? 0.6
  });
});

const port = Number(process.env.PORT ?? 7001);
httpServer.listen(port, () => {
  logger.info({ port }, 'ASR gateway ready');
});
