# TDOP Maintainers and Contacts

Owners, roles, and contact points for the TDOP project (Phase 01, task P01-T15).
Contact details that cannot be verified are marked `[TBD]` — never invent them
(entry rules in `PROJECT_MANAGEMENT.md`).

## Ownership

| Level | Owner | Notes |
|---|---|---|
| Organization | GitHub organization [`Tanzanian-Opportunities`](https://github.com/Tanzanian-Opportunities) | Owns all TDOP repositories (Decision DEC-006) |
| Repository owner (maintainer of record) | GitHub account [`felix202422`](https://github.com/felix202422) | Account that created and pushes to the repositories (visible in git history); final decision authority |
| Index / overview | `TDOP-docs/PROJECT_OVERVIEW.md` | Absorbed from the former `Tanzanian_Opportunities` umbrella index, which was dissolved (DEC-012) |
| Source of truth | `TDOP-docs` | `PROJECT_MANAGEMENT.md` governs what is real |

## Roles

| Role | Responsibility | Held by |
|---|---|---|
| Project owner | Priorities, scope, phase sign-off, decisions (DEC-xxx) | Repository owner |
| Maintainer / reviewer | Code and documentation review against `CODING_STANDARDS.md`, merge to `develop` | Repository owner (additional reviewers `[TBD]`) |
| Security contact | Receives vulnerability reports, coordinates disclosure | Via GitHub private vulnerability reporting on any TDOP repository (see `SECURITY.md`) |
| Verification / moderation (platform) | Trust-workspace duties inside the product | Assigned platform users (Phase 12/14) |

## Contact points

| Purpose | Channel | Status |
|---|---|---|
| Bugs, features, tasks | GitHub issues in the relevant repository (templates provided) | Active |
| Security vulnerabilities | GitHub **private vulnerability reporting** (`Security` tab → Report a vulnerability) on any TDOP repository — do **not** open a public issue | Active (see `SECURITY.md`) |
| Conduct concerns | Report per `CODE_OF_CONDUCT.md` enforcement section | Contact address `[TBD]` |
| General / business contact | `[TBD]` — email to be provided by the project owner | `[TBD]` |

## Onboarding

1. Read `PROJECT_MANAGEMENT.md` (current position + latest session).
2. Read `DEVELOPMENT_GUIDE.md` and `CODING_STANDARDS.md`.
3. Branch from `develop`; open PRs against `develop`; never start future-phase work.

*This file is updated by the project owner; session updates are append-only in
`PROJECT_MANAGEMENT.md`.*
