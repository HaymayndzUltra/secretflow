#!/usr/bin/env node
const axios = require('axios');

const seeds = [
  {
    query: 'integration strategy',
    expected: ['doc-1']
  }
];

async function main() {
  const url = process.env.RETRIEVAL_URL ?? 'http://localhost:7002';
  const { data } = await axios.post(`${url}/search`, { query: seeds[0].query, limit: 3 });
  const results = (data.results ?? []).map(item => item.id);
  const precision = seeds[0].expected.filter(id => results.includes(id)).length / Math.max(results.length, 1);
  console.log(JSON.stringify({ precision, results }, null, 2));
}

main().catch(err => {
  console.error('Precision bench failed', err.message);
  process.exit(1);
});
