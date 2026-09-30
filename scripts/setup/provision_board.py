"""Provision the org Kanban board ("TDOP Delivery") - idempotent.

Ensures the project exists, has a short description, and has a single-select
status field carrying the six official states. Missing-field creation is a
best-effort path reported as data (HTTP/GraphQL errors are never raised).
Usage:  GH_TOKEN=... python scripts/setup/provision_board.py
"""

import sys

from gh import graphql, ok

ORG = "Tanzanian-Opportunities"
PROJECT_TITLE = "TDOP Delivery"
SHORT_DESCRIPTION = (
    "TDOP delivery board - six-state Kanban (BACKLOG / TO DO / IN PROGRESS / "
    "CODE REVIEW / TESTING / DONE). Mirrors TDOP-docs/PROJECT_MANAGEMENT.md."
)
STATES = ["BACKLOG", "TO DO", "IN PROGRESS", "CODE REVIEW", "TESTING", "DONE"]
STATE_COLORS = ["ededed", "0075ca", "fbca04", "5319e7", "0e8a16", "0e8a16"]

QUERY_PROJECTS = """
query($org: String!) {
  organization(login: $org) {
    id
    projectsV2(first: 20) {
      nodes {
        id
        title
        shortDescription
        fields(first: 30) {
          nodes {
            __typename
            ... on ProjectV2SingleSelectField {
              id
              name
              options { id name }
            }
          }
        }
      }
    }
  }
}
"""

CREATE_PROJECT = """
mutation($ownerId: ID!, $title: String!) {
  createProjectV2(input: { ownerId: $ownerId, title: $title }) {
    projectV2 { id title }
  }
}
"""

UPDATE_DESCRIPTION = """
mutation($projectId: ID!, $text: String!) {
  updateProjectV2(input: { projectId: $projectId, shortDescription: $text }) {
    projectV2 { id }
  }
}
"""

CREATE_FIELD = """
mutation($projectId: ID!, $name: String!, $options: [ProjectV2SingleSelectFieldOptionInput!]) {
  createProjectV2Field(
    input: { projectId: $projectId, name: $name, dataType: SINGLE_SELECT, options: $options }
  ) {
    projectV2SingleSelectField { id name options { name } }
  }
}
"""


def option_inputs():
    return [
        {"name": name, "color": color}
        for name, color in zip(STATES, STATE_COLORS)
    ]


def find_status_field(project):
    fields = [
        f
        for f in project["fields"]["nodes"]
        if f.get("__typename") == "ProjectV2SingleSelectField"
    ]
    for wanted in ("TDOP Status", "Status"):
        for f in fields:
            if f["name"] == wanted:
                names = [o["name"] for o in (f.get("options") or [])]
                if all(s in names for s in STATES):
                    return f, True
                if f["name"] == "TDOP Status":
                    return f, False
    return None, False


def main():
    status, data = graphql(QUERY_PROJECTS, {"org": ORG})
    if not ok(status) or (data or {}).get("errors") or not data:
        print(f"FAIL  cannot read org projects: HTTP {status}: {data}")
        sys.exit(1)
    org = data["data"]["organization"]
    project = next(
        (p for p in org["projectsV2"]["nodes"] if p["title"] == PROJECT_TITLE), None
    )

    if project is None:
        st, body = graphql(CREATE_PROJECT, {"ownerId": org["id"], "title": PROJECT_TITLE})
        if not ok(st) or (body or {}).get("errors"):
            print(f"FAIL  cannot create project: HTTP {st}: {body}")
            sys.exit(1)
        project = body["data"]["createProjectV2"]["projectV2"]
        print(f"OK    created project '{PROJECT_TITLE}'")
        st, body = graphql(
            UPDATE_DESCRIPTION, {"projectId": project["id"], "text": SHORT_DESCRIPTION}
        )
        print(
            "OK    short description set"
            if ok(st) and not (body or {}).get("errors")
            else f"WARN  short description not set: {st}: {body}"
        )
        st, body = graphql(
            CREATE_FIELD,
            {
                "projectId": project["id"],
                "name": "TDOP Status",
                "options": option_inputs(),
            },
        )
        print(
            "OK    status field created with six states"
            if ok(st) and not (body or {}).get("errors")
            else f"WARN  status field creation failed (provision manually): {st}: {body}"
        )
        print(f"\nBoard '{PROJECT_TITLE}' provisioned.")
        return

    print(f"OK    project '{PROJECT_TITLE}' already exists ({project['id']})")
    if not project.get("shortDescription"):
        st, body = graphql(
            UPDATE_DESCRIPTION, {"projectId": project["id"], "text": SHORT_DESCRIPTION}
        )
        print(
            "OK    short description set"
            if ok(st) and not (body or {}).get("errors")
            else f"WARN  short description not set: {st}: {body}"
        )
    else:
        print("OK    short description present")

    field, complete = find_status_field(project)
    if field and complete:
        print(f"OK    status field '{field['name']}' has all six states")
    elif field:
        st, body = graphql(
            CREATE_FIELD,
            {"projectId": project["id"], "name": field["name"], "options": option_inputs()},
        )
        print(
            "OK    status options repaired"
            if ok(st) and not (body or {}).get("errors")
            else f"WARN  status options not repaired (do it in the UI): {st}: {body}"
        )
    else:
        st, body = graphql(
            CREATE_FIELD,
            {
                "projectId": project["id"],
                "name": "TDOP Status",
                "options": option_inputs(),
            },
        )
        print(
            "OK    status field created"
            if ok(st) and not (body or {}).get("errors")
            else f"WARN  status field not created (do it in the UI): {st}: {body}"
        )
    print("\nBoard check complete.")


if __name__ == "__main__":
    main()
