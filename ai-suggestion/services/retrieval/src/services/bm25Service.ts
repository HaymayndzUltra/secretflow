import winkBM25, {
  type TokenPrepTask,
  type WinkDocument
} from 'wink-bm25-text-search';
import type { DocumentChunk, RetrievalResult } from './vectorStore';

const bm25 = winkBM25();
let isReady = false;

export function resetBM25(): void {
  bm25.reset();
  bm25.defineConfig({
    fldWeights: { text: 1 }
  });
  const lowercase: TokenPrepTask = token => token.toLowerCase();
  bm25.definePrepTasks([lowercase]);
  isReady = true;
}

export function indexChunk(chunk: DocumentChunk): void {
  if (!isReady) {
    resetBM25();
  }
  bm25.addDoc(
    {
      id: chunk.id,
      text: chunk.text,
      source: chunk.source,
      span: chunk.span
    },
    chunk.id
  );
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
    const doc = bm25.doc(docId) as WinkDocument;
    const text = typeof doc.text === 'string' ? doc.text : '';
    const source = typeof doc.source === 'string' ? doc.source : 'unknown';
    const spanValue = doc.span;
    let span: [number, number] = [0, 0];
    if (Array.isArray(spanValue) && spanValue.length === 2) {
      const [start, end] = spanValue;
      span = [Number(start), Number(end)];
    }
    const chunk: RetrievalResult = {
      id: String(docId),
      text,
      source,
      span,
      score: Number(score)
    };
    return chunk;
  });
}
