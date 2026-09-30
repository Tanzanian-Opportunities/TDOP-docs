# Changelog — TDOP (Tanzania Digital Opportunity Platform)

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Rule: meaningful project changes must never be silently omitted.** Any change that
affects features, behavior, security, database schema, infrastructure, public API,
or project governance must be recorded here in the same change set that introduces it.

## How to update this file

1. `[Unreleased]` is grouped **by project part** (repository, board, or governance
   unit). Record each change under the part it happened in, so every part's history
   is visible at a glance.
2. Each entry should be a short, factual bullet. Start with a verb (`Add`, `Change`,
   `Fix`, `Remove`, `Deprecate`, `Secure`).
3. Security-relevant changes must start with **`Security:`** so they can never be
   buried inside unrelated bullets.
4. **Phase lifecycle (3 steps):** the `Phase completion status` table below tracks
   every phase as `Planned` → `In progress` → `Completed`. This lifecycle is
   **independent of the six-state task Kanban** (DEC-008).
   - When a phase starts being implemented, its row becomes `In progress`.
   - When a phase is fully done, its row becomes `Completed` **and** a consolidated
     phase-closure entry is added (under the release section that finishes the phase)
     summarizing the phase's final changes for every part — then work moves to the
     next phase, whose row flips from `Planned` to `In progress`.
   - All remaining phases stay `Planned` until their start criteria are met.
5. When a release is cut (git tag `vX.Y.Z`), move everything from `[Unreleased]` into
   a new section `## [X.Y.Z] — YYYY-MM-DD` (including any phase-closure summaries)
   and start a fresh empty `[Unreleased]`.
6. Documentation-only changes belong in the owning part under `Documentation`.
   Governance documents (`CONTRIBUTING.md`, `PROJECT_MANAGEMENT.md`, `SECURITY*.md`, …)
   count as changes.

## Phase completion status

3-step lifecycle per phase: **Planned → In progress → Completed**. Independent of the
Kanban task states (DEC-008); progress percentages live in
`PROJECT_MANAGEMENT.md` §5.

| Phase | Name | Status |
|---|---|---|
| 01 | Project Initiation | Completed |
| 02 | Requirements Engineering | Planned |
| 03 | System Analysis | Planned |
| 04 | System Architecture | Planned |
| 05 | Database Design | Planned |
| 06 | API & Contract Design | Planned |
| 07 | Development Environment | Planned |
| 08 | Backend Foundation | Planned |
| 09 | Frontend Foundation | Planned |
| 10 | Authentication & Authorization | Planned |
| 11 | User & Profile Module | Planned |
| 12 | Organization Module | Planned |
| 13 | Opportunity Core | Planned |
| 14 | Trust & Verification | Planned |
| 15 | Discovery & Search | Planned |
| 16 | Application Engine | Planned |
| 17 | Notification System | Planned |
| 18 | Deadline & Freshness | Planned |
| 19 | Personalization & Matching | Planned |
| 20 | Administration & Governance | Planned |
| 21 | Analytics & Outcomes | Planned |
| 22 | Advanced Data Quality & Source Management | Planned |
| 23 | External Opportunity Ingestion | Planned |
| 24 | Advanced Intelligence / AI | Planned |
| 25 | Communication Expansion | Planned |
| 26 | Subscription / Business Model | Planned |
| 27 | Complete Security Hardening | Planned |
| 28 | Complete Testing | Planned |
| 29 | Performance & Reliability | Planned |
| 30 | Deployment & CI/CD | Planned |
| 31 | Beta Release | Planned |
| 32 | Production Launch | Planned |
| 33 | Continuous Improvement | Planned |

## Categories

| Category | Use for |
|---|---|
| `Added` | New features, endpoints, pages, documents |
| `Changed` | Behavior or implementation changes to existing functionality |
| `Deprecated` | Features that will be removed in a future release |
| `Removed` | Features, files, or endpoints removed |
| `Fixed` | Bug fixes |
| `Security` | Vulnerability fixes, hardening, security-relevant changes |
| `Breaking` | Backward-incompatible API, schema, or configuration changes |
| `Infrastructure` | CI/CD, Docker, Nginx, Cloudflare, environment, tooling changes |
| `Database` | Flyway migrations, schema, seed-data changes |
| `Documentation` | README, specs, guides, governance documents |

---

## [Unreleased]

### TDOP-docs

