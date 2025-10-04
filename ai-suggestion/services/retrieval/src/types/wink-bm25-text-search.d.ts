declare module 'wink-bm25-text-search' {
  export type PrepTask = (token: string, index: number, tokens: string[]) => string | string[] | false | null | undefined;

  export interface WinkDoc {
    id: string | number;
    text: string;
    [key: string]: unknown;
  }

  export type SearchResultTuple = [string | number, number];

  export interface WinkBM25 {
    reset(): void;
    defineConfig(config: { fldWeights: Record<string, number> }): void;
    definePrepTasks(tasks: PrepTask[]): void;
    addDoc(doc: Record<string, unknown>, id: string | number): void;
    consolidate(): void;
    search(query: string, limit?: number): SearchResultTuple[];
    doc(id: string | number): Record<string, unknown> | undefined;
  }

  function winkBM25(): WinkBM25;

  export = winkBM25;
}
