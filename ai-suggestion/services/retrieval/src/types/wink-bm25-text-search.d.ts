declare module 'wink-bm25-text-search' {
  export type TokenPrepTask = (
    token: string,
    index: number,
    tokens: string[]
  ) => string | false | undefined;

  export type SearchResult = [string | number, number];

  export interface WinkDocument {
    [key: string]: unknown;
  }

  export interface WinkBM25 {
    reset(): void;
    defineConfig(config: { fldWeights: Record<string, number> }): void;
    definePrepTasks(tasks: TokenPrepTask[]): void;
    addDoc(doc: WinkDocument, id: string | number): void;
    consolidate(): void;
    search(query: string, limit?: number): SearchResult[];
    doc(id: string | number): WinkDocument;
  }

  export default function winkBM25(): WinkBM25;
}
