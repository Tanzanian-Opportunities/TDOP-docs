# Templates (canonical copies)

Canonical copies of the cross-repository boilerplate required by the Phase 0
prompt. Each repository holds its own copy; **this directory is the master** -
when a template changes, update every repository's copy in the same change set.

| Template | Destination in an app repo |
| --- | --- |
| `workflows/ci-<stack>.yml` | `.github/workflows/ci.yml` (pick the stack) |
| `workflows/project-board.yml` | `.github/workflows/project-board.yml` (identical in **all** repos) |
| `dependabot/<repo>.yml` | `.github/dependabot.yml` |
| `CODEOWNERS` | `.github/CODEOWNERS` |
| `.editorconfig` | `.editorconfig` |
| `SECURITY.md` | `SECURITY.md` (adjust the advisory URL per repository) |
| `LICENSE-PROPRIETARY.txt` | `LICENSE` (app repositories only - all rights reserved, DEC-013) |
| `ISSUE_TEMPLATE/bug_report.md` | `.github/ISSUE_TEMPLATE/bug_report.md` |
| `ISSUE_TEMPLATE/feature_request.md` | `.github/ISSUE_TEMPLATE/feature_request.md` |
| `pull_request_template.md` | `.github/pull_request_template.md` |

CI expectations (prompt section 5): run on push to `main`/`develop` and on
pull requests, pin third-party actions to major tags, cancel superseded PR
runs, and finish green on `develop` before a phase counts as Completed.
