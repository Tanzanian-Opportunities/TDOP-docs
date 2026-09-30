# Security Standards — TDOP

**Project:** Tanzania Digital Opportunity Platform (TDOP)

`SECURITY.md` explains **how vulnerabilities are reported and handled**.
**This file** defines the **technical security standards TDOP must follow during
development**. These standards are binding: a task cannot reach `DONE` in
`PROJECT_MANAGEMENT.md` while a applicable standard here is unmet.

Where a standard reflects something already implemented in the repository, the
current implementation is named so future work does not regress it. Where a standard
is not yet met, it is marked **GAP** and must be tracked as a task (currently visible
in the `PROJECT_MANAGEMENT.md` Master Kanban / Existing Implementation Audit).

**Stack in scope:** Java 21, Spring Boot 3.3, Spring Security, JWT (jjwt), PostgreSQL,
Flyway (backend); React 18, TypeScript, Vite (frontend); Docker, Nginx (infrastructure).

---

## 1. Authentication

### 1.1 Password storage and handling

- Passwords are hashed with **BCrypt** (`BCryptPasswordEncoder` — see
  `SecurityConfig.java`). Plaintext passwords must never be stored, logged, returned
  by an API, or included in error messages.
- Passwords must be validated at registration/reset against minimum length and
  complexity rules defined in one place (backend validation is authoritative; the
  frontend may mirror it for UX only).
- Password reset and email-verification tokens are single-use, random, stored
  server-side, and expire (reset: 30 minutes; verification: 60 minutes — as
  implemented). Expired or used tokens must be invalidated in the database, not only
  ignored.
- Credential comparison must be constant-time where feasible; authentication failures
  must not reveal whether an account exists.

### 1.2 JWT security

- The signing secret comes **only** from the `JWT_SECRET` environment variable
  (`application.yml: secret: ${JWT_SECRET}`). Hard-coded secrets are prohibited.
- `JWT_SECRET` must be a high-entropy value (≥ 256 bits), unique per environment, and
  must never appear in git, logs, or frontend bundles.
- Access tokens are short-lived; refresh tokens are long-lived
  (`refresh-expiration: 604800000` ms = 7 days) and are **persisted server-side**
  (migration `V12__persist_tokens_to_db.sql`) so they can be revoked.
- Tokens must be validated on every request for: signature, expiry, issuer/audience
  (if configured), and revocation status.
- Rotating/revoking refresh tokens on use (reuse detection) is a **GAP** tracked in
  the roadmap; until implemented, logout must delete the stored refresh token.
- Secrets and tokens must never be written to application logs
  (`logback-spring.xml` must not log `Authorization` headers or bodies containing
  tokens).

### 1.3 Session and account protection

- Account lockout: **5 failed attempts → 15-minute lockout** (implemented).
- Login rate limiting: **20 requests/minute/IP** (implemented via the rate-limit
  filter). Rate limits must also protect registration, password reset, and refresh.
- Logout must invalidate the session/refresh token server-side, not just clear client
  state.
- Password changes and resets must invalidate all other active sessions/refresh
  tokens for that user **GAP**.
- Concurrent-session visibility and revocation is listed in the Super Admin
  workspace; until implemented, treat refresh-token deletion as the revocation
  mechanism.

## 2. Authorization

### 2.1 Role-based access control (RBAC)

- TDOP uses fixed platform roles (`SEEKER`, `ORGANIZATION`,
  `ORGANIZATION_ADMIN`, `ORGANIZATION_MEMBER`, `VERIFICATION_OFFICER`, `MODERATOR`,
  `ADMIN`, `SUPER_ADMIN`). Roles and permission assignments live in the database
  (`rbac` package, migration `V7__rbac_org_teams_opportunity_lifecycle.sql`).
- Every protected endpoint must declare its required role/permission. Endpoints must
  be **deny-by-default**: unauthenticated requests are rejected except explicitly
  public routes.
- The RBAC service must be enforced at the method/endpoint layer, not only encoded in
  the frontend UI. Hiding a button is never sufficient authorization (**GAP**: PRD
  notes URL-level checks only — RBAC service not fully wired).

### 2.2 Least privilege and ownership

- **Least privilege:** a role receives only the permissions required for its
  function. `ORGANIZATION_MEMBER` must not perform `ORGANIZATION_ADMIN` actions;
  `MODERATOR` must not perform `SUPER_ADMIN` governance actions.
- **Ownership checks:** organization members may only read/modify their own
  organization's opportunities and applications (implemented). Every object-level
  endpoint (`/{id}`) must verify that the caller owns or is permitted to access the
  object — otherwise return `404` (preferred, to avoid existence leaks) or `403`
  consistently.
- **Organization isolation:** cross-tenant queries must always be scoped by the
  caller's organization ID server-side.
