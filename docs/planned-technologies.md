# Planned Technologies

One explainer per technology used or planned for TDOP (Phase 0 prompt,
section 2). "Status" says whether the technology is **in use** today or
**planned** for a later phase. Decisions referenced: DEC-005 (stack of
record), DEC-009 (edge topology), DEC-010 (mobile stack).

## Backend

| Technology | Status | Explainer |
| --- | --- | --- |
| Java 21 | in use | LTS language for the backend; records/sealed types and virtual threads fit the API workload. |
| Spring Boot 3.3 | in use | Opinionated framework giving REST, dependency injection, configuration, and actuator endpoints with minimal boilerplate. |
| Spring Security + JWT | in use | Authentication/authorization: stateless JWT access tokens, refresh tokens persisted in the database, BCrypt password hashing. |
| Spring Data JPA | in use | Repository layer over PostgreSQL with Hibernate; typed queries and paging for all domain access. |
| Flyway | in use | Versioned SQL migrations (`db/migration`) applied at startup - schema history is code-reviewed like any other change. |
| Maven | in use | Build tool (`mvn -B test` in CI); dependency management for the JVM ecosystem. |
| springdoc-openapi | in use | Generates the OpenAPI/Swagger UI from code at `/api/v1`, keeping API docs in sync with handlers. |
| Nginx | in use | Origin reverse proxy in `TDOP-backend/nginx.conf` (DEC-009): TLS termination support, buffering, rate limiting in front of the JVM. |
| SLF4J + Logback | in use | Structured logging to console and rolling files; log level configured per environment. |

## Frontend

| Technology | Status | Explainer |
| --- | --- | --- |
| React 18 | in use | Component model and hooks for the SPA; large ecosystem for form/state libraries. |
| TypeScript 5 | in use | Static types across the SPA; catches API-contract drift at compile time. |
| Vite 5 | in use | Dev server and bundler with fast HMR; production build is plain static files served by nginx. |
| Tailwind CSS 3 | in use | Utility-first styling: design tokens (TDOP palette) live in the config, no dead CSS. |
| React Router 6 | in use | Client-side routing (hash/browser router) for the SPA views. |
| TanStack Query | in use | Server-state cache: retries, invalidation, and loading states for all API calls. |
| Zustand | in use | Minimal client-side store for session/UI state that does not belong on the server. |
| React Hook Form | in use | Performant forms with validation wiring for seeker/org flows. |
| i18next | in use | English + Swahili localization; keys are the source of truth for user-facing strings. |
| Vitest + React Testing Library | in use | Jest-compatible unit tests against components' accessible behavior; 36 tests run in CI. |
| ESLint | in use | Lint gate in CI (`npm run lint`, blocking) with `@typescript-eslint` rules. |

## Mobile

| Technology | Status | Explainer |
| --- | --- | --- |
| Flutter | planned | Single Dart codebase for Android + iOS (DEC-010); hot reload and widget tests fit the shared TDOP UI. |
| Dart | planned | Language of the Flutter app; same strong-typing culture as the TypeScript side. |
| flutter_dotenv-style config | planned | Will consume `.env.example` (API base URL, environment flag) when the app scaffold lands. |

## Data and storage

| Technology | Status | Explainer |
| --- | --- | --- |
| PostgreSQL 16 | in use | Primary relational store; relational integrity for orgs/opportunities/applications; JSONB for flexible profile fields. |
| Redis | planned | Caching and token/refresh-session revocation (phase: performance/reliability); also rate-limit backing. |
| Local filesystem uploads | in use | File storage for avatars/documents behind a path-traversal-safe API; object storage is a later decision. |

## Infrastructure, edge, and delivery

| Technology | Status | Explainer |
| --- | --- | --- |
| Docker | in use | Reproducible builds (multi-stage, non-root) for backend and frontend images. |
| Docker Compose | in use | One-command local stack (PostgreSQL, backend, frontend, Adminer) and the deployment baseline for `TDOP-infra`. |
| Cloudflare | in use | Production edge: DNS, TLS, CDN, and WAF in front of origin (DEC-009); no extra paid load balancer. |
| GitHub Actions | in use | CI for all five repositories (install -> lint -> build -> test) plus board automation. |
| Dependabot | in use | Weekly update PRs per stack ecosystem + github-actions in every repository. |

## Intelligence and communications (future)

| Technology | Status | Explainer |
| --- | --- | --- |
| Machine-learning matching | planned | Phase 7 AI features: skill/interest embeddings to rank opportunities (starts as heuristics, evolves). |
| Elasticsearch | planned | Full-text search once Postgres FTS outgrows the use case (title/description/tags today). |
| WhatsApp / SMS gateways | planned | Phase 6 integrations for deadline reminders where email does not reach users. |
| Payment provider (M-Pesa etc.) | planned | Phase 6/25 subscriptions; provider chosen by a future decision record. |
| SMTP email delivery | in use | Verification, reset, notifications, weekly digest via the configured mail service. |
