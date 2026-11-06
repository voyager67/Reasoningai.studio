---
name: researchforge-citation-verification
description: >-
  Check DOI and bibliographic metadata against authoritative registries, detect mismatches and unresolved references, and produce a citation audit. Use before submission or when a bibliography may contain hallucinated citations.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Citation Verification

## Purpose

Verify that a cited work is real and that the metadata matches the cited source. Existence, metadata match, and claim support are separate checks.

## Input

Bring any material already available: BibTeX, RIS, CSL JSON, CSV, or a reference list; optional manuscript passages containing the claims those references support. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Extract DOI, title, authors, year, venue, and URL for each record. Preserve the original citation for comparison.
2. Normalize DOI syntax and query Crossref or another authoritative registry. Use the publisher record or repository page as a second check when metadata conflicts.
3. Compare title, first author, year, venue, and DOI independently. Return “mismatch” when fields disagree materially.
4. For records without DOI, search by exact title and author in suitable scholarly indexes and label the result “candidate match” until confirmed.
5. Verify the version: preprint, proceedings, journal article, correction, retraction, or updated version.
6. Separately inspect whether the source actually supports the sentence. A correct DOI does not prove claim support.
7. Produce a repair queue with evidence links and confidence, not silent automatic substitutions.

## Required output

A row per reference: original key; normalized DOI; registry status; metadata match; version notes; claim-support status; resolver/registry URL; confidence; and recommended action.

## Integrity and safety gates

- Never create a plausible-looking reference to fill a gap.
- Never label a citation “verified” solely because its DOI URL resolves.
- Do not silently replace a mismatched source.
- A registry outage or rate limit must be reported as “not checked”, not “not found”.

## Related skills

`bibtex-hygiene`, `literature-search-strategy`, `deep-paper-reading`, `results-to-claims`

## Example request

> Audit every entry in refs.bib and identify fabricated, mismatched, incomplete, and unverified citations.
