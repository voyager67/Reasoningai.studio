from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

SECRET_PATTERNS = [
    ("openai_api_key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("github_token", re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}")),
    ("aws_access_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("private_key_block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("generic_api_key_assignment", re.compile(r'(?i)(?:api[_-]?key|secret|access[_-]?token)\s*[:=]\s*[\"\']?[A-Za-z0-9_./+=-]{20,}')),
]


def scan_secrets(paths: list[str | Path]) -> list[dict]:
    """Scan text files recursively and report locations, never secret values."""
    findings = []
    ignored = {".git", ".venv", "venv", "__pycache__", "node_modules", "dist", "build"}
    candidates: list[Path] = []
    for raw in paths:
        path = Path(raw)
        if path.is_file():
            candidates.append(path)
        elif path.is_dir():
            candidates.extend(p for p in path.rglob("*") if p.is_file() and not any(part in ignored for part in p.parts))
    seen = set()
    for path in candidates:
        resolved = path.resolve()
        if resolved in seen or path.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".zip", ".pyc"}:
            continue
        seen.add(resolved)
        try:
            if path.stat().st_size > 2_000_000:
                continue
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue
        for number, line in enumerate(lines, 1):
            for kind, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    findings.append({"file": str(path), "line": number, "kind": kind})
    return findings


def sha256_manifest(root: str | Path, output: str | Path | None = None) -> list[dict]:
    base = Path(root).resolve()
    records = []
    ignored_dirs = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", "build", "dist"}
    target_path = Path(output).resolve() if output else None
    for path in sorted(p for p in base.rglob("*") if p.is_file()):
        if any(part in ignored_dirs for part in path.relative_to(base).parts):
            continue
        if target_path is not None and path.resolve() == target_path:
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        records.append({"path": path.relative_to(base).as_posix(), "sha256": digest, "bytes": path.stat().st_size})
    if output:
        target = Path(output)
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["path", "sha256", "bytes"])
            writer.writeheader()
            writer.writerows(records)
    return records


def audit_claim_ledger(path: str | Path) -> dict:
    required = {"claim_id", "claim", "source_id", "locator", "evidence_status"}
    with Path(path).open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fields = set(reader.fieldnames or [])
        if not required.issubset(fields):
            raise ValueError("Claim ledger is missing columns: " + ", ".join(sorted(required - fields)))
        rows = list(reader)
    issues = []
    for i, row in enumerate(rows, 2):
        for field in ("claim_id", "claim", "source_id", "locator", "evidence_status"):
            if not str(row.get(field, "")).strip():
                issues.append({"row": i, "kind": "missing_field", "field": field})
        status = str(row.get("evidence_status", "")).strip().lower()
        if status not in {"supported", "partially_supported", "contradicted", "unverified", "not_applicable"}:
            issues.append({"row": i, "kind": "invalid_evidence_status", "value": status})
        if status in {"unverified", "contradicted"}:
            issues.append({"row": i, "kind": "claim_requires_review", "value": status})
    return {"rows": len(rows), "issues": issues, "passed": not issues}
