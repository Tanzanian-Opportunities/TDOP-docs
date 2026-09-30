# TDOP Software Requirements Specification (SRS)

**Project:** Tanzania Digital Opportunity Platform (TDOP)
**Repository:** `TDOP-docs/Specs/SRS.md`
**Status:** Draft for Phase 02 baseline (requirements review and sign-off happen in
PHASE 02 - Requirements Engineering, tasks P02-T01 - P02-T06)
**Sources:** `README_PRD.md` (product requirements), `Specs/TDOP_MASTER_SPEC.md`
(architecture), `EXISTING_IMPLEMENTATION_AUDIT.md` (verified current state),
`SECURITY_STANDARDS.md` (security requirements), `PROJECT_MANAGEMENT.md` (33-phase
roadmap).

> No requirement in this document is invented: every item is derived from the
> documents above. Unknowns are marked `[TBD]`.

---

## 1. Introduction

### 1.1 Purpose

This SRS specifies the software requirements of the TDOP platform: a digital
opportunity discovery and progress platform connecting **seekers**,
**organizations**, and **platform operators** in Tanzania. It is the working
requirements artifact that Phase 02 consolidates, numbers, reviews, and signs off.

### 1.2 Scope

TDOP comprises:

- a **backend REST API** (Java 21 / Spring Boot 3.3, PostgreSQL 16, Flyway) -
  `TDOP-backend`;
- a **web application** (React 18 / TypeScript / Vite / Tailwind) -
  `TDOP-frontend`;
- **deployment** (Docker Compose, Nginx origin proxy, Cloudflare edge) -
  `TDOP-infra` + `TDOP-backend/nginx.conf`;
- a **planned mobile application** (Flutter / Dart, cross-device) -
  `TDOP-mobile`;
- **governance and documentation** - `TDOP-docs`.

Out of scope for this document: commercial terms beyond the subscription engine
placeholder (Phase 26), and platform features explicitly deferred in
`README_PRD.md` §6.1.

### 1.3 Definitions

| Term | Meaning |
|---|---|
| Seeker | Opportunity seeker: browses, applies, tracks opportunities |
| Organization | Opportunity provider: publishes and manages opportunities |
| Trust workspace | Verification, moderation, reports, escalations, appeals tooling |
| Platform operator | Moderator, verification officer, admin, super admin |
| Lifecycle | State machine governing opportunities/applications/reports |

## 2. Overall description

### 2.1 Product perspective

TDOP is a multi-tenant web platform with role-based access, an opportunity
lifecycle engine, trust/verification workflows, discovery/search, notifications,
and administration workspaces. The backend is authoritative for all business rules
(`README_PRD.md` §12.1).

### 2.2 User classes and roles (PRD §3)

| # | Role | Primary capabilities |
|---|---|---|
| 1 | `SEEKER` | Browse/search/save/compare opportunities; apply; track applications; profile |
| 2 | `ORGANIZATION` | Organization member: create/publish opportunities; review applications |
| 3 | `ORGANIZATION_ADMIN` | Organization owner/administrator incl. team management |
| 4 | `ORGANIZATION_MEMBER` | Bounded organization participation |
| 5 | `VERIFICATION_OFFICER` | Reviews verification requests with evidence |
| 6 | `MODERATOR` | Moderation queue: approve/reject/suspend/archive/request-information |
| 7 | `ADMIN` | Platform administration, users, analytics, audit |
| 8 | `SUPER_ADMIN` | Governance, security, intelligence, feature controls (18 pages) |
| 9 | (unauthenticated guest) | Public browsing of published opportunities/stats |

### 2.3 Operating environment

- Browsers: modern evergreen desktop + mobile (mobile-first design, PRD §24).
- Server: Linux container runtime; PostgreSQL 16; SMTP for email.
- Edge: Cloudflare (DNS/TLS/CDN/WAF) in front of the Nginx origin proxy.
- Localization: English + Swahili (i18next); low-bandwidth, data-conscious usage.

### 2.4 Constraints

