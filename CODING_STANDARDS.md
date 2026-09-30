# TDOP Coding Standards

**Binding coding standards for every TDOP repository.** All contributions - human or
AI-assisted - must meet these standards before they can pass Code Review
(`DEVELOPMENT_GUIDE.md` §8). Security-specific requirements remain governed by
[`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md); lifecycle, branching, and PR
process are governed by [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md).

Scope: `TDOP-backend`, `TDOP-frontend`, `TDOP-infra`, `TDOP-mobile`, and all
documentation in `TDOP-docs`.

## 1. General rules

- Small, focused functions and classes; intention-revealing names; no dead code.
- No commented-out code merged; no `TODO` without an issue or task reference
  (`P<NN>-T<NN>` or issue link).
- Fail fast with meaningful exceptions; handle errors where they can be handled;
  never swallow exceptions silently.
- Do not invent facts: code, docs, and estimates reflect what exists; unknowns stay
  `[TBD]`.
- No secrets, keys, passwords, or `.env` values in code, tests, fixtures, commits,
  or documentation (see `SECURITY.md`).
- Every change ships with its documentation updates (README, CHANGELOG,
  `PROJECT_MANAGEMENT.md` session) in the same change set.

## 2. Git and commits

- Branch model (DEC-007): branch from `develop`; PRs target `develop`; `main` is
  releases only.
- Conventional Commits: `type: imperative summary` (≤ 72 chars), types
  `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `perf`, `build`, `ci`.
  Body explains *why*; `Refs P<NN>-T<NN>` footer when tied to a task.
- `BREAKING CHANGE:` footer for incompatible API or schema changes.
- Small, reviewable commits; never commit build output (`target/`, `dist/`,
  `node_modules/`), logs, or IDE files.
- Never force-push shared branches; address review feedback with new commits.

## 3. Backend - Java 21 / Spring Boot 3.3

**Layering**

- Strict flow: `controller` → `service` → `repository`. Controllers do request
  validation and mapping only - no business logic, no SQL, no authorization
  decisions beyond declaring requirements.
- DTOs for all API input/output (`dto/request`, `dto/response`); never expose JPA
  entities on the wire.
- Business rules live in the domain service, never in the client.

**Style and structure**

- Package root `tdop.*`; keep the existing package layout (see README
  Project Layout) - do not create parallel structures.
- Java: camelCase methods/fields, PascalCase types, UPPER_SNAKE constants; explicit
  types on public API; `final` for immutable locals where it aids clarity.
- Lombok consistently (`@Getter`, `@Setter`, `@Builder`, `@RequiredArgsConstructor`) -
  no hand-written boilerplate it already covers.
- Use `Optional`/explicit null handling; never return `null` collections.
- Validation with Jakarta Bean Validation on request DTOs (`@Valid`); fail with
  `400` and the standard error body.

**Errors and security**

- Throw domain exceptions (`NotFoundException`, `ForbiddenException`, …) handled by
  `GlobalExceptionHandler`; never leak stack traces or internal messages to clients.
- Authorization is enforced server-side on every endpoint (ownership + role checks,
  `SECURITY_STANDARDS.md` §2). Hidden UI is not access control.
- Log with SLF4J; no passwords/tokens/PII in logs; correlation via existing logback
  configuration.

**Tests (required for DoD)**

- JUnit 5 + Mockito (+ H2 for repository/integration slices); tests live in
  `src/test/java/tdop/**` mirroring main packages.
- Name tests `methodOrBehaviour_condition_expectedResult`; assert behavior, not
  implementation details. Every fixed bug gets a regression test.

## 4. Database - PostgreSQL / Flyway

- Migrations: `V<next>__<snake_case_description>.sql` in
  `TDOP-backend/src/main/resources/db/migration/`. **Version numbers must be
  unique** - a collision has happened before (V10/V11) and broke startup.
- Never edit a migration that has been applied anywhere; always add a new version.
- Additive-first on live data: add nullable/defaulted column → backfill → constrain.
- Index new query patterns; keep seed/demo data in guarded seed migrations only.
- A schema change requires: migration + entity/DTO updates + tests + a `Database`
  entry in `CHANGELOG.md`.

## 5. Frontend - React 18 / TypeScript 5

- Strict TypeScript: no `any` without a written justification; shared types in
  `src/types/`; API contracts mirrored from the backend DTOs.
- Function components + hooks; keep components small; presentational logic separated
  from data fetching.
- API calls only through `src/services/` (the shared axios instance) - no ad-hoc
  `fetch`, no direct axios in components.
- Server state via TanStack Query; UI/global state via Zustand or React Context -
  do not add another state library.
- Styling exclusively with Tailwind CSS using existing design tokens; no second
  styling system; reuse `src/components/ui/*` primitives before writing new ones.
- **All user-visible strings go through i18n** (`src/i18n/en.json` +
  `sw.json`); never hard-code display text; new keys are added to *both* files.
- Dates/money/roles through the existing utils (`formatDate`, `formatSalary`,
  `formatRole`) - no ad-hoc formatting in components.
- Accessibility: semantic HTML, labelled inputs, keyboard navigation, alt text
  (target WCAG 2.2 AA).
- Tests: Vitest + React Testing Library in `src/tests/`; cover hooks, services, and
  user-facing flows; a fixed bug gets a regression test.

## 6. Infrastructure

- Compose files live in `TDOP-infra`; build contexts assume sibling clones
  (`../TDOP-backend`, `../TDOP-frontend`) - keep that layout.
- Nginx edge configuration lives in `TDOP-backend/nginx.conf`; the frontend image
  uses `TDOP-frontend/nginx.conf` (DEC-009). Changes to either must keep the
  security headers and rate limits intact (`SECURITY_STANDARDS.md` §7).
- Cloudflare fronts production (DNS/TLS/CDN/WAF); dashboard/API credentials never
  touch the repository.
- Helper scripts must be portable (script-relative paths, environment variables for
  machine-specific values) - no absolute developer paths, no hard-coded passwords.

## 7. Internationalization

- English (`en`) and Swahili (`sw`) parity for every user-visible string.
- Keep keys namespaced by feature (`opportunities.detail.*`); never delete a key
  still referenced in code; document cultural/date/number formats per
  `Specs/TDOP_MASTER_SPEC.md`.

## 8. Documentation standards

- Markdown in `TDOP-docs`; tables for structured data; links between documents stay
  valid (relative within a repository, full URLs across repositories).
- Update the right file for the right purpose: requirements → `README_PRD.md`,
  progress/tasks → `PROJECT_MANAGEMENT.md` + `TASK_BREAKDOWN.md`, changes →
  `CHANGELOG.md` (grouped by project part), decisions → `PROJECT_MANAGEMENT.md` §14
  (append-only), security → `SECURITY*.md`.
- Session logs and decision history are **append-only** - never rewrite past
  entries; correct the present, not the past.
- No invented technologies, contacts, dates, or percentages; `[TBD]` for unknowns.

## 9. Definition of Done checklist (standards view)

A change meets standards only when all of the following hold:

1. Follows the layering and naming rules above for its language.
2. Tests written/updated and green (`mvn test` / `npm test`).
3. No secrets, no dead code, no commented-out code, no unjustified `any`.
4. User-visible strings internationalized (`en` + `sw`).
5. Security requirements of `SECURITY_STANDARDS.md` respected for touched areas.
6. README/CHANGELOG/`PROJECT_MANAGEMENT.md` updated in the same change set.
7. Reviewed against this file in Code Review (`DEVELOPMENT_GUIDE.md` §8).

## Related

- [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) - lifecycle, branching, PR flow
- [`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md) - binding security requirements
- [`CONTRIBUTING.md`](CONTRIBUTING.md) - contribution workflow and merge requirements
- [`PROJECT_MANAGEMENT.md`](PROJECT_MANAGEMENT.md) - live source of truth (§14 decisions)
- [Kanban board](https://github.com/orgs/Tanzanian-Opportunities/projects/1)
