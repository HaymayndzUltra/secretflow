# Benchmark Playbook

The `bench/` folder includes lightweight harnesses that simulate live-call workloads without requiring network access or model weights. Benchmarks focus on latency budgets (ASR, retrieval, LLM TTFB, overlay render) and retrieval quality.

## Available Scripts

- `bench/latency.py` – synthetic latency sampler aligned with target budgets.
- `bench/retrieval_precision.js` – evaluates precision@k against the fixture corpus (see below).
- `bench/generation_ttfb.js` – drives the orchestrator SSE endpoint and records TTFB and completion latency.

## Running Benchmarks

```bash
# Ensure dependencies are installed
npm install
pip install -r requirements.txt  # optional if python deps evolve

# Run all Node/TS tests and bench harnesses
make bench

# Individual runs
node bench/retrieval_precision.js
node bench/generation_ttfb.js
python bench/latency.py
```

All scripts default to stub mode so they run without GPU models. When GPU models are available, set the environment variables in `.env` to point to local model weights.

## Fixture Corpus

A tiny fixture corpus lives in `docs/fixtures/` (created during ingestion tests). Use `make ingest` to load it into Qdrant and the BM25 cache.

## Metrics Collected

- `asr_partials`, `retrieval`, `llm_ttfb`, `overlay_render` latency estimates (ms)
- Precision@k for seeded queries (default k=3)
- Suggestion TTFB and full response latency (ms)

Benchmarks emit JSON payloads so they can be scraped by CI or Grafana Loki in the future.
