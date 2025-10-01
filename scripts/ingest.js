#!/usr/bin/env node
const axios = require('axios');

const directory = process.argv[2] ?? './docs';

async function main() {
  const url = process.env.RETRIEVAL_URL ?? 'http://localhost:7002';
  const response = await axios.post(`${url}/ingest`, { directory });
  console.log('Ingestion complete:', response.data);
}

main().catch(err => {
  console.error('Ingestion failed', err.message);
  process.exit(1);
});
