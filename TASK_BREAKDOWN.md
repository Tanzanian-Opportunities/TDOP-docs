# TDOP Task Breakdown - 177 Tasks / 33 Phases

**Project:** Tanzania Digital Opportunity Platform (TDOP)
**Source:** extracted from [PROJECT_MANAGEMENT.md](PROJECT_MANAGEMENT.md) sections 6 (Master Kanban) and 7 (Phase Kanban Boards); original section numbering is preserved below.
**Live mirror:** every task here is a card on the org Kanban board: https://github.com/orgs/Tanzanian-Opportunities/projects/1

> The Kanban board mirrors this file. Update PROJECT_MANAGEMENT.md / this file first (per its rules), then move the card on the board.

> **Path note (multi-repository layout, DEC-007):** `Docs/` references in task descriptions mean this repository (`TDOP-docs`); specifications now live under `Specs/` (e.g. `Docs/DEPLOYMENT_CHECKLIST.md` = `Specs/DEPLOYMENT_CHECKLIST.md`). `TDOP-backend/`, `TDOP-frontend/`, `TDOP-infra/` mean those sibling repositories.

---

## 6. Master Kanban

All project tasks across all 33 phases, grouped hierarchically by phase.

Legend: **Priority** — `P0` current-phase critical · `P1` critical path · `P2`
important · `P3` later/optional. **Owner** — `—` unassigned. Dates are `YYYY-MM-DD`;
`—` = not started/completed. **Created** = 2026-09-30 for the initial task set.

### PHASE 01 — Project Initiation

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P01-T01 | 01 | Formalize MIT license | Add LICENSE matching README declaration | P0 | — | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T02 | 01 | Create changelog | CHANGELOG.md with categories and recording rules | P0 | — | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T03 | 01 | Create code of conduct | Behavior standards, reporting, enforcement | P0 | — | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T04 | 01 | Create security policy | SECURITY.md reporting, severity, response | P0 | — | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T05 | 01 | Create security standards | Binding technical security rules | P0 | P01-T04 | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T06 | 01 | Create contribution guide | Workflow, branches, PRs, DoR/DoD | P0 | P01-T04 | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T07 | 01 | Create development guide | Lifecycle, stack, standards, Kanban rules | P0 | P01-T05, P01-T06 | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T08 | 01 | Initialize project tracker | PROJECT_MANAGEMENT.md live Kanban system | P0 | P01-T02, P01-T07 | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T09 | 01 | Validate documentation consistency | Existence, phase count, states, cross-refs | P0 | P01-T01 – P01-T08 | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T10 | 01 | Draft existing-implementation audit | Inventory existing code against 33 phases | P1 | P01-T08 | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T11 | 01 | Initialize governance logs | Seed decision, risk, and blocker logs | P1 | P01-T08 | DONE | Maintainer | 2026-09-30 | 2026-09-30 | 2026-09-30 | — | — |
| P01-T12 | 01 | Verify audit evidence | Confirm audit rows against source files | P1 | P01-T10 | IN PROGRESS | Maintainer | 2026-09-30 | 2026-09-30 | — | — | Verify remaining file-level evidence |
| P01-T13 | 01 | Add issue and PR templates | Create .github issue and PR templates | P1 | P01-T06 | TO DO | — | 2026-09-30 | — | — | — | Schedule in Session 02 |
| P01-T14 | 01 | Add CI skeleton | Build, lint, test workflow in .github/workflows | P1 | P01-T07 | TO DO | — | 2026-09-30 | — | — | — | Schedule in Session 02 |
| P01-T15 | 01 | Define owners and contacts | Maintainer roles and [TBD] contact placeholders | P2 | — | TO DO | — | 2026-09-30 | — | — | — | Owner fills placeholders |

### PHASE 02 — Requirements Engineering

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P02-T01 | 02 | Consolidate requirements baseline | Turn PRD and specs into versioned requirements | P1 | Phase 01 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 02 start |
| P02-T02 | 02 | Assign requirement IDs | IDs and acceptance criteria for core journeys | P1 | P02-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P02-T01 |
| P02-T03 | 02 | Define non-functional requirements | Performance, accessibility, security, i18n targets | P1 | P02-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P02-T01 |
| P02-T04 | 02 | Build traceability matrix | Map requirements to phases and tasks | P1 | P02-T02, P02-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P02-T03 |
| P02-T05 | 02 | Requirements review and sign-off | Stakeholder acceptance of baseline | P1 | P02-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P02-T04 |
| P02-T06 | 02 | Establish change-control rules | How requirements change after sign-off | P2 | P02-T05 | BACKLOG | — | 2026-09-30 | — | — | — | After P02-T05 |

### PHASE 03 — System Analysis

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P03-T01 | 03 | Gap analysis | Existing system vs approved requirements | P1 | Phase 02 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 03 start |
| P03-T02 | 03 | Use-case analysis | Seeker, org, trust, admin journeys modeled | P1 | P03-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P03-T01 |
| P03-T03 | 03 | State-machine and data-flow analysis | Opportunity, application, report flows | P1 | P03-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P03-T02 |
| P03-T04 | 03 | Feasibility analysis | Technical, operational, cost feasibility | P2 | P03-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P03-T01 |
| P03-T05 | 03 | Update risk register | Fold analysis findings into risk register | P2 | P03-T03, P03-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P03-T04 |

### PHASE 04 — System Architecture

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P04-T01 | 04 | Document target architecture | Layered backend, SPA frontend, infra baseline | P1 | Phase 03 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 04 start |
| P04-T02 | 04 | Define module boundaries | Package boundaries and API surface | P1 | P04-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P04-T01 |
| P04-T03 | 04 | Record architecture decisions | Enter decisions into the decision log | P1 | P04-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P04-T02 |
| P04-T04 | 04 | Define quality attributes | Scalability, availability, maintainability targets | P2 | P04-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P04-T01 |
| P04-T05 | 04 | Architecture review and sign-off | Acceptance of architecture baseline | P1 | P04-T03, P04-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P04-T04 |

### PHASE 05 — Database Design

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P05-T01 | 05 | Logical ER model | Core entities and relationships | P1 | Phase 04 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 05 start |
| P05-T02 | 05 | Review existing schema | Audit migrations V1–V14 against the model | P1 | P05-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P05-T01 |
| P05-T03 | 05 | Index and constraint design | Indexes, keys, referential integrity | P1 | P05-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P05-T02 |
| P05-T04 | 05 | Retention and privacy design | Data retention and personal-data handling | P2 | P05-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P05-T01 |
| P05-T05 | 05 | Migration strategy | Flyway versioning and safe-change rules | P1 | P05-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P05-T02 |
| P05-T06 | 05 | Database design sign-off | Acceptance of schema design baseline | P1 | P05-T03, P05-T04, P05-T05 | BACKLOG | — | 2026-09-30 | — | — | — | After P05-T05 |

### PHASE 06 — API & Contract Design

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P06-T01 | 06 | Endpoint inventory | Full /api/v1 resource and endpoint list | P1 | Phase 05 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 06 start |
| P06-T02 | 06 | Error and DTO conventions | Standard error contract and DTO rules | P1 | P06-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P06-T01 |
| P06-T03 | 06 | OpenAPI contract maintenance | Generate and keep springdoc contract current | P1 | P06-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P06-T02 |
| P06-T04 | 06 | Versioning and pagination rules | API versioning, pagination, filtering standards | P1 | P06-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P06-T01 |
| P06-T05 | 06 | Contract review with consumers | Frontend confirms contract fit | P1 | P06-T03, P06-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P06-T04 |

### PHASE 07 — Development Environment

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P07-T01 | 07 | Standardize local setup | Verify README setup and .env.example files | P1 | Phase 06 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 07 start |
| P07-T02 | 07 | Configure lint and format tooling | ESLint, Prettier, Java style consistency | P1 | P07-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P07-T01 |
| P07-T03 | 07 | Docker dev profile | Reproducible local orchestration | P1 | P07-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P07-T01 |
| P07-T04 | 07 | Seed data strategy | Deterministic, environment-guarded seed data | P2 | P07-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P07-T03 |
| P07-T05 | 07 | Onboarding dry-run | New-developer setup test and doc fixes | P2 | P07-T02, P07-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P07-T04 |

