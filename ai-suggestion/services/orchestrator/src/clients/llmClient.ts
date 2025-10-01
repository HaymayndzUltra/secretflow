import axios from 'axios';
import { Readable } from 'stream';

const primaryModel = process.env.PRIMARY_MODEL ?? 'qwen2.5:14b-instruct';
const fallbackModel = process.env.FALLBACK_MODEL ?? 'llama3.2:8b';

export interface GenerationChunk {
  token: string;
  done: boolean;
}

export async function *streamGenerate(prompt: string): AsyncGenerator<GenerationChunk> {
  const baseURL = process.env.OLLAMA_URL ?? 'http://localhost:11434';
  const models = [primaryModel, fallbackModel];
  for (const model of models) {
    try {
      const response = await axios.post(
        `${baseURL}/api/generate`,
        {
          model,
          prompt,
          stream: true
        },
        { responseType: 'stream', timeout: 5000 }
      );
      const stream = response.data as Readable;
      for await (const chunk of stream) {
        const text = chunk.toString();
        yield { token: text, done: false };
      }
      return;
    } catch (err) {
      if (model === models[models.length - 1]) {
        yield { token: 'LLM unavailable, using template response.', done: true };
      }
    }
  }
  yield { token: '', done: true };
}
