# Phase 0 Report — Project Setup

**Status:** Completed
**Date:** 2026-09-30
**Business phase:** Phase 0 — Project Setup (canonical roadmap: `docs/business/roadmap.md`)
**Engineering phase:** PHASE 01 — Project Initiation (`Completed`, 15/15 tasks; DEC-004 — no auto-crediting)
**Author:** Maintainer (repository owner) with AI coding-assist session

---

## 1. Summary

Phase 0 delivered the complete project skeleton: a five-repository GitHub
organization, governance documentation, a live Kanban board mirroring the
177-task breakdown, CI on every repository, standard repository files, board
automation, labels, provisioning scripts, and the contract-hub `docs/` structure
required by the project-setup prompt. No product code was written; existing
code remains inventoried in `EXISTING_IMPLEMENTATION_AUDIT.md`.

## 2. Deliverables

- [x] GitHub organization `Tanzanian-Opportunities` with five repositories
      (`TDOP-docs`, `TDOP-backend`, `TDOP-frontend`, `TDOP-infra`, `TDOP-mobile`),
      each with `main` + `develop` branches and `develop` as the integration
      branch (umbrella index `Tanzanian_Opportunities` dissolved, DEC-012).
- [x] Governance set: `PROJECT_MANAGEMENT.md`, `DEVELOPMENT_GUIDE.md`,
      `CONTRIBUTING.md`, `SECURITY.md`, `SECURITY_STANDARDS.md`,
      `CODE_OF_CONDUCT.md`, `MAINTAINERS.md`, `CODING_STANDARDS.md`,
      `TASK_BREAKDOWN.md`, `EXISTING_IMPLEMENTATION_AUDIT.md`, `CHANGELOG.md`,
      `LICENSE`.
- [x] Contract-hub `docs/` structure: `business/roadmap.md` (phases 0–10),
      `requirements/SRS.md`, `development/project-management.md`,
      `planned-technologies.md`, `decisions/` (ADR-0001–ADR-0014 + index),
      this report.
- [x] `templates/` (CI workflows, `project-board.yml`, dependabot configs,
      `CODEOWNERS`, `.editorconfig`, `SECURITY.md`, license, issue/PR templates)
      and `scripts/setup/` (idempotent Python provisioning, `GH_TOKEN` env var,
      retries, HTTP errors as data).
- [x] Board "TDOP Delivery" with the six-state `TDOP Status` field mirroring all
      177 tasks; labels `type:*`, `component:*`, `priority:*` in every repository.
- [x] Board automation: identical `.github/workflows/project-board.yml` in all
      five repositories implementing the prompt's six rules (opened→BACKLOG,
      assigned→IN PROGRESS, PR opened→CODE REVIEW with closing-linked issues,
      merged→TESTING, never auto-DONE, closed→DONE).
- [x] CI in every repository: `npm ci → lint → build → test` (frontend, blocking
      lint), backend/frontend/docs/infra/mobile workflows, push triggers on
      `main` + `develop`, PR triggers against both, PR concurrency cancellation.
- [x] Standard files: `.github/CODEOWNERS`, `.editorconfig`,
      `.github/dependabot.yml`, `SECURITY.md`, `LICENSE` (app repositories),
      `.env.example` (mobile), `.gitignore` (docs, infra), issue + PR templates.
- [x] Branch protection on `develop` in all five repositories (see §4).

## 3. Verification

- `scripts/validate.ps1`: **OVERALL PASS** (all checks green) after every
  governance change.
- Frontend: `npm run lint` 0 errors, `npm run build` green, `npm test -- --run`
  36/36 passing.
- CI: all workflows green on `develop` for all five repositories.
- Board automation verified live with a scratch issue and a scratch PR, then
  cleaned up (Session 06).

## 4. Deviations and limitations (owner-accepted)

| # | Prompt expectation | What was done | Why |
|---|---|---|---|
| 1 | Private repositories with paid-plan branch protection | Repositories stay **public**; free branch protection on `develop` (PR required, required CI check, admins not enforced) | Owner directive "Keep public + free protection" (DEC-014); branch protection requires a paid plan on private repositories. Documented in `DEVELOPMENT_GUIDE.md` §6. |
| 2 | `.github/CODEOWNERS` with `@{{ORG}}` team | `* @felix202422` (repository owner) | No teams exist in the organization; teams require organization administration setup outside this session. |
| 3 | Monolithic original layout | Split into five component repositories + dissolved umbrella index (DEC-007, DEC-012) | Owner decisions; contract-hub duties live in `TDOP-docs`. |
| 4 | Single license | MIT license of record in `TDOP-docs` for governance docs; proprietary `LICENSE` in the four application repositories (DEC-013, amends DEC-011) | Owner directive: application code proprietary, governance hub open. |
| 5 | Requirements docs under one path | `docs/requirements/SRS.md` canonical; `Specs/SRS.md` kept as a pointer stub | Validator and existing references still resolve the `Specs/` path. |

## 5. Evidence

- Repository: `Tanzanian-Opportunities/TDOP-docs`, branch `develop`
- Key files: `PROJECT_MANAGEMENT.md` (Session 06, DEC-013/DEC-014),
  `CHANGELOG.md` (`## Phase 0 - Project Setup - Completed`), this report,
  `scripts/validate.ps1`, `scripts/setup/`, `templates/`, `docs/`

## 6. Next

Business Phase 1 — UI/UX Design (planned). Engineering continues from
PHASE 02 — Requirements Engineering (P02-T01) per `PROJECT_MANAGEMENT.md` §18.
