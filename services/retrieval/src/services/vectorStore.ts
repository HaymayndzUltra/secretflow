import { QdrantClient } from '@qdrant/js-client-rest';
import { embedText } from './embeddingService';
import { logger } from '../utils/logger';

export interface DocumentChunk {
  id: string;
  text: string;
  source: string;
  span: [number, number];
}

export interface RetrievalResult extends DocumentChunk {
  score: number;
  rerankScore?: number;
}

const COLLECTION = process.env.QDRANT_COLLECTION ?? 'call-companion-docs';

const client = new QdrantClient({
  url: process.env.QDRANT_URL ?? 'http://localhost:6333',
  apiKey: process.env.QDRANT_API_KEY
});

export async function ensureCollection(): Promise<void> {
  try {
    await client.getCollections();
    await client.createCollection(COLLECTION, {
      vectors: {
        size: 64,
        distance: 'Cosine'
      }
    });
  } catch (err: any) {
    if (err?.status === 409) {
      logger.debug('Collection exists');
      return;
    }
    if (err?.response?.status === 409) {
      return;
    }
    logger.warn({ err }, 'ensureCollection fallback (offline?)');
  }
}

export async function upsertChunk(chunk: DocumentChunk): Promise<void> {
  const embedding = await embedText(chunk.text);
  try {
    await client.upsert(COLLECTION, {
      wait: false,
      points: [
        {
          id: chunk.id,
          vector: embedding.vector,
          payload: {
            source: chunk.source,
            span: chunk.span,
            model: embedding.model,
            text: chunk.text
          }
        }
      ]
    });
  } catch (err) {
    logger.warn({ err }, 'Upsert failed, caching only');
  }
}

export async function queryVector(text: string, limit = 5): Promise<RetrievalResult[]> {
  const embedding = await embedText(text);
  try {
    const response = await client.search(COLLECTION, {
      vector: embedding.vector,
      limit,
      with_payload: true
    });
    return response
      .filter(result => result.payload)
      .map(result => ({
        id: String(result.id),
        text: String(result.payload?.text ?? ''),
        source: String(result.payload?.source ?? 'unknown'),
        span: (result.payload?.span as [number, number]) ?? [0, 0],
        score: Number(result.score)
      }));
  } catch (err) {
    logger.warn({ err }, 'Vector search offline fallback');
    return [];
  }
}
