.PHONY: dev test bench ingest clean build

dev:
	docker compose up --build

dev-light:
	docker compose --profile core up --build

dev-full:
	docker compose --profile monitoring up --build

test:
	npm test --workspaces

bench:
	python3 bench/latency.py
	node bench/retrieval_precision.js || true
	node bench/generation_ttfb.js || true

ingest:
	node scripts/ingest.js

clean:
	docker compose down -v
	rm -rf node_modules services/*/node_modules services/*/dist

build:
	npm run build --workspaces
