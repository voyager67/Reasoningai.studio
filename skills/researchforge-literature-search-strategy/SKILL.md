---
name: researchforge-literature-search-strategy
description: >-
  Design reproducible searches across scholarly databases, produce exact query strings and a search log, and use backward/forward citation chasing. Use for related work, scoping reviews, systematic reviews, or novelty checks.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Literature Search Strategy

## Purpose

Find relevant literature transparently without pretending that one search engine or a small result sample represents the entire field.

## Input

Bring any material already available: research question, discipline, date range, languages, inclusion/exclusion criteria, seed papers, and databases/tools available. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Break the question into concept blocks and list synonyms, acronyms, spelling variants, controlled vocabulary, and domain-specific terms.
2. Choose sources by discipline and coverage: Crossref/OpenAlex for metadata discovery; Semantic Scholar for citation discovery; arXiv for preprints; PubMed/Europe PMC for biomedical work; DBLP for computer science; discipline-specific indexes when available.
3. Write Boolean queries with field restrictions and exact phrases. Create a broad recall-oriented query and a narrower precision-oriented query.
4. Run a pilot search. Inspect the first relevant and irrelevant records, then refine terms while preserving every query version and date.
5. Record database, query, run date, filters, returned count, export format, and any access limitations.
6. Deduplicate by DOI, then normalized title plus year/first author; manually resolve collisions.
7. Use backward and forward citation chasing from strong seed papers. Log each expansion round and stop rule.
8. Report what was searched and what was not searchable. Do not describe a convenience search as exhaustive.

## Required output

A search protocol with database rationale, exact query strings, run dates, filters, search log, deduplication rules, seed set, citation-chasing log, and a transparent coverage statement.

## Integrity and safety gates

- Never invent search hits, counts, database coverage, or a date of search.
- Do not use publisher access restrictions as evidence that a paper does not exist.
- Label preprints and peer-reviewed versions distinctly.
- A search result snippet is discovery evidence, not sufficient evidence for a technical claim.

## Related skills

`research-question-framing`, `paper-triage`, `systematic-review`, `citation-verification`

## Example request

> Build a reproducible search strategy for recent work on parameter-efficient fine-tuning of small language models.
