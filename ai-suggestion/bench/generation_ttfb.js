#!/usr/bin/env node
const axios = require('axios');

async function main() {
  const url = process.env.ORCHESTRATOR_URL ?? 'http://localhost:7003';
  const start = Date.now();
  const response = await axios.post(`${url}/suggest`, { transcript: 'Need integration guidance.' }, { responseType: 'stream' });
  const stream = response.data;
  let firstChunk = true;
  stream.on('data', () => {
    if (firstChunk) {
      const ttfb = Date.now() - start;
      console.log(JSON.stringify({ ttfb }, null, 2));
      firstChunk = false;
    }
  });
  stream.on('end', () => process.exit(0));
}

main().catch(err => {
  console.error('Generation bench failed', err.message);
  process.exit(1);
});
