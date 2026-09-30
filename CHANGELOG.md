# Changelog — TDOP (Tanzania Digital Opportunity Platform)

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Rule: meaningful project changes must never be silently omitted.** Any change that
affects features, behavior, security, database schema, infrastructure, public API,
or project governance must be recorded here in the same change set that introduces it.

## How to update this file

1. Add your entries under the `[Unreleased]` section, inside the correct category.
2. Each entry should be a short, factual bullet. Start with a verb (`Add`, `Change`,
   `Fix`, `Remove`, `Deprecate`, `Secure`).
3. When a release is cut (git tag `vX.Y.Z`), move everything from `[Unreleased]` into
   a new section `## [X.Y.Z] — YYYY-MM-DD` and start a fresh empty `[Unreleased]`.
4. Breaking changes and security changes must always be listed explicitly — never
   bury them inside unrelated bullets.
5. Documentation-only changes belong under `Documentation`. Governance documents
   (`CONTRIBUTING.md`, `PROJECT_MANAGEMENT.md`, `SECURITY*.md`, …) count as changes.

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
| `Infrastructure` | CI/CD, Docker, Nginx, environment, tooling changes |
| `Database` | Flyway migrations, schema, seed-data changes |
| `Documentation` | README, specs, guides, governance documents |

---

## [Unreleased]

### Added

- `TASK_BREAKDOWN.md` — Master Kanban (177 tasks) and all 33 phase boards extracted
  from `PROJECT_MANAGEMENT.md` sections 6/7 (original numbering preserved); path
  note added for the multi-repository layout.
- `EXISTING_IMPLEMENTATION_AUDIT.md` — inventory of pre-existing code extracted from
  `PROJECT_MANAGEMENT.md` section 16, with path notes for the component repositories.
- `Specs/` directory — `TDOP_MASTER_SPEC.md`, `IMPLEMENTATION & FUTURE ROADMAP.md`
  (+ `.docx`), and `DEPLOYMENT_CHECKLIST.md` moved from the old `Docs/` layout.
- Organization GitHub Projects Kanban board
  (`https://github.com/orgs/Tanzanian-Opportunities/projects/1`, view
  `Kanban Board`) with all 177 tasks as cards and the six official states as
  columns; card statuses verified equal to `TASK_BREAKDOWN.md`
  (162 `BACKLOG`, 3 `TO DO`, 1 `IN PROGRESS`, 11 `DONE`).

### Changed

- **Repository restructured into component repositories** (Decision DEC-007):
  `TDOP-backend`, `TDOP-frontend`, `TDOP-infra`, `TDOP-docs`, and `TDOP-mobile`
  created under the `Tanzanian-Opportunities` organization with history preserved
  via `git subtree split`; `Tanzanian_Opportunities` remains as the umbrella index
  repository. Governance set, `README_PRD.md`, and `LICENSE` now live in
  `TDOP-docs`.
- `PROJECT_MANAGEMENT.md` slimmed to the live tracker (sessions, phases, logs,
  decisions, rules); task boards and the audit moved to the new files above.
- Branch strategy updated for every repository: `develop` is the default/integration
  branch, `main` holds releases; PRs target `develop`
  (`DEVELOPMENT_GUIDE.md` §6, `CONTRIBUTING.md` §4/§6).
- Documentation cross-references updated for the new layout
  (`Docs/` → `Specs/`, repository structure, clone instructions, board links).
- Uncommitted backend work-in-progress carried from the monorepo working tree into
  `TDOP-backend`: JWT and error-handling hardening, H2 test dependency plus surefire
  test-configuration fix, expanded controller/service test suites and a new
  `DeadlineReminderRepository`; `mvn test` green (89 tests).
- Flyway migration version collisions fixed while carrying the WIP: the duplicates
  `V10__data_integrity_indexes.sql` and `V11__escalations_and_appeals.sql`
  (clashing with `V10__normalize_application_status` and
  `V11__email_verification_tokens`) renumbered to `V13`/`V14`.
- Development helper scripts kept with their component repositories in portable
  form (`run_backend.ps1`/`run_backend.bat`, `run_frontend.bat`,
  `check_servers.ps1`).

### Security

- `check_db.ps1` (developer helper) contained a plaintext database password; scrubbed
  to an environment-variable prompt before inclusion in `TDOP-infra`.

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

### Added
- ...

### Changed
- ...

### Fixed
- ...

### Security
- ...

### Breaking
- ...

### Infrastructure
- ...

### Database
- ...

### Documentation
- ...
```