- **ADMIN vs SUPER_ADMIN boundaries** must follow `Specs/TDOP_MASTER_SPEC.md`
  (sections 5.2 and 19.2): SUPER_ADMIN owns platform governance/configuration;
  ADMIN owns day-to-day operations.

## 3. API security

- **Validation:** every request body, path variable, and query parameter is validated
  (`spring-boot-starter-validation`, DTO-level `@Valid`). Invalid input → `400` with a
  standard error body; never a stack trace.
- **Input sanitization:** treat all user-provided content (opportunity titles,
  descriptions, tags, profiles, file names) as untrusted. Strip/escape control
  characters; never build SQL/HTML/OS commands from user input by concatenation.
- **Rate limiting:** applied globally and tightened on auth endpoints (see 1.3).
  All new sensitive endpoints (submit, verify, moderate, upload) must be covered.
- **Secure error handling:** global exception handling returns a consistent error
  contract (`code`, `message`, optional field errors). Production responses must not
  expose exception class names, SQL, stack traces, or internal paths. 5xx responses
  log details server-side and return a generic message.
- **HTTP method and content type:** use correct verbs; reject unexpected content
  types; support only JSON for API bodies (uploads use multipart with size limits).
- **CORS:** restricted to the configured frontend origin(s); credentials only if
  required; never `*` with credentials in production.
- **Pagination:** list endpoints are paginated (prevents unbounded data export).
- **File upload:** filename sanitization, path-traversal protection (implemented),
  extension/MIME allow-list, size limit, storage outside the web root, and no
  executable content served as HTML. Stored files must be re-validated on download
  (content-type sniffing).
- **API versioning:** public API surface lives under `/api/v1`. Breaking changes
  require a new version segment and a `Breaking` changelog entry.
- **OpenAPI:** springdoc is available; endpoint changes must keep documentation
  consistent with `Specs/TDOP_MASTER_SPEC.md`.

## 4. Database

- **Parameterized queries only:** use JPA/JPQL or JDBC bind parameters. String-built
  queries (e.g. `EntityManager` with concatenated JPQL/SQL from user input) are
  prohibited; native SQL must use bind variables. `LIKE` patterns from user input must
  escape `%` and `_`.
- **Migrations:** schema changes are made **only** through Flyway migrations
  (`TDOP-backend/src/main/resources/db/migration/V*__.sql`). Never edit an applied
  migration; add a new versioned file. Migrations must be reversible where practical
  and reviewed like code (they run against real data).
- **Least-privilege database account:** the application connects with a dedicated
  role that can only `SELECT/INSERT/UPDATE/DELETE` on required objects — no superuser,
  no DDL at runtime (**GAP**: verify the deployed role; default PostgreSQL
  `POSTGRES_USER` in `TDOP-infra` must not be the application user in production).
- **Secrets management:** `DB_PASSWORD` comes from the environment (`.env`, not
  committed). No credentials in migration/seed SQL, connection strings, or code.
- **Backups:** production database must have scheduled backups with a tested restore
  procedure (**GAP** — tracked as infrastructure task). Backups contain personal data
  and are subject to the same protection as production.
- **Seed data:** `V2__seed_data.sql` / `V8__sample_organizations.sql` contain demo
  accounts with known passwords — they must never be applied to a production
  environment (**GAP**: add an environment guard before production launch,
  Phase 32).
- **Audit trail:** security-relevant actions (login, role change, verification,
  moderation) are recorded in the audit log; audit records must be append-only from
  application code.

## 5. Frontend

- **XSS prevention:** React's default escaping is relied upon; `dangerouslySetInnerHTML`
  is prohibited without strict sanitization. User-generated content rendered as HTML
  must be sanitized server-side and client-side.
- **Secure token storage:** store access/refresh tokens in `httpOnly`, `Secure`,
  `SameSite` cookies where the architecture allows; if `localStorage` is used, document
  it as an accepted risk and mitigate with short-lived access tokens and refresh
  rotation (**GAP** — current approach must be verified and recorded in the audit).
  Never store passwords or raw personal documents in client storage.
- **Authentication handling:** auth state is centralized (auth context/store); route
  guards must be complemented by server-side authorization (see section 2 — the
  frontend guard is UX only).
- **Dependency security:** run `npm audit` before releases; upgrade vulnerable
  dependencies; dev-only tooling must not ship in production bundles.
- **Environment variables:** only `VITE_*` values are exposed to the browser — they
  are public by definition. Never put secrets in `VITE_*` variables.
- **Security headers** (enforced by Nginx/Docker config): `X-Frame-Options`,
  `X-Content-Type-Options`, `Referrer-Policy`, `Strict-Transport-Security`,
  `X-XSS-Protection`, and a restrictive Content-Security-Policy (**GAP**: CSP not yet
  declared — Phase 27).
