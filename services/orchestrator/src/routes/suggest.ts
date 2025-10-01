import { Router } from 'express';
import { Server } from 'socket.io';
import { z } from 'zod';
import { detectIntent, buildPrompt } from '../utils/promptRouter';
import { searchEvidence } from '../clients/retrievalClient';
import { streamGenerate } from '../clients/llmClient';

const requestSchema = z.object({
  transcript: z.string(),
  limit: z.number().min(1).max(5).default(3)
});

export function createSuggestRouter(io: Server): Router {
  const router = Router();

  router.post('/', async (req, res) => {
    const parse = requestSchema.safeParse(req.body ?? {});
    if (!parse.success) {
      return res.status(400).json({ error: 'invalid_request', details: parse.error.flatten() });
    }

    const { transcript, limit } = parse.data;
    const intent = detectIntent(transcript);
    const evidence = await searchEvidence(transcript, limit);

    const prompt = buildPrompt(intent, evidence, transcript);

    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');

    const startTime = Date.now();
    const stream = streamGenerate(prompt);
    let accumulated = '';

    for await (const chunk of stream) {
      accumulated += chunk.token;
      const payload = {
        token: chunk.token,
        done: chunk.done,
        intent,
        evidence,
        latency: Date.now() - startTime
      };
      res.write(`data: ${JSON.stringify(payload)}\n\n`);
      io.of('/overlay').emit('suggestion', {
        suggestions: [
          {
            id: evidence[0]?.id ?? 'template',
            text: accumulated || 'Template suggestion pending evidence',
            confidence: evidence.length ? 0.8 : 0.4,
            evidence: evidence.map(ev => ev.id)
          }
        ]
      });
      if (chunk.done) {
        break;
      }
    }
    res.end();
  });

  return router;
}