| ID | Constraint |
|---|---|
| C-01 | Stack of record (DEC-005): Java 21 / Spring Boot 3.3 / PostgreSQL / Flyway; React 18 / TypeScript / Vite / Tailwind; Docker Compose; mobile Flutter/Dart (DEC-010) |
| C-02 | License: MIT (single `LICENSE` in `TDOP-docs`, DEC-008) |
| C-03 | Governance: 33-phase roadmap authoritative (DEC-002); six-state task Kanban (DEC-003); phase status lifecycle Planned → In progress → Completed (DEC-008) |
| C-04 | API base path `/api/v1`; breaking changes require a version segment |
| C-05 | No fabricated data (PRD §12.5); pre-existing code never auto-credits phase completion (DEC-004) |
| C-06 | Security per `SECURITY_STANDARDS.md` (8 binding areas) |

## 3. Functional requirements

Format: `FR-<AREA>-<NN>` — *requirement*. Acceptance criteria are the phase/task
acceptance criteria where the area is implemented; formal traceability to
`TASK_BREAKDOWN.md` IDs is produced by P02-T04.

### 3.1 Authentication and accounts (Phase 10)

| ID | Requirement |
|---|---|
| FR-AUTH-01 | The system shall register a user with email verification (token expiry 60 min) |
| FR-AUTH-02 | The system shall authenticate via email + password and issue JWT access + refresh tokens (refresh persisted in DB) |
| FR-AUTH-03 | The system shall support logout (token revocation) and refresh-token rotation |
| FR-AUTH-04 | The system shall provide forgot/reset password with 30-minute reset tokens |
| FR-AUTH-05 | The system shall lock accounts after 5 failed attempts (15-minute lockout) |
| FR-AUTH-06 | The system shall rate-limit login attempts (20/min/IP) |
| FR-AUTH-07 | The system shall support the nine roles of §2.2 with server-side enforcement on every endpoint |

### 3.2 Profiles (Phase 11)

| ID | Requirement |
|---|---|
| FR-PROF-01 | Seeker profiles shall capture education, skills, experience, interests, career goals |
| FR-PROF-02 | Users shall control profile visibility (public/limited/private) |
| FR-PROF-03 | Users shall manage document uploads (type/size validation, traversal-safe storage) |
| FR-PROF-04 | Users shall manage notification preferences (in-app, email) |

### 3.3 Organizations (Phase 12)

| ID | Requirement |
|---|---|
| FR-ORG-01 | Organizations shall have profiles with verification state |
| FR-ORG-02 | The system shall implement the verification flow: submit evidence → officer review → approve/reject (PRD §7.2) |
| FR-ORG-03 | Organization admins shall manage team members and roles |
| FR-ORG-04 | Organization members shall only access their own organization's data (isolation, PRD §12.3) |

### 3.4 Opportunity engine (Phase 13)

| ID | Requirement |
|---|---|
| FR-OPP-01 | The system shall support the opportunity types of PRD §4.1 with the common model (PRD §4.3) |
| FR-OPP-02 | Opportunities shall follow the lifecycle DRAFT → SUBMITTED → VERIFIED → APPROVED → PUBLISHED → CLOSING_SOON → EXPIRED with validated transitions |
| FR-OPP-03 | Owners shall create/edit/delete their own opportunities only |
| FR-OPP-04 | The system shall persist status history for every lifecycle transition |
| FR-OPP-05 | The action engine (PRD §4.4) shall expose apply/save/compare/share actions contextually |

### 3.5 Applications (Phase 16)

| ID | Requirement |
|---|---|
| FR-APP-01 | Seekers shall apply to opportunities and receive status tracking with history |
| FR-APP-02 | Organizations shall update application status through validated transitions |
| FR-APP-03 | Seekers shall save opportunities and compare them side by side |
| FR-APP-04 | External-application and internal-application flows shall both be supported (roadmap §18) |

### 3.6 Trust and verification (Phase 14)

