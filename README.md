## Next.js FastAPI Template


The Next.js FastAPI Template provides a solid foundation for scalable, high-performance web applications, following clean architecture and best practices. It simplifies development by integrating FastAPI, Pydantic, and Next.js with TypeScript and Zod, ensuring end-to-end type safety and schema validation between frontend and backend.

The FastAPI backend supports fully asynchronous operations, optimizing database queries, API routes, and test execution for better performance. Deployment is seamless, with both backend and frontend fully deployable to Vercel, enabling quick product releases with minimal configuration.

### Key features
✔ End-to-end type safety – Automatically generated typed clients from the OpenAPI schema ensure seamless API contracts between frontend and backend.

✔ Hot-reload updates – The client updates automatically when backend routes change, keeping FastAPI and Next.js in sync.

✔ Versatile foundation – Designed for MVPs and production-ready applications, with a pre-configured authentication system and API layer.

✔ Quick deployment – Deploys a full-stack application—including authentication flow and a dashboard—on Vercel in just a few steps.

✔ Production-ready authentication – Includes a pre-configured authentication system and dashboard interface, allowing you to immediately start development with user management features.

## Technology stack
This template features a carefully selected set of technologies to ensure efficiency, scalability, and ease of use:

- Zod + TypeScript – Type safety and schema validation across the stack.
- fastapi-users – Complete authentication system with:
    - Secure password hashing
    - JWT authentication
- Email-based password recovery
- shadcn/ui – Prebuilt React components with Tailwind CSS.
- OpenAPI-fetch – Fully typed client generation from the OpenAPI schema.
- UV – Simplified dependency management and packaging.
- Docker Compose – Consistent environments for development and production.
- Pre-commit hooks – Automated code linting, formatting, and validation before commits.
- Vercel Deployment – Serverless backend and scalable frontend, deployable with minimal configuration.
- PostgreSQL with SQLAlchemy and Alembic – Robust database management and migrations.
- Pytest and Playwright – Comprehensive testing for backend and end-to-end scenarios.
- GitHub Actions – CI/CD pipelines for automated testing and deployment.
- Just - Command runner – Simplified task execution with a `Justfile`.

## Getting Started

### Installing and Activating Pre-Commit Hooks¶
To activate pre-commit hooks, run the following commands for each configuration file:

For the local configuration file:

`pre-commit install -c .pre-commit-config.yaml`

Running Pre-Commit Checks¶
To manually run the pre-commit checks on all files, use:

`pre-commit run --all-files -c .pre-commit-config.yaml`

or

`pre-commit run --all-files -c .pre-commit-config.docker.yaml``

Updating Pre-Commit Hooks

To update the hooks to their latest versions, run:

`pre-commit autoupdate`


## End-to-end tests

The Playwright test suite lives under `frontend/e2e` and validates the authentication flow from the browser perspective. To execute the tests locally:

1. Ensure the FastAPI backend is running and reachable at `http://127.0.0.1:8000` (or export `PLAYWRIGHT_API_BASE_URL` with the correct address).
2. Install the Playwright browsers once with `pnpm exec playwright install --with-deps`.
3. From `frontend`, run `pnpm test:e2e`.

You can override the frontend URL Playwright uses by exporting `PLAYWRIGHT_BASE_URL` or the port via `PLAYWRIGHT_WEB_PORT`.



*Disclaimer: This project is not affiliated with Vercel.*