### PHASE 08 — Backend Foundation

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P08-T01 | 08 | Standardize package structure | Align controllers/services/repos with guide | P1 | Phase 07 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 08 start |
| P08-T02 | 08 | Global exception handling | Unified error responses, no stack traces | P1 | P08-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P08-T01 |
| P08-T03 | 08 | Logging standards | Logback config, levels, security-event logging | P1 | P08-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P08-T01 |
| P08-T04 | 08 | Configuration profiles | Dev/prod profiles and secret handling | P1 | P08-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P08-T01 |
| P08-T05 | 08 | Backend test harness | Test fixtures, H2 setup, common helpers | P1 | P08-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P08-T02 |

### PHASE 09 — Frontend Foundation

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P09-T01 | 09 | Component baseline | Shared components and design tokens | P1 | Phase 07 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 09 start |
| P09-T02 | 09 | Route structure and layouts | Router config and page shells | P1 | P09-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P09-T01 |
| P09-T03 | 09 | API service layer | Standardize axios client and error mapping | P1 | P09-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P09-T02 |
| P09-T04 | 09 | Auth state and route guards | Central auth store and guard components | P1 | P09-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P09-T03 |
| P09-T05 | 09 | i18n and frontend test harness | Complete en/sw coverage; Vitest baseline | P2 | P09-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P09-T02 |

### PHASE 10 — Authentication & Authorization

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P10-T01 | 10 | Complete auth flows | Register, login, refresh, logout, reset, verify | P1 | Phase 08, Phase 09 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 10 start |
| P10-T02 | 10 | Enforce RBAC on endpoints | Deny-by-default endpoint authorization | P1 | P10-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P10-T01 |
| P10-T03 | 10 | Refresh-token revocation | Rotation, reuse detection, logout revocation | P1 | P10-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P10-T01 |
| P10-T04 | 10 | Verify lockout and rate limits | Lockout, throttling, token-expiry behavior | P1 | P10-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P10-T01 |
| P10-T05 | 10 | Auth security tests | 401/403, expired and revoked token coverage | P1 | P10-T02, P10-T03, P10-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P10-T04 |

### PHASE 11 — User & Profile Module

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P11-T01 | 11 | Profile CRUD and completeness | Profile read/update and completeness rules | P1 | Phase 10 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 11 start |
| P11-T02 | 11 | Career data management | Education, skills, experience, career goals | P1 | P11-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P11-T01 |
| P11-T03 | 11 | Document upload security review | User document handling per security standards | P1 | P11-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P11-T01 |
| P11-T04 | 11 | Profile privacy settings | Visibility controls for profile data | P2 | P11-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P11-T01 |
| P11-T05 | 11 | Profile module tests | Unit and integration coverage | P1 | P11-T02, P11-T03, P11-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P11-T04 |

### PHASE 12 — Organization Module

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P12-T01 | 12 | Organization profiles and teams | Org profile CRUD and membership | P1 | Phase 11 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 12 start |
| P12-T02 | 12 | Verification workflow completion | Evidence review, approve/reject/re-verify | P1 | P12-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P12-T01 |
| P12-T03 | 12 | Org team roles | Team roles and permission assignments | P1 | P12-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P12-T01 |
| P12-T04 | 12 | Organization isolation tests | Cross-tenant access must fail | P1 | P12-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P12-T03 |
| P12-T05 | 12 | Organization workspace UI | Complete org-facing screens | P2 | P12-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P12-T02 |

### PHASE 13 — Opportunity Core

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P13-T01 | 13 | Opportunity model alignment | Data model vs type contract in PRD/spec | P1 | Phase 12 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 13 start |
| P13-T02 | 13 | Lifecycle state-machine hardening | Draft→…→Expired transitions validated | P1 | P13-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P13-T01 |
| P13-T03 | 13 | Moderation workflow completion | Approve, reject, suspend, archive, request info | P1 | P13-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P13-T02 |
| P13-T04 | 13 | Expiry engine correctness | Closing-soon and expiry transitions | P1 | P13-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P13-T02 |
| P13-T05 | 13 | Opportunity module tests | Unit and integration coverage | P1 | P13-T03, P13-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P13-T04 |

### PHASE 14 — Trust & Verification

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P14-T01 | 14 | Evidence-based verification | Verification with evidence and audit trail | P1 | Phase 13 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 14 start |
| P14-T02 | 14 | Report investigation workflow | Create, assign, investigate, resolve, dismiss | P1 | P14-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P14-T01 |
| P14-T03 | 14 | Escalation and appeals | Escalation paths and appeal handling | P1 | P14-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P14-T02 |
| P14-T04 | 14 | Anti-fraud signal tuning | Risk signals accuracy and false-positive rate | P2 | P14-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P14-T01 |
| P14-T05 | 14 | Trust decision audit trail | Every trust decision recorded and queryable | P1 | P14-T03, P14-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P14-T04 |

### PHASE 15 — Discovery & Search

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P15-T01 | 15 | Search strategy | SQL baseline and future index decision | P1 | Phase 13 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 15 start |
| P15-T02 | 15 | Filter, sort, pagination performance | Query performance and index support | P1 | P15-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P15-T01 |
| P15-T03 | 15 | Saved items and comparison | Saved opportunities and side-by-side compare | P2 | P15-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P15-T01 |
| P15-T04 | 15 | Search relevance test set | Relevance and regression fixtures | P1 | P15-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P15-T02 |
| P15-T05 | 15 | Search analytics | Query and result instrumentation | P2 | P15-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P15-T02 |

### PHASE 16 — Application Engine

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P16-T01 | 16 | Application submission and tracking | Submit, track, and history flows | P1 | Phase 13 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 16 start |
| P16-T02 | 16 | Status transition rules | Valid application states and transitions | P1 | P16-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P16-T01 |
| P16-T03 | 16 | Organization review flow | Org-side application review and decisions | P1 | P16-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P16-T02 |
| P16-T04 | 16 | External application paths | External and email application handling | P2 | P16-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P16-T01 |
| P16-T05 | 16 | Application engine tests | Coverage for all transitions | P1 | P16-T02, P16-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P16-T03 |

### PHASE 17 — Notification System

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P17-T01 | 17 | In-app notification completeness | Events, list, read/unread behavior | P1 | Phase 16 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 17 start |
| P17-T02 | 17 | Email delivery reliability | SMTP error handling, retries, logging | P1 | P17-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P17-T01 |
| P17-T03 | 17 | Notification preferences | Per-event channel preferences | P2 | P17-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P17-T01 |
| P17-T04 | 17 | Notification templates | en/sw templates for all events | P2 | P17-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P17-T03 |
| P17-T05 | 17 | Notification tests | Delivery and preference coverage | P1 | P17-T02, P17-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P17-T04 |

### PHASE 18 — Deadline & Freshness

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P18-T01 | 18 | Deadline job robustness | Hourly scheduling reliability and idempotency | P1 | Phase 13 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 18 start |
| P18-T02 | 18 | Transition accuracy | Expiry and closing-soon correctness | P1 | P18-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P18-T01 |
| P18-T03 | 18 | Reminder correctness | Deadline reminder timing and deduplication | P1 | P18-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P18-T02 |
| P18-T04 | 18 | Freshness detection | Stale opportunity detection and re-check | P2 | P18-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P18-T02 |
| P18-T05 | 18 | Job monitoring | Failure alerting for scheduled jobs | P1 | P18-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P18-T01 |

### PHASE 19 — Personalization & Matching

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P19-T01 | 19 | Matching rule engine | Skills, interests, location matching | P1 | Phase 15 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 19 start |
| P19-T02 | 19 | Personalized feed | Profile-based opportunity feed | P1 | P19-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P19-T01 |
| P19-T03 | 19 | Similar-opportunity refinement | Improve similarity ranking | P2 | P19-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P19-T01 |
| P19-T04 | 19 | Matching evaluation metrics | Measure match quality | P1 | P19-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P19-T02 |
| P19-T05 | 19 | Recommendation explainability | Show why an item was recommended | P2 | P19-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P19-T04 |

### PHASE 20 — Administration & Governance

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P20-T01 | 20 | Admin dashboard and user management | Admin operations surface | P1 | Phase 14 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 20 start |
| P20-T02 | 20 | Permission management interface | Manage roles and permissions safely | P1 | P20-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P20-T01 |
| P20-T03 | 20 | Platform configuration governance | Controlled key-value configuration changes | P1 | P20-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P20-T01 |
| P20-T04 | 20 | Audit log queries | Searchable, tamper-resistant audit trail | P1 | P20-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P20-T01 |
| P20-T05 | 20 | Governance policies | Retention, moderation SLAs, escalation policy | P2 | P20-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P20-T03 |

