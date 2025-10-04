import winkBM25 from 'wink-bm25-text-search';
import { DocumentChunk, RetrievalResult } from './vectorStore';

const bm25 = winkBM25();
let isReady = false;

export function resetBM25(): void {
  bm25.reset();
  bm25.defineConfig({
    fldWeights: { text: 1 }
  });
  bm25.definePrepTasks([token => token.toLowerCase()]);
  isReady = true;
}

export function indexChunk(chunk: DocumentChunk): void {
  if (!isReady) {
    resetBM25();
  }
  bm25.addDoc({
    id: chunk.id,
    text: chunk.text,
    source: chunk.source,
    span: chunk.span
  }, chunk.id);
}

export function finalizeBM25(): void {
  if (!isReady) {
    resetBM25();
  }
  bm25.consolidate();
}

export function searchBM25(query: string, limit = 5): RetrievalResult[] {
  if (!isReady) {
    resetBM25();
  }
  const results = bm25.search(query, limit);
  return results.map(([docId, score]) => {
    const doc = bm25.doc(docId) as DocumentChunk | undefined;
    return {
      id: String(docId),
      text: doc?.text ?? '',
      source: doc?.source ?? 'unknown',
      span: doc?.span ?? [0, 0],
      score: Number(score ?? 0)
    };
  });
}