- **Added** `TASK_BREAKDOWN.md` — Master Kanban (177 tasks) and all 33 phase boards
  extracted from `PROJECT_MANAGEMENT.md` sections 6/7 (original numbering preserved);
  path note for the multi-repository layout.
- **Added** `EXISTING_IMPLEMENTATION_AUDIT.md` — inventory of pre-existing code
  extracted from `PROJECT_MANAGEMENT.md` section 16, with path notes.
- **Added** `Specs/` directory — `TDOP_MASTER_SPEC.md`,
  `IMPLEMENTATION & FUTURE ROADMAP.md` (+ `.docx`), and `DEPLOYMENT_CHECKLIST.md`
  moved from the old `Docs/` layout.
- **Added** `CODING_STANDARDS.md` — binding coding standards for the Java/Spring
  backend, React/TypeScript frontend, SQL/Flyway, i18n, testing, and Git workflow.
- **Added** `Specs/SRS.md` — Software Requirements Specification draft (scope,
  actors, constraints, FR/NFR requirements, traceability) as the Phase 02
  requirements-baseline input.
- **Added** `MAINTAINERS.md` — ownership, roles, and contact points; `[TBD]`
  placeholders in `SECURITY.md` and `CODE_OF_CONDUCT.md` now point here (P01-T15).
- **Added** `scripts/validate.ps1` — repository-relative documentation consistency
  validator (governance files, 33-phase order, 177 unique task IDs, state
  vocabulary, phase lifecycle) used locally and by CI (P01-T09).
- **Added** `.github/` issue templates (`bug_report`, `feature_request`) and
  `pull_request_template.md` for every repository (P01-T13).
- **Added** completion roadmap section at the top of
  `Specs/IMPLEMENTATION & FUTURE ROADMAP.md` — the clear 33-phase path to completion
  with per-phase status.
- **Added** this file's `Phase completion status` table (3-step phase lifecycle,
  independent of the Kanban) and the per-part change-grouping convention (DEC-008).
- **Changed** `PROJECT_MANAGEMENT.md` slimmed to the live tracker (sessions, phases,
  logs, decisions, rules); task boards and the audit moved to the new files above.
- **Changed** branch strategy for every repository: `develop` is the
  default/integration branch, `main` holds releases; PRs target `develop`
  (`DEVELOPMENT_GUIDE.md` §6, `CONTRIBUTING.md` §4/§6).
- **Changed** documentation cross-references for the new layout (`Docs/` → `Specs/`,
  repository structure, clone instructions, board links).
- **Changed** `LICENSE` consolidated here as the single license of record for all
  repositories (DEC-011); removed from every other repository.
- **Changed** `PROJECT_MANAGEMENT.md` Session 04 recorded; DEC-008 (phase
  lifecycle), DEC-009 (Cloudflare edge / Nginx origin), DEC-010 (Flutter mobile
  stack), DEC-011 (single license) added; Phase Tracker §5, dashboard, §2, §8,
  §16–§18 converted to the `Planned` / `In progress` / `Completed` lifecycle.
- **Changed** `TASK_BREAKDOWN.md` P01-T12 – P01-T15 moved to `DONE`; all 33 phase
  record statuses converted to the phase lifecycle vocabulary.
- **Changed** `EXISTING_IMPLEMENTATION_AUDIT.md` evidence verification (P01-T12):
  all 27 file-path references resolved against the component-repository clones —
  27 found, 0 missing.
- **Changed** `DEVELOPMENT_GUIDE.md` repository tree updated: Nginx edge config moved
  to `TDOP-backend`, `CODING_STANDARDS.md` added, Cloudflare recorded as the
  production edge.
- **Changed** `SECURITY.md` scope now lists `TDOP-infra/` Compose config,
  `TDOP-backend/nginx.conf`, and the Cloudflare edge configuration.

### TDOP-backend

- **Changed** uncommitted backend work-in-progress carried from the monorepo working
  tree: JWT and error-handling hardening, H2 test dependency plus surefire
  test-configuration fix, expanded controller/service test suites and a new
  `DeadlineReminderRepository`; `mvn test` green (89 tests).
- **Fixed** Flyway migration version collisions: the duplicate
  `V10__data_integrity_indexes.sql` and `V11__escalations_and_appeals.sql`
  (clashing with `V10__normalize_application_status` and
  `V11__email_verification_tokens`) renumbered to `V13`/`V14`.
- **Added** `nginx.conf` — the deployment Nginx edge proxy (rate-limited `/api`,
  `/ws`, `/swagger-ui`, `/health`, SPA static fallback, security headers) moved here
  from `TDOP-infra/nginx/` (DEC-009).
