import { Router } from 'express';
import { z } from 'zod';
import { queryVector } from '../services/vectorStore';
import { searchBM25 } from '../services/bm25Service';
import { rerank } from '../services/rerankerService';

const router = Router();

const querySchema = z.object({
  query: z.string(),
  limit: z.number().min(1).max(10).default(5)
});

router.post('/', async (req, res) => {
  const parse = querySchema.safeParse(req.body);
  if (!parse.success) {
    return res.status(400).json({ error: 'invalid_request', details: parse.error.flatten() });
  }

  const { query, limit } = parse.data;
  const [dense, sparse] = await Promise.all([queryVector(query, limit), Promise.resolve(searchBM25(query, limit))]);
  const unionMap = new Map<string, any>();
  [...dense, ...sparse].forEach(item => {
    if (!unionMap.has(item.id)) {
      unionMap.set(item.id, { ...item, score: item.score ?? 0 });
    }
  });
  const union = Array.from(unionMap.values());
  const reranked = await rerank(query, union).slice(0, limit);
  res.json({
    status: 'ok',
    results: reranked,
    diagnostics: {
      denseCount: dense.length,
      sparseCount: sparse.length,
      reranked: reranked.length
    }
  });
});

export default router;
