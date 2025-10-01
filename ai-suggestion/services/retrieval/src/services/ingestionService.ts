import fs from 'fs';
import path from 'path';
import { randomUUID } from 'crypto';
import { finalizeBM25, indexChunk } from './bm25Service';
import { DocumentChunk, ensureCollection, upsertChunk } from './vectorStore';
import { logger } from '../utils/logger';

function chunkText(text: string, spanSize = 512): { text: string; span: [number, number] }[] {
  const words = text.split(/\s+/);
  const chunks: { text: string; span: [number, number] }[] = [];
  for (let i = 0; i < words.length; i += spanSize) {
    const part = words.slice(i, i + spanSize).join(' ');
    chunks.push({ text: part, span: [i, i + spanSize] });
  }
  return chunks;
}

export interface IngestionResult {
  processed: number;
  sources: string[];
}

export async function ingestDirectory(dir: string): Promise<IngestionResult> {
  await ensureCollection();
  const resolved = path.resolve(dir);
  const files = fs.readdirSync(resolved);
  let processed = 0;
  const sources: string[] = [];

  for (const file of files) {
    const fullPath = path.join(resolved, file);
    if (fs.statSync(fullPath).isDirectory()) {
      continue;
    }
    const text = fs.readFileSync(fullPath, 'utf-8');
    const docId = randomUUID();
    const chunks = chunkText(text);
    for (const chunk of chunks) {
      const chunkRecord: DocumentChunk = {
        id: `${docId}-${chunk.span[0]}`,
        text: chunk.text,
        source: fullPath,
        span: chunk.span
      };
      indexChunk(chunkRecord);
      await upsertChunk(chunkRecord);
      processed += 1;
    }
    sources.push(fullPath);
  }

  finalizeBM25();
  logger.info({ processed, sources }, 'Ingestion completed');
  return { processed, sources };
}