- **External links** opened with `rel="noopener noreferrer"`.

## 6. Infrastructure

- **HTTPS everywhere** in production: TLS terminated at Nginx/reverse proxy; HTTP
  redirected to HTTPS; HSTS enabled after TLS is confirmed working.
- **Secrets:** provided via environment/.env files excluded from git; in production
  prefer a secret manager or orchestrator secrets. Rotating `JWT_SECRET` invalidates
  existing tokens — plan rotation windows.
- **Container security:** multi-stage builds, non-root users (implemented in both
  Dockerfiles), pinned base images with periodic rebuilds for CVE fixes, no build
  tools in runtime images, read-only filesystem where possible, and resource limits.
- **Network/firewall:** only required ports are published (PostgreSQL must not be
  publicly reachable; Adminer must not exist in production), services communicate over
  an internal Docker network.
- **Logging:** structured application logging (console + rolling files) with
  log rotation; never log secrets, tokens, passwords, or full personal records.
  Security events (auth failures, lockouts, permission denials) are logged with
  actor, target, and timestamp.
- **Monitoring/health:** health checks exposed for containers; failed authentications
  and error rates monitored. Alerting targets are a **GAP** (Observability is listed
  as Partial in `README_PRD.md`).

## 7. Secure development

- **Dependency scanning:** backend — OWASP dependency check or equivalent in CI
  (**GAP**: no CI workflows exist yet); frontend — `npm audit`. Findings are triaged
  using the severity table in `SECURITY.md`.
- **Code review:** no production change merges without review against
  `DEVELOPMENT_GUIDE.md` standards; security-sensitive code (auth, authz, uploads,
  payments, external ingestion) always gets explicit reviewer attention on the
  checklist.
- **Security testing:** unit/integration tests must include at least:
  unauthorized access to a protected endpoint (`401/403`), cross-organization access
  attempt, and invalid/expired token cases. Penetration-style testing and DAST are
  scheduled in **PHASE 27 — Complete Security Hardening** and **PHASE 28 — Complete
  Testing**.
- **Vulnerability management:** reports follow `SECURITY.md`; fixed issues are
  recorded in `CHANGELOG.md` under `Security`; outstanding risks live in the
  `PROJECT_MANAGEMENT.md` Risk Register.
- **Secrets in code:** pre-commit/CI must block committed secrets (`.env` is
  git-ignored; add secret scanning when CI exists — **GAP**).
- **Input fuzzing / abuse cases:** abuse cases for moderation, verification, and
  application flows are tested as part of Phase 28.

## 8. Privacy

- **Minimize personal data:** collect only what the feature needs (profile fields
  defined in `README_PRD.md` §8). Do not collect ID numbers, financial data, or
  documents unless a feature explicitly requires them and Phase 20 governance approves
  the field.
- **Protect sensitive data:** uploaded documents (`V5__user_documents.sql`) are
  access-controlled to the owner and authorized staff; personal data is excluded from
  logs, analytics events, and error messages.
- **Retention:** define and implement retention periods for accounts, applications,
  uploaded documents, tokens, and logs (**GAP** — retention policy is TBD; must be
  defined in Phase 20 / Phase 27).
- **Access control on personal data:** seekers see their own data; organizations see
  only applicants to their opportunities; staff access is role-restricted and
  auditable.
- **User rights:** account deletion/export requests are handled by platform governance
  (**GAP** — TBD design in Phase 20).
- **Third parties:** no third-party analytics or trackers are added without a
  documented decision in the `PROJECT_MANAGEMENT.md` Decision Log.

## 9. Standards checklist (Definition of Done for security-relevant tasks)

A security-relevant task is not `DONE` unless:

- [ ] Authentication/authorization requirements for the change are identified.
- [ ] Inputs are validated server-side; output encoding is correct.
- [ ] Ownership/tenant checks exist for object-level endpoints.
- [ ] No secrets, tokens, or personal data in code, logs, or errors.
- [ ] Tests cover the allow and deny paths (including `401`/`403`).
- [ ] Migration (if any) follows the Flyway rules and does not edit applied files.
- [ ] Reviewer explicitly checked this file's applicable sections.
- [ ] `CHANGELOG.md` updated (`Security`/`Breaking` where applicable).

## 10. Related documents

- [`SECURITY.md`](SECURITY.md) — reporting, disclosure, severity, response.
- [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) — lifecycle and engineering rules.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — `security/<name>` branches and review.
- [`PROJECT_MANAGEMENT.md`](PROJECT_MANAGEMENT.md) — gaps tracked as tasks, risks,
  and blockers.
- `Specs/TDOP_MASTER_SPEC.md` — authoritative role and workspace boundaries.
