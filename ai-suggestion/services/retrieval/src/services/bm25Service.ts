import winkBM25 from 'wink-bm25-text-search';
import { DocumentChunk } from './vectorStore';

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

export function searchBM25(query: string, limit = 5): DocumentChunk[] {
  if (!isReady) {
    resetBM25();
  }
  const results = bm25.search(query, limit);
  return results.map(result => ({
    id: String(result[0]),
    text: String(bm25.doc(result[0]).text),
    source: String(bm25.doc(result[0]).source),
    span: bm25.doc(result[0]).span as [number, number]
  }));
}
