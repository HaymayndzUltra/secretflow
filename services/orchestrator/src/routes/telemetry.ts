import { Router } from 'express';
import { z } from 'zod';
import client from 'prom-client';

const router = Router();

const acceptanceGauge = new client.Gauge({
  name: 'assistant_acceptance_rate',
  help: 'Suggestion acceptance rate',
  registers: []
});

const latencyHistogram = new client.Histogram({
  name: 'assistant_latency_ms',
  help: 'Suggestion latency histogram',
  buckets: [100, 200, 400, 600, 800],
  registers: []
});

const bodySchema = z.object({
  accepted: z.boolean(),
  latency: z.number().nonnegative()
});

router.post('/', (req, res) => {
  const parse = bodySchema.safeParse(req.body);
  if (!parse.success) {
    return res.status(400).json({ error: 'invalid_request' });
  }
  latencyHistogram.observe(parse.data.latency);
  acceptanceGauge.set(parse.data.accepted ? 1 : 0);
  res.json({ status: 'ok' });
});

export const telemetryMetrics = { acceptanceGauge, latencyHistogram };

export default router;
