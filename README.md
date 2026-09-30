# TDOP Documentation (`TDOP-docs`)

**Tanzania Digital Opportunity Platform (TDOP)** — governance, specifications, and
the live project-management source of truth.

This repository is the documentation hub of the TDOP organization
([`Tanzanian-Opportunities`](https://github.com/Tanzanian-Opportunities)). Code lives
in the component repositories listed below.

**Live Kanban board (mirrors the tracker):**
https://github.com/orgs/Tanzanian-Opportunities/projects/1

## Repository map

| Repository | Contents |
|---|---|
| [`TDOP-backend`](https://github.com/Tanzanian-Opportunities/TDOP-backend) | Java 21 / Spring Boot 3.3 REST API (PostgreSQL, Flyway) + Nginx edge config |
| [`TDOP-frontend`](https://github.com/Tanzanian-Opportunities/TDOP-frontend) | React 18 / TypeScript / Vite / Tailwind SPA |
| [`TDOP-infra`](https://github.com/Tanzanian-Opportunities/TDOP-infra) | Docker Compose orchestration, Cloudflare edge |
| [`TDOP-docs`](https://github.com/Tanzanian-Opportunities/TDOP-docs) | This repository - governance, specs, project management, project overview |
| [`TDOP-mobile`](https://github.com/Tanzanian-Opportunities/TDOP-mobile) | Planned mobile application (Flutter / Dart, DEC-010) |

The former `Tanzanian_Opportunities` umbrella index repository was dissolved and
its content moved into this repository (DEC-012) — start with
[`PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md).

Clone the repositories side by side in one directory — the Docker build contexts
(`../TDOP-backend`, `../TDOP-frontend`) depend on that layout.

## Contents of this repository

| File | Purpose |
|---|---|
| [`PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md) | Project overview, repository map, technology stack, quick start, status (absorbed from the former umbrella index, DEC-012) |
| [`PROJECT_MANAGEMENT.md`](PROJECT_MANAGEMENT.md) | **Live source of truth**: current position, sessions, roadmap, phase tracker, decisions, risks, rules |
| [`TASK_BREAKDOWN.md`](TASK_BREAKDOWN.md) | Master Kanban (177 tasks) and all 33 phase boards |
| [`EXISTING_IMPLEMENTATION_AUDIT.md`](EXISTING_IMPLEMENTATION_AUDIT.md) | Inventory of pre-existing code and its actual state (DEC-004) |
| [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) | Engineering lifecycle, structure, stack, setup, standards, release process |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution workflow, branch naming, PRs, DoR/DoD |
| [`SECURITY.md`](SECURITY.md) | Vulnerability reporting and disclosure |
| [`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md) | Binding technical security standards |
| [`CODING_STANDARDS.md`](CODING_STANDARDS.md) | Binding coding standards (Java/Spring, React/TS, SQL, i18n, Git) |
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Contributor behavior and enforcement |
| [`CHANGELOG.md`](CHANGELOG.md) | Change history per project part + phase completion status |
| [`MAINTAINERS.md`](MAINTAINERS.md) | Owners, roles, and contact placeholders |
| [`README_PRD.md`](README_PRD.md) | Product requirements document |
| [`LICENSE`](LICENSE) | MIT license text - the single license of record for all repositories |
| [`Specs/`](Specs/) | `SRS.md`, `TDOP_MASTER_SPEC.md`, `IMPLEMENTATION & FUTURE ROADMAP.md` (+ `.docx`), `DEPLOYMENT_CHECKLIST.md` |

## How tracking works

- Six official states, in order only:
  `BACKLOG → TO DO → IN PROGRESS → CODE REVIEW → TESTING → DONE` (DEC-003).
- `PROJECT_MANAGEMENT.md` + `TASK_BREAKDOWN.md` are the source of truth; the
  organization Kanban board mirrors them card-for-card. Update the files first,
  then move the board card to the same state.
- Every development session begins by reading `PROJECT_MANAGEMENT.md`
  (`Current Project Status` → latest session → current phase board) and ends by
  updating it.

## Branches

All TDOP repositories use the same model (DEC-007): `develop` (default, integration)
and `main` (releases, tagged `vX.Y.Z`). See `DEVELOPMENT_GUIDE.md` §6.

## License

MIT — see [`LICENSE`](LICENSE).
