# TDOP Business Roadmap

**Canonical phase list (Phase 0 prompt, section 2).** Eleven business phases,
0 through 10, with a status per phase. Finished phases are marked
**Completed** (never "COMPLETE" or "in progress" - see Decision DEC-008 for the
lifecycle vocabulary).

This is the business-level view. The detailed engineering breakdown (33 phases,
177 tasks) lives in [`TASK_BREAKDOWN.md`](../../TASK_BREAKDOWN.md) and
[`PROJECT_MANAGEMENT.md`](../../PROJECT_MANAGEMENT.md) section 5; the step
roadmap lives in [`Specs/IMPLEMENTATION & FUTURE ROADMAP.md`](../../Specs/IMPLEMENTATION%20%26%20FUTURE%20ROADMAP.md).

## Phases

| Phase | Name | Status |
| --- | --- | --- |
| 0 | Project Setup | Completed |
| 1 | UI/UX Design | Planned |
| 2 | Database Design | Planned |
| 3 | Backend Development | Planned |
| 4 | Frontend Development | Planned |
| 5 | Mobile Development | Planned |
| 6 | Integrations | Planned |
| 7 | AI Features | Planned |
| 8 | Testing | Planned |
| 9 | Deployment | Planned |
| 10 | Launch | Planned |

## Phase descriptions

- **0 Project Setup** - repositories, scaffolding, CI, and project management;
  no product features. Report: [`phase-0-report.md`](../phase-0-report.md).
- **1 UI/UX Design** - design system, wireframes, interactive prototypes.
- **2 Database Design** - schema, migrations, seed strategy.
- **3 Backend Development** - REST API implementation against the SRS.
- **4 Frontend Development** - React web application.
- **5 Mobile Development** - Flutter application (DEC-010).
- **6 Integrations** - payments, messaging, external opportunity sources.
- **7 AI Features** - matching, recommendations, intelligent services.
- **8 Testing** - unit, integration, end-to-end, load, accessibility.
- **9 Deployment** - production infrastructure and rollout (Cloudflare edge, DEC-009).
- **10 Launch** - public release and hypercare.

## Mapping to the engineering plan

Business phases are wider than single engineering phases; for example,
business phase 0 corresponds to engineering `PHASE 01 - Project Initiation`
(Completed) plus the Phase 0 alignment work recorded in Session 06, and
business phases 3-5 span engineering phases 08-24 of the 33-phase plan.
`PROJECT_MANAGEMENT.md` remains the source of truth for engineering progress.