### PHASE 21 — Analytics & Outcomes

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P21-T01 | 21 | Analytics event model | Defined, privacy-aware events | P2 | Phase 20 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 21 start |
| P21-T02 | 21 | Outcome model | Post-application outcome tracking | P2 | P21-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P21-T01 |
| P21-T03 | 21 | Dashboards | Seeker, organization, admin views | P2 | P21-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P21-T01 |
| P21-T04 | 21 | Analytics data validation | Accuracy checks against source data | P2 | P21-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P21-T03 |
| P21-T05 | 21 | Analytics privacy review | No personal-data leakage in metrics | P1 | P21-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P21-T02 |

### PHASE 22 — Advanced Data Quality & Source Management

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P22-T01 | 22 | Duplicate detection | Detect and handle duplicate opportunities | P2 | Phase 21 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 22 start |
| P22-T02 | 22 | Quality scoring rules | Completeness and quality scoring | P2 | P22-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P22-T01 |
| P22-T03 | 22 | Source registry | Source credibility and provenance records | P2 | P22-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P22-T01 |
| P22-T04 | 22 | Content sanitization pipeline | Normalize and sanitize ingested content | P1 | P22-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P22-T02 |
| P22-T05 | 22 | Quality metrics reporting | Data-quality dashboards and alerts | P3 | P22-T02, P22-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P22-T03 |

### PHASE 23 — External Opportunity Ingestion

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P23-T01 | 23 | Connector architecture | Pluggable source-connector design | P2 | Phase 22 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 23 start |
| P23-T02 | 23 | Ingestion pipeline | Fetch, validate, dedupe, publish | P2 | P23-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P23-T01 |
| P23-T03 | 23 | Attribution and provenance UI | Show source and last-checked date | P2 | P23-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P23-T02 |
| P23-T04 | 23 | Ingestion monitoring | Failure handling and retry reporting | P1 | P23-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P23-T02 |
| P23-T05 | 23 | Ingestion security review | SSRF, payload-size, and parser safety | P1 | P23-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P23-T02 |

### PHASE 24 — Advanced Intelligence / AI

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P24-T01 | 24 | AI scope and guardrails | Decide AI features, record decision | P2 | Phase 19, Phase 23 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 24 start |
| P24-T02 | 24 | Summarization and eligibility explanation | Summaries and eligibility rationale | P3 | P24-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P24-T01 |
| P24-T03 | 24 | Smart search and semantic matching | Semantics beyond keyword matching | P3 | P24-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P24-T01 |
| P24-T04 | 24 | Model evaluation and explainability | Quality metrics and explainability | P2 | P24-T02, P24-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P24-T03 |
| P24-T05 | 24 | AI privacy and responsible-use policy | Data-use and fairness constraints | P1 | P24-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P24-T01 |

### PHASE 25 — Communication Expansion

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P25-T01 | 25 | WhatsApp channel architecture | Design for WhatsApp delivery | P2 | Phase 17 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 25 start |
| P25-T02 | 25 | Channel integration | Implement configured channels | P2 | P25-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P25-T01 |
| P25-T03 | 25 | Multi-channel routing and preferences | Route by preference and availability | P2 | P25-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P25-T02 |
| P25-T04 | 25 | Template and compliance rules | Message templates and platform rules | P1 | P25-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P25-T02 |
| P25-T05 | 25 | Channel delivery tests | Delivery, fallback, failure coverage | P1 | P25-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P25-T03 |

### PHASE 26 — Subscription / Business Model

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P26-T01 | 26 | Plan and entitlement definition | Define plans and what each unlocks | P2 | Phase 20 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 26 start |
| P26-T02 | 26 | Payment provider decision | Choose and record payment integration | P1 | P26-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P26-T01 |
| P26-T03 | 26 | Feature gating | Server-side entitlement enforcement | P1 | P26-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P26-T02 |
| P26-T04 | 26 | Billing events and receipts | Billing history and receipts | P2 | P26-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P26-T02 |
| P26-T05 | 26 | Subscription tests | Entitlement and billing coverage | P1 | P26-T03, P26-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P26-T04 |

### PHASE 27 — Complete Security Hardening

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P27-T01 | 27 | Remediate security-standard gaps | Close every GAP in SECURITY_STANDARDS.md | P1 | Phase 26 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 27 start |
| P27-T02 | 27 | Penetration test | DAST and manual abuse-case testing | P1 | P27-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P27-T01 |
| P27-T03 | 27 | CSP and header hardening | Content-Security-Policy and header matrix | P1 | P27-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P27-T01 |
| P27-T04 | 27 | Secret management runbook | Storage, rotation, incident procedure | P1 | P27-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P27-T01 |
| P27-T05 | 27 | Dependency vulnerability remediation | Fix findings from scanning | P1 | P27-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P27-T02 |

### PHASE 28 — Complete Testing

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P28-T01 | 28 | End-to-end test suite | Critical journeys automated | P1 | Phase 27 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 28 start |
| P28-T02 | 28 | Accessibility testing | WCAG 2.2 AA verification | P1 | P28-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P28-T01 |
| P28-T03 | 28 | Cross-browser and device testing | Mobile-first browser matrix | P1 | P28-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P28-T01 |
| P28-T04 | 28 | Coverage targets and reporting | Coverage thresholds in CI | P1 | P28-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P28-T01 |
| P28-T05 | 28 | Regression suite stabilization | Flaky-test cleanup, stable baseline | P1 | P28-T02, P28-T03, P28-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P28-T04 |

### PHASE 29 — Performance & Reliability

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P29-T01 | 29 | Load testing | Baseline latency and throughput | P1 | Phase 28 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 29 start |
| P29-T02 | 29 | Query and index optimization | Fix hot queries from load tests | P1 | P29-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P29-T01 |
| P29-T03 | 29 | Caching strategy | Decide and implement caching | P2 | P29-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P29-T01 |
| P29-T04 | 29 | Resilience engineering | Retries, timeouts, graceful degradation | P1 | P29-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P29-T01 |
| P29-T05 | 29 | Monitoring and alerting | Metrics, health checks, alerts | P1 | P29-T02, P29-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P29-T03 |

### PHASE 30 — Deployment & CI/CD

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P30-T01 | 30 | CI pipeline | Build, lint, test, scan on every change | P1 | Phase 29 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 30 start |
| P30-T02 | 30 | Delivery pipeline | Repeatable deploys to environments | P1 | P30-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P30-T01 |
| P30-T03 | 30 | Infrastructure hardening | Compose/Nginx hardening, config as code | P1 | P30-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P30-T02 |
| P30-T04 | 30 | Backup and restore runbook | Tested backups and restore procedure | P1 | P30-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P30-T02 |
| P30-T05 | 30 | Deployment checklist validation | Execute Docs/DEPLOYMENT_CHECKLIST.md | P1 | P30-T03, P30-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P30-T04 |

### PHASE 31 — Beta Release

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P31-T01 | 31 | Beta scope and participants | Define scope and recruitment | P1 | Phase 30 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 31 start |
| P31-T02 | 31 | Beta deployment and monitoring | Deploy beta and watch health | P1 | P31-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P31-T01 |
| P31-T03 | 31 | Feedback collection and triage | Gather and prioritize feedback | P1 | P31-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P31-T02 |
| P31-T04 | 31 | Beta bugfix cycle | Fix blocking issues from beta | P1 | P31-T03 | BACKLOG | — | 2026-09-30 | — | — | — | After P31-T03 |
| P31-T05 | 31 | Beta exit review | Decide go/no-go for launch | P1 | P31-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P31-T04 |

### PHASE 32 — Production Launch

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P32-T01 | 32 | Pre-launch checklist | Secrets, seed data removed, HTTPS, backups | P1 | Phase 31 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 32 start |
| P32-T02 | 32 | Production deployment and smoke tests | Go live and verify critical flows | P1 | P32-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P32-T01 |
| P32-T03 | 32 | Launch communications | Announce availability honestly | P2 | P32-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P32-T02 |
| P32-T04 | 32 | Post-launch monitoring window | Watch errors, load, and user reports | P1 | P32-T02 | BACKLOG | — | 2026-09-30 | — | — | — | After P32-T02 |
| P32-T05 | 32 | Launch sign-off | Confirm production stability | P1 | P32-T03, P32-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P32-T04 |

### PHASE 33 — Continuous Improvement