- **Added** portable development helpers `run_backend.ps1` / `run_backend.bat` and
  absolute cross-repository README links.
- **Added** `.github/` issue/PR templates and CI skeleton
  `.github/workflows/ci.yml` (JDK 21, `mvn -B test`) (P01-T13/T14).
- **Removed** `LICENSE` — the single license of record lives in `TDOP-docs`.

### TDOP-frontend

- **Changed** README repository links made absolute (relative sibling links break on
  GitHub) and the Kanban board link added.
- **Added** portable development helper `run_frontend.bat`.
- **Added** `.github/` issue/PR templates and CI skeleton
  `.github/workflows/ci.yml` (`npm ci`, lint, test) (P01-T13/T14).
- **Fixed** `src/tests/App.test.tsx` now renders `App` inside the providers
  `main.tsx` provides (`QueryClientProvider`, `I18nextProvider`,
  `ThemeProvider`, `NotificationProvider`); suite green 36/36.
- **Changed** CI lint step is `continue-on-error` until an ESLint config exists
  (lint gate activates with its owning phase); test step is blocking and passing.
- **Removed** `LICENSE` — the single license of record lives in `TDOP-docs`.

### TDOP-infra

- **Added** README documenting the sibling-clone layout required by the Compose build
  contexts, service/port tables, and environment setup.
- **Added** smoke-check helpers `check_db.ps1` / `check_db.sql` / `check_servers.ps1`.
- **Added** Cloudflare documented as part of the project: production edge for DNS,
  TLS, CDN caching, and WAF/bot protection in front of the origin (DEC-009).
- **Removed** `nginx/nginx.conf` — relocated to `TDOP-backend/nginx.conf` where the
  API it protects lives (DEC-009); the frontend container keeps its own
  `TDOP-frontend/nginx.conf`.
- **Removed** `LICENSE` — the single license of record lives in `TDOP-docs`.
- **Added** `.github/` issue/PR templates and CI skeleton
  `.github/workflows/ci.yml` (`docker compose config` validation) (P01-T13/T14).
- **Infrastructure** CI supplies throwaway `POSTGRES_PASSWORD` / `JWT_SECRET`
  placeholders so `${VAR:?}` interpolation resolves during config validation.
- **Security:** `check_db.ps1` contained a plaintext database password; scrubbed to
  an environment-variable prompt (`PGPASSWORD`).

### TDOP-mobile

- **Added** initial README, `.gitignore`, `.github/` issue/PR templates, and a CI
  skeleton that starts Flutter analysis once `pubspec.yaml` exists (P01-T13/T14);
  `workflow_dispatch` trigger for manual runs.
- **Changed** README now records the decided mobile stack: **Flutter / Dart**,
  one codebase for Android and iOS (DEC-010).
- **Removed** `LICENSE` — the single license of record lives in `TDOP-docs`.

### Tanzanian_Opportunities (umbrella index)

- **Changed** README rewritten as the repository-map index: repository table with
  technology stacks, project-wide technology stack section (including Cloudflare),
  quick start with sibling clone instructions, and documentation pointers.
- **Changed** all moved content removed (422 paths): governance set, `Docs/`, and
  component directories now live in their component repositories (DEC-007).
- **Removed** `LICENSE` — linked to `TDOP-docs` instead (DEC-011).
- **Added** `.github/` issue/PR templates (P01-T13); no build workflow — the
  umbrella index has nothing to compile.

### Organization Kanban board

- **Added** GitHub Projects board `TDOP Delivery`
  (`https://github.com/orgs/Tanzanian-Opportunities/projects/1`, views
  `Kanban Board` + `All Tasks`) with all 177 tasks as cards and the six official
  states as columns; custom field `TDOP Status`. Card statuses verified equal to
  `TASK_BREAKDOWN.md` (162 `BACKLOG`, 3 `TO DO`, 1 `IN PROGRESS`, 11 `DONE`).
- **Changed** Phase 01 closure: the four remaining cards (P01-T12 – P01-T15) moved
  to `DONE`; board now mirrors `TASK_BREAKDOWN.md` at 162 `BACKLOG` / 15 `DONE`.
- **Infrastructure** first CI runs recorded on `develop`: all five workflows
  (`TDOP-docs`, `TDOP-backend`, `TDOP-frontend`, `TDOP-infra`, `TDOP-mobile`)
  completed `success`.

### Phase closure