| ID | Requirement |
|---|---|
| FR-TRUST-01 | The trust workspace shall provide verification, moderation, reports, escalations, and appeals queues |
| FR-TRUST-02 | Users shall file reports; moderators shall assign, investigate, resolve or dismiss |
| FR-TRUST-03 | Escalations and appeals shall follow their own state machines with evidence |
| FR-TRUST-04 | Anti-fraud risk signals shall be recorded and surfaced to operators |
| FR-TRUST-05 | Moderation actions shall be audit-logged with actor and reason |

### 3.7 Discovery (Phase 15)

| ID | Requirement |
|---|---|
| FR-DISC-01 | The system shall support multi-field search (title, description, category, tags) with filters (PRD §8.2) |
| FR-DISC-02 | The system shall rank/filter results by relevance and lifecycle freshness |
| FR-DISC-03 | The system shall recommend opportunities by skill/interest/location matching |
| FR-DISC-04 | The system shall present similar opportunities |
| FR-DISC-05 | Saved searches/digests shall respect user preferences (Phase 17/19) |

### 3.8 Notifications (Phase 17)

| ID | Requirement |
|---|---|
| FR-NOTIF-01 | The system shall deliver in-app notifications for domain events (PRD §9.1) |
| FR-NOTIF-02 | The system shall deliver email notifications via SMTP with templates |
| FR-NOTIF-03 | Deadline reminders shall be issued by the deadline engine (hourly: expire, closing_soon, reminders) |
| FR-NOTIF-04 | A weekly digest shall be sent (Monday 08:00) |
| FR-NOTIF-05 | Users shall control channel preferences; WhatsApp/SMS remain planned (Phase 25) |

### 3.9 Administration (Phases 20-21)

| ID | Requirement |
|---|---|
| FR-ADMIN-01 | Admin workspace: user management (list, suspend, role change), moderation, reports, analytics, audit log |
| FR-ADMIN-02 | Super Admin workspace: 18 pages covering governance, security, intelligence, taxonomy, features, sessions, notifications, integrations, background jobs |
| FR-ADMIN-03 | Platform configuration shall be stored as runtime key-value configuration |
| FR-ADMIN-04 | Analytics shall expose platform metrics (supply, demand, action, trust, retention - roadmap §53) |
| FR-ADMIN-05 | Audit logs shall be immutable records of privileged actions |

### 3.10 Internationalization and accessibility (Phases 9, 24)

| ID | Requirement |
|---|---|
| FR-I18N-01 | All user-visible strings shall be available in English and Swahili |
| FR-I18N-02 | The UI shall be mobile-first and data-conscious |
| FR-I18N-03 | The UI shall target WCAG 2.2 AA (tracked gap, Phase 28) |

### 3.11 Mobile application (TDOP-mobile, planned)

| ID | Requirement |
|---|---|
| FR-MOB-01 | The mobile app shall provide the seeker core journeys (browse, search, apply, track, notifications) using Flutter/Dart for cross-device reach (DEC-010) |
| FR-MOB-02 | The mobile app shall consume the same backend API (`/api/v1`) with identical authorization rules |

## 4. Non-functional requirements

| ID | Requirement | Source |
|---|---|---|
| NFR-01 | Security: authentication, authorization, API, database, frontend, infrastructure, secure development, and privacy standards are binding | `SECURITY_STANDARDS.md` |
| NFR-02 | Availability of core read paths target `[TBD]` (defined in Phase 29) | - |
| NFR-03 | Performance: paginated list endpoints; indexed query patterns per migration standards; load targets `[TBD]` (Phase 29) | - |
| NFR-04 | Reliability: lifecycle state machines reject invalid transitions; migrations are additive-first | `DEVELOPMENT_GUIDE.md` §10 |
| NFR-05 | Maintainability: documented standards, 33-phase governance, append-only logs | `CODING_STANDARDS.md` |
| NFR-06 | Portability: containerized deployment; sibling-repo build layout | `TDOP-infra` |
| NFR-07 | Observability: structured logging (logback console + rolling file); audit log | audit row "Observability: Partial" |
| NFR-08 | Localization completeness for shipped features (en + sw key parity) | `CODING_STANDARDS.md` §7 |

## 5. External interfaces

