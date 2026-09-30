# Development Guide — TDOP

**Project:** Tanzania Digital Opportunity Platform (TDOP)

This is the central engineering guide for TDOP. It defines how the project is built,
reviewed, tested, documented, released — and how tasks move through the Kanban.
It is written for the project's actual stack; do not assume tools that are not
listed here.

**Companion documents**

| Document | Role |
|---|---|
| [`PROJECT_MANAGEMENT.md`](PROJECT_MANAGEMENT.md) | **Live source of truth**: phase, task, session, logs |
| [`TASK_BREAKDOWN.md`](TASK_BREAKDOWN.md) | Master Kanban (177 tasks) + all 33 phase boards |
| [`EXISTING_IMPLEMENTATION_AUDIT.md`](EXISTING_IMPLEMENTATION_AUDIT.md) | Inventory of pre-existing code |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution workflow, branches, PRs, DoR/DoD |
| [`SECURITY.md`](SECURITY.md) | Vulnerability reporting and disclosure |
| [`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md) | Binding technical security rules |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Community behavior |
| [`CHANGELOG.md`](CHANGELOG.md) | Change history (never silently omit changes) |
| `README.md` | This repository's index and orientation |
| `README_PRD.md` | Product requirements |
| `Specs/TDOP_MASTER_SPEC.md` | Architecture and implementation specification |

**Live Kanban board (mirrors the tracker):**
https://github.com/orgs/Tanzanian-Opportunities/projects/1

---

## 1. Development lifecycle

Every change follows this lifecycle:

```text
Planning            → task defined in PROJECT_MANAGEMENT.md (phase, DoR)
   ↓
Implementation      → branch, code, tests, docs written together
   ↓
Code Review         → pull request, reviewed against standards
   ↓
Testing             → automated suites + targeted manual verification
   ↓
Documentation       → README / spec / CHANGELOG updated in the same change set
   ↓
Merge               → into `develop` when merge requirements are met
   ↓
Deployment          → Docker Compose per TDOP-infra, Nginx origin proxy, Cloudflare edge
```

## 2. Repository structure

TDOP is organized as sibling repositories under the
[`Tanzanian-Opportunities`](https://github.com/Tanzanian-Opportunities)
organization (Decision DEC-007). Clone them side by side in one directory — the
Docker build contexts (`../TDOP-backend`, `../TDOP-frontend`) depend on this layout.

```text
github.com/Tanzanian-Opportunities/
├── TDOP-backend/               Java 21 / Spring Boot API
│   ├── src/main/java/tdop/
│   │   ├── controller/         REST controllers (admin/, organization/, trust/)
│   │   ├── service/            business logic
│   │   ├── repository/         Spring Data JPA
│   │   ├── entity/ + dto/      persistence model, API contracts
│   │   ├── config/             Spring configuration: SecurityConfig,
│   │   │                       JwtAuthenticationFilter, RateLimitFilter
│   │   ├── rbac/               roles, permissions, authorization service
│   │   ├── organization/       organization domain services
│   │   ├── notification/       in-app + email notification
│   │   ├── audit/              audit logging
│   │   └── exception/ + mapper/ + util as needed
│   ├── src/main/resources/
│   │   ├── application*.yml    configuration (dev/prod profiles)
│   │   ├── db/migration/       Flyway migrations (V1..Vn)
│   │   └── logback-spring.xml  logging configuration
│   ├── src/test/java/          unit & integration tests
│   ├── nginx.conf              deployment Nginx edge proxy (moved from infra)
│   ├── Dockerfile, .env.example, README.md
│   └── pom.xml                 Maven build (Java 21, Spring Boot 3.3)
├── TDOP-frontend/              React 18 + TypeScript SPA
│   ├── src/pages/              route components (Admin/, Auth/, Organization/,
│   │                           Seeker/, SuperAdmin/, Trust/, Support/)
│   ├── src/components/         reusable UI
│   ├── src/services/           API client layer (axios)
│   ├── src/hooks/ + context/   state and auth handling
│   ├── src/types/              shared TypeScript types
│   ├── src/i18n/               English / Swahili translations
│   ├── src/tests/              Vitest tests (setup, services, hooks, pages)
│   ├── Dockerfile, nginx.conf, .env.example, README.md
│   └── package.json            scripts: dev, build, test, lint, format
├── TDOP-infra/                 Docker Compose, env examples, Cloudflare edge
│   ├── docker-compose.yml      build contexts ../TDOP-backend, ../TDOP-frontend
│   ├── docker-compose.dev.yml
│   └── .env.example
├── TDOP-docs/                  governance, specs, project management (this guide)
│   ├── PROJECT_MANAGEMENT.md   live source of truth (sessions, phases, logs)
│   ├── TASK_BREAKDOWN.md       master Kanban + 33 phase boards (177 tasks)
│   ├── EXISTING_IMPLEMENTATION_AUDIT.md
│   ├── CHANGELOG.md · CONTRIBUTING.md · CODE_OF_CONDUCT.md
│   ├── SECURITY.md · SECURITY_STANDARDS.md · DEVELOPMENT_GUIDE.md
│   ├── CODING_STANDARDS.md · LICENSE
│   ├── README_PRD.md
│   └── Specs/                  TDOP_MASTER_SPEC, roadmap, DEPLOYMENT_CHECKLIST
└── TDOP-mobile/                planned mobile application (Flutter/Dart, DEC-010)

Branches (every repository): `develop` (default, integration) + `main` (releases).
```

Issue/PR templates and each repository's CI workflows belong in that repository's
`.github/` directory (workflows are a documented GAP until P01-T13/P01-T14).

## 3. Technology stack

| Layer | Technology |
|---|---|
| Backend | Java 21, Spring Boot 3.3 (Web, Data JPA, Security, Validation, Mail, AOP) |
| Auth | Spring Security + JWT (jjwt 0.12.x), BCrypt, refresh tokens persisted in DB |
| Database | PostgreSQL 16, Flyway migrations |
| API docs | springdoc-openapi (Swagger UI) |
| Frontend | React 18, TypeScript 5, Vite 5, React Router 6, Tailwind CSS 3 |
| Data/state | TanStack Query, Zustand, react-hook-form, axios |
| i18n | i18next (English / Swahili) |
| Mobile | Flutter, Dart (`TDOP-mobile`, DEC-010) |
| Tests | JUnit 5, Mockito, H2 (backend); Vitest + Testing Library (frontend) |
| Build/infra | Maven, npm, Docker Compose, Nginx (origin proxy), Cloudflare edge |
| Logging | SLF4J + Logback (console + rolling file) |

Versions are declared in `TDOP-backend/pom.xml` and `TDOP-frontend/package.json`.
Changing a major version is a decision → record it in the Decision Log.

## 4. Local setup

Prerequisites: **Java 21+**, **Maven 3.8+**, **Node.js 18+**, **PostgreSQL 14+**
(port 5432). Docker is optional but recommended for a clean database.

```bash
# Clone the component repositories as siblings (required by docker compose contexts)
git clone https://github.com/Tanzanian-Opportunities/TDOP-backend.git
git clone https://github.com/Tanzanian-Opportunities/TDOP-frontend.git
git clone https://github.com/Tanzanian-Opportunities/TDOP-infra.git
git clone https://github.com/Tanzanian-Opportunities/TDOP-docs.git

# Database
createdb tdop            # or use Docker: see TDOP-infra/docker-compose.yml

# Backend
cd TDOP-backend
cp .env.example .env     # set DB_PASSWORD, JWT_SECRET (never commit .env)
mvn spring-boot:run      # → http://localhost:8080  (API base /api/v1)

# Frontend
cd TDOP-frontend
cp .env.example .env     # VITE_API_URL
npm install
npm run dev              # → http://localhost:3000 (proxies /api to backend)
```

Full-stack via Docker:

```bash
cd TDOP-infra
cp .env.example .env     # REQUIRED: POSTGRES_PASSWORD, JWT_SECRET
docker compose up -d --build
```

Services: `tdop-postgres` (5432), `tdop-backend` (8080), `tdop-frontend` (3000),
`tdop-adminer` (8082 — **dev only, never production**).

Seeded demo accounts are listed in `README.md`. They exist only through Flyway seed
migrations and must not exist in production.

## 5. Environment variables

| File | Variables | Notes |
|---|---|---|
| `TDOP-backend/.env.example` | `DB_USERNAME`, `DB_PASSWORD`, `JWT_SECRET`, `MAIL_*` | `.env` is git-ignored |
| `TDOP-frontend/.env.example` | `VITE_API_URL` | `VITE_*` values are public in the bundle |
| `TDOP-infra/.env.example` | `POSTGRES_USER`, `POSTGRES_PASSWORD`, `JWT_SECRET` | per-environment secrets |

Rules: no hard-coded secrets anywhere; add new variables to `.env.example` with a
placeholder in the same PR; never print secret values to logs.

## 6. Branch strategy

Every TDOP repository uses the same two permanent branches (Decision DEC-007):

- `develop` — **default branch**; the integration branch; all feature work and PRs
  target it.
- `main` — release/stable branch; always deployable; releases are tagged here.
- Short-lived branches named per `CONTRIBUTING.md` §4:
  `feature/<name>`, `fix/<name>`, `security/<name>`, `docs/<name>`,
  `refactor/<name>`, `test/<name>`, `chore/<name>`.
- Branch from the latest `develop`; rebase before requesting review if `develop`
  moved.
- No force-pushes on `main` or `develop`.
- Releases: merge `develop` → `main`, tag `vX.Y.Z` on `main`, merge back to
  `develop`.

### Branch protection

Protected rules on `develop` in every repository (enabled for all five repos):

- Pull requests required; the CI workflow must pass before merging.
- Administrators are **not** enforced, so scripted/admin pushes (governance
  sessions) still work; everyone else follows the PR path.
- `main` receives releases only; no force-pushes or deletions on either branch.

**Plan limitation (documented instead of attempted for private repos, per the
Phase 0 prompt):** GitHub branch-protection rules on **private** repositories
require a paid plan (GitHub Pro / Team / Enterprise). TDOP repositories are
currently **public**, so the free branch-protection tier applies and the rules
above are active (Decision DEC-014). If the repositories are ever made
private, these rules would require a paid plan - re-evaluate at that point.

## 7. Commit conventions

Conventional Commits (see `CONTRIBUTING.md` §5):

```text
feat: add deadline reminder scheduling to notification service

Reminders were only created in-app; email delivery failed silently on SMTP
errors. Adds retry logging and a regression test.

Refs P17-T03
```

- `type: imperative summary`, ≤ 72 chars.
- `BREAKING CHANGE:` footer for incompatible API/schema changes.
- No secrets, no `target/`, `dist/`, `*.log`, `.env`.

## 8. Pull request workflow

1. Open PR from your branch → `develop`.
2. Move the task to `CODE REVIEW` in `PROJECT_MANAGEMENT.md`.
3. Reviewer checks: correctness, standards, tests, security, docs, changelog.
4. Address comments with new commits (avoid rewriting history after review starts).
5. Approvals + checks green → `TESTING`; run full suites; attach results.
6. Pass → `DONE`; merge; delete the branch.

Merge requirements are listed in `CONTRIBUTING.md` §6.

## 9. Coding standards

### General

- Small, focused functions/classes; clear names; no dead code.
- No commented-out code left in merges; no `TODO` without an issue/task reference.
- Fail fast with meaningful exceptions; handle errors where they can be handled.
- Never swallow exceptions silently.

### Backend (Java/Spring)

- Layering: `controller` → `service` → `repository`. Controllers do validation and
  mapping only — no business logic in controllers, no SQL in controllers.
- DTOs for all API input/output (`dto/request`, `dto/response`); never expose entities
  directly.
- Validation with Jakarta annotations on request DTOs (`@Valid`).
- Business rules live in the domain service, not in the client.
- Use `Optional`/explicit null handling consistently; avoid returning null collections.
- Lombok is available (`@Getter/@Setter/@Builder` etc.) — use consistently.
- Exceptions: throw domain/app exceptions handled by the global exception handler;
  never leak stack traces to clients.
- Authorization checks belong server-side on every endpoint (see
  `SECURITY_STANDARDS.md` §2).

### Frontend (React/TypeScript)

- Strict TypeScript: no `any` without justification; shared types in `src/types/`.
- Components: function components + hooks; keep components small and presentational
  where possible.
- API calls only through `src/services/` (axios client) — no ad-hoc `fetch` in
  components.
- Server state via TanStack Query; UI state via Zustand/context.
- Styling with Tailwind; follow the existing design tokens, don't introduce a second
  styling system.
- All user-visible strings go through i18n (`en` + `sw`), never hard-coded.
- Accessibility: semantic HTML, labels, keyboard navigation, alt text (target
  WCAG 2.2 AA — tracked as a gap).
- Date/money formatting via existing utils (`formatDate`, `formatSalary`).

## 10. Database migrations

- Tool: **Flyway**, files in `TDOP-backend/src/main/resources/db/migration/`.
- Naming: `V<next>__<snake_case_description>.sql` (e.g.
  `V15__notification_preferences_index.sql`).
- Never edit a migration that has been applied anywhere — always add a new version.
- Write migrations to be safe on existing data: additive first (add column nullable /
  with default), then backfill, then constrain.
- Indexes for new query patterns; document them in the migration.
- Seed/demo data belongs in seed migrations and must be guarded from production use.
- Schema changes require: migration file + entity/DTO updates + tests + a `Database`
  entry in `CHANGELOG.md`.

## 11. API development

- Base path `/api/v1`. Breaking changes → new version segment + `Breaking` changelog
  entry.
- Conventional REST verbs: `GET` read, `POST` create, `PUT/PATCH` update,
  `DELETE` remove; responses use clear status codes (`200/201/204/400/401/403/404/409/500`).
- Request/response DTOs with validation; standard error body from the global
  exception handler.
- Pagination on list endpoints (`page`, `size`, sort).
- Document endpoints in springdoc/OpenAPI; keep `Specs/TDOP_MASTER_SPEC.md` aligned
  for architectural changes.
- Rate-limit and authorization requirements per `SECURITY_STANDARDS.md` §3.
- Add/extend tests for each new endpoint (controller + service).

## 12. Frontend development

```bash
npm run dev        # start Vite dev server
npm run lint       # ESLint
npm run format     # Prettier
npm run test       # Vitest
npm run build      # tsc + vite build
```

- Add routes under `src/pages/...` and register them with the router.
- Reuse existing components before creating new ones.
- Handle loading/error/empty states for every data view.
- Verify responsive behavior (mobile-first — most users are on mobile/low bandwidth).

## 13. Backend development

```bash
mvn compile        # compile
mvn test           # unit + integration tests (H2 for tests)
mvn spring-boot:run  # run locally
```

- Profiles: `application-dev.yml`, `application-prod.yml`, `application.yml`.
- Add tests alongside code: service logic → unit tests; endpoints → controller tests;
  security rules → integration tests (`security/` test package).
- Keep scheduled jobs (deadline engine, digests) idempotent and log their runs.

## 14. Testing

| Level | Backend | Frontend |
|---|---|---|
| Unit | JUnit 5 + Mockito (`src/test/java/tdop/service`) | Vitest (`src/tests/`) |
| Integration | `@SpringBootTest`/MVC tests (`controller`, `security`) | Component tests (Testing Library) |
| E2E | **GAP — Phase 28** | **GAP — Phase 28** |
| Performance | **GAP — Phase 29** | **GAP — Phase 29** |

Rules:

- New behavior → tests in the same PR. Bug fix → regression test that fails before
  the fix.
- Never weaken/delete a test to make a change pass without explicit review.
- Run both suites before moving a task to `TESTING`.
- Record test commands + results in the session log of `PROJECT_MANAGEMENT.md`.

## 15. Debugging

- Backend: attach a debugger or use logs (`TDOP-backend/logs/tdop*.log`); enable
  debug logging for a package via `application-dev.yml` (temporarily).
- Reproduce with the smallest possible input; confirm with a failing test first.
- Frontend: React DevTools + browser network tab; check the axios client and proxy.
- Database: inspect with Adminer (dev) or `psql`; compare against the Flyway history
  table (`flyway_schema_history`).
- Never debug with real personal data in logs or screenshots.

## 16. Logging

- Backend uses SLF4J/Logback (`logback-spring.xml`): console + rolling file with
  rotation. Log levels: `ERROR` (action needed), `WARN` (degraded), `INFO`
  (significant business events), `DEBUG` (diagnostics, dev only).
- Log security-relevant events: login success/failure, lockouts, permission denials,
  verification/moderation decisions — with actor, target, timestamp.
- **Never log** passwords, tokens, JWT secrets, full personal records, or request
  bodies containing credentials.
- Frontend: minimal console logging; no sensitive data in analytics/console.
- One log statement per event — avoid duplicate/noisy logging in loops.

## 17. Security

- Read `SECURITY_STANDARDS.md` before touching auth, authz, uploads, external
  ingestion, or payments.
- Threat-model new features during planning (what can go wrong? who can access what?).
- Validate input server-side, encode output, enforce ownership per request.
- Secrets only via environment; `.env` never committed.
- Vulnerability reports → `SECURITY.md` (private, never public).
- Dependency checks before release: `npm audit`, backend dependency scanning when CI
  exists.

## 18. Documentation

- Update docs in the same PR as the behavior change.
- Keep each repository's `README.md` accurate for setup/status changes;
  `README_PRD.md` and `Specs/TDOP_MASTER_SPEC.md` for product/architecture changes.
- Governance/workflow changes → `PROJECT_MANAGEMENT.md` + `CHANGELOG.md`.
- Write for a new contributor: explain *why*, not just *what*.
- Use TODO/TBD placeholders instead of inventing facts, contacts, or dates.

## 19. Release process

1. Confirm Definition of Done for everything in the release; phase exit criteria
   satisfied if a phase is completing.
2. Update `[Unreleased]` → `## [X.Y.Z] — YYYY-MM-DD` in `CHANGELOG.md`
   (SemVer: major = breaking, minor = features, patch = fixes).
3. Update `README.md` status sections and `PROJECT_MANAGEMENT.md`
   (phase/DONE, sessions).
4. Merge `develop` → `main`; tag `vX.Y.Z` on `main`.
5. Build: `mvn -f TDOP-backend/pom.xml package`, `npm run build` (frontend).
6. Deploy per `Specs/DEPLOYMENT_CHECKLIST.md` and `TDOP-infra/`
   (`docker compose up -d --build`); verify health checks.
7. Post-release: verify smoke flows (login, browse, apply, notify), then move the
   next phase into `TO DO`.

## 20. Project management workflow (Kanban)

Tasks move only through the six official states:

```text
BACKLOG → TO DO → IN PROGRESS → CODE REVIEW → TESTING → DONE
```

How to move work:

| When | Action in `PROJECT_MANAGEMENT.md` |
|---|---|
| Before starting | Confirm phase + Definition of Ready; set `Owner`, status `IN PROGRESS`, `Started` |
| During work | Update session log: files changed, progress, blockers, decisions |
| PR opened | Status → `CODE REVIEW`; add reviewer |
| Review approved | Status → `TESTING`; attach test results |
| Tests pass + DoD met | Status → `DONE`; add `Completed` date; update phase progress |
| Something fails | Move back to the appropriate state; record Issue / Cause / Required Fix / Next Action |
| Blocked | Keep current state; add an entry to the Blocker Log |

Never: mark unfinished work `DONE`, invent custom statuses, skip a phase, or delete
session history. Full rules, phase definitions, and logs live in
[`PROJECT_MANAGEMENT.md`](PROJECT_MANAGEMENT.md); task-level boards live in
[`TASK_BREAKDOWN.md`](TASK_BREAKDOWN.md). The organization Kanban board
(https://github.com/orgs/Tanzanian-Opportunities/projects/1) mirrors those files —
update the files first, then move the card to the same state.

## 21. Definition of Done (summary)

Implementation complete · code follows standards · tests written and passing ·
security considered · documentation updated · code reviewed · no unresolved blocker ·
changelog updated when required · project management updated.
(Full version: `PROJECT_MANAGEMENT.md` §10 and `CONTRIBUTING.md` §8.)
