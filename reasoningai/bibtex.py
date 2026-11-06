from __future__ import annotations

import re
from pathlib import Path

ENTRY_START = re.compile(r"@([A-Za-z]+)\s*\{\s*([^,]+),", re.M)
DOI_RE = re.compile(r'(?i)\bdoi\s*=\s*[\{"]([^}\"]+)[}\"]')


def parse_entries(text: str) -> list[dict]:
    """Parse the common BibTeX form with balanced outer braces.

    This intentionally avoids pretending to be a full BibTeX grammar. It reads
    entry type/key and DOI fields for quick integrity checks; use BibTeX tooling
    for macros, nested expressions, and complex edge cases.
    """
    entries = []
    for match in ENTRY_START.finditer(text):
        start = match.start()
        opening = text.find("{", match.start())
        depth, end = 0, None
        in_quote, escaped = False, False
        for i in range(opening, len(text)):
            ch = text[i]
            if escaped:
                escaped = False
                continue
            if ch == "\\":
                escaped = True
                continue
            if ch == '"':
                in_quote = not in_quote
            if not in_quote:
                if ch == "{": depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        end = i + 1
                        break
        if end is None:
            entries.append({"type": match.group(1).lower(), "key": match.group(2).strip(), "doi": "", "error": "unclosed entry"})
            continue
        block = text[start:end]
        doi_match = DOI_RE.search(block)
        doi = doi_match.group(1).strip() if doi_match else ""
        entries.append({"type": match.group(1).lower(), "key": match.group(2).strip(), "doi": doi, "error": ""})
    return entries


def audit_file(path: str | Path) -> dict:
    source = Path(path)
    text = source.read_text(encoding="utf-8", errors="replace")
    entries = parse_entries(text)
    keys, dois = {}, {}
    issues = []
    for item in entries:
        key = item["key"].lower()
        if key in keys:
            issues.append({"kind": "duplicate_key", "value": item["key"]})
        keys[key] = 1
        doi = item["doi"].lower().removeprefix("https://doi.org/").removeprefix("doi:")
        if doi:
            if doi in dois:
                issues.append({"kind": "duplicate_doi", "value": item["doi"], "entries": [dois[doi], item["key"]]})
            dois[doi] = item["key"]
        if item["error"]:
            issues.append({"kind": "parse_issue", "entry": item["key"], "detail": item["error"]})
    if not entries:
        issues.append({"kind": "no_entries", "value": str(source)})
    return {"file": str(source), "entry_count": len(entries), "entries": entries, "issues": issues, "passed": not issues}
