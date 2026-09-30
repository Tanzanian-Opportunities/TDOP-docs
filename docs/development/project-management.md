# Project Management (board workflow, automation, fields, labels, rules)

This file documents **how the delivery board works** (Phase 0 prompt,
section 2). The live, authoritative progress tracker -
current position, sessions, decisions, risks -
remains [`PROJECT_MANAGEMENT.md`](../../PROJECT_MANAGEMENT.md) at the
repository root.

## Board

- **Board:** [TDOP Delivery](https://github.com/orgs/Tanzanian-Opportunities/projects/1)
  (organization project, kanban layout, private).
- **Mirror rule:** the board mirrors `PROJECT_MANAGEMENT.md`; no task is real
  unless it exists in the tracker (and vice versa - 177 cards = 177 tasks).

## Board workflow (six official states)

`BACKLOG` -> `TO DO` -> `IN PROGRESS` -> `CODE REVIEW` -> `TESTING` -> `DONE`

| State | Meaning |
| --- | --- |
| BACKLOG | Identified, not yet groomed |
| TO DO | Groomed and queued for a work cycle |
| IN PROGRESS | Actively being worked |
| CODE REVIEW | Change open as a pull request, under review |
| TESTING | Merged, awaiting verification on develop |
| DONE | Verified and closed |

States are fixed by DEC-003; phase lifecycle wording (`Planned / In progress /
Completed`) is separate (DEC-008).

## Automation map

`.github/workflows/project-board.yml` - **identical in all five repositories** -
applies these rules (prompt section 4):

| Event | Board move |
| --- | --- |
| Issue opened | -> `BACKLOG` |
| Issue assigned | -> `IN PROGRESS` |
| Pull request opened | -> `CODE REVIEW` (also moves its closing-linked issues) |
| Pull request merged | -> `TESTING` (never auto-`DONE`) |
| Issue closed | -> `DONE` |

Notes:

- The workflow adds the issue/PR to the board automatically if it is not on it
  yet (`addProjectV2ItemById`), then sets the status field.
- It authenticates with `secrets.GH_TOKEN` (classic PAT with `project` scope),
  falling back to the built-in `GITHUB_TOKEN`.
- Verification: a scratch issue + scratch PR were walked through all five rules
  and cleaned up (recorded in `PROJECT_MANAGEMENT.md` Session 06).

## Fields

| Field | Kind | Purpose |
| --- | --- | --- |
| `TDOP Status` | single select (custom) | The six workflow states above - the field automation writes |
| Title, Assignees, Labels, Repository, Milestone, Created, Updated, Closed | built-in | GitHub defaults |

The vestigial default `Status` field (`Todo / In progress / Done`) is unused;
`TDOP Status` is the field of record. Phase, component, priority, and due-date
information is carried by labels (below) and by the phase tracking issues -
GitHub Projects v2 due-date/iteration fields are intentionally not used yet.

## Labels (every repository)

| Group | Labels |
| --- | --- |
| `type:` | `type:bug`, `type:feature`, `type:docs`, `type:chore` |
| `component:` | `component:frontend`, `component:backend`, `component:mobile`, `component:docs`, `component:database`, `component:devops` |
| `priority:` | `priority:high`, `priority:medium`, `priority:low` |

Provisioned idempotently by [`scripts/setup/provision_labels.py`](../../scripts/setup/provision_labels.py);
issue templates pre-apply `type:bug` / `type:feature`.

## Rules

1. Issue opened -> Backlog; issue assigned -> In Progress; PR opened ->
   Code Review; PR merged -> Testing (never auto-Done); issue closed -> Done.
2. Cards move only through the six states - never skip TESTING to DONE.
3. The board is updated by automation or by scripts, not by hand-editing
   historical cards (DEC-004: nothing auto-credits completion).
4. Phase statuses use `Planned / In progress / Completed` only (DEC-008).
5. One scratch issue + PR per automation verification, cleaned up afterwards.
6. Branch protection on `develop`: pull requests required, CI status check
   required, administrators not enforced (see `DEVELOPMENT_GUIDE.md` section 6
   for the private-repo paid-plan limitation).

## Related scripts

| Script | Purpose |
| --- | --- |
| [`scripts/setup/provision_board.py`](../../scripts/setup/provision_board.py) | Ensure the project, description, and six-state field exist |
| [`scripts/setup/provision_labels.py`](../../scripts/setup/provision_labels.py) | Ensure labels exist in all repositories |
| [`scripts/setup/seed_phase_issues.py`](../../scripts/setup/seed_phase_issues.py) | Seed the 11 canonical phase issues (0-10) and link them to the board |
