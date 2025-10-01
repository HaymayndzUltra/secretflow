import http from 'http';
import express from 'express';
import cors from 'cors';
import client from 'prom-client';
import { Server } from 'socket.io';
import { createSuggestRouter } from './routes/suggest';
import telemetryRoute, { telemetryMetrics } from './routes/telemetry';
import { logger } from './utils/logger';

const app = express();
app.use(cors());
app.use(express.json({ limit: '1mb' }));

const register = new client.Registry();
client.collectDefaultMetrics({ register });
register.registerMetric(telemetryMetrics.acceptanceGauge);
register.registerMetric(telemetryMetrics.latencyHistogram);

const httpServer = http.createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: '*'
  }
});

io.of('/overlay');

app.use('/suggest', createSuggestRouter(io));
app.post('/telemetry', telemetryRoute);

app.get('/health', (_req, res) => {
  res.json({ status: 'ok' });
});

app.get('/metrics', async (_req, res) => {
  res.setHeader('Content-Type', register.contentType);
  res.send(await register.metrics());
});

const port = Number(process.env.PORT ?? 7003);

httpServer.listen(port, () => {
  logger.info({ port }, 'Orchestrator ready');
});
