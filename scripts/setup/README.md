# TDOP setup scripts

Idempotent provisioning scripts for Phase 0 (prompt section 2). Python 3,
standard library only (`urllib`), no third-party packages.

## Requirements

- `GH_TOKEN` environment variable set to a classic PAT with `repo`, `project`,
  and `admin:org` scopes (retrieved from the Windows Credential Manager via
  `git credential fill` on this machine).

```powershell
$env:GH_TOKEN = (git credential fill <<... # or paste the token)
$env:GH_TOKEN = Get-Content $env:TEMP\tdop_tok.txt -Raw
python scripts/setup/provision_labels.py
python scripts/setup/provision_board.py
python scripts/setup/seed_phase_issues.py
```

## Behaviour

- **Idempotent**: anything that already exists is reported and skipped
  (HTTP 422 "already exists" counts as success-as-data).
- **Retries**: network errors, rate limits (403/429 with
  `X-RateLimit-*` headers), and 5xx responses are retried with exponential
  backoff (max 4 retries).
- **Errors as data**: HTTP error responses are returned as `(status, payload)`
  tuples and printed; they never raise. Exit code 1 only if an operation
  ultimately failed.

## Scripts

| Script | Purpose |
| --- | --- |
| `provision_labels.py` | Ensures `type:*`, `component:*`, `priority:*` labels in all 5 repos |
| `provision_board.py` | Ensures the "TDOP Delivery" project, its description, and the six-state status field |
| `seed_phase_issues.py` | Creates the 11 canonical phase tracking issues (0-10) and links them to the board |
| `gh.py` | Shared client (not run directly) |