| ID | Phase | Task | Description | Priority | Dependencies | Status | Owner | Created | Started | Completed | Blocker | Next Action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P33-T01 | 33 | Continuous backlog grooming | Keep tasks ready and prioritized | P2 | Phase 32 | BACKLOG | — | 2026-09-30 | — | — | — | Plan at PHASE 33 start |
| P33-T02 | 33 | Metrics-driven improvement cycles | Use analytics to drive changes | P2 | P33-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P33-T01 |
| P33-T03 | 33 | Security maintenance cadence | Regular scanning, patching, reviews | P1 | P33-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P33-T01 |
| P33-T04 | 33 | Documentation maintenance | Keep docs accurate as code changes | P2 | P33-T01 | BACKLOG | — | 2026-09-30 | — | — | — | After P33-T01 |
| P33-T05 | 33 | Quarterly roadmap review | Reassess roadmap and priorities | P2 | P33-T02, P33-T03, P33-T04 | BACKLOG | — | 2026-09-30 | — | — | — | After P33-T04 |

---

## 7. Phase Kanban Boards

Every phase has its own specification record and its own Kanban board using the six
official states. Phases not yet started carry all tasks in `BACKLOG`.

### PHASE 01 — Project Initiation

**Objective:** Establish project governance, licensing, and the live project-management foundation.
**Description:** Creates the eight governance documents, the Git-based Kanban system, the decision/risk/blocker logs, and the first audit of existing code.
**Dependencies:** — (first phase)
**Deliverables:** `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `DEVELOPMENT_GUIDE.md`, `LICENSE`, `SECURITY.md`, `SECURITY_STANDARDS.md`, `CONTRIBUTING.md`, `PROJECT_MANAGEMENT.md`
**Tasks:** P01-T01 – P01-T15 (15)
**Acceptance criteria:** All eight governance files exist and pass the documentation consistency check; logs initialized; audit drafted and verified.
**Testing requirements:** Documentation consistency validation (file existence, 33-phase count, Kanban-state set, cross-references). No code tests applicable.
**Documentation requirements:** All governance documents created; entries added to `CHANGELOG.md`.
**Security considerations:** `SECURITY.md` and `SECURITY_STANDARDS.md` created; no secrets or invented contact details in any document.
**Exit criteria:** P01-T01 – P01-T15 all DONE; validation passed; no open blockers.
**Status:** IN PROGRESS · **Current progress:** 75% · **Blockers:** None
**Next action:** Complete P01-T12, then P01-T13 – P01-T15.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P01-T13 | Add issue and PR templates | P1 | P01-T06 |
| P01-T14 | Add CI skeleton | P1 | P01-T07 |
| P01-T15 | Define owners and contacts | P2 | — |
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
| P01-T12 | Verify audit evidence | Maintainer | 2026-09-30 |
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|
| P01-T01 | Formalize MIT license | 2026-09-30 |
| P01-T02 | Create changelog | 2026-09-30 |
| P01-T03 | Create code of conduct | 2026-09-30 |
| P01-T04 | Create security policy | 2026-09-30 |
| P01-T05 | Create security standards | 2026-09-30 |
| P01-T06 | Create contribution guide | 2026-09-30 |
| P01-T07 | Create development guide | 2026-09-30 |
| P01-T08 | Initialize project tracker | 2026-09-30 |
| P01-T09 | Validate documentation consistency | 2026-09-30 |
| P01-T10 | Draft existing-implementation audit | 2026-09-30 |
| P01-T11 | Initialize governance logs | 2026-09-30 |

> Phase 01 tasks are documentation-only; for them the Definition of Done applies with
> tests marked not-applicable and "code review" performed as a documentation
> consistency review (see Session 01).

### PHASE 02 — Requirements Engineering

**Objective:** Establish an approved, traceable requirements baseline.
**Description:** Consolidate `README_PRD.md` and `Docs/` specifications into versioned requirements with IDs, acceptance criteria, non-functional requirements, and a traceability matrix.
**Dependencies:** PHASE 01 (complete)
**Deliverables:** Requirements baseline, NFR set, traceability matrix, change-control rules
**Tasks:** P02-T01 – P02-T06 (6)
**Acceptance criteria:** Every core journey has numbered requirements with acceptance criteria, mapped to phases/tasks.
**Testing requirements:** Peer review/walkthrough of each requirement against PRD and spec sections.
**Documentation requirements:** Requirements baseline added under `Docs/`; `CHANGELOG.md` entry.
**Security considerations:** Security and privacy requirements captured by reference to `SECURITY_STANDARDS.md`.
**Exit criteria:** P02-T01 – P02-T06 all DONE; sign-off recorded in the Decision Log.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 01 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P02-T01 | Consolidate requirements baseline | P1 | Phase 01 |
| P02-T02 | Assign requirement IDs | P1 | P02-T01 |
| P02-T03 | Define non-functional requirements | P1 | P02-T01 |
| P02-T04 | Build traceability matrix | P1 | P02-T03 |
| P02-T05 | Requirements review and sign-off | P1 | P02-T04 |
| P02-T06 | Establish change-control rules | P2 | P02-T05 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 03 — System Analysis

**Objective:** Analyze the existing system against requirements to expose gaps, constraints, and risks.
**Description:** Gap analysis, use-case modeling, state-machine/data-flow analysis, feasibility assessment, and risk-register updates.
**Dependencies:** PHASE 02 (complete)
**Deliverables:** Gap analysis report, use-case models, state/data-flow models, feasibility notes, updated Risk Register
**Tasks:** P03-T01 – P03-T05 (5)
**Acceptance criteria:** Every requirement gap is mapped to a task; all critical user flows are modeled.
**Testing requirements:** Peer review of analysis artifacts; consistency check against the requirements baseline.
**Documentation requirements:** Analysis documents under `Docs/`; `CHANGELOG.md` entry.
**Security considerations:** Security-relevant gaps recorded in the Risk Register.
**Exit criteria:** P03-T01 – P03-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 02 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P03-T01 | Gap analysis | P1 | Phase 02 |
| P03-T02 | Use-case analysis | P1 | P03-T01 |
| P03-T03 | State-machine and data-flow analysis | P1 | P03-T02 |
| P03-T04 | Feasibility analysis | P2 | P03-T01 |
| P03-T05 | Update risk register | P2 | P03-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 04 — System Architecture

**Objective:** Define and approve the target architecture baseline.
**Description:** Layered backend / SPA frontend / infrastructure architecture, module boundaries, API surface, quality attributes, and recorded architecture decisions.
**Dependencies:** PHASE 03 (complete)
**Deliverables:** Architecture document, module map, Decision Log entries, quality attributes
**Tasks:** P04-T01 – P04-T05 (5)
**Acceptance criteria:** Architecture addresses every requirement group; key decisions recorded with alternatives and impact.
**Testing requirements:** Architecture review walkthrough against requirements and security standards.
**Documentation requirements:** `Docs/TDOP_MASTER_SPEC.md` alignment; Decision Log entries in this file.
**Security considerations:** Architecture reviewed against the applicable sections of `SECURITY_STANDARDS.md`.
**Exit criteria:** P04-T01 – P04-T05 all DONE; review sign-off recorded.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 03 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P04-T01 | Document target architecture | P1 | Phase 03 |
| P04-T02 | Define module boundaries | P1 | P04-T01 |
| P04-T03 | Record architecture decisions | P1 | P04-T02 |
| P04-T04 | Define quality attributes | P2 | P04-T01 |
| P04-T05 | Architecture review and sign-off | P1 | P04-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 05 — Database Design

**Objective:** Produce an approved data design consistent with requirements and the existing schema.
**Description:** ER model, review of existing Flyway migrations, index/constraint design, retention and privacy design, and migration strategy.
**Dependencies:** PHASE 04 (complete)
**Deliverables:** ER model, schema review report, index plan, retention design, migration rules
**Tasks:** P05-T01 – P05-T06 (6)
**Acceptance criteria:** Model covers all requirement entities; schema gaps are listed as tasks; migration rules documented.
**Testing requirements:** Data-model review; representative queries validated against proposed indexes.
**Documentation requirements:** Database design document and migration conventions; `CHANGELOG.md` (`Database`) entries for later changes.
**Security considerations:** Least-privilege database accounts, secret handling, and personal-data retention rules.
**Exit criteria:** P05-T01 – P05-T06 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 04 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P05-T01 | Logical ER model | P1 | Phase 04 |
| P05-T02 | Review existing schema | P1 | P05-T01 |
| P05-T03 | Index and constraint design | P1 | P05-T02 |
| P05-T04 | Retention and privacy design | P2 | P05-T01 |
| P05-T05 | Migration strategy | P1 | P05-T02 |
| P05-T06 | Database design sign-off | P1 | P05-T05 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 06 — API & Contract Design

**Objective:** Define the API contract before implementation.
**Description:** Endpoint inventory, error/DTO conventions, OpenAPI maintenance, versioning/pagination rules, and a consumer review with the frontend.
**Dependencies:** PHASE 05 (complete)
**Deliverables:** API inventory, standard error contract, OpenAPI baseline, conventions document
**Tasks:** P06-T01 – P06-T05 (5)
**Acceptance criteria:** Every requirement maps to an endpoint (or documents why none is needed); consumers accept the contract.
**Testing requirements:** Sample-request validation of the contract; OpenAPI generation check.
**Documentation requirements:** springdoc/OpenAPI output and `Docs/TDOP_MASTER_SPEC.md` updated; `CHANGELOG.md` entry.
**Security considerations:** Authentication/authorization requirement noted for every endpoint.
**Exit criteria:** P06-T01 – P06-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 05 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P06-T01 | Endpoint inventory | P1 | Phase 05 |
| P06-T02 | Error and DTO conventions | P1 | P06-T01 |
| P06-T03 | OpenAPI contract maintenance | P1 | P06-T02 |
| P06-T04 | Versioning and pagination rules | P1 | P06-T01 |
| P06-T05 | Contract review with consumers | P1 | P06-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 07 — Development Environment

**Objective:** Provide a reproducible development environment for all contributors.
**Description:** Standardized local setup, lint/format tooling, Docker dev profile, deterministic seed strategy, and an onboarding dry-run.
**Dependencies:** PHASE 06 (complete)
**Deliverables:** Setup documentation, tool configurations, dev compose profile, seed policy, onboarding report
**Tasks:** P07-T01 – P07-T05 (5)
**Acceptance criteria:** A new developer can run database, backend, and frontend using the documentation alone.
**Testing requirements:** Onboarding dry-run; lint/format/test tooling executes cleanly.
**Documentation requirements:** `README.md` and `DEVELOPMENT_GUIDE.md` setup sections verified and corrected.
**Security considerations:** `.env.example` files contain placeholders only; `.env` remains git-ignored.
**Exit criteria:** P07-T01 – P07-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 06 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P07-T01 | Standardize local setup | P1 | Phase 06 |
| P07-T02 | Configure lint and format tooling | P1 | P07-T01 |
| P07-T03 | Docker dev profile | P1 | P07-T01 |
| P07-T04 | Seed data strategy | P2 | P07-T03 |
| P07-T05 | Onboarding dry-run | P2 | P07-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 08 — Backend Foundation

**Objective:** Establish a standardized, testable backend foundation.
**Description:** Package structure standardization, global exception handling, logging standards, configuration profiles, and the backend test harness.
**Dependencies:** PHASE 07 (complete)
**Deliverables:** Standardized structure, unified error contract, logging configuration, dev/prod profiles, test harness
**Tasks:** P08-T01 – P08-T05 (5)
**Acceptance criteria:** All endpoints return the standard error format; no stack traces leak; suites run green.
**Testing requirements:** `mvn test` passes; error-path tests added for the exception handler.
**Documentation requirements:** `DEVELOPMENT_GUIDE.md` backend sections verified; `CHANGELOG.md` entries.
**Security considerations:** No secrets in configuration; error responses expose no internals (standards §3.4).
**Exit criteria:** P08-T01 – P08-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 07 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P08-T01 | Standardize package structure | P1 | Phase 07 |
| P08-T02 | Global exception handling | P1 | P08-T01 |
| P08-T03 | Logging standards | P1 | P08-T01 |
| P08-T04 | Configuration profiles | P1 | P08-T01 |
| P08-T05 | Backend test harness | P1 | P08-T02 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 09 — Frontend Foundation

**Objective:** Establish a standardized frontend foundation.
**Description:** Component baseline and design tokens, routing and layouts, API service layer, auth state and route guards, i18n completion, and the Vitest harness.
**Dependencies:** PHASE 07 (complete)
**Deliverables:** Component baseline, router/layouts, axios service layer, auth store, i18n coverage, test harness
**Tasks:** P09-T01 – P09-T05 (5)
**Acceptance criteria:** Pages render through the router with shared components and full en/sw translation keys.
**Testing requirements:** `npm run test`, `npm run lint`, and `npm run build` pass.
**Documentation requirements:** `DEVELOPMENT_GUIDE.md` frontend sections verified; `CHANGELOG.md` entries.
**Security considerations:** No secrets in `VITE_*` variables; route guards complement (never replace) server authorization.
**Exit criteria:** P09-T01 – P09-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 07 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P09-T01 | Component baseline | P1 | Phase 07 |
| P09-T02 | Route structure and layouts | P1 | P09-T01 |
| P09-T03 | API service layer | P1 | P09-T02 |
| P09-T04 | Auth state and route guards | P1 | P09-T03 |
| P09-T05 | i18n and frontend test harness | P2 | P09-T02 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 10 — Authentication & Authorization

**Objective:** Deliver complete, tested authentication and authorization.
**Description:** Complete auth flows, endpoint-level RBAC enforcement, refresh-token revocation, lockout/rate-limit verification, and an auth security test suite.
**Dependencies:** PHASE 08 and PHASE 09 (complete)
**Deliverables:** Working auth flows, enforced RBAC, token revocation, security tests
**Tasks:** P10-T01 – P10-T05 (5)
**Acceptance criteria:** Every protected endpoint denies unauthorized access; revocation, lockout, and expiry behave as specified.
**Testing requirements:** 401/403, expired-token, revoked-token, and lockout tests green.
**Documentation requirements:** Auth sections of `Docs/TDOP_MASTER_SPEC.md` verified; `CHANGELOG.md` `Security` entry.
**Security considerations:** `SECURITY_STANDARDS.md` §1–§2 are binding for this phase.
**Exit criteria:** P10-T01 – P10-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 08 and PHASE 09 exit.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P10-T01 | Complete auth flows | P1 | Phase 08, Phase 09 |
| P10-T02 | Enforce RBAC on endpoints | P1 | P10-T01 |
| P10-T03 | Refresh-token revocation | P1 | P10-T01 |
| P10-T04 | Verify lockout and rate limits | P1 | P10-T01 |
| P10-T05 | Auth security tests | P1 | P10-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 11 — User & Profile Module

**Objective:** Deliver complete, private, tested user-profile functionality.
**Description:** Profile CRUD and completeness rules, career-data management, document-upload security review, visibility/privacy settings, and module tests.
**Dependencies:** PHASE 10 (complete)
**Deliverables:** Profile APIs and UI, privacy controls, tests
**Tasks:** P11-T01 – P11-T05 (5)
**Acceptance criteria:** Users fully manage their own profile; documents are handled per standards; privacy settings enforced server-side.
**Testing requirements:** Profile unit and integration tests, including ownership-denial cases.
**Documentation requirements:** Profile sections of spec/PRD verified; `CHANGELOG.md` entry.
**Security considerations:** `SECURITY_STANDARDS.md` §3 upload rules and ownership checks apply.
**Exit criteria:** P11-T01 – P11-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 10 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P11-T01 | Profile CRUD and completeness | P1 | Phase 10 |
| P11-T02 | Career data management | P1 | P11-T01 |
| P11-T03 | Document upload security review | P1 | P11-T01 |
| P11-T04 | Profile privacy settings | P2 | P11-T01 |
| P11-T05 | Profile module tests | P1 | P11-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 12 — Organization Module

**Objective:** Deliver organization profiles, teams, and verification.
**Description:** Organization CRUD and membership, the evidence-based verification workflow, team roles/permissions, cross-tenant isolation tests, and workspace UI.
**Dependencies:** PHASE 11 (complete)
**Deliverables:** Organization module, verification workflow, team roles, isolation tests, workspace UI
**Tasks:** P12-T01 – P12-T05 (5)
**Acceptance criteria:** Cross-organization access is always denied; verification states are enforced and audited.
**Testing requirements:** Tenant-isolation and verification-workflow tests.
**Documentation requirements:** Trust/organization spec sections verified; `CHANGELOG.md` entry.
**Security considerations:** Tenant isolation and least-privilege team roles (`SECURITY_STANDARDS.md` §2.2).
**Exit criteria:** P12-T01 – P12-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 11 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P12-T01 | Organization profiles and teams | P1 | Phase 11 |
| P12-T02 | Verification workflow completion | P1 | P12-T01 |
| P12-T03 | Org team roles | P1 | P12-T01 |
| P12-T04 | Organization isolation tests | P1 | P12-T03 |
| P12-T05 | Organization workspace UI | P2 | P12-T02 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 13 — Opportunity Core

**Objective:** Deliver a correct, moderated opportunity lifecycle.
**Description:** Data-model alignment with the opportunity type contract, lifecycle state-machine hardening, moderation workflow completion, expiry-engine correctness, and tests.
**Dependencies:** PHASE 12 (complete)
**Deliverables:** Opportunity module with enforced lifecycle, moderation, expiry behavior, tests
**Tasks:** P13-T01 – P13-T05 (5)
**Acceptance criteria:** Invalid lifecycle transitions are rejected; moderation decisions are audited; expiry transitions are accurate.
**Testing requirements:** Lifecycle, moderation, and expiry test coverage.
**Documentation requirements:** Lifecycle sections of spec/PRD verified; `CHANGELOG.md` entries.
**Security considerations:** Ownership checks on opportunity management; moderation access control.
**Exit criteria:** P13-T01 – P13-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 12 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P13-T01 | Opportunity model alignment | P1 | Phase 12 |
| P13-T02 | Lifecycle state-machine hardening | P1 | P13-T01 |
| P13-T03 | Moderation workflow completion | P1 | P13-T02 |
| P13-T04 | Expiry engine correctness | P1 | P13-T02 |
| P13-T05 | Opportunity module tests | P1 | P13-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 14 — Trust & Verification

**Objective:** Deliver evidence-based, auditable trust workflows.
**Description:** Verification with evidence, report investigation, escalation and appeal handling, anti-fraud signal tuning, and a complete decision audit trail.
**Dependencies:** PHASE 13 (complete)
**Deliverables:** Trust workspace workflows, fraud-signal tuning, audit trail
**Tasks:** P14-T01 – P14-T05 (5)
**Acceptance criteria:** Every trust decision is evidence-backed, recorded, and queryable; appeals can overturn decisions.
**Testing requirements:** Workflow tests including report, escalation, and appeal paths.
**Documentation requirements:** Trust sections of spec/PRD verified; `CHANGELOG.md` entry.
**Security considerations:** Role-restricted trust actions; audit records are append-only.
**Exit criteria:** P14-T01 – P14-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 13 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P14-T01 | Evidence-based verification | P1 | Phase 13 |
| P14-T02 | Report investigation workflow | P1 | P14-T01 |
| P14-T03 | Escalation and appeals | P1 | P14-T02 |
| P14-T04 | Anti-fraud signal tuning | P2 | P14-T01 |
| P14-T05 | Trust decision audit trail | P1 | P14-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 15 — Discovery & Search

**Objective:** Deliver fast, relevant opportunity discovery.
**Description:** Search strategy (SQL baseline and future index decision), filter/sort/pagination performance, saved items and comparison, relevance tests, and search analytics.
**Dependencies:** PHASE 13 (complete)
**Deliverables:** Search endpoints and UI, relevance test set, search metrics
**Tasks:** P15-T01 – P15-T05 (5)
**Acceptance criteria:** Search meets defined relevance and latency expectations; relevance regressions are caught by tests.
**Testing requirements:** Relevance regression fixtures; query-performance checks.
**Documentation requirements:** Discovery sections of spec/PRD verified; `CHANGELOG.md` entry.
**Security considerations:** Rate limiting on search endpoints; no cross-tenant data leakage via search.
**Exit criteria:** P15-T01 – P15-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 13 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P15-T01 | Search strategy | P1 | Phase 13 |
| P15-T02 | Filter, sort, pagination performance | P1 | P15-T01 |
| P15-T03 | Saved items and comparison | P2 | P15-T01 |
| P15-T04 | Search relevance test set | P1 | P15-T02 |
| P15-T05 | Search analytics | P2 | P15-T02 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 16 — Application Engine

**Objective:** Deliver reliable application submission and tracking.
**Description:** Submission and tracking flows, status transition rules with history, organization-side review, external/email application paths, and tests.
**Dependencies:** PHASE 13 (complete)
**Deliverables:** Application module with history and organization review flows
**Tasks:** P16-T01 – P16-T05 (5)
**Acceptance criteria:** All valid transitions succeed, invalid ones are rejected, and history is complete per applicant and organization.
**Testing requirements:** Transition coverage tests for every allowed and disallowed move.
**Documentation requirements:** Application sections of spec/PRD verified; `CHANGELOG.md` entry.
**Security considerations:** Ownership checks; applicants' personal data visible only to permitted parties.
**Exit criteria:** P16-T01 – P16-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 13 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P16-T01 | Application submission and tracking | P1 | Phase 13 |
| P16-T02 | Status transition rules | P1 | P16-T01 |
| P16-T03 | Organization review flow | P1 | P16-T02 |
| P16-T04 | External application paths | P2 | P16-T01 |
| P16-T05 | Application engine tests | P1 | P16-T03 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 17 — Notification System

**Objective:** Deliver complete, reliable notifications on all configured channels.
**Description:** In-app notification completeness, email delivery reliability with retries and logging, notification preferences, en/sw templates, and tests.
**Dependencies:** PHASE 16 (complete)
**Deliverables:** Notification service, preferences, templates, delivery tests
**Tasks:** P17-T01 – P17-T05 (5)
**Acceptance criteria:** Events deliver on every configured channel; failures are logged and retried; preferences are respected.
**Testing requirements:** Delivery tests for success and failure paths (SMTP errors).
**Documentation requirements:** Notification sections of spec/PRD verified; `CHANGELOG.md` entry.
**Security considerations:** No personal data in logs; preference enforcement; template injection safety.
**Exit criteria:** P17-T01 – P17-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 16 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P17-T01 | In-app notification completeness | P1 | Phase 16 |
| P17-T02 | Email delivery reliability | P1 | P17-T01 |
| P17-T03 | Notification preferences | P2 | P17-T01 |
| P17-T04 | Notification templates | P2 | P17-T03 |
| P17-T05 | Notification tests | P1 | P17-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 18 — Deadline & Freshness

**Objective:** Keep deadlines and opportunity freshness accurate and observable.
**Description:** Deadline job robustness and idempotency, expiry/closing-soon accuracy, reminder correctness, stale-opportunity detection, and job monitoring.
**Dependencies:** PHASE 13 (complete)
**Deliverables:** Hardened scheduler, monitoring/alerting for jobs, freshness detection
**Tasks:** P18-T01 – P18-T05 (5)
**Acceptance criteria:** Jobs are idempotent; failures alert; transitions and reminders are accurate and de-duplicated.
**Testing requirements:** Scheduler tests using a controlled clock; reminder de-duplication tests.
**Documentation requirements:** Deadline/freshness documentation; `CHANGELOG.md` entry.
**Security considerations:** Jobs run with least-privilege credentials; no reminder spam or token leakage.
**Exit criteria:** P18-T01 – P18-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 13 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P18-T01 | Deadline job robustness | P1 | Phase 13 |
| P18-T02 | Transition accuracy | P1 | P18-T01 |
| P18-T03 | Reminder correctness | P1 | P18-T02 |
| P18-T04 | Freshness detection | P2 | P18-T02 |
| P18-T05 | Job monitoring | P1 | P18-T01 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 19 — Personalization & Matching

**Objective:** Deliver explainable personalization.
**Description:** Matching rule engine (skills, interests, location), personalized feed, similarity refinement, evaluation metrics, and recommendation explainability.
**Dependencies:** PHASE 15 (complete)
**Deliverables:** Matching engine, personalized feed, evaluation metrics, explanations
**Tasks:** P19-T01 – P19-T05 (5)
**Acceptance criteria:** Recommendations are measurable against a baseline and come with a stated reason.
**Testing requirements:** Matching evaluation fixtures with expected outcomes.
**Documentation requirements:** Matching/personalization sections of spec; `CHANGELOG.md` entry.
**Security considerations:** Only permitted profile data may feed personalization (standards §8).
**Exit criteria:** P19-T01 – P19-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 15 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P19-T01 | Matching rule engine | P1 | Phase 15 |
| P19-T02 | Personalized feed | P1 | P19-T01 |
| P19-T03 | Similar-opportunity refinement | P2 | P19-T01 |
| P19-T04 | Matching evaluation metrics | P1 | P19-T02 |
| P19-T05 | Recommendation explainability | P2 | P19-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 20 — Administration & Governance

**Objective:** Deliver administration and governance capabilities.
**Description:** Admin dashboard and user management, permission-management interface, platform-configuration governance, audit-log queries, and governance policies.
**Dependencies:** PHASE 14 (complete)
**Deliverables:** Admin/governance surfaces, audit queries, policy documents
**Tasks:** P20-T01 – P20-T05 (5)
**Acceptance criteria:** Admin actions are authorized, audited, and follow documented policies.
**Testing requirements:** Admin authorization tests (including ADMIN vs SUPER_ADMIN boundaries).
**Documentation requirements:** Governance policies documented; spec admin sections verified; `CHANGELOG.md` entry.
**Security considerations:** `SECURITY_STANDARDS.md` §2 boundaries between ADMIN and SUPER_ADMIN.
**Exit criteria:** P20-T01 – P20-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 14 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P20-T01 | Admin dashboard and user management | P1 | Phase 14 |
| P20-T02 | Permission management interface | P1 | P20-T01 |
| P20-T03 | Platform configuration governance | P1 | P20-T01 |
| P20-T04 | Audit log queries | P1 | P20-T01 |
| P20-T05 | Governance policies | P2 | P20-T03 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 21 — Analytics & Outcomes

**Objective:** Deliver trustworthy analytics and outcome tracking.
**Description:** Privacy-aware analytics event model, post-application outcome model, dashboards, data-accuracy validation, and a privacy review.
**Dependencies:** PHASE 20 (complete)
**Deliverables:** Analytics pipeline, dashboards, outcome tracking, privacy review record
**Tasks:** P21-T01 – P21-T05 (5)
**Acceptance criteria:** Metrics reconcile with source data; no personal data leaks into analytics output.
**Testing requirements:** Data-accuracy checks comparing aggregates to source records.
**Documentation requirements:** Analytics/outcome spec sections; `CHANGELOG.md` entry.
**Security considerations:** Aggregation and minimization per `SECURITY_STANDARDS.md` §8.
**Exit criteria:** P21-T01 – P21-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 20 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P21-T01 | Analytics event model | P2 | Phase 20 |
| P21-T02 | Outcome model | P2 | P21-T01 |
| P21-T03 | Dashboards | P2 | P21-T01 |
| P21-T04 | Analytics data validation | P2 | P21-T03 |
| P21-T05 | Analytics privacy review | P1 | P21-T02 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 22 — Advanced Data Quality & Source Management

**Objective:** Raise data quality and manage opportunity sources.
**Description:** Duplicate detection, completeness/quality scoring, source registry with credibility, content sanitization pipeline, and quality metrics.
**Dependencies:** PHASE 21 (complete)
**Deliverables:** Quality rules, source registry, quality reports
**Tasks:** P22-T01 – P22-T05 (5)
**Acceptance criteria:** Duplicates are detected and handled; every source is tracked with provenance.
**Testing requirements:** Quality-rule tests with representative fixtures.
**Documentation requirements:** Data-quality and source-management spec; `CHANGELOG.md` entry.
**Security considerations:** Sanitization prevents stored XSS; ingestion inputs validated (standards §3.2).
**Exit criteria:** P22-T01 – P22-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 21 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P22-T01 | Duplicate detection | P2 | Phase 21 |
| P22-T02 | Quality scoring rules | P2 | P22-T01 |
| P22-T03 | Source registry | P2 | P22-T01 |
| P22-T04 | Content sanitization pipeline | P1 | P22-T02 |
| P22-T05 | Quality metrics reporting | P3 | P22-T03 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 23 — External Opportunity Ingestion

**Objective:** Ingest external opportunities safely and transparently.
**Description:** Pluggable connector architecture, fetch/validate/dedupe/publish pipeline, attribution and provenance UI, monitoring, and a security review.
**Dependencies:** PHASE 22 (complete)
**Deliverables:** Ingestion pipeline, provenance display, monitoring and failure handling
**Tasks:** P23-T01 – P23-T05 (5)
**Acceptance criteria:** Ingested items are validated, deduplicated, attributed, and only published after moderation rules pass.
**Testing requirements:** Pipeline tests including malformed and hostile input.
**Documentation requirements:** Ingestion spec and source-attribution documentation; `CHANGELOG.md` entry.
**Security considerations:** SSRF protection, payload-size limits, egress controls (`SECURITY_STANDARDS.md` §7).
**Exit criteria:** P23-T01 – P23-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 22 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P23-T01 | Connector architecture | P2 | Phase 22 |
| P23-T02 | Ingestion pipeline | P2 | P23-T01 |
| P23-T03 | Attribution and provenance UI | P2 | P23-T02 |
| P23-T04 | Ingestion monitoring | P1 | P23-T02 |
| P23-T05 | Ingestion security review | P1 | P23-T02 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 24 — Advanced Intelligence / AI

**Objective:** Add intelligence features responsibly.
**Description:** AI scope and guardrails decision, summarization and eligibility explanation, smart search and semantic matching, model evaluation and explainability, and a responsible-use policy.
**Dependencies:** PHASE 19 and PHASE 23 (complete)
**Deliverables:** Selected AI features, evaluation results, AI privacy/responsible-use policy
**Tasks:** P24-T01 – P24-T05 (5)
**Acceptance criteria:** Features meet defined evaluation thresholds and are explainable; policy approved before release.
**Testing requirements:** Evaluation sets with quality thresholds; output-safety tests.
**Documentation requirements:** AI policy and spec sections; `CHANGELOG.md` entry.
**Security considerations:** Privacy/fairness constraints; third-party model data use requires a Decision Log entry.
**Exit criteria:** P24-T01 – P24-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 19 and PHASE 23 exit.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P24-T01 | AI scope and guardrails | P2 | Phase 19, Phase 23 |
| P24-T02 | Summarization and eligibility explanation | P3 | P24-T01 |
| P24-T03 | Smart search and semantic matching | P3 | P24-T01 |
| P24-T04 | Model evaluation and explainability | P2 | P24-T03 |
| P24-T05 | AI privacy and responsible-use policy | P1 | P24-T01 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 25 — Communication Expansion

**Objective:** Expand delivery channels beyond email and in-app notifications.
**Description:** WhatsApp channel architecture, channel integration, multi-channel routing with preference center, template/compliance rules, and delivery tests.
**Dependencies:** PHASE 17 (complete)
**Deliverables:** Channel integrations, preference center, delivery tests
**Tasks:** P25-T01 – P25-T05 (5)
**Acceptance criteria:** Messages route per user preference with fallback, and failures are visible.
**Testing requirements:** Channel delivery tests including provider failure and fallback.
**Documentation requirements:** Channel architecture documentation; `CHANGELOG.md` entry.
**Security considerations:** Provider credentials in environment only; user opt-in consent recorded.
**Exit criteria:** P25-T01 – P25-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 17 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P25-T01 | WhatsApp channel architecture | P2 | Phase 17 |
| P25-T02 | Channel integration | P2 | P25-T01 |
| P25-T03 | Multi-channel routing and preferences | P2 | P25-T02 |
| P25-T04 | Template and compliance rules | P1 | P25-T02 |
| P25-T05 | Channel delivery tests | P1 | P25-T03 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 26 — Subscription / Business Model

**Objective:** Deliver the subscription/business model.
**Description:** Plan and entitlement definition, payment provider decision and integration, server-side feature gating, billing events and receipts, and tests.
**Dependencies:** PHASE 20 (complete)
**Deliverables:** Payment integration, entitlements, billing history and receipts
**Tasks:** P26-T01 – P26-T05 (5)
**Acceptance criteria:** Entitlements are enforced server-side; billing events reconcile with receipts.
**Testing requirements:** Entitlement and billing tests, including denied-feature paths.
**Documentation requirements:** Plans/pricing documentation; `CHANGELOG.md` entries (incl. `Breaking` if API changes).
**Security considerations:** Never store card data directly; payment provider handled per their standards (§8 of `SECURITY_STANDARDS.md`).
**Exit criteria:** P26-T01 – P26-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 20 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P26-T01 | Plan and entitlement definition | P2 | Phase 20 |
| P26-T02 | Payment provider decision | P1 | P26-T01 |
| P26-T03 | Feature gating | P1 | P26-T02 |
| P26-T04 | Billing events and receipts | P2 | P26-T02 |
| P26-T05 | Subscription tests | P1 | P26-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 27 — Complete Security Hardening

**Objective:** Close all known security gaps before release.
**Description:** Remediation of every GAP in `SECURITY_STANDARDS.md`, penetration/DAST testing, CSP and header hardening, secret-management runbook, and dependency vulnerability remediation.
**Dependencies:** PHASE 26 (complete)
**Deliverables:** Hardened configuration, pen-test report, secret-management runbook, patched dependencies
**Tasks:** P27-T01 – P27-T05 (5)
**Acceptance criteria:** No unresolved critical or high findings; every standards GAP is closed or explicitly risk-accepted in the Decision Log.
**Testing requirements:** DAST and manual abuse-case testing plus the full regression suite.
**Documentation requirements:** `SECURITY.md`/`SECURITY_STANDARDS.md` updated; `CHANGELOG.md` `Security` entries.
**Security considerations:** This phase is security — all sections of `SECURITY_STANDARDS.md` apply.
**Exit criteria:** P27-T01 – P27-T05 all DONE; zero open critical/high findings.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 26 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P27-T01 | Remediate security-standard gaps | P1 | Phase 26 |
| P27-T02 | Penetration test | P1 | P27-T01 |
| P27-T03 | CSP and header hardening | P1 | P27-T01 |
| P27-T04 | Secret management runbook | P1 | P27-T01 |
| P27-T05 | Dependency vulnerability remediation | P1 | P27-T02 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 28 — Complete Testing

**Objective:** Achieve comprehensive test coverage and quality evidence.
**Description:** End-to-end suite for critical journeys, accessibility testing (WCAG 2.2 AA), cross-browser/device testing, coverage targets and reporting, and regression-suite stabilization.
**Dependencies:** PHASE 27 (complete)
**Deliverables:** E2E suite, accessibility report, coverage thresholds, stable regression suite
**Tasks:** P28-T01 – P28-T05 (5)
**Acceptance criteria:** Critical journeys automated and green; coverage targets met; no known flaky tests blocking releases.
**Testing requirements:** This phase is testing — full suites run in CI for every change.
**Documentation requirements:** Test reports stored under `Docs/`; `CHANGELOG.md` entries.
**Security considerations:** Security regression tests from PHASE 10/27 remain green.
**Exit criteria:** P28-T01 – P28-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 27 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P28-T01 | End-to-end test suite | P1 | Phase 27 |
| P28-T02 | Accessibility testing | P1 | P28-T01 |
| P28-T03 | Cross-browser and device testing | P1 | P28-T01 |
| P28-T04 | Coverage targets and reporting | P1 | P28-T01 |
| P28-T05 | Regression suite stabilization | P1 | P28-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 29 — Performance & Reliability

**Objective:** Meet performance and reliability targets under expected load.
**Description:** Load testing and baselines, query/index optimization, caching strategy, resilience engineering, and monitoring/alerting.
**Dependencies:** PHASE 28 (complete)
**Deliverables:** Load-test baselines, optimizations, caching implementation, monitoring and alerts
**Tasks:** P29-T01 – P29-T05 (5)
**Acceptance criteria:** Latency and throughput targets met at expected peak load; failures alert.
**Testing requirements:** Load and stress tests; post-optimization comparison against baseline.
**Documentation requirements:** Performance report and tuning notes; `CHANGELOG.md` (`Infrastructure`) entries.
**Security considerations:** DoS protections and rate limits verified under load.
**Exit criteria:** P29-T01 – P29-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 28 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P29-T01 | Load testing | P1 | Phase 28 |
| P29-T02 | Query and index optimization | P1 | P29-T01 |
| P29-T03 | Caching strategy | P2 | P29-T01 |
| P29-T04 | Resilience engineering | P1 | P29-T01 |
| P29-T05 | Monitoring and alerting | P1 | P29-T03 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 30 — Deployment & CI/CD

**Objective:** Deliver repeatable, automated delivery.
**Description:** CI pipeline (build, lint, test, scan), delivery pipeline and environments, infrastructure hardening, backup/restore runbook, and deployment-checklist validation.
**Dependencies:** PHASE 29 (complete)
**Deliverables:** CI/CD workflows, hardened infrastructure, backup/restore runbook, validated checklist
**Tasks:** P30-T01 – P30-T05 (5)
**Acceptance criteria:** Every change runs build/lint/test/scan; deployment is repeatable; restore drill succeeded.
**Testing requirements:** Pipeline dry-runs and a backup restore drill.
**Documentation requirements:** Runbooks and `Docs/DEPLOYMENT_CHECKLIST.md` validated; `CHANGELOG.md` (`Infrastructure`) entries.
**Security considerations:** Secrets management and least-privilege deploy credentials (`SECURITY_STANDARDS.md` §6).
**Exit criteria:** P30-T01 – P30-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 29 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P30-T01 | CI pipeline | P1 | Phase 29 |
| P30-T02 | Delivery pipeline | P1 | P30-T01 |
| P30-T03 | Infrastructure hardening | P1 | P30-T02 |
| P30-T04 | Backup and restore runbook | P1 | P30-T02 |
| P30-T05 | Deployment checklist validation | P1 | P30-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 31 — Beta Release

**Objective:** Validate the platform with real beta users.
**Description:** Beta scope and participant selection, beta deployment and monitoring, feedback collection and triage, a bugfix cycle, and the exit review.
**Dependencies:** PHASE 30 (complete)
**Deliverables:** Beta environment, triaged feedback backlog, beta exit report
**Tasks:** P31-T01 – P31-T05 (5)
**Acceptance criteria:** No open critical beta issues; exit review records a go/no-go decision.
**Testing requirements:** Beta-driven regression; reproducible test for every beta-blocking bug.
**Documentation requirements:** Beta report under `Docs/`; `CHANGELOG.md` entries for fixes.
**Security considerations:** Beta data handling rules; no production secrets in the beta environment.
**Exit criteria:** P31-T01 – P31-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 30 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P31-T01 | Beta scope and participants | P1 | Phase 30 |
| P31-T02 | Beta deployment and monitoring | P1 | P31-T01 |
| P31-T03 | Feedback collection and triage | P1 | P31-T02 |
| P31-T04 | Beta bugfix cycle | P1 | P31-T03 |
| P31-T05 | Beta exit review | P1 | P31-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 32 — Production Launch

**Objective:** Launch TDOP to production safely.
**Description:** Pre-launch checklist (secrets, seed-data removal, HTTPS, backups), production deployment with smoke tests, launch communications, post-launch monitoring, and sign-off.
**Dependencies:** PHASE 31 (complete)
**Deliverables:** Production deployment, smoke-test results, launch sign-off record
**Tasks:** P32-T01 – P32-T05 (5)
**Acceptance criteria:** Critical flows verified in production; checklist complete; monitoring window clean.
**Testing requirements:** Production smoke tests for login, discovery, application, and notification flows.
**Documentation requirements:** `README.md` status and release notes; `CHANGELOG.md` release section dated.
**Security considerations:** Demo/seed accounts removed; HTTPS enforced; backups verified; secrets rotated if needed.
**Exit criteria:** P32-T01 – P32-T05 all DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 31 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P32-T01 | Pre-launch checklist | P1 | Phase 31 |
| P32-T02 | Production deployment and smoke tests | P1 | P32-T01 |
| P32-T03 | Launch communications | P2 | P32-T02 |
| P32-T04 | Post-launch monitoring window | P1 | P32-T02 |
| P32-T05 | Launch sign-off | P1 | P32-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

### PHASE 33 — Continuous Improvement

**Objective:** Improve the platform continuously after launch.
**Description:** Continuous backlog grooming, metrics-driven improvement cycles, security maintenance cadence, documentation maintenance, and quarterly roadmap reviews.
**Dependencies:** PHASE 32 (complete)
**Deliverables:** Recurring improvement cycles with recorded outcomes
**Tasks:** P33-T01 – P33-T05 (5)
**Acceptance criteria:** Each improvement period produces prioritized, shipped, and measured changes.
**Testing requirements:** Regression suite runs on every improvement before release.
**Documentation requirements:** Continuous documentation upkeep; `CHANGELOG.md` updated per release.
**Security considerations:** Regular dependency scanning, patching, and security review cadence.
**Exit criteria:** Continuous phase — exit reviewed quarterly; all current-cycle tasks DONE.
**Status:** BACKLOG · **Current progress:** 0% · **Blockers:** None
**Next action:** Begin when PHASE 32 exits.

#### BACKLOG
| ID | Task | Priority | Dependency |
|---|---|---|---|
| P33-T01 | Continuous backlog grooming | P2 | Phase 32 |
| P33-T02 | Metrics-driven improvement cycles | P2 | P33-T01 |
| P33-T03 | Security maintenance cadence | P1 | P33-T01 |
| P33-T04 | Documentation maintenance | P2 | P33-T01 |
| P33-T05 | Quarterly roadmap review | P2 | P33-T04 |
#### TO DO
| ID | Task | Priority | Dependency |
|---|---|---|---|
#### IN PROGRESS
| ID | Task | Owner | Started |
|---|---|---|---|
#### CODE REVIEW
| ID | Task | Reviewer |
|---|---|---|
#### TESTING
| ID | Task | Test |
|---|---|---|
#### DONE
| ID | Task | Completed |
|---|---|---|

