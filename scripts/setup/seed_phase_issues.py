"""Seed one tracking issue per canonical phase (0-10) and link it to the board.

Idempotent: existing phase issues are detected by title and not duplicated.
Usage:  GH_TOKEN=... python scripts/setup/seed_phase_issues.py
"""

import sys

from gh import get, graphql, ok, post

ORG = "Tanzanian-Opportunities"
DOCS_REPO = "TDOP-docs"
PROJECT_NUMBER = 1

PHASES = [
    (0, "Project Setup", "Repositories, scaffolding, CI, project management."),
    (1, "UI/UX Design", "Design system, wireframes, prototypes."),
    (2, "Database Design", "Schema, migrations, seed strategy."),
    (3, "Backend Development", "API implementation."),
    (4, "Frontend Development", "Web application."),
    (5, "Mobile Development", "Flutter application."),
    (6, "Integrations", "Payments, messaging, external services."),
    (7, "AI Features", "Matching, recommendations, intelligence."),
    (8, "Testing", "Unit, integration, end-to-end, load."),
    (9, "Deployment", "Production infrastructure and rollout."),
    (10, "Launch", "Public release."),
]

FIND_PROJECT = """
query($org: String!, $number: Int!) {
  organization(login: $org) { projectV2(number: $number) { id } }
}
"""

LINK_AND_SET = """
mutation($projectId: ID!, $contentId: ID!) {
  addProjectV2ItemById(input: { projectId: $projectId, contentId: $contentId }) {
    item { id }
  }
}
"""

SET_STATUS = """
mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $optionId: ID!) {
  updateProjectV2ItemFieldValue(
    input: { projectId: $projectId, itemId: $itemId, fieldId: $fieldId,
             value: { singleSelectOptionId: $optionId } }
  ) { projectV2Item { id } }
}
"""

STATUS_FIELD = """
query($org: String!, $number: Int!) {
  organization(login: $org) {
    projectV2(number: $number) {
      id
      fields(first: 30) {
        nodes {
          __typename
          ... on ProjectV2SingleSelectField { id name options { id name } }
        }
      }
    }
  }
}
"""


def main():
    # Existing issues (state=all so reopened ones count too).
    st, issues = get(f"/repos/{ORG}/{DOCS_REPO}/issues", {"state": "all", "per_page": 100})
    if not ok(st):
        print(f"FAIL  cannot list issues: HTTP {st}: {issues}")
        sys.exit(1)
    existing = {i["title"]: i["node_id"] for i in issues if "pull_request" not in i}

    st, board = graphql(STATUS_FIELD, {"org": ORG, "number": PROJECT_NUMBER})
    if not ok(st) or (board or {}).get("errors"):
        print(f"FAIL  cannot read board: HTTP {st}: {board}")
        sys.exit(1)
    project = board["data"]["organization"]["projectV2"]
    fields = [
        f
        for f in project["fields"]["nodes"]
        if f.get("__typename") == "ProjectV2SingleSelectField"
    ]
    field = next((f for f in fields if f["name"] == "TDOP Status"), None) or next(
        (f for f in fields if f["name"] == "Status"), None
    )
    backlog = next(
        (o for o in (field.get("options") or []) if o["name"] == "BACKLOG"), None
    ) if field else None
    if not field or not backlog:
        print("FAIL  board has no status field with a BACKLOG option")
        sys.exit(1)

    created = linked = existed = failed = 0
    for number, name, blurb in PHASES:
        title = f"Phase {number} - {name}"
        node_id = None
        if title in existing:
            node_id = existing[title]
            existed += 1
        else:
            body = (
                f"Canonical business phase {number} of the TDOP roadmap.\n\n"
                f"{blurb}\n\n"
                "Tracked in docs/business/roadmap.md. Statuses: Planned / In progress / "
                "Completed. Seeded by scripts/setup/seed_phase_issues.py."
            )
            st, issue = post(
                f"/repos/{ORG}/{DOCS_REPO}/issues",
                {
                    "title": title,
                    "body": body,
                    "labels": ["type:chore", "component:docs"],
                },
            )
            if not ok(st):
                failed += 1
                print(f"FAIL  '{title}': HTTP {st}: {issue}")
                continue
            node_id = issue["node_id"]
            created += 1

        if not node_id:
            continue
        st, link = graphql(
            LINK_AND_SET,
            {
                "projectId": project["id"],
                "contentId": node_id,
            },
        )
        item_id = (
            ((link or {}).get("data") or {}).get("addProjectV2ItemById", {})
            .get("item", {})
            .get("id")
        )
        if ok(st) and item_id:
            linked += 1
            graphql(
                SET_STATUS,
                {
                    "projectId": project["id"],
                    "itemId": item_id,
                    "fieldId": field["id"],
                    "optionId": backlog["id"],
                },
            )
        else:
            print(f"WARN  '{title}' not linked to board: {st}: {link}")

    print(
        f"\nPhases: {created} created, {existed} already existed, "
        f"{linked} linked to board, {failed} failed"
    )
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
