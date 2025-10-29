# Variables
BACKEND_DIR := "backend"
FRONTEND_DIR := "frontend"
DOCKER_COMPOSE := "docker compose"

# Help
help:
    @echo "Available commands:"
    @just --list

setup: ## Setup the project
    cd {{FRONTEND_DIR}} && pnpm install
    cd {{BACKEND_DIR}} && uv sync
    pre-commit install -c .pre-commit-config.yaml

# Backend commands
start-backend: ## Start the backend server with FastAPI and hot reload
	cd {{BACKEND_DIR}} && ./start.sh

test-backend ARGS="": ## Run backend tests using pytest
    cd {{BACKEND_DIR}} && uv run pytest {{ARGS}}

# Frontend commands
start-frontend: ## Start the frontend server with pnpm and hot reload
    cd {{FRONTEND_DIR}} && ./start.sh

typecheck: ## Run TypeScript type checking
    cd {{FRONTEND_DIR}} && pnpm run typecheck

# Development commands
dev: ## Start both backend and frontend servers concurrently
    @echo "Starting backend and frontend servers..."
    cd {{FRONTEND_DIR}} && ./start.sh & cd {{BACKEND_DIR}} && ./start.sh

lint: ## Run linting for both backend and frontend
    cd {{BACKEND_DIR}} && uv run ruff check . --fix
    cd {{FRONTEND_DIR}} && pnpm run lint:fix

format: ## Run formatting checks for both backend and frontend
    cd {{BACKEND_DIR}} && uv run ruff format --check .
    cd {{FRONTEND_DIR}} && pnpm run format

test: ## Run tests for both backend and frontend
    cd {{BACKEND_DIR}} && uv run pytest
    cd {{FRONTEND_DIR}} && pnpm run test

test-e2e: ## Run E2E tests for frontend
    cd {{FRONTEND_DIR}} && pnpm run test:e2e

generate-client: ## Generate OpenAPI schema and regenerate frontend client
	@echo "Generating OpenAPI schema..."
	cd {{BACKEND_DIR}} && uv run python -m commands.generate_openapi_schema
	@echo "Regenerating frontend client..."
	cd {{FRONTEND_DIR}} && pnpm run generate-client


## Docker commands
docker-up-db: ## Start the database
    {{DOCKER_COMPOSE}} up -d db

docker-up-test-db: ## Start the test database
  {{DOCKER_COMPOSE}} up -d db_test

docker-migrate: ## Run database migrations using Alembic
    {{DOCKER_COMPOSE}} run --rm backend alembic upgrade head

docker-create-migration MESSAGE="": ## Create a new migration. Usage: just create-migration MESSAGE="add scenarios table"
    {{DOCKER_COMPOSE}} run --rm backend alembic revision --autogenerate -m "{{MESSAGE}}"
