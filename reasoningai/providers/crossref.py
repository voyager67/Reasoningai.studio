from __future__ import annotations

from .common import request_json, encode_query

BASE = "https://api.crossref.org/works"


def lookup_doi(doi: str) -> dict:
    clean = doi.strip()
    clean = clean.removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    clean = clean.removeprefix("doi:").strip()
    if not clean or any(ch.isspace() for ch in clean):
        raise ValueError("Provide one DOI without surrounding text")
    payload = request_json(f"{BASE}/{encode_query(clean)}")
    msg = payload.get("message") or {}
    authors = []
    for author in msg.get("author") or []:
        parts = [author.get("given", ""), author.get("family", "")]
        full = " ".join(p for p in parts if p).strip()
        if full:
            authors.append(full)
    issued = msg.get("published") or msg.get("published-print") or msg.get("created") or {}
    date_parts = issued.get("date-parts") or [[""]]
    date = "-".join(str(x) for x in date_parts[0]) if date_parts else ""
    return {
        "doi": msg.get("DOI", clean),
        "title": (msg.get("title") or [""])[0],
        "authors": "; ".join(authors),
        "container_title": (msg.get("container-title") or [""])[0],
        "published": date,
        "type": msg.get("type", ""),
        "publisher": msg.get("publisher", ""),
        "url": msg.get("URL", ""),
        "indexed": bool(msg),
    }
