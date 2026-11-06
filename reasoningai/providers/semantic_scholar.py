from __future__ import annotations

import os
from .common import request_json, encode_query

BASE = "https://api.semanticscholar.org/graph/v1/paper/search"
FIELDS = "title,year,authors,externalIds,abstract,url,citationCount,openAccessPdf"


def search(query: str, limit: int = 10) -> list[dict]:
    key = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "").strip()
    if not key:
        raise RuntimeError("Semantic Scholar requires SEMANTIC_SCHOLAR_API_KEY. Set it in your local environment; never commit it.")
    if not query.strip():
        raise ValueError("Search query must not be empty")
    if not 1 <= limit <= 100:
        raise ValueError("Limit must be between 1 and 100")
    url = f"{BASE}?query={encode_query(query)}&limit={limit}&fields={FIELDS}"
    payload = request_json(url, headers={"x-api-key": key})
    rows = []
    for item in payload.get("data", []):
        authors = "; ".join(a.get("name", "") for a in item.get("authors", []) if a.get("name"))
        pdf = item.get("openAccessPdf") or {}
        ids = item.get("externalIds") or {}
        rows.append({
            "source": "Semantic Scholar",
            "source_id": item.get("paperId", ""),
            "doi": ids.get("DOI", ""),
            "title": item.get("title", ""),
            "year": item.get("year", "") or "",
            "type": "",
            "authors": authors,
            "venue": "",
            "cited_by_count": item.get("citationCount", 0) or 0,
            "is_open_access": bool(pdf.get("url")),
            "landing_page_url": item.get("url", "") or "",
            "abstract": item.get("abstract", "") or "",
        })
    return rows
