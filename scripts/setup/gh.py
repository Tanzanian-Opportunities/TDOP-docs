"""Shared GitHub API client for the TDOP setup scripts (stdlib only).

Design rules (Phase 0 prompt, section 2):
- Reads GH_TOKEN from the environment; never hard-codes tokens.
- Retries network errors and transient HTTP failures with exponential backoff.
- HTTP error responses are returned as data (status, payload) - never raised.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API_ROOT = "https://api.github.com"
MAX_RETRIES = 4
RETRYABLE = (408, 429, 500, 502, 503, 504)


def _token():
    tok = os.environ.get("GH_TOKEN", "")
    if not tok:
        sys.exit("error: GH_TOKEN environment variable is not set")
    return tok


def _backoff(attempt, exc=None):
    delay = 2 ** attempt
    if exc is not None:
        try:
            reset = int(exc.headers.get("X-RateLimit-Reset", "0"))
            if reset and exc.headers.get("X-RateLimit-Remaining") == "0":
                delay = min(max(reset - time.time(), 1), 60)
        except Exception:
            pass
    time.sleep(delay)


def request(method, path, body=None, params=None):
    """Return (status, payload). Network/HTTP failures are data, not exceptions."""
    url = path if path.startswith("http") else API_ROOT + path
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    data = json.dumps(body).encode("utf-8") if body is not None else None
    last = (0, {"error": "network unreachable after retries"})
    for attempt in range(MAX_RETRIES + 1):
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", "Bearer " + _token())
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        if data:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8")
                return resp.status, (json.loads(raw) if raw else None)
        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", "replace")
            try:
                payload = json.loads(raw) if raw else None
            except ValueError:
                payload = {"raw": raw}
            if exc.code in RETRYABLE and attempt < MAX_RETRIES:
                _backoff(attempt, exc)
                last = (exc.code, payload)
                continue
            return exc.code, payload  # HTTP errors are data
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last = (0, {"error": str(exc)})
            if attempt < MAX_RETRIES:
                _backoff(attempt)
                continue
    return last


def get(path, params=None):
    return request("GET", path, params=params)


def post(path, body=None):
    return request("POST", path, body=body)


def put(path, body=None):
    return request("PUT", path, body=body)


def graphql(query, variables=None):
    return request("POST", "/graphql", body={"query": query, "variables": variables or {}})


def ok(status):
    """True for the statuses the scripts treat as success (2xx)."""
    return isinstance(status, int) and 200 <= status < 300