| Interface | Specification |
|---|---|
| REST API | `/api/v1`, JSON, conventional verbs/status codes, pagination (`page`,`size`,sort), OpenAPI via springdoc (`DEVELOPMENT_GUIDE.md` §11) |
| Error contract | Standard error body from `GlobalExceptionHandler`; no stack traces to clients |
| Email | SMTP submission via Spring Mail; template-based messages |
| Files | Local filesystem storage with path-traversal protection; type/size limits |
| Web edge | Nginx origin proxy (`TDOP-backend/nginx.conf`): `/api/`, `/ws/`, `/swagger-ui/`, `/health`; Cloudflare in front |
| Frontend ↔ API | axios client in `src/services/`; token refresh handled centrally |

## 6. Data requirements

Core entities (existing, verified in `EXISTING_IMPLEMENTATION_AUDIT.md`): `User`,
profiles (`SeekerProfile`, `Education`, `Experience`, `Skill`, `Interest`,
`CareerGoal`), `OrganizationProfile` + membership/invitations,
`Opportunity` (+ status history), `Application` (+ status history), `Report`,
`Escalation`, `Appeal`, `ModerationAction`, `AuditLog`, `Notification`,
`VerificationRequest/Document`, `UserDocument`, `RiskSignal`, `RevokedToken`,
`PlatformConfig`, `DeadlineReminder`, RBAC (`Role`, `Permission`).

- Schema changes are governed by Flyway migrations (unique versions, additive-first).
- Seed/demo data must be guarded from production use (Phase 32 environment guard).
- Privacy handling per `SECURITY_STANDARDS.md` §8 and `SECURITY.md`.

## 7. Requirements traceability (draft)

| Requirement area | Primary phase(s) | Status (per audit) |
|---|---|---|
| Governance/PM (this SRS' home) | 01 | Completed |
| Requirements baseline/sign-off | 02 | Planned |
| Auth | 10 | Implemented (hardening in later phases) |
| Profiles | 11 | Implemented |
| Organizations | 12 | Implemented |
| Opportunity core | 13 | Implemented |
| Trust & verification | 14 | Implemented |
| Discovery/search | 15 | Partial (multi-field search exists; filters to complete) |
| Applications | 16 | Implemented |
| Notifications | 17 | Implemented (WhatsApp/SMS planned) |
| Deadlines | 18 | Implemented |
| Personalization | 19 | Partial (rule-based baseline) |
| Administration | 20 | Implemented |
| Analytics | 21 | Partial |
| Intelligence/AI | 24 | Planned |
| Security hardening | 27 | Partial |
| Testing (E2E/load) | 28 | Partial |
| Deployment/CI | 30 | Partial (CI skeleton added in Phase 01) |
| Mobile | via `TDOP-mobile` | Planned (Flutter/Dart) |

Full task-level traceability is produced by P02-T04 against
`TASK_BREAKDOWN.md`.

## 8. Verification approach

- Documentation phases: consistency validation (`TDOP-docs/scripts/validate.ps1`)
  and peer walkthrough (per-phase testing requirements in `TASK_BREAKDOWN.md`).
- Code phases: automated suites (`mvn test`, `npm test`) plus the phase's testing
  requirements; every bug fix carries a regression test.
- Requirements review/sign-off: P02-T05, recorded as a Decision Log entry.

## 9. Appendices

- A: `README_PRD.md` — product requirements source.
- B: `Specs/TDOP_MASTER_SPEC.md` — architecture and implementation specification.
- C: `EXISTING_IMPLEMENTATION_AUDIT.md` — verified current state (DEC-004).
- D: `SECURITY_STANDARDS.md` — binding security requirements.
- E: `TASK_BREAKDOWN.md` — 177 tasks across 33 phases.

## Related

- [`../README_PRD.md`](../README_PRD.md) · [`TDOP_MASTER_SPEC.md`](TDOP_MASTER_SPEC.md) ·
  [`../PROJECT_MANAGEMENT.md`](../PROJECT_MANAGEMENT.md)
- [Kanban board](https://github.com/orgs/Tanzanian-Opportunities/projects/1)
