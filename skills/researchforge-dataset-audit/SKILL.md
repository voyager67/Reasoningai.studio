---
name: researchforge-dataset-audit
description: >-
  Audit a research dataset for provenance, license, schema, missingness, duplicates, leakage, split integrity, class imbalance, and sensitive-data risk.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Dataset Audit

## Purpose

Identify dataset risks before training or publishing results. The audit should be useful without exposing raw records in its report.

## Input

Bring any material already available: dataset files, data card or source URL, license/terms, intended task, schema, label definitions, and split metadata. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Record dataset origin, collection date, version, license, consent/permissions, intended use, and known restrictions.
2. Validate schema, types, required fields, missingness, invalid labels, and unexpected category values.
3. Check duplicate rows and duplicate content using hashes or normalized text; report counts and split locations, not sensitive raw content.
4. Test train/validation/test boundaries for exact duplicates, near-duplicates where feasible, subject overlap, temporal leakage, and source overlap.
5. Inspect class balance, group sizes, outliers, label quality, annotation agreement, and sampling bias.
6. Review for personal, sensitive, copyrighted, or otherwise restricted data; minimize collection and avoid publishing raw data without rights.
7. Document transformations, exclusions, version hashes, and limitations. Recommend a remediation plan before model training.

## Required output

Dataset audit report with provenance and license status, schema summary, quality counts, split-overlap findings, class distribution, privacy review, known limitations, and release recommendation.

## Integrity and safety gates

- Do not infer a license from a download page or assume public availability means unrestricted reuse.
- Do not expose sample text, identifiers, or personal data in logs by default.
- Do not claim absence of leakage from a simple exact-duplicate check alone.
- Do not redistribute data when rights are unclear.

## Related skills

`ml-experiment-planning`, `reproducibility-audit`, `research-ethics-and-data-governance`

## Example request

> Audit this CSV/JSONL dataset for missing labels, duplicates across splits, leakage, and license questions.
