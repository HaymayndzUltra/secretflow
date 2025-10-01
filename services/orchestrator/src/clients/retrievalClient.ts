import axios from 'axios';

const baseURL = process.env.RETRIEVAL_URL ?? 'http://localhost:7002';

export interface Evidence {
  id: string;
  text: string;
  source: string;
  span: [number, number];
  rerankScore: number;
}

export async function searchEvidence(query: string, limit = 5): Promise<Evidence[]> {
  try {
    const response = await axios.post(`${baseURL}/search`, { query, limit }, { timeout: 200 });
    return response.data.results ?? [];
  } catch (err) {
    return [];
  }
}
