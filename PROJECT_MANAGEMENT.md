# TDOP Project Management

**Project:** Tanzania Digital Opportunity Platform (TDOP)
**Repository:** https://github.com/Tanzanian-Opportunities/TDOP-docs (governance and project management)
**Component repositories:** [`Tanzanian_Opportunities`](https://github.com/Tanzanian-Opportunities/Tanzanian_Opportunities) (umbrella index) · [`TDOP-backend`](https://github.com/Tanzanian-Opportunities/TDOP-backend) · [`TDOP-frontend`](https://github.com/Tanzanian-Opportunities/TDOP-frontend) · [`TDOP-infra`](https://github.com/Tanzanian-Opportunities/TDOP-infra) · [`TDOP-mobile`](https://github.com/Tanzanian-Opportunities/TDOP-mobile) · [`TDOP-docs`](https://github.com/Tanzanian-Opportunities/TDOP-docs)
**Live Kanban board:** https://github.com/orgs/Tanzanian-Opportunities/projects/1

> **This file is the authoritative, live source of truth for TDOP project progress.**
> Every development session (human or AI agent) begins by reading it and ends by
> updating it. No task is considered real unless it exists in this file; no work is
> considered complete unless this file says so and the Definition of Done is satisfied.
>
> Agent/developer entry procedure:
> 1. Read `Current Project Status` and `CURRENT PROJECT POSITION`.
> 2. Read `LIVE DEVELOPMENT SESSION` (latest session) and the current phase's board.
> 3. Check dependencies and the Definition of Ready.
> 4. Continue only from the current project position — never start future-phase work.
> 5. Update sessions, task states, changelog, and logs when meaningful work occurs.

Related documents: [`TASK_BREAKDOWN.md`](TASK_BREAKDOWN.md) (177 tasks, 33 phase
boards) · [`EXISTING_IMPLEMENTATION_AUDIT.md`](EXISTING_IMPLEMENTATION_AUDIT.md) ·
[`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) ·
[`CONTRIBUTING.md`](CONTRIBUTING.md) · [`SECURITY.md`](SECURITY.md) ·
[`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md) · [`CHANGELOG.md`](CHANGELOG.md)

---

## Current Project Status

| Field | Value |
|---|---|
| Current Phase | PHASE 01 — Project Initiation |
| Overall Status | IN PROGRESS |
| Overall Progress | 6% |
| Current Session | Session 03 |
| Last Updated | 2026-09-30 13:45 |
| Current Objective | Establish the project governance and documentation foundation |
| Current Blocker | None |
| Next Action | Verify audit evidence (P01-T12), then add issue/PR templates, CI skeleton, and owner/contact definitions (P01-T13 – P01-T15) |

---

## 1. Project Overview

### 1.1 Identity

| Field | Value |
|---|---|
| Project name | Tanzania Digital Opportunity Platform |
| Short name | TDOP |
| Purpose | Connect opportunity seekers with trusted opportunities and organizations through discovery, verification, moderation, application tracking, notifications, personalization, governance, analytics, and (later) intelligent and externally sourced opportunity services |
| Priorities | Trust · Opportunity discovery · Verification · Transparency · Security · Accessibility · Reliability · Maintainability · Explainability · User privacy · Responsible technology |
| Repository layout | Multi-repository organization [`Tanzanian-Opportunities`](https://github.com/Tanzanian-Opportunities): `TDOP-backend` (Java 21, Spring Boot 3.3, PostgreSQL, Flyway) · `TDOP-frontend` (React 18, TypeScript, Vite, Tailwind) · `TDOP-infra` (Docker Compose, Nginx) · `TDOP-docs` (governance, specs, this file) · `TDOP-mobile` (planned) · `Tanzanian_Opportunities` (umbrella index) |
| License | MIT (`LICENSE`, declared in `README.md`) — see Decision DEC-001 |

### 1.2 Governance document set

| File | Purpose |
|---|---|
| `PROJECT_MANAGEMENT.md` | Live Kanban, phases, sessions, logs (this file) |
| `DEVELOPMENT_GUIDE.md` | Engineering lifecycle and standards |
| `CONTRIBUTING.md` | Contribution workflow and merge requirements |
| `SECURITY.md` | Vulnerability reporting and disclosure |
| `SECURITY_STANDARDS.md` | Binding technical security standards |
| `CODE_OF_CONDUCT.md` | Contributor behavior and enforcement |
| `CHANGELOG.md` | Change history; changes must never be silently omitted |
| `LICENSE` | MIT license text |
| `TASK_BREAKDOWN.md` | Master Kanban (177 tasks) and all 33 phase boards (extracted from this file, §6/§7) |
| `EXISTING_IMPLEMENTATION_AUDIT.md` | Inventory of pre-existing code (extracted from this file, §16) |

### 1.3 Official Kanban states

Tasks move through exactly these states, in order, and no others:

```text
BACKLOG → TO DO → IN PROGRESS → CODE REVIEW → TESTING → DONE
```

- If work is blocked, the task keeps its current state and a blocker is recorded in
  §12 (Blocker Log).
- Phase-level status uses `BACKLOG`, `TO DO`, `IN PROGRESS`, or `DONE`.
- Custom statuses ("Started", "Almost Done", "Waiting", …) are forbidden.

### 1.4 Progress calculation method (documented)

```text
Phase Progress   = DONE tasks ÷ total tasks in phase × 100,
                   rounded to the nearest 25% step (0% / 25% / 50% / 75% / 100%)

Overall Progress = total DONE tasks ÷ total tasks in all phases × 100,
                   rounded to the nearest whole percent
```

Progress is computed from completed tasks only — never estimated. Example (current):
Phase 01 has 15 tasks, 11 DONE → 73.3% → **75%**. Project total: 177 tasks, 11 DONE →
6.2% → **6%**.

---

## 2. CURRENT PROJECT POSITION

```text
Current Phase:
PHASE 01 — Project Initiation

Phase Progress:
75%   (11 of 15 tasks DONE)

Current Kanban Column:
IN PROGRESS

Current Task:
P01-T12 — Verify audit evidence against source files

Completed:
P01-T01 Formalize MIT license
P01-T02 Create CHANGELOG.md
P01-T03 Create CODE_OF_CONDUCT.md
P01-T04 Create SECURITY.md
P01-T05 Create SECURITY_STANDARDS.md
P01-T06 Create CONTRIBUTING.md
P01-T07 Create DEVELOPMENT_GUIDE.md
P01-T08 Initialize PROJECT_MANAGEMENT.md
P01-T09 Documentation consistency validation
P01-T10 Draft existing-implementation audit
P01-T11 Initialize decision, risk, and blocker logs

Remaining:
P01-T12 Verify audit evidence          (IN PROGRESS)
P01-T13 Add issue and PR templates     (TO DO)
P01-T14 Add CI skeleton                (TO DO)
P01-T15 Define owners and contacts     (TO DO)

Blocker:
None

Next:
Finish P01-T12, then P01-T13 – P01-T15; PHASE 01 exits when its exit criteria are met

Last Completed Phase:
(none — PHASE 01 is the first phase)

Next Phase:
PHASE 02 — Requirements Engineering
```

---

## 3. LIVE DEVELOPMENT SESSION

Historical sessions are append-only. **Never delete or overwrite a past session.**
A new session is appended as `Session 02`, `Session 03`, …

### Session 01

Date: 2026-09-30

Phase:
PHASE 01 — Project Initiation

Objective:
Establish the complete project governance and live project-management documentation
foundation for TDOP.

Tasks Started:
- P01-T01 … P01-T11 (governance documentation set)
- P01-T12 (audit evidence verification)

Tasks Completed:
- P01-T01 Formalize MIT license
- P01-T02 Create CHANGELOG.md
- P01-T03 Create CODE_OF_CONDUCT.md
- P01-T04 Create SECURITY.md
- P01-T05 Create SECURITY_STANDARDS.md
- P01-T06 Create CONTRIBUTING.md
- P01-T07 Create DEVELOPMENT_GUIDE.md
- P01-T08 Initialize PROJECT_MANAGEMENT.md (this file)
- P01-T09 Documentation consistency validation
- P01-T10 Draft existing-implementation audit
- P01-T11 Initialize decision, risk, and blocker logs

Files Changed:
- `LICENSE` (created)
- `CHANGELOG.md` (created)
- `CODE_OF_CONDUCT.md` (created)
- `SECURITY.md` (created)
- `SECURITY_STANDARDS.md` (created)
- `CONTRIBUTING.md` (created)
- `DEVELOPMENT_GUIDE.md` (created)
- `PROJECT_MANAGEMENT.md` (created)
- `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `PROJECT_MANAGEMENT.md`,
  `Docs/DEPLOYMENT_CHECKLIST.md` — repository URLs updated after the transfer to the
  `Tanzanian-Opportunities` organization
- `CHANGELOG.md` — transfer documented

Tests Run:
- Documentation consistency validation (see §15 Change History for the checklist):
  file existence (8/8), phase-sequence count (33), phase-name match, Kanban-state
  set (6 states), cross-document references, DoR/DoD consistency, initial-state
  consistency.
- No code tests applicable (documentation-only change set).

Issues Found:
- `README.md` declared "License: MIT" but no `LICENSE` file existed → fixed (P01-T01).
- No `.github/workflows` CI configuration exists → recorded as P01-T14 (TO DO).
- No issue/PR templates exist → recorded as P01-T13 (TO DO).
- `Docs/IMPLEMENTATION & FUTURE ROADMAP.md` contains an older 7-phase planning model;
  the 33-phase sequence in this file is authoritative (DEC-002).

Blockers:
- None.

Decisions Made:
- DEC-001 MIT license formalized (see §14)
- DEC-002 33-phase roadmap is authoritative
- DEC-003 Six-state Kanban is the only permitted workflow
- DEC-004 Existing code is audited, never auto-credited as phase completion
- DEC-005 Technology stack of record confirmed from repository
- DEC-006 Repository transferred to the `Tanzanian-Opportunities` GitHub organization

Next Action:
Complete P01-T12, then P01-T13 – P01-T15; when Phase 01 exit criteria are satisfied,
move PHASE 01 to DONE and PHASE 02 to TO DO.

Developer / Agent:
Maintainer (repository owner) with AI coding-assist session.

### Session 02

Date: 2026-09-30

Phase:
PHASE 01 — Project Initiation

Objective:
Owner-directed restructure: split the monorepo into component repositories with
history, establish the organization-level GitHub Kanban board as the live mirror of
this tracker, and keep every document consistent with the new layout.

Tasks Started:
- P01-T12 (continued — audit evidence references re-pointed to the extracted file)

Tasks Completed:
- None from the 177-task set (restructuring is governance/infrastructure work
  directed by the owner outside the phase task list; no task states changed).

Files Changed:
- Repository split executed with `git subtree split` (history preserved):
  `TDOP-backend`, `TDOP-frontend`, `TDOP-infra`, and `Docs` exported from the
  umbrella into `Tanzanian-Opportunities/TDOP-backend`, `TDOP-frontend`,
  `TDOP-infra`, and `TDOP-docs`; `TDOP-mobile` created (planned, stack TBD).
  The umbrella `Tanzanian_Opportunities` repository remains as an index (DEC-007).
- `PROJECT_MANAGEMENT.md` slimmed: §6/§7 (Master Kanban + 33 phase boards) moved to
  `TASK_BREAKDOWN.md`; §16 (audit) moved to `EXISTING_IMPLEMENTATION_AUDIT.md`.
- Governance set, `README_PRD.md`, and `LICENSE` relocated to `TDOP-docs`; specs
  moved under `Specs/`.
- Org Kanban board created: https://github.com/orgs/Tanzanian-Opportunities/projects/1
  (`TDOP Delivery`, views `Kanban Board` + `All Tasks`).

Tests Run:
- Documentation consistency validation re-run for the multi-repository layout.
- Board verified via GitHub API: 177 cards, status distribution 162 BACKLOG /
  3 TO DO / 1 IN PROGRESS / 11 DONE — matches `TASK_BREAKDOWN.md` exactly.

Issues Found:
- GitHub's built-in project `Status` field cannot represent the six official states
  through the API (no option mutations) → custom field `TDOP Status` created with
  the six ordered states; the board view's columns are set to that field.
- `check_db.ps1` contained a plaintext database password → scrubbed to an
  environment-variable prompt before inclusion in `TDOP-infra`.

Blockers:
- None.

Decisions Made:
- DEC-007 Multi-repository split with umbrella index repository and an
  organization Kanban board mirroring `TASK_BREAKDOWN.md` (see §14)

Next Action:
Continue P01-T12 (verify every audit row against source files), then P01-T13 –
P01-T15.

Developer / Agent:
Maintainer (repository owner) with AI coding-assist session.

---

### Session 03

Date: 2026-09-30

Phase:
PHASE 01 - Project Initiation

Objective:
Finish the DEC-007 multi-repository split: assemble `TDOP-docs`, carry the pending
backend working-tree changes into `TDOP-backend`, give every repository its
README/LICENSE/branch setup with `develop` as default, and reduce the umbrella to
its index README.

Tasks Started:
- None new (same owner-directed restructure outside the phase task list).

Tasks Completed:
- None from the 177-task set (no task states changed).

Files Changed:
- `TDOP-docs` assembled and pushed: governance set, `Specs/`, `TASK_BREAKDOWN.md`,
  `EXISTING_IMPLEMENTATION_AUDIT.md`, slimmed `PROJECT_MANAGEMENT.md`, README index.
- `TDOP-backend`: uncommitted WIP carried as commits on `develop` (JWT/error-handling
  hardening, expanded test suites, H2/surefire test fix, new
  `DeadlineReminderRepository`); duplicate Flyway `V10`/`V11` renumbered to
  `V13`/`V14`; absolute README links; portable `run_backend.ps1`/`run_backend.bat`;
  MIT `LICENSE`.
- `TDOP-frontend`: README links made absolute, portable `run_frontend.bat`,
  MIT `LICENSE`.
- `TDOP-infra`: new README (sibling-clone layout, services/environment tables), MIT
  `LICENSE`, smoke-check helpers `check_db.ps1`/`check_db.sql`/`check_servers.ps1`
  (plaintext password removed - reads `PGPASSWORD`).
- `TDOP-mobile`: initial README (stack TBD by design) + `LICENSE` + `.gitignore`.
- Umbrella `Tanzanian_Opportunities`: content removed (422 paths staged), README
  rewritten as the repository-map index; local helper-script copies deleted after
  their portable versions were committed to the component repositories.

Tests Run:
- `TDOP-backend`: `mvn test` - 89 tests, 0 failures, BUILD SUCCESS (JAVA_HOME set
  to the local JDK 26 toolchain).
- Board verified via GitHub API during population: 177 cards, 162 BACKLOG /
  3 TO DO / 1 IN PROGRESS / 11 DONE.
- Documentation validator updated for the multi-repository layout and executed
  (see final session report for results).

Issues Found:
- The umbrella working tree still carried the backend WIP as uncommitted
  modifications; it was the live development state, so it was committed to
  `TDOP-backend` before the umbrella content was removed - nothing was lost.
- `TDOP-frontend/README.md` used relative sibling links that break on GitHub; fixed
  to full URLs (backend/infra/docs done the same way).

Blockers:
- None.

Decisions Made:
- DEC-007 (continuation): every repository defaults to `develop`; `main` keeps the
  import snapshot as the release baseline.

Next Action:
Run P01-T12 - P01-T15 (verify audit rows against source files), then Phase 02.

Developer / Agent:
Maintainer (repository owner) with AI coding-assist session.

---

## 4. Master Roadmap

Official phase sequence — do **not** rename, reorder, remove, merge, or skip phases:

```text
FOUNDATION
  Phase 01 → Phase 07
    PHASE 01 — Project Initiation
    PHASE 02 — Requirements Engineering
    PHASE 03 — System Analysis
    PHASE 04 — System Architecture
    PHASE 05 — Database Design
    PHASE 06 — API & Contract Design
    PHASE 07 — Development Environment

CORE PLATFORM
  Phase 08 → Phase 20
    PHASE 08 — Backend Foundation
    PHASE 09 — Frontend Foundation
    PHASE 10 — Authentication & Authorization
    PHASE 11 — User & Profile Module
    PHASE 12 — Organization Module
    PHASE 13 — Opportunity Core
    PHASE 14 — Trust & Verification
    PHASE 15 — Discovery & Search
    PHASE 16 — Application Engine
    PHASE 17 — Notification System
    PHASE 18 — Deadline & Freshness
    PHASE 19 — Personalization & Matching
    PHASE 20 — Administration & Governance

INTELLIGENCE & ECOSYSTEM
  Phase 21 → Phase 26
    PHASE 21 — Analytics & Outcomes
    PHASE 22 — Advanced Data Quality & Source Management
    PHASE 23 — External Opportunity Ingestion
    PHASE 24 — Advanced Intelligence / AI
    PHASE 25 — Communication Expansion
    PHASE 26 — Subscription / Business Model

PRODUCTION READINESS
  Phase 27 → Phase 30
    PHASE 27 — Complete Security Hardening
    PHASE 28 — Complete Testing
    PHASE 29 — Performance & Reliability
    PHASE 30 — Deployment & CI/CD

RELEASE
  Phase 31 → Phase 32
    PHASE 31 — Beta Release
    PHASE 32 — Production Launch

EVOLUTION
  Phase 33
    PHASE 33 — Continuous Improvement
```

Stage flow:

```text
FOUNDATION (01–07)
   ↓
CORE PLATFORM (08–20)
   ↓
INTELLIGENCE & ECOSYSTEM (21–26)
   ↓
PRODUCTION READINESS (27–30)
   ↓
RELEASE (31–32)
   ↓
EVOLUTION (33)
```

---

## 5. Phase Tracker

Progress = DONE tasks ÷ total tasks, rounded to the nearest 25% step (§1.4).

| Phase | Name | Status | Progress | Dependencies | Blockers |
| --- | --- | --- | ---: | --- | --- |
| 01 | Project Initiation | IN PROGRESS | 75% | — | None |
| 02 | Requirements Engineering | BACKLOG | 0% | 01 | None |
| 03 | System Analysis | BACKLOG | 0% | 02 | None |
| 04 | System Architecture | BACKLOG | 0% | 03 | None |
| 05 | Database Design | BACKLOG | 0% | 04 | None |
| 06 | API & Contract Design | BACKLOG | 0% | 05 | None |
| 07 | Development Environment | BACKLOG | 0% | 06 | None |
| 08 | Backend Foundation | BACKLOG | 0% | 07 | None |
| 09 | Frontend Foundation | BACKLOG | 0% | 07 | None |
| 10 | Authentication & Authorization | BACKLOG | 0% | 08, 09 | None |
| 11 | User & Profile Module | BACKLOG | 0% | 10 | None |
| 12 | Organization Module | BACKLOG | 0% | 11 | None |
| 13 | Opportunity Core | BACKLOG | 0% | 12 | None |
| 14 | Trust & Verification | BACKLOG | 0% | 13 | None |
| 15 | Discovery & Search | BACKLOG | 0% | 13 | None |
| 16 | Application Engine | BACKLOG | 0% | 13 | None |
| 17 | Notification System | BACKLOG | 0% | 16 | None |
| 18 | Deadline & Freshness | BACKLOG | 0% | 13 | None |
| 19 | Personalization & Matching | BACKLOG | 0% | 15 | None |
| 20 | Administration & Governance | BACKLOG | 0% | 14 | None |
| 21 | Analytics & Outcomes | BACKLOG | 0% | 20 | None |
| 22 | Advanced Data Quality & Source Management | BACKLOG | 0% | 21 | None |
| 23 | External Opportunity Ingestion | BACKLOG | 0% | 22 | None |
| 24 | Advanced Intelligence / AI | BACKLOG | 0% | 19, 23 | None |
| 25 | Communication Expansion | BACKLOG | 0% | 17 | None |
| 26 | Subscription / Business Model | BACKLOG | 0% | 20 | None |
| 27 | Complete Security Hardening | BACKLOG | 0% | 26 | None |
| 28 | Complete Testing | BACKLOG | 0% | 27 | None |
| 29 | Performance & Reliability | BACKLOG | 0% | 28 | None |
| 30 | Deployment & CI/CD | BACKLOG | 0% | 29 | None |
| 31 | Beta Release | BACKLOG | 0% | 30 | None |
| 32 | Production Launch | BACKLOG | 0% | 31 | None |
| 33 | Continuous Improvement | BACKLOG | 0% | 32 | None |

**Phase transition rule:** a phase becomes `DONE` only when its exit criteria (§7) are
satisfied. Then `Previous Phase → DONE`, `Next Phase → TO DO`, and §2 (Current Project
Position) is updated in the same change set.

---


## 6. Master Kanban - moved to TASK_BREAKDOWN.md

All 177 tasks across all 33 phases now live in [TASK_BREAKDOWN.md](TASK_BREAKDOWN.md) (Master Kanban table plus all 33 phase boards, original section 6/7 numbering preserved), and every task is mirrored as a card on the org Kanban board: https://github.com/orgs/Tanzanian-Opportunities/projects/1

Task states are updated in TASK_BREAKDOWN.md here, then the matching board card is moved to the same state.

---

## 7. Phase Kanban Boards - moved to TASK_BREAKDOWN.md

The 33 phase specification records and their Kanban boards moved to [TASK_BREAKDOWN.md](TASK_BREAKDOWN.md). Phase exit criteria referenced by sections 10, 17, and 18 are in that file under section 7, PHASE nn.

## 8. Current Sprint / Work Cycle

| Field | Value |
|---|---|
| Work cycle | Cycle 01 |
| Phase | PHASE 01 — Project Initiation |
| Goal | Establish the complete governance and project-management foundation |
| Tasks in scope | P01-T01 – P01-T15 |
| Definition of Ready applied | Requirement (master governance brief) understood; acceptance criteria = the eight files + validation; no external dependencies; owner assigned |
| Exit criteria | All 15 tasks DONE; consistency validation passed; no open blockers |
| Status | IN PROGRESS (11/15 DONE, 1 IN PROGRESS, 3 TO DO) |

Future cycles are appended here (Cycle 02, Cycle 03, …) — never delete a cycle record.

---

## 9. Definition of Ready

A task may move from `TO DO` to `IN PROGRESS` only when **all** of the following hold:

- [ ] Requirement understood
- [ ] Acceptance criteria defined
- [ ] Dependencies identified (and `DONE`, unless the task is explicit parallel preparation)
- [ ] Relevant design/spec available (or explicitly marked "no design needed")
- [ ] Required environment available (per `DEVELOPMENT_GUIDE.md` §4)
- [ ] Task has an owner

If any item fails, the task stays in `TO DO`/`BACKLOG` and the missing item is recorded
as a blocker (§12).

---

## 10. Definition of Done

A task may move to `DONE` only when **all applicable** items hold:

- [ ] Implementation complete
- [ ] Code follows standards (`DEVELOPMENT_GUIDE.md`)
- [ ] Tests written
- [ ] Tests pass
- [ ] Security considered (`SECURITY_STANDARDS.md` applicable sections)
- [ ] Documentation updated
- [ ] Code reviewed
- [ ] No unresolved blocker
- [ ] `CHANGELOG.md` updated when required
- [ ] Project management updated (`PROJECT_MANAGEMENT.md`)

Applicability: documentation-only tasks may mark *Tests written/passed* and *Code
review* as applicable-with-justification (documentation consistency review) — but the
justification must be recorded in the session log, never assumed.

---

## 11. Dependencies

Hard dependency chains — a dependent task must not enter `IN PROGRESS` while its
dependency is incomplete (except explicit parallel preparation):

```text
Requirements        → Analysis → Architecture → Database → API → Backend / Frontend
PHASE 02            → 03       → 04           → 05       → 06  → 08 / 09

Authentication      → Profiles → Organizations → Opportunities → Applications
PHASE 10            → 11       → 12            → 13            → 16

Core Opportunity Platform → Discovery → Matching → AI
PHASE 13                  → 15        → 19       → 24

Stable Application → Security Hardening → Testing → Performance → Deployment
PHASE 26            → 27                → 28       → 29          → 30 → 31 → 32 → 33
```

The authoritative phase-by-phase dependency table is §5 (Phase Tracker); task-level
dependencies are in §6 (Master Kanban) and each phase board (§7).

---

## 12. Blocker Log

Status values: `OPEN` · `RESOLVED` · `WONT FIX`.

| Blocker ID | Date | Phase | Description | Impact | Owner | Resolution | Status |
|---|---|---|---|---|---|---|---|
| — | — | — | No blockers recorded as of 2026-09-30 (Session 01) | — | — | — | — |

Rules:

- When a task cannot proceed, keep its current Kanban state and add a row here.
- A blocker is closed only with a recorded `Resolution` and status `RESOLVED`
  (or an explicit `WONT FIX` justification in the Decision Log).
- Open blockers are surfaced in the Current Project Status dashboard.

---

## 13. PROJECT RISK REGISTER

Risks are identified possibilities, **not** statements of current fact.

Status values: `OPEN` · `MITIGATED` · `CLOSED`.

| Risk ID | Risk | Phase | Probability | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|---|
| RSK-01 | **Security** — authentication/authorization flaws expose seeker or organization data | 10, 27 | Medium | Critical | Deny-by-default RBAC, security tests (P10-T05), hardening phase, `SECURITY_STANDARDS.md` binding | Maintainer | OPEN |
| RSK-02 | **Security** — secrets committed to the repository or leaked in logs | all | Medium | High | `.env` ignored, secret scanning when CI exists (P30-T01), log rules, rotation runbook (P27-T04) | Maintainer | OPEN |
| RSK-03 | **Data quality** — stale, duplicate, or misleading opportunities erode trust | 13, 22 | High | High | Moderation workflow, freshness engine (Phase 18), duplicate detection (Phase 22), source registry | Maintainer | OPEN |
| RSK-04 | **Privacy** — personal data over-collection or exposure through analytics/logs | 11, 20, 21 | Medium | High | Data minimization rules, analytics privacy review (P21-T05), retention policy (P05-T04, P20-T05) | Maintainer | OPEN |
| RSK-05 | **Scope creep** — feature breadth outruns a small team's capacity | all | High | High | 33-phase roadmap with dependency gates; Definition of Ready; change control (P02-T06) | Maintainer | OPEN |
| RSK-06 | **Technical debt** — existing implementation accumulates undocumented shortcuts | 1–13 | High | Medium | Existing Implementation Audit (§16), standards in `DEVELOPMENT_GUIDE.md`, review before merge | Maintainer | OPEN |
| RSK-07 | **Infrastructure** — no CI/CD, backups, or monitoring yet; manual deployment errors | 29, 30 | High | High | Phase 29–30 tasks; deployment checklist; backup/restore runbook (P30-T04) | Maintainer | OPEN |
| RSK-08 | **Third-party dependency** — vulnerable or abandoned libraries (Spring, React, jjwt, Docker base images) | 27, 30 | Medium | Medium | Dependency scanning, pinned versions, patch cadence (P33-T03) | Maintainer | OPEN |
| RSK-09 | **Performance** — search/list queries degrade as opportunity volume grows | 15, 29 | Medium | Medium | Index design (P05-T03), performance tasks (P15-T02), load testing (P29-T01) | Maintainer | OPEN |
| RSK-10 | **Project management** — phase skipping or "DONE" inflation corrupts the tracker | all | Medium | High | Six-state Kanban, Definition of Done, dependency rules, session history append-only | Maintainer | OPEN |
| RSK-11 | **Delivery** — external ingestion pulls in spam, scams, or infringing content | 22, 23 | Medium | High | Source registry, sanitization, moderation gate before publishing, ingestion security review (P23-T05) | Maintainer | OPEN |
| RSK-12 | **Adoption** — beta feedback reveals product/market mismatch | 31, 32 | Medium | High | Beta phase with explicit exit review and go/no-go decision (P31-T05) | Maintainer | OPEN |

---

## 14. ARCHITECTURAL & PROJECT DECISIONS

Status values: `Accepted` · `Proposed` · `Superseded` · `Rejected`.

| Decision ID | Date | Decision | Reason | Alternatives Considered | Impact | Phase | Status |
|---|---|---|---|---|---|---|---|
| DEC-001 | 2026-09-30 | License TDOP under the **MIT License** (formalized in `LICENSE`) | The project owner already declared "License: MIT" in `README.md`; no license file existed to back the declaration | Proprietary license; "License: To Be Determined" placeholder; making no change | Repository now carries an explicit license; copyright holder recorded from commit history and amendable by the owner | 01 | Accepted |
| DEC-002 | 2026-09-30 | The **33-phase roadmap** in §4 is the authoritative project progression | A single fixed phase sequence is required for governance; the repository's older 7-phase outlines are product-planning sketches with different names | Keeping the older `Docs/IMPLEMENTATION & FUTURE ROADMAP.md` phase model; merging both models | All tracking follows the 33-phase sequence; the older roadmap remains as a historical product-planning document only | 01 | Accepted |
| DEC-003 | 2026-09-30 | Adopt the **six-state Kanban** (`BACKLOG → TO DO → IN PROGRESS → CODE REVIEW → TESTING → DONE`) as the only permitted task states | Prevents ambiguous statuses and makes project position readable at a glance | Free-form status lists; three-state to-do/done models | All boards, sessions, and definitions (DoR/DoD) use exactly these states | 01 | Accepted |
| DEC-004 | 2026-09-30 | Existing repository code is inventoried in the **Existing Implementation Audit** and never auto-credits phase completion | Pre-existing code has not been verified against phase exit criteria; claiming completion would falsify the tracker | Marking implemented features as completed phases; ignoring existing code entirely | Phases start at 0% regardless of code that exists; audit drives future verification tasks | 01 | Accepted |
| DEC-005 | 2026-09-30 | **Technology stack of record**: Java 21 / Spring Boot 3.3 / PostgreSQL / Flyway (backend), React 18 / TypeScript / Vite / Tailwind (frontend), Docker Compose / Nginx (infra) | These are the stacks actually present and declared in `README.md`, `pom.xml`, and `package.json` | Re-platforming now; treating the stack as undecided | Development standards, environment setup, and hiring/training expectations are defined for this stack | 01 | Accepted |
| DEC-006 | 2026-09-30 | Repository ownership transferred to the GitHub organization **`Tanzanian-Opportunities`** (repo name unchanged: `Tanzanian_Opportunities`) | Project owner created the organization and requested the move so the project is owned by the organization rather than a personal account | Keep the repository under the personal account; rename the repository during transfer | Clone, advisory, and documentation URLs change; GitHub redirects the old URLs; local `origin` remote updated | 01 | Accepted |
| DEC-007 | 2026-09-30 | Split the monorepo into **component repositories** (`TDOP-backend`, `TDOP-frontend`, `TDOP-infra`, `TDOP-docs`, `TDOP-mobile`) with `main` + `develop` branches each, keep `Tanzanian_Opportunities` as an **umbrella index**, and mirror all 177 tasks as cards on an **organization GitHub Projects Kanban board** (six official states as columns) | Owner decision: clearer ownership per component, history preserved via `git subtree split`, and a live board alongside the Git-based tracker | Keep the monorepo untouched; manually recreate tasks on the board | Clone instructions and paths change (sibling-cloned component repos); this file + `TASK_BREAKDOWN.md` remain the source of truth and the board mirrors them | 01 | Accepted |

---

## 15. Change History

Changes to `PROJECT_MANAGEMENT.md` itself (append-only).

| Date | Session | Change | Author |
|---|---|---|---|
| 2026-09-30 | Session 01 | File created: dashboard, position, session log, roadmap, phase tracker (33 phases), master Kanban (177 tasks), 33 phase boards, DoR/DoD, dependencies, blocker log, risk register, decision log, audit, rules, next actions | Maintainer with AI coding-assist |
| 2026-09-30 | Session 01 | Documentation consistency validation executed (results recorded in Session 01) | Maintainer with AI coding-assist |
| 2026-09-30 | Session 01 | Governance foundation committed and pushed to `origin/main` (commit `66632a3`) | Maintainer with AI coding-assist |
| 2026-09-30 | Session 01 | Repository transferred to the `Tanzanian-Opportunities` GitHub organization (DEC-006); repository URLs updated in `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, this file, and `Docs/DEPLOYMENT_CHECKLIST.md`; local `origin` remote repointed | Maintainer with AI coding-assist |
| 2026-09-30 | Session 02 | Multi-repository split executed with history (DEC-007); this file slimmed — §6/§7 extracted to `TASK_BREAKDOWN.md`, §16 extracted to `EXISTING_IMPLEMENTATION_AUDIT.md`; governance set relocated to `TDOP-docs` with specs under `Specs/` | Maintainer with AI coding-assist |
| 2026-09-30 | Session 02 | Organization Kanban board created (`Tanzanian-Opportunities/projects/1`) with 177 task cards and the six official states as columns; card statuses verified equal to this tracker | Maintainer with AI coding-assist |

Validation checklist performed for P01-T09:

- [x] All 8 governance files exist
- [x] Exactly 33 phases, names and order match the official sequence
- [x] Exactly the 6 official Kanban states used, no invented states
- [x] Phase numbers, names, and dependencies consistent between §4, §5, §6, §7
- [x] DoD consistent between this file and `CONTRIBUTING.md`
- [x] DoR consistent between this file and `CONTRIBUTING.md`
- [x] Security docs and development docs do not contradict each other
- [x] Contribution workflow matches development workflow
- [x] Changelog rules match project-management rules
- [x] Current project position matches the initial state (PHASE 01, IN PROGRESS)

---


## 16. EXISTING IMPLEMENTATION AUDIT - moved to EXISTING_IMPLEMENTATION_AUDIT.md

The full inventory of pre-existing code, its actual state, and evidence paths moved to [EXISTING_IMPLEMENTATION_AUDIT.md](EXISTING_IMPLEMENTATION_AUDIT.md) (original section 16 numbering noted in that file). Task **P01-T12** (verify every row against actual source files) remains IN PROGRESS.

---

## 17. Development Rules

Binding rules for every developer and AI agent working on TDOP:

1. Read this file first; determine current phase, Kanban state, and active task.
2. Check dependencies and the Definition of Ready before starting work.
3. Continue only from the current project position — never start future-phase features.
4. Update this file after meaningful work: task states, dates, progress, session log.
5. Record files changed, tests run, blockers, and decisions in the session.
6. Update `CHANGELOG.md` when a change is user-visible, security-relevant, breaking,
   or infrastructure/database related.
7. Update documentation when behavior changes.
8. Never mark unfinished work `DONE`.
9. Never silently skip a phase or reorder the phase sequence.
10. Never delete historical session information — append `Session 02`, `Session 03`, …
11. Never invent statuses outside the six official states.
12. Never invent contact details, team members, dates, or technologies.
13. A phase becomes `DONE` only when its exit criteria (§7) are satisfied.
14. If blocked, keep the Kanban state and log the blocker (§12).
15. Record significant architectural/project choices in the Decision Log (§14).

---

## 18. Next Actions

Immediate (this work cycle, PHASE 01):

1. **P01-T12** — Verify every row of the Existing Implementation Audit (§16) against
   actual source files; correct evidence paths; keep the task `IN PROGRESS` until the
   whole inventory is file-verified.
2. **P01-T13** — Create issue and pull-request templates under `.github/`.
3. **P01-T14** — Create a CI skeleton workflow (build, lint, test) under
   `.github/workflows/`.
4. **P01-T15** — Define maintainer roles and fill the `[TBD]` contact placeholders in
   `SECURITY.md` and `CODE_OF_CONDUCT.md`.
5. When all Phase 01 exit criteria (§7, PHASE 01) are met: mark Phase 01 `DONE`,
   record the transition in §15, and move **PHASE 02 — Requirements Engineering** to
   `TO DO`.

Standing rules for the next session:

- Read this file first; continue only from the current position (§2).
- Append `Session 02` — never edit Session 01.
- Update task states, phase progress, changelog, and logs as work happens.
