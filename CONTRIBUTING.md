# Contributing to TDOP

**Project:** Tanzania Digital Opportunity Platform (TDOP)
**Repository:** https://github.com/Tanzanian-Opportunities/TDOP-docs
(component repositories and layout: `DEVELOPMENT_GUIDE.md` §2)

Thank you for contributing. This document is the single entry point for how work
enters and moves through the project. It is intentionally short: details live in the
linked documents so nothing is duplicated or contradicted.

**Read first:** [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — by participating you
agree to it.

---

## 1. Contribution lifecycle

Every contribution follows exactly this path:

```text
Issue
  ↓
Backlog          (tracked in PROJECT_MANAGEMENT.md — status BACKLOG)
  ↓
To Do            (status TO DO — ready, dependencies satisfied)
  ↓
Implementation   (status IN PROGRESS — work happens on a branch)
  ↓
Code Review      (status CODE REVIEW — pull request opened)
  ↓
Testing          (status TESTING — automated + manual verification)
  ↓
Done             (status DONE — Definition of Done satisfied)
```

These six states are the **only** permitted statuses. Do not invent states such as
"Almost Done" or "Waiting". If work is blocked, keep the task in its current state
and record the blocker in `PROJECT_MANAGEMENT.md` (Blocker Log).

The authoritative task list, phase, and current position are in
[`PROJECT_MANAGEMENT.md`](PROJECT_MANAGEMENT.md) (task boards:
[`TASK_BREAKDOWN.md`](TASK_BREAKDOWN.md)). The engineering rules for doing
the work are in [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md). The organization
Kanban board (https://github.com/orgs/Tanzanian-Opportunities/projects/1) mirrors
the tracker — update the files first, then move the card to the same state.

## 2. Reporting issues

1. Search existing issues first — add to an open issue rather than duplicating.
2. Open a new issue using this structure:
   - **Title:** short, specific (`[Backend] Refresh token reuse not detected`)
   - **What happened / what is expected**
   - **Steps to reproduce**
   - **Environment** (branch/commit, OS, browser if relevant)
   - **Impact** (users affected, data risk)
   - **Proposed fix**, if you have one
3. **Security issues are not ordinary issues.** Follow [`SECURITY.md`](SECURITY.md)
   and report privately. Never disclose an unpatched vulnerability publicly.
4. The issue is added to `PROJECT_MANAGEMENT.md` in `BACKLOG` (or `TO DO` if it is
   immediately actionable) with an ID and phase assignment.

## 3. Selecting a task

- Pick from `PROJECT_MANAGEMENT.md`: start with the **current phase**, in
  `TO DO`, respecting the **Definition of Ready** (section 7 below).
- Do not start tasks from future phases. Dependencies must be `DONE` before a task
  moves to `IN PROGRESS`, unless the task explicitly concerns parallel preparation.
- Claim the task by setting its `Owner`, moving it to `IN PROGRESS`, and recording
  the `Started` date — in the same change set or a preceding one.
- If you cannot continue, say so: keep the state honest and log the blocker.

## 4. Branch naming

```text
feature/<name>     new functionality
fix/<name>         bug fix
security/<name>    security fix or hardening
docs/<name>        documentation only
refactor/<name>    structural change without behavior change
test/<name>        tests only
chore/<name>       maintenance, tooling, dependencies
```

Rules:

- Lowercase, hyphen-separated, and short but descriptive:
  `feature/opportunity-deadline-reminders`.
- Branch from `develop` (the default branch in every TDOP repository).
- One concern per branch — do not mix a feature with an unrelated refactor.
- Delete the branch after merge.

## 5. Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

```text
<type>: <short imperative summary>

<body — why, and what changed technically>

<footer — BREAKING CHANGE: ..., Closes #123>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `security`, `perf`,
`build`, `ci`, `i18n`.

Rules:

- Subject ≤ 72 characters, imperative mood ("add", not "added"/"adds").
- Explain **why** in the body when it is not obvious.
- Reference the issue/task ID (e.g. `Refs P13-T04`, `Closes #42`).
- No secrets, no `.env` values, no generated artifacts (`target/`, `dist/`, logs).
- Keep the history readable: rebase/fixup before merge rather than after.

## 6. Pull requests

1. Push your branch and open a PR against `develop`.
2. PR description must contain:
   - **What** changed and **why**
   - **Task/issue ID** from `PROJECT_MANAGEMENT.md`
   - **Screenshots** for UI changes
   - **Testing** performed (commands run + results)
   - **Checklist:** Definition of Done (section 8) items, marked or marked N/A with
     reason
   - **Changelog** entry added (or explicit "no changelog needed — why")
3. Keep PRs small and reviewable (target < ~400 changed lines where practical).
4. Mark the task `CODE REVIEW` in `PROJECT_MANAGEMENT.md` when the PR is opened.
5. All conversations resolved + checks green → move to `TESTING`.
6. After tests pass → `DONE` (with completed date).

### Merge requirements

A PR may be merged only when **all** of the following hold:

- [ ] Definition of Done satisfied (section 8)
- [ ] At least one approving review (for security-sensitive areas: explicit security
      review per `SECURITY_STANDARDS.md`)
- [ ] All automated checks pass (build, lint, tests) — CI is a **GAP** until Phase 30;
      until then, the PR author attaches command output
- [ ] No unresolved blockers
- [ ] `CHANGELOG.md` updated when the change is user-visible, security-relevant,
      breaking, or infrastructure/database related
- [ ] Project management updated (`PROJECT_MANAGEMENT.md`)
- [ ] Documentation updated when behavior changed (`DEVELOPMENT_GUIDE.md`, specs,
      README as applicable)
- [ ] No merge conflicts with `develop`
- [ ] Branch deleted after merge; squash or rebase per maintainer preference

## 7. Definition of Ready

A task may move to `IN PROGRESS` only when:

- [ ] Requirement understood
- [ ] Acceptance criteria defined
- [ ] Dependencies identified (and `DONE`, unless parallel preparation)
- [ ] Relevant design/spec available (or explicitly "no design needed")
- [ ] Required environment available (local setup per `DEVELOPMENT_GUIDE.md`)
- [ ] Task has an owner

If these are not met, the task stays in `TO DO`/`BACKLOG` and the missing information
is recorded as the blocker.

## 8. Definition of Done

A task may move to `DONE` only when all applicable items hold:

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

Items marked *(documentation-only: not applicable)* — such as tests for a pure
markdown change — must be explicitly noted as N/A in the PR, never silently skipped.

## 9. Tests

- Backend: `mvn test` in `TDOP-backend/`. Bug fixes need a regression test.
- Frontend: `npm run test` in `TDOP-frontend/`. UI changes need component tests where
  practical.
- Run the relevant suite locally before requesting review; attach results to the PR.
- Never delete or weaken an existing test to make a change pass — fix the code or
  justify the test change in review.

## 10. Documentation

- Behavior/API change → update the corresponding docs in the same PR.
- New endpoint → keep OpenAPI/springdoc and `Specs/TDOP_MASTER_SPEC.md` consistent.
- Governance/workflow change → update `PROJECT_MANAGEMENT.md` (and `CHANGELOG.md`).
- User-facing change → update the relevant repository's `README.md` where relevant.

## 11. Changelog

- Every meaningful change adds a bullet to `[Unreleased]` in
  [`CHANGELOG.md`](CHANGELOG.md) under the right category.
- Categories: `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`,
  `Breaking`, `Infrastructure`, `Database`, `Documentation`.
- **Changes must never be silently omitted.**

## 12. Security

- Vulnerability reports: [`SECURITY.md`](SECURITY.md) — **private channels only**.
- Security work happens on `security/<name>` branches and follows
  [`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md).
- Never commit secrets. Rotate immediately if one leaks (see `SECURITY.md` §5).

## 13. Code of Conduct

Report unacceptable behavior per [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Reports
are confidential; retaliation for good-faith reports is prohibited.

## 14. Related documents

| Document | Purpose |
|---|---|
| [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) | Community behavior |
| [`DEVELOPMENT_GUIDE.md`](DEVELOPMENT_GUIDE.md) | How to build, test, review, release |
| [`PROJECT_MANAGEMENT.md`](PROJECT_MANAGEMENT.md) | Tasks, phases, sessions, logs |
| [`SECURITY.md`](SECURITY.md) | Vulnerability reporting |
| [`SECURITY_STANDARDS.md`](SECURITY_STANDARDS.md) | Technical security requirements |
| [`CHANGELOG.md`](CHANGELOG.md) | Change history |
| `README_PRD.md` / `Specs/` | Product and architecture specification |
