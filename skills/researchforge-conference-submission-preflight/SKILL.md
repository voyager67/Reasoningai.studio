---
name: researchforge-conference-submission-preflight
description: >-
  Audit a manuscript and artifacts against a target conference or journal’s current author instructions, formatting rules, anonymization, ethics, and submission requirements.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Conference Submission Preflight

## Purpose

Catch avoidable submission defects without claiming that a checklist guarantees acceptance or complete compliance.

## Input

Bring any material already available: target venue and track, manuscript source/PDF, supplementary files, references, author metadata, and submission deadline. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Identify the exact venue, track, year, submission type, and official author-instruction URL. Retrieve the current rules rather than relying on memory.
2. Record paper length, page/word limits, formatting template, reference style, supplementary rules, and allowed appendices.
3. Check anonymization, acknowledgements, self-citations, repository links, author metadata, and conflict-of-interest declarations.
4. Audit figures, tables, fonts, accessibility, embedded fonts, PDF metadata, and supplementary file formats.
5. Check ethics statements, data/code availability, funding, competing interests, and required declarations.
6. Run citation and claim-evidence checks; confirm every referenced artifact is present and accessible under venue rules.
7. Generate a requirement-by-requirement table with source URL, observed status, and uncertainty; flag rules that require a human or portal check.

## Required output

Submission preflight table with exact official requirement, source link, status, evidence, file/location, and owner; plus unresolved risks and final human checks.

## Integrity and safety gates

- Never assume venue rules are unchanged from a previous year.
- Do not claim compliance based on an inaccessible or unofficial mirror.
- Do not reveal author identities when double-blind rules prohibit it.
- Do not guarantee acceptance or portal validation.

## Related skills

`abstract-and-title`, `bibtex-hygiene`, `citation-verification`, `research-ethics-and-data-governance`

## Example request

> Check this ICLR/NeurIPS-style submission against the current official author instructions and list every unresolved item.
