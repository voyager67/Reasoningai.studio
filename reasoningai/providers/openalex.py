from __future__ import annotations

from .common import request_json, encode_query

BASE = "https://api.openalex.org/works"
FIELDS = "id,doi,title,publication_year,type,cited_by_count,authorships,primary_location,open_access,abstract_inverted_index"


def _abstract_from_inverted_index(index: dict | None) -> str:
    if not isinstance(index, dict):
        return ""
    positions: list[tuple[int, str]] = []
    for word, offsets in index.items():
        if isinstance(offsets, list):
            for pos in offsets:
                if isinstance(pos, int):
                    positions.append((pos, word))
    positions.sort(key=lambda item: item[0])
    return " ".join(word for _, word in positions)


def normalize(record: dict) -> dict:
    authors = []
    for item in record.get("authorships") or []:
        author = (item or {}).get("author") or {}
        name = author.get("display_name")
        if name:
            authors.append(name)
    location = record.get("primary_location") or {}
    source = location.get("source") or {}
    oa = record.get("open_access") or {}
    return {
        "source": "OpenAlex",
        "source_id": record.get("id", ""),
        "doi": record.get("doi", "") or "",
        "title": record.get("title", "") or "",
        "year": record.get("publication_year", "") or "",
        "type": record.get("type", "") or "",
        "authors": "; ".join(authors),
        "venue": source.get("display_name", "") or "",
        "cited_by_count": record.get("cited_by_count", 0) or 0,
        "is_open_access": oa.get("is_oa", False),
        "landing_page_url": location.get("landing_page_url", "") or "",
        "abstract": _abstract_from_inverted_index(record.get("abstract_inverted_index")),
    }


def search(query: str, limit: int = 10) -> list[dict]:
    if not query.strip():
        raise ValueError("Search query must not be empty")
    if not 1 <= limit <= 100:
        raise ValueError("Limit must be between 1 and 100")
    url = f"{BASE}?search={encode_query(query)}&per_page={limit}&select={FIELDS}"
    payload = request_json(url)
    return [normalize(item) for item in payload.get("results", [])]
