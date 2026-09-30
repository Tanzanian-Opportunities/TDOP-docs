# Existing Implementation Audit (Project Management Section 16)

**Source:** extracted from [PROJECT_MANAGEMENT.md](PROJECT_MANAGEMENT.md) section 16. This audit does not change official phase status (Decision DEC-004).

> **Path note:** after the multi-repository split, evidence paths prefixed TDOP-backend/, TDOP-frontend/, TDOP-infra/ refer to those repositories (they carry the same prefix as in the original monorepo). Unprefixed src/..., config, and migration paths are relative to the component repository named in the row.

---

## 16. EXISTING IMPLEMENTATION AUDIT

Inventory of code that already exists in the repository. **This audit does not change
official phase status** (DEC-004). "Actual State" values follow `README_PRD.md` §6.2:
`Implemented` / `Partial` / `Planned` / `Future`.

| Existing Feature | Related Phase | Actual State | Evidence | Required Action |
|---|---|---|---|---|
| JWT authentication (register, login, refresh, logout, forgot/reset) | 10 | Implemented (hardening pending) | `TDOP-backend/src/main/java/tdop/config/SecurityConfig.java`, `JwtAuthenticationFilter.java`, `controller/AuthController.java` | Verify against `SECURITY_STANDARDS.md` §1; complete revocation (P10-T03) |
| Rate limiting and account lockout | 10 | Implemented | `config/RateLimitFilter.java`; `README.md` (20 req/min/IP; 5 attempts → 15 min) | Verify behavior with tests (P10-T04) |
| RBAC roles and permissions infrastructure | 10, 20 | Partial | `rbac/` package; `V7__rbac_org_teams_opportunity_lifecycle.sql`; `README_PRD.md` §6.1 "Partial — URL-level only" | Wire RBAC service to endpoints (P10-T02) |
| User profiles (education, skills, experience, goals) | 11 | Implemented | `README.md`; migrations `V1`, `V3`, `V5` | Verify against requirements in Phase 11 |
| Organization profiles and verification workflow | 12 | Implemented | `README.md`; `organization/` package; `V8__sample_organizations.sql` | Isolation tests (P12-T04) |
| Opportunity lifecycle and moderation | 13 | Implemented | `README.md` lifecycle states; `controller/organization`, `controller/trust` | State-machine audit (P13-T02) |
| Reports, escalations, appeals, anti-fraud signals | 14 | Implemented | `README.md`; `V14__escalations_and_appeals.sql` | Audit-trail completeness (P14-T05) |
| Search (multi-field, SQL LIKE) and filters | 15 | Partial | `README_PRD.md` §8.1 "Partial — SQL LIKE" | Search strategy (P15-T01) |
| Applications with status tracking and history | 16 | Implemented | `README.md`; `ApplicationService`/`ApplicationController` tests | Transition-rule audit (P16-T02) |
| Notifications (in-app + email), weekly digest | 17 | Partial | `notification/` package; `README_PRD.md` §9 "email not sent" for deadline events | Email reliability work (P17-T02) |
| Deadline engine (hourly jobs) | 18 | Implemented (monitoring gap) | `README.md` "Deadline engine (hourly…)" | Job monitoring (P18-T05) |
| Recommendations and similar opportunities | 19 | Partial | `RecommendationService.java`, `RecommendationController.java`; `README_PRD.md` §6.1 "basic rule-based" | Baseline for Phase 19 personalization |
| Admin dashboard, user management, audit log, analytics | 20, 21 | Partial | `controller/admin`; `audit/` package; `README_PRD.md` §6.1 Observability "Partial" | Coverage verification in Phase 20/21 |
| Flyway migrations V1–V14 | 5 | Implemented | `TDOP-backend/src/main/resources/db/migration/` (13 files) | Schema review task (P05-T02) |
| Docker/Nginx deployment (`TDOP-infra`) | 30 | Partial | `docker-compose.yml`, `nginx/nginx.conf`; Adminer present in compose | CI absent (P01-T14, P30-T01); remove Adminer from production |
| Tests: backend JUnit/Mockito/H2, frontend Vitest | 28 | Partial | `TDOP-backend/src/test/java/tdop/**`, `TDOP-frontend/src/tests/**` | Coverage assessment (P28-T04) |
| English/Swahili localization | 9 | Partial | `src/i18n/`; `README.md` "partial localization" | Complete key coverage (P09-T05) |
| Seeded demo accounts with known passwords | 32 | Implemented (production risk) | `V2__seed_data.sql`, `V8__sample_organizations.sql`, `README.md` | Environment guard before launch (P32-T01) |
| Redis caching, push notifications, WhatsApp/SMS, payments, ML matching, Elasticsearch, E2E/load testing, WCAG 2.2 AA | 24, 25, 26, 28, 29 | Planned | `README.md` "Planned / Not Yet Implemented" | Remains in the phase backlog; no code credit |
