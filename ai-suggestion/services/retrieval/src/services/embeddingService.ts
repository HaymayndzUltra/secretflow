import { createHash } from 'crypto';
import { logger } from '../utils/logger';

export interface EmbeddingResult {
  vector: number[];
  model: string;
}

const MODEL = process.env.EMBEDDING_MODEL ?? 'bge-large-en-v1.5';

export async function embedText(text: string): Promise<EmbeddingResult> {
  if (!text.trim()) {
    return { vector: [], model: MODEL };
  }

  if (process.env.ALLOW_GPU !== 'false') {
    logger.debug({ length: text.length }, 'Embedding via GPU stub');
  }

  const hash = createHash('sha256').update(text).digest();
  const vector = Array.from(hash.slice(0, 64)).map(byte => (byte / 255) * 2 - 1);
  return { vector, model: MODEL };
}
