from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from . import __version__
from .bibtex import audit_file
from .integrity import scan_secrets, sha256_manifest, audit_claim_ledger
from .screening import initialise_screening, summarise_screening


def _write_records(rows: list[dict], output: str | None) -> None:
    if not rows:
        print("No records returned.")
        return
    fields = list(dict.fromkeys(k for row in rows for k in row.keys()))
    if output:
        with Path(output).open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote {len(rows)} records to {output}")
    else:
        print(json.dumps(rows, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="reasoningai", description="Evidence-first research utilities")
    parser.add_argument("--version", action="version", version=f"ReasoningAI Studio {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    search = sub.add_parser("search", help="Search a scholarly metadata provider")
    search.add_argument("query")
    search.add_argument("--provider", choices=["openalex", "semantic-scholar"], default="openalex")
    search.add_argument("--limit", type=int, default=10)
    search.add_argument("--output", help="Write normalized records to CSV")

    doi = sub.add_parser("doi-check", help="Resolve DOI metadata through Crossref")
    doi.add_argument("dois", nargs="+")

    bib = sub.add_parser("bib-audit", help="Check BibTeX keys and DOI duplicates")
    bib.add_argument("file")

    screen = sub.add_parser("screen-init", help="Add blank title/abstract and full-text screening fields to a CSV")
    screen.add_argument("input_csv")
    screen.add_argument("output_csv")

    prisma = sub.add_parser("prisma", help="Summarize screening decisions entered in a CSV")
    prisma.add_argument("screening_csv")
    prisma.add_argument("--output", help="Write JSON summary to a file")

    claims = sub.add_parser("claim-audit", help="Check traceability fields in a claim-evidence ledger")
    claims.add_argument("ledger_csv")

    manifest = sub.add_parser("manifest", help="Create SHA-256 hashes for a research directory")
    manifest.add_argument("directory")
    manifest.add_argument("--output", default="sha256-manifest.csv")

    secrets = sub.add_parser("secret-scan", help="Scan files for common secret patterns")
    secrets.add_argument("paths", nargs="+")

    doctor = sub.add_parser("doctor", help="Show local runtime and provider configuration")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "search":
            if args.provider == "openalex":
                from .providers.openalex import search
            else:
                from .providers.semantic_scholar import search
            _write_records(search(args.query, args.limit), args.output)
        elif args.command == "doi-check":
            from .providers.crossref import lookup_doi
            results = []
            for doi in args.dois:
                try:
                    results.append(lookup_doi(doi))
                except Exception as exc:
                    results.append({"input": doi, "indexed": False, "error": str(exc)})
            print(json.dumps(results, ensure_ascii=False, indent=2))
            return 0 if all(r.get("indexed") for r in results) else 2
        elif args.command == "bib-audit":
            result = audit_file(args.file)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0 if result["passed"] else 2
        elif args.command == "screen-init":
            count = initialise_screening(args.input_csv, args.output_csv)
            print(f"Created screening ledger for {count} records: {args.output_csv}")
        elif args.command == "prisma":
            result = summarise_screening(args.screening_csv)
            rendered = json.dumps(result, ensure_ascii=False, indent=2)
            if args.output:
                Path(args.output).write_text(rendered + "\n", encoding="utf-8")
                print(f"Wrote screening summary to {args.output}")
            else:
                print(rendered)
        elif args.command == "claim-audit":
            result = audit_claim_ledger(args.ledger_csv)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return 0 if result["passed"] else 2
        elif args.command == "manifest":
            records = sha256_manifest(args.directory, args.output)
            print(f"Hashed {len(records)} files into {args.output}")
        elif args.command == "secret-scan":
            findings = scan_secrets(args.paths)
            if findings:
                print(json.dumps(findings, indent=2))
                return 2
            print("No known secret patterns detected. This is not a guarantee that files are secret-free.")
        elif args.command == "doctor":
            import os, platform
            print(json.dumps({
                "version": __version__,
                "python": platform.python_version(),
                "openalex": "available_without_key (subject to provider limits)",
                "crossref": "available_without_key (subject to provider limits)",
                "semantic_scholar_key_configured": bool(os.getenv("SEMANTIC_SCHOLAR_API_KEY")),
                "contact_email_configured": bool(os.getenv("REASONINGAI_CONTACT_EMAIL")),
                "network_calls": "only on explicit search and doi-check commands",
            }, indent=2))
        return 0
    except (ValueError, OSError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
