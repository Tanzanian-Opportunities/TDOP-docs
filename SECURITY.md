# Security Policy — TDOP

**Project:** Tanzania Digital Opportunity Platform (TDOP)
**Repository:** https://github.com/Tanzanian-Opportunities/TDOP-docs
(component repositories: `DEVELOPMENT_GUIDE.md` §2)

This document explains **how security vulnerabilities in TDOP are reported and
handled**. The binding technical rules that development must follow are defined
separately in [`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md).

> ## DO NOT publicly disclose an unpatched vulnerability.
>
> Do not open a public GitHub issue, pull request, discussion, or social-media post
> describing an exploitable vulnerability before a fix has been released and the
> maintainer has agreed on a disclosure date.

---

## 1. Supported versions

TDOP has not yet cut a tagged release. Until the first tagged release, security
fixes land on `develop` (the default branch) and are merged to `main` in every
affected repository.

| Version / branch | Supported |
|---|---|
| `develop` + `main` (pre-release, 0.x development) | ✅ Yes — security fixes land here |
| Tagged releases `vX.Y.Z` (once published) | ✅ Latest minor/patch only |
| Older tagged releases | ❌ No — users must upgrade |
| Local forks / unlisted branches | ❌ No — maintainers do not patch third-party forks |

Once releases exist, this table is updated as part of the release process described
in `DEVELOPMENT_GUIDE.md` (Release process).

## 2. Reporting a vulnerability

### 2.1 Preferred channel (private)

Use GitHub's private vulnerability reporting on the repository where the
vulnerability exists:

- **Backend:** https://github.com/Tanzanian-Opportunities/TDOP-backend/security/advisories/new
- **Frontend:** https://github.com/Tanzanian-Opportunities/TDOP-frontend/security/advisories/new
- **Infrastructure, docs, or if unsure:** https://github.com/Tanzanian-Opportunities/TDOP-docs/security/advisories/new

### 2.2 Alternative channels

- Repository maintainer profile (request a private contact channel):
  https://github.com/felix202422
- Dedicated security contact: **[TBD — security contact address to be provided by the
  project owner. Do not invent or guess an address.]** Placeholder ownership and all
  contact points are catalogued in [`MAINTAINERS.md`](MAINTAINERS.md) (P01-T15).

### 2.3 What to include

- Vulnerability type (e.g. SQL injection, broken access control, JWT misuse) and
  affected component (backend endpoint, frontend page, Docker image, migration).
- Affected version / commit SHA or branch.
- Step-by-step reproduction, or a proof-of-concept script.
- Impact: what an attacker can do, and which data or functions are exposed.
- Any suggested fix or mitigating configuration.
- Your preferred credit name (or request to be left anonymous).

### 2.4 What happens next (response expectations)

| Step | Expectation |
|---|---|
| Acknowledgement | Within **5 business days** of receipt |
| Triage & severity assignment | Within **10 business days** (see section 4) |
| Fix or mitigation plan | Critical: **72 hours** to a mitigation; High: **7 days**; Medium: **30 days**; Low: next scheduled release |
| Coordinated disclosure | Agree a public disclosure date with the reporter, normally after a fix is available |
| Credit | Reporters are credited in `CHANGELOG.md` unless they decline |

These are targets, not guarantees. If a target will be missed, the maintainer must
tell the reporter why and give a revised date.

### 2.5 Responsible disclosure

- Report privately first; give maintainers reasonable time to fix before publishing.
- Do not access data that is not yours, do not degrade the service (no denial-of-
  service, mass data extraction, or persistence beyond what is needed to prove the
  issue).
- Do not pivot to unrelated systems, or share the finding with third parties before
  coordinated disclosure.

## 3. Severity handling

Severity is assigned using CVSS v3.1 base score where possible, adjusted for TDOP
context (data sensitivity, exploitability in the deployed architecture).

| Severity | CVSS v3.1 | Example | Target mitigation time |
|---|---|---|---|
| **CRITICAL** | 9.0 – 10.0 | Authentication bypass; JWT secret leak; SQL injection exposing all user data | 72 hours |
| **HIGH** | 7.0 – 8.9 | Broken object-level authorization; stored XSS; privilege escalation to ADMIN | 7 days |
| **MEDIUM** | 4.0 – 6.9 | Missing rate limit on a sensitive endpoint; verbose error leaking non-sensitive internals | 30 days |
| **LOW** | 0.1 – 3.9 | Missing security header; low-impact information disclosure | Next release |
| **NONE** | 0.0 | No security impact — reclassified as an ordinary bug | Normal backlog |

## 4. Security update process

1. **Receive** report privately (section 2).
2. **Reproduce** on a local/dev environment; confirm affected components.
3. **Assign severity** (section 3) and record the issue in `PROJECT_MANAGEMENT.md`
   (Blocker Log if it blocks current work; Risk Register if it is a standing risk).
4. **Develop the fix** on a `security/<name>` branch per `CONTRIBUTING.md`.
5. **Review** — a second reviewer (or, with a single maintainer, a self-review after a
   cool-down plus automated tests) is required for security fixes.
6. **Test** — regression test proving the vulnerability is closed, plus the existing
   suite (`mvn test` / `npm run test`).
7. **Release** — patch lands on `main`; affected users are notified through the
   advisory; the change is recorded under `Security` (and `Breaking` if applicable) in
   `CHANGELOG.md`.
8. **Disclose** — close the advisory and publish details on the agreed date.

## 5. Sensitive information warning

The following must **never** be committed to this repository, placed in issue/PR
text, logged, or shipped in a client bundle:

- Database credentials (`DB_PASSWORD`), JWT signing secret (`JWT_SECRET`), SMTP
  credentials (`MAIL_USERNAME` / `MAIL_PASSWORD`), or API keys of any kind.
- `.env` files (only `.env.example` files are committed).
- Real user personal data, uploaded identity documents, or application documents.
- Production database dumps, logs containing tokens, or session cookies.
- Private vulnerability reports.

Existing `.env.example` files (`TDOP-backend/`, `TDOP-frontend/`, `TDOP-infra/`)
contain placeholders only. If a secret is ever committed: rotate it **immediately**,
treat it as compromised, and record the incident under `Security` in `CHANGELOG.md`.

## 6. Emergency security procedure

For an actively exploited or imminently exploitable vulnerability:

1. Treat as **CRITICAL** regardless of CVSS; start the 72-hour mitigation clock.
2. If a secret is compromised: rotate it first (database password, `JWT_SECRET`, SMTP
   credentials), then invalidate affected sessions/refresh tokens.
3. If user data exposure is possible: prepare an honest user notification describing
   what data was affected, and preserve logs as evidence.
4. If a deployed instance must be shut down to contain the incident: stop public
   access (`docker compose down` or equivalent), keep the database intact for
   analysis, and communicate status through a placeholder channel
   **[TBD — public status page / announcement channel]**.
5. After containment: perform a root-cause review, add regression coverage, and record
   the incident in `CHANGELOG.md` (`Security` section) and in the
   `PROJECT_MANAGEMENT.md` Decision Log if the incident forces an architectural change.

## 7. Scope

### In scope

- Source code in this repository (backend, frontend, infrastructure).
- The Docker Compose deployment configuration in `TDOP-infra/`.
- The Nginx edge configuration in `TDOP-backend/nginx.conf`.
- The Cloudflare edge configuration (dashboard/API) that fronts production.
- Authentication, authorization, and session handling.
- Data handling of seeker, organization, and application data.

### Out of scope

- Social engineering of project participants or end users.
- Denial-of-service against live infrastructure (report the *possibility* only).
- Vulnerabilities in third-party dependencies without a demonstrable impact on TDOP →
  report to the dependency upstream, then notify TDOP if action is needed.
- Findings in environments not deployed from this repository.

## 8. Related documents

- [`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md) — technical standards development
  must follow (authentication, authorization, API, database, frontend, infrastructure,
  privacy).
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — `security/<name>` branch and review rules.
- [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) — security section of the engineering
  lifecycle.
- [`PROJECT_MANAGEMENT.md`](PROJECT_MANAGEMENT.md) — risk register and blocker log.
