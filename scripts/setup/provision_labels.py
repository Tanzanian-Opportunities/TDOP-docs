"""Provision the standard label set (type / component / priority) in every repo.

Idempotent: labels that already exist are reported as present (HTTP 422 is data).
Usage:  GH_TOKEN=... python scripts/setup/provision_labels.py
"""

import sys

from gh import get, ok, post

ORG = "Tanzanian-Opportunities"
REPOS = ["TDOP-docs", "TDOP-backend", "TDOP-frontend", "TDOP-infra", "TDOP-mobile"]

LABELS = [
    # type
    ("type:bug", "d73a4a", "Something is broken"),
    ("type:feature", "0075ca", "New capability"),
    ("type:docs", "0052cc", "Documentation change"),
    ("type:chore", "e4e669", "Maintenance / housekeeping"),
    # component
    ("component:frontend", "1d76db", "Web frontend (React)"),
    ("component:backend", "5319e7", "Backend API (Spring Boot)"),
    ("component:mobile", "0e8a16", "Mobile app (Flutter)"),
    ("component:docs", "fbca04", "Documentation / governance"),
    ("component:database", "d93f0b", "Schema, migrations, data"),
    ("component:devops", "7057ff", "CI, Docker, edge, deployment"),
    # priority
    ("priority:high", "b60205", "High priority"),
    ("priority:medium", "e99695", "Medium priority"),
    ("priority:low", "c2e0c6", "Low priority"),
]


def main():
    failures = 0
    for repo in REPOS:
        status, payload = get(f"/repos/{ORG}/{repo}")
        if not ok(status):
            print(f"FAIL  {repo}: cannot read repo (HTTP {status}: {payload})")
            failures += 1
            continue
        created = existing = failed = 0
        for name, color, description in LABELS:
            st, body = post(
                f"/repos/{ORG}/{repo}/labels",
                {"name": name, "color": color, "description": description},
            )
            if ok(st):
                created += 1
            elif st == 422:  # label already exists - data, not an error
                existing += 1
            else:
                failed += 1
                print(f"FAIL  {repo}/{name}: HTTP {st}: {body}")
        failures += failed
        print(f"OK    {repo}: {created} created, {existing} already present, {failed} failed")
    if failures:
        print(f"\n{failures} label operation(s) failed")
        sys.exit(1)
    print("\nAll labels provisioned.")


if __name__ == "__main__":
    main()
