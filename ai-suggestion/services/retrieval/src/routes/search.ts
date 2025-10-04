import { Router } from 'express';
import { z } from 'zod';
import { queryVector, type RetrievalResult } from '../services/vectorStore';
import { searchBM25 } from '../services/bm25Service';
import { rerank, type RerankResult } from '../services/rerankerService';

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
  for (const item of [...dense, ...sparse]) {
    const existing = unionMap.get(item.id);
    if (!existing || item.score > existing.score) {
      unionMap.set(item.id, { ...item });
    }
  }

  const union = Array.from(unionMap.values());
  const reranked: RerankResult[] = (await rerank(query, union)).slice(0, limit);
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
