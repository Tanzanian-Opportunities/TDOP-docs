# TDOP — Tanzania Digital Opportunity Platform

A digital opportunity discovery and progress platform connecting **seekers**,
**organizations**, and **platform operators** in Tanzania.

**Multi-repository project** under the
[`Tanzanian-Opportunities`](https://github.com/Tanzanian-Opportunities)
organization — backend API, web frontend, Docker infrastructure, documentation,
and a planned mobile app.

> This overview was absorbed from the former `Tanzanian_Opportunities` umbrella
> index repository, which was dissolved and deleted by owner decision
> (DEC-012). This file is now the project overview of record; the governance
> hub is [`README.md`](README.md) in this repository.

**Live Kanban board:** https://github.com/orgs/Tanzanian-Opportunities/projects/1

## Repository Map

| Repository | Contents | Stack |
|---|---|---|
| [`TDOP-docs`](https://github.com/Tanzanian-Opportunities/TDOP-docs) | Governance, specs, project management, this overview (source of truth) | Markdown |
| [`TDOP-backend`](https://github.com/Tanzanian-Opportunities/TDOP-backend) | REST API + Nginx edge config | Java 21, Spring Boot 3.3, Spring Security + JWT, PostgreSQL, Flyway |
| [`TDOP-frontend`](https://github.com/Tanzanian-Opportunities/TDOP-frontend) | Web application | React 18, TypeScript, Vite, Tailwind CSS, React Router |
| [`TDOP-infra`](https://github.com/Tanzanian-Opportunities/TDOP-infra) | Docker Compose orchestration, Cloudflare edge | Docker Compose, Cloudflare |
| [`TDOP-mobile`](https://github.com/Tanzanian-Opportunities/TDOP-mobile) | Planned mobile application | Flutter, Dart (Android + iOS, DEC-010) |

Every repository uses two branches: `develop` (default, integration) and `main`
(releases). See [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) §6.

## Technology Stack

The full stack of the project (stack of record: DEC-005, DEC-010):

| Layer | Technology |
|---|---|
| Backend | Java 21, Spring Boot 3.3 (Web, Data JPA, Security, Validation, Mail, AOP) |
| Authentication | Spring Security + JWT (jjwt 0.12), BCrypt, refresh tokens persisted in DB |
| Database | PostgreSQL 16, Flyway migrations |
| API docs | springdoc-openapi (Swagger UI), base path `/api/v1` |
| Frontend | React 18, TypeScript 5, Vite 5, React Router 6, Tailwind CSS 3 |
| Frontend data/state | TanStack Query, Zustand, React Hook Form, axios |
| i18n | i18next — English + Swahili |
| Mobile | Flutter + Dart — one codebase for all supported devices (Android/iOS) |
| Edge / CDN / DNS / WAF | Cloudflare |
| Origin proxy | Nginx (`TDOP-backend/nginx.conf`; the frontend container ships its own) |
| Deployment | Docker Compose (PostgreSQL, backend, frontend) |
| Testing | JUnit 5 + Mockito + H2 (backend); Vitest + React Testing Library (frontend) |
| Build | Maven (backend), npm (frontend), Flutter (mobile) |
| Logging | SLF4J + Logback (console + rolling file) |
| Binding standards | [`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md), [`CODING_STANDARDS.md`](CODING_STANDARDS.md) |

## Current Implementation Status

### Implemented

- JWT authentication (login, register, refresh, logout, forgot/reset password)
- 9 platform roles: `SEEKER`, `ORGANIZATION`, `ORGANIZATION_ADMIN`, `ORGANIZATION_MEMBER`, `VERIFICATION_OFFICER`, `MODERATOR`, `ADMIN`, `SUPER_ADMIN`
- User profiles (education, skills, experience, interests, career goals)
- Organization profiles with verification workflow
- Opportunity listings with full lifecycle (DRAFT → SUBMITTED → VERIFIED → APPROVED → PUBLISHED → CLOSING_SOON → EXPIRED)
- Applications with status tracking and history
- Saved opportunities and side-by-side comparison
- Moderation workflow (approve/reject/suspend/archive/request-information)
- Report investigation (create → assign → investigate → resolve/dismiss)
- Escalation and appeal systems
- Anti-fraud risk signal detection
- Deadline engine (hourly: expire, closing_soon, reminders with email delivery)
- In-app notifications and email notifications (SMTP)
- File upload (local filesystem with path traversal protection)
- Platform configuration (key-value store in DB)
- RBAC infrastructure (roles, permissions, role-permission assignments)
- Admin dashboard, user management, analytics, audit log
- Trust workspace (verification, moderation, reports, escalations, appeals)
- Super Admin workspace (18 pages: governance, security, intelligence, taxonomy, features, sessions, notifications, integrations, background jobs)
- English/Swahili partial localization
- Multi-field search (title, description, category, tags) with filtered search endpoint
- Opportunity recommendations (skill/interest/location matching)
- Similar opportunities engine
- Social sharing (WhatsApp, Twitter, LinkedIn, Facebook)
- Weekly digest email service (Monday 8AM cron)
- Security headers (X-Frame-Options, HSTS, Referrer-Policy, XSS-Protection)
- Account lockout (5 failed attempts → 15min lockout)
- Login rate limiting (20 requests/min/IP)
- Password reset token expiry (30min)
- Email verification tokens with expiry (60min)
- Opportunity ownership checks (org members can only manage their own)
- Lifecycle state machine validation (Opportunity, Application, Report)
- Production-ready Dockerfile (non-root user, multi-stage build)
- Frontend Dockerfile with nginx (SPA fallback, security headers, gzip)
- Production logging (logback: console + rolling file)

> This inventory does **not** grant phase completion (Decision DEC-004); the
> verified-by-file audit lives in
> [`EXISTING_IMPLEMENTATION_AUDIT.md`](EXISTING_IMPLEMENTATION_AUDIT.md).

### Planned / Not Yet Implemented

- Redis caching and token revocation
- Push notifications (web/mobile)
- WhatsApp / SMS integration
- Payment / subscription engine
- Machine learning matching
- Elasticsearch
- E2E testing, load testing
- Full accessibility (WCAG 2.2 AA)

## Quick Start (Local Development)

Clone the repositories **as siblings** in one directory (the Docker build contexts
depend on this layout):

```bash
git clone https://github.com/Tanzanian-Opportunities/TDOP-backend.git
git clone https://github.com/Tanzanian-Opportunities/TDOP-frontend.git
git clone https://github.com/Tanzanian-Opportunities/TDOP-infra.git
git clone https://github.com/Tanzanian-Opportunities/TDOP-docs.git
```

### Prerequisites

- Java 21+
- Maven 3.8+
- Node.js 18+
- PostgreSQL (port 5432)

### 1. Database

Create a PostgreSQL database named `tdop`. Flyway creates and seeds the schema on backend startup.

### 2. Backend

```bash
cd TDOP-backend
cp .env.example .env   # set DB_PASSWORD, JWT_SECRET
mvn spring-boot:run
```

Serves on `http://localhost:8080` (API base `/api/v1`).

### 3. Frontend

```bash
cd TDOP-frontend
cp .env.example .env
npm install
npm run dev
```

Serves on `http://localhost:3000`, proxying `/api` to the backend.

## Seeded Demo Accounts

Flyway seeds 13 users in `V2__seed_data.sql` and `V8__sample_organizations.sql`
(**development only — must not exist in production**):

| Email | Role | Password |
|---|---|---|
| `admin@tdop.go.tz` | ADMIN | `admin123` |
| `superadmin@tdop.go.tz` | ADMIN | `superadmin` |
| `admin2024@tdop.go.tz` | ADMIN | `admin2024` |
| `john.mwangi@email.com` | SEEKER | `seeker123` |
| `amina.hassan@email.com` | SEEKER | `seeker123` |
| `info@tanzgold.com` | ORGANIZATION (verified) | `org123` |
| `contact@safaricomTZ.com` | ORGANIZATION | `org123` |
| `hr@crdbbank.com` | ORGANIZATION | `org123` |
| `careers@vodacom.co.tz` | ORGANIZATION (verified) | `org123` |
| `hr@nmbbank.com` | ORGANIZATION | `org123` |

## Docker Deployment

```bash
cd TDOP-infra
cp .env.example .env   # REQUIRED: set POSTGRES_PASSWORD and JWT_SECRET
docker compose up -d --build
```

Services: `tdop-postgres` (PostgreSQL 16), `tdop-backend` (port 8080), `tdop-frontend` (port 3000), `tdop-adminer` (port 8082, dev only).

Full deployment procedure: [`Specs/DEPLOYMENT_CHECKLIST.md`](Specs/DEPLOYMENT_CHECKLIST.md).

## Documentation

| Document | Purpose |
|---|---|
| [`PROJECT_MANAGEMENT.md`](PROJECT_MANAGEMENT.md) | **Live source of truth**: phase, tasks, sessions, decisions |
| [`TASK_BREAKDOWN.md`](TASK_BREAKDOWN.md) | Master Kanban (177 tasks) and all 33 phase boards |
| [`README_PRD.md`](README_PRD.md) | Product requirements document |
| [`Specs/SRS.md`](Specs/SRS.md) | Software requirements specification |
| [`Specs/TDOP_MASTER_SPEC.md`](Specs/TDOP_MASTER_SPEC.md) | Architecture and implementation specification |
| [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) | Engineering lifecycle and standards |
| [`CODING_STANDARDS.md`](CODING_STANDARDS.md) | Binding coding standards |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution workflow |
| [`SECURITY.md`](SECURITY.md) | Vulnerability reporting and disclosure |
| [`MAINTAINERS.md`](MAINTAINERS.md) | Owners and contacts |
| [`CHANGELOG.md`](CHANGELOG.md) | Change history per project part + phase completion status |

## License

MIT — see [`LICENSE`](LICENSE) (single license of record, kept in `TDOP-docs`).
