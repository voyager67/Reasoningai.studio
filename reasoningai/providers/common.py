from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

USER_AGENT = "ReasoningAI-Studio/1.0 (research metadata utility; contact: {contact})"


def request_json(url: str, *, headers: dict[str, str] | None = None, timeout: int = 20) -> Any:
    """Fetch JSON from an explicitly selected public scholarly endpoint."""
    contact = os.getenv("REASONINGAI_CONTACT_EMAIL", "not-provided")
    request_headers = {
        "Accept": "application/json",
        "User-Agent": USER_AGENT.format(contact=contact),
    }
    if headers:
        request_headers.update(headers)
    req = urllib.request.Request(url, headers=request_headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            raw = response.read()
    except urllib.error.HTTPError as exc:
        detail = exc.read(500).decode("utf-8", errors="replace")
        raise RuntimeError(f"Provider returned HTTP {exc.code}: {detail}") from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"Could not reach scholarly provider: {exc}") from exc
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("Provider returned invalid JSON") from exc


def encode_query(value: str) -> str:
    return urllib.parse.quote(value.strip(), safe="")