- **Phase 01 — Project Initiation: Completed (2026-09-30, Session 04)** —
  consolidated final state of the phase per part:
  - `TDOP-docs`: governance set complete (`LICENSE`, `CHANGELOG.md`,
    `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `DEVELOPMENT_GUIDE.md`,
    `SECURITY.md`, `SECURITY_STANDARDS.md`, `PROJECT_MANAGEMENT.md`), plus
    `TASK_BREAKDOWN.md`, `EXISTING_IMPLEMENTATION_AUDIT.md`,
    `CODING_STANDARDS.md`, `MAINTAINERS.md`, `scripts/validate.ps1`, and
    `Specs/` (incl. `SRS.md` and the completion roadmap); audit evidence
    verified 27/27; DEC-001 – DEC-011 recorded; validation passed.
  - `TDOP-backend` / `TDOP-frontend` / `TDOP-infra` / `TDOP-mobile` / umbrella:
    per-repo READMEs with technology stacks, license consolidated into
    `TDOP-docs` (DEC-011), `.github/` issue/PR templates, CI skeletons
    (P01-T13/T14).
  - Organization Kanban board: all 15 Phase 01 cards `DONE`, mirroring the
    tracker.
  - Phase status flipped `In progress` → `Completed` in
    `Phase completion status`; next phase (02) stays `Planned` until its work
    starts (DEC-008).

---

## [0.1.0] — Unreleased (in preparation)

First governance baseline. This section will be dated when the first tag is cut.

### Added

- `LICENSE` — MIT license file formalizing the "License: MIT" declaration already
  present in `README.md`.
- `CHANGELOG.md` — this file; project-wide rule that meaningful changes must not be
  silently omitted.
- `CODE_OF_CONDUCT.md` — contributor standards for respectful, inclusive, professional
  collaboration on TDOP.
- `CONTRIBUTING.md` — contribution workflow from issue to merge, including branch
  naming, commit conventions, review, testing, and changelog obligations.
- `DEVELOPMENT_GUIDE.md` — central engineering guide: lifecycle, repository structure,
  technology stack, local setup, branch strategy, coding standards, testing, security,
  documentation, release process, and Kanban workflow.
- `SECURITY.md` — vulnerability reporting, responsible disclosure, severity handling,
  and response expectations.
- `SECURITY_STANDARDS.md` — binding technical security standards for authentication,
  authorization, API, database, frontend, infrastructure, secure development, and
  privacy.
- `PROJECT_MANAGEMENT.md` — live Git-based Kanban project-management system: current
  project position, live development sessions, 33-phase roadmap, phase tracker, master
  Kanban, per-phase Kanban boards, decision log, blocker log, risk register, and
  existing-implementation audit.

### Documentation

- Official 33-phase development roadmap recorded as the authoritative project
  progression (PHASE 01 — Project Initiation → PHASE 33 — Continuous Improvement).
- Official six-state Kanban workflow recorded: `BACKLOG → TO DO → IN PROGRESS →
  CODE REVIEW → TESTING → DONE`.
- Repository transferred from the personal account to the GitHub organization
  `Tanzanian-Opportunities`; all documentation repository URLs (clone instructions,
  security advisory link, conduct/contribution headers) updated to
  `https://github.com/Tanzanian-Opportunities/Tanzanian_Opportunities`
  (old URLs redirect).
- Repository governance documents cross-reference each other
  (`CONTRIBUTING.md` → `DEVELOPMENT_GUIDE.md` → `PROJECT_MANAGEMENT.md`,
  `SECURITY.md` → `SECURITY_STANDARDS.md`).

### Notes

- Development work performed before this governance baseline exists only in git
  history (`git log`). It was deliberately **not** backfilled into this changelog as
  fabricated release entries. The pre-existing codebase is instead inventoried in
  `EXISTING_IMPLEMENTATION_AUDIT.md` (originally section 16 of
  `PROJECT_MANAGEMENT.md`), which does not alter official phase completion status.

---

## Release template (copy when cutting a release)

```markdown
## [X.Y.Z] — YYYY-MM-DD

### <Part / repository>
- **Added** ...
- **Changed** ...
- **Fixed** ...
- **Security:** ...
- **Breaking** ...
- **Infrastructure** ...
- **Database** ...
- **Documentation** ...

### Phase closure (only when a phase completes)
- **Phase NN — <Name>: Completed** — consolidated final changes of the phase per
  part; phase status flipped to Completed in `Phase completion status`; the next
  phase stays `Planned` until its work starts (DEC-008).
```
