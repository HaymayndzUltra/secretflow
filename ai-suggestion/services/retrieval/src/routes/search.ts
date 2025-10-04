import { Router } from 'express';
import { z } from 'zod';
import { queryVector, RetrievalResult } from '../services/vectorStore';
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
  const [dense, sparse] = await Promise.all([
    queryVector(query, limit),
    Promise.resolve(searchBM25(query, limit))
  ]);

  const unionMap = new Map<string, RetrievalResult>();
  [...dense, ...sparse].forEach(item => {
    const existing = unionMap.get(item.id);
    if (!existing) {
      unionMap.set(item.id, { ...item, score: item.score ?? 0 });
      return;
    }
    const score = Math.max(existing.score ?? 0, item.score ?? 0);
    unionMap.set(item.id, { ...existing, ...item, score });
  });

  const union = Array.from(unionMap.values());
  const reranked = (await rerank(query, union)).slice(0, limit);
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
