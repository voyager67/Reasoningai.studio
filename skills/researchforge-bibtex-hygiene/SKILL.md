---
name: researchforge-bibtex-hygiene
description: >-
  Clean and normalize BibTeX libraries, identify duplicate or malformed entries, standardize DOI and URL fields, and preserve citation-key stability.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# BibTeX Hygiene

## Purpose

Improve bibliography quality without changing the identity of cited sources or damaging LaTeX syntax.

## Input

Bring any material already available: one or more .bib files, target citation style or publisher requirements, and key naming preferences. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Parse entries conservatively and preserve original text before editing. Flag entries that the parser cannot confidently interpret.
2. Normalize field names and DOI forms; remove tracking parameters from URLs only when the canonical destination is certain.
3. Detect likely duplicates by DOI, then normalized title plus author/year. Never merge ambiguous records automatically.
4. Check required fields by entry type and flag missing information rather than inventing it.
5. Preserve capitalization in acronyms and proper nouns with braces where BibTeX style requires it.
6. Keep stable citation keys by default; propose a rename map only when duplicates or collisions require it.
7. Compile a minimal LaTeX test when available and inspect unresolved citations and bibliography warnings.

## Required output

A cleaned candidate .bib file, change report, duplicate review queue, unresolved-field list, and a key-preservation map. Keep the untouched original as the source of truth until review.

## Integrity and safety gates

- Do not guess publication dates, page ranges, venues, or author order.
- Do not merge preprint and final publication entries without explicit version handling.
- Do not strip braces or capitalization protection indiscriminately.
- Do not overwrite the only copy of the user's bibliography.

## Related skills

`citation-verification`, `conference-submission-preflight`, `scientific-writing`

## Example request

> Clean this BibTeX file while preserving keys and listing every uncertain duplicate rather than merging it.
