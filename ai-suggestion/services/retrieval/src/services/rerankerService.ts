import { createHash } from 'crypto';
import { RetrievalResult } from './vectorStore';

export interface RerankResult extends RetrievalResult {
  rerankScore: number;
}

function fingerprint(text: string): number[] {
  const hash = createHash('sha256').update(text).digest();
  return Array.from(hash.slice(0, 32)).map(byte => byte / 255);
}

export async function rerank(query: string, candidates: RetrievalResult[]): Promise<RerankResult[]> {
  const queryVector = fingerprint(query);
  return candidates
    .map(candidate => {
      const candidateVector = fingerprint(candidate.text);
      const score = candidateVector.reduce((acc, value, index) => acc + value * (queryVector[index] ?? 0), 0);
      return { ...candidate, rerankScore: score };
    })
    .sort((a, b) => b.rerankScore - a.rerankScore);
}
