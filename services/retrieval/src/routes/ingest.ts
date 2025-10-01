import { Router } from 'express';
import { z } from 'zod';
import { ingestDirectory } from '../services/ingestionService';

const router = Router();

const bodySchema = z.object({
  directory: z.string().default('./docs')
});

router.post('/', async (req, res) => {
  const parse = bodySchema.safeParse(req.body ?? {});
  if (!parse.success) {
    return res.status(400).json({ error: 'invalid_request', details: parse.error.flatten() });
  }

  try {
    const result = await ingestDirectory(parse.data.directory);
    return res.json({ status: 'ok', result });
  } catch (err: any) {
    return res.status(500).json({ error: 'ingest_failed', message: err?.message ?? 'unknown error' });
  }
});

export default router;
