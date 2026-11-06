from __future__ import annotations

import csv
from pathlib import Path

BASE_FIELDS = ["record_id", "title", "year", "authors", "doi", "abstract"]
DECISION_FIELDS = ["title_abstract_decision", "title_abstract_reason", "full_text_available", "full_text_decision", "full_text_exclusion_reason", "reviewer", "notes"]


def initialise_screening(input_csv: str | Path, output_csv: str | Path) -> int:
    source, target = Path(input_csv), Path(output_csv)
    with source.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        if not fields:
            raise ValueError("Input CSV has no header row")
        rows = list(reader)
    missing = [name for name in ("title",) if name not in fields]
    if missing:
        raise ValueError("Input CSV is missing required column(s): " + ", ".join(missing))
    if "record_id" not in fields:
        fields.append("record_id")
    for name in DECISION_FIELDS:
        if name not in fields:
            fields.append(name)
    with target.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for i, row in enumerate(rows, start=1):
            row.setdefault("record_id", f"record-{i:05d}")
            for name in DECISION_FIELDS:
                row.setdefault(name, "")
            writer.writerow(row)
    return len(rows)


def summarise_screening(path: str | Path) -> dict:
    with Path(path).open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    total = len(rows)
    duplicates = sum(1 for r in rows if str(r.get("duplicate", "")).strip().lower() in {"1", "true", "yes", "y"})
    screened = total - duplicates
    decisions = [str(r.get("title_abstract_decision", "")).strip().lower() for r in rows]
    excluded_ta = sum(d == "exclude" for d in decisions)
    advanced = sum(d in {"include", "maybe", "unclear"} for d in decisions)
    full_text_excluded = sum(str(r.get("full_text_decision", "")).strip().lower() == "exclude" for r in rows)
    full_text_included = sum(str(r.get("full_text_decision", "")).strip().lower() == "include" for r in rows)
    no_full_text = sum(str(r.get("full_text_available", "")).strip().lower() in {"no", "false", "0"} for r in rows if str(r.get("title_abstract_decision", "")).strip().lower() in {"include", "maybe", "unclear"})
    reasons: dict[str, int] = {}
    for row in rows:
        reason = str(row.get("full_text_exclusion_reason", "")).strip() or str(row.get("title_abstract_reason", "")).strip()
        if str(row.get("full_text_decision", "")).strip().lower() == "exclude" and reason:
            reasons[reason] = reasons.get(reason, 0) + 1
    return {
        "records_imported": total,
        "duplicates_marked": duplicates,
        "records_after_deduplication": screened,
        "title_abstract_excluded": excluded_ta,
        "records_advanced_to_full_text": advanced,
        "full_text_not_available": no_full_text,
        "full_text_excluded": full_text_excluded,
        "studies_marked_included": full_text_included,
        "full_text_exclusion_reasons": reasons,
        "note": "Counts reflect only rows and decisions entered in this CSV. Confirm database-specific PRISMA stages and reconcile multiple reports per study before publication.",
    }
