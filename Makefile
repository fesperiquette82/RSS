.PHONY: up down logs seed test-api test-mobile lint format

up:
	docker compose up --build -d

down:
	docker compose down -v

logs:
	docker compose logs -f api

seed:
	docker compose exec api python -m app.seed

test-api:
	cd apps/api && pytest -q

test-mobile:
	cd apps/mobile && npm test -- --runInBand

lint:
	cd apps/api && ruff check . && black --check .
	cd apps/mobile && npm run lint

format:
	cd apps/api && black .
	cd apps/mobile && npm run format
