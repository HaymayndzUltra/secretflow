import http from 'http';
import express from 'express';
import cors from 'cors';
import client from 'prom-client';
import ingestRoute from './routes/ingest';
import searchRoute from './routes/search';
import { logger } from './utils/logger';

const app = express();
app.use(cors());
app.use(express.json({ limit: '2mb' }));

const register = new client.Registry();
client.collectDefaultMetrics({ register });

app.use('/ingest', ingestRoute);
app.use('/search', searchRoute);

app.get('/health', (_req, res) => {
  res.json({ status: 'ok', mode: process.env.ALLOW_GPU === 'false' ? 'cpu-stub' : 'gpu-preferred' });
});

app.get('/metrics', async (_req, res) => {
  res.setHeader('Content-Type', register.contentType);
  res.send(await register.metrics());
});

const httpServer = http.createServer(app);
const port = Number(process.env.PORT ?? 7002);

httpServer.listen(port, () => {
  logger.info({ port }, 'Retrieval service ready');
});
