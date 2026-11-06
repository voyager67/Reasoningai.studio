---
name: researchforge-paper-triage
description: >-
  Screen paper titles and abstracts against predeclared criteria, deduplicate candidate records, and keep an auditable inclusion/exclusion log. Use when a literature search returns more papers than can be read in full.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Paper Triage

## Purpose

Reduce a candidate corpus in a consistent and explainable way while minimizing silent selection bias.

## Input

Bring any material already available: bibliographic exports, research question, inclusion/exclusion criteria, date and language limits, and screening resources. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Freeze the screening question and criteria before looking at outcomes where possible.
2. Normalize records and deduplicate using DOI, then title/author/year with manual review of near-duplicates.
3. Screen title and abstract independently against each criterion. Use “unclear” when the abstract does not contain enough information.
4. For unclear records, inspect the full text or mark the reason full text was unavailable; do not infer exclusion from the abstract alone.
5. Record one primary exclusion reason for every excluded full-text report and preserve secondary notes separately.
6. For high-stakes reviews, use two independent screeners on a sample or all records and resolve disagreements with a documented rule.
7. Summarize counts at each stage without converting them into a PRISMA diagram unless the review actually followed that process.

## Required output

A screened record table with stable ID, DOI, title, decision, criterion-level notes, primary exclusion reason, reviewer, and timestamp; plus stage counts and unresolved records.

## Integrity and safety gates

- Do not exclude a result because it contradicts the expected hypothesis.
- Do not treat inaccessible full text as proof of irrelevance.
- Do not count conference and journal versions as separate independent studies without a reason.
- Keep screening criteria and records private when they contain confidential review material.

## Related skills

`literature-search-strategy`, `deep-paper-reading`, `systematic-review`

## Example request

> Screen 180 exported records on multimodal deepfake detection and provide inclusion decisions with explicit reasons.
