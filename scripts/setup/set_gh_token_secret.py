"""Set the GH_TOKEN repository secret (Actions + Dependabot) in all repos.

The project-board automation needs a PAT with `project` scope because the
default GITHUB_TOKEN cannot resolve organization ProjectV2 boards. Secrets are
encrypted client-side with libsodium sealed box (PyNaCl), per the GitHub API.

Idempotent: re-running re-encrypts and updates the same secret.
Usage:  GH_TOKEN=... python scripts/setup/set_gh_token_secret.py
"""

import base64
import sys

import nacl.public

from gh import ok, put, get

ORG = "Tanzanian-Opportunities"
REPOS = ["TDOP-docs", "TDOP-backend", "TDOP-frontend", "TDOP-infra", "TDOP-mobile"]
SECRET_NAME = "GH_TOKEN"


def seal(token: str, public_key_b64: str) -> str:
    pk = nacl.public.PublicKey(base64.b64decode(public_key_b64))
    sealed = nacl.public.SealedBox(pk).encrypt(token.encode("utf-8"))
    return base64.b64encode(sealed).decode("ascii")


def set_secret(api_prefix: str, token: str) -> str:
    """api_prefix: 'actions/secrets' or 'dependabot/secrets'."""
    st, key = get(f"/repos/{ORG}/{repo}/{api_prefix}/public-key")
    if not ok(st):
        return f"FAIL key {st}: {key}"
    encrypted = seal(token, key["key"])
    st, resp = put(
        f"/repos/{ORG}/{repo}/{api_prefix}/{SECRET_NAME}",
        {"encrypted_value": encrypted, "key_id": key["key_id"]},
    )
    return "OK" if ok(st) else f"FAIL set {st}: {resp}"


if __name__ == "__main__":
    import os

    token = os.environ.get("GH_TOKEN", "")
    if not token:
        sys.exit("error: GH_TOKEN environment variable is not set")
    failed = False
    for repo in REPOS:
        a = set_secret("actions/secrets", token)
        d = set_secret("dependabot/secrets", token)
        print(f"{repo}: actions={a} dependabot={d}", flush=True)
        failed = failed or a.startswith("FAIL") or d.startswith("FAIL")
    sys.exit(1 if failed else 0)
