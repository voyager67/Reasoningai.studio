---
name: researchforge-deep-paper-reading
description: >-
  Read a research paper critically and extract its question, contribution, method, evidence, assumptions, limitations, and reproducibility details with page-level traceability.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Deep Paper Reading

## Purpose

Convert a paper from a citation into a trustworthy, structured understanding. Separate what the authors claim from what their experiments establish.

## Input

Bring any material already available: PDF or full text, bibliographic record, research question, and any specific claim you need to verify. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Confirm the paper identity, version, venue, date, and whether it is a preprint, accepted manuscript, or published version.
2. Read abstract, figures/tables, methods, results, limitations, and related work in a deliberate pass; then revisit sections needed to resolve ambiguity.
3. Extract the research question, contribution, assumptions, task definition, dataset, sample, baseline, metrics, experimental setup, and compute.
4. For every headline result, capture the exact metric, comparator, split, uncertainty interval or variance, and location in the paper.
5. Separate author interpretation from direct observations. Note alternative explanations and threats to validity.
6. Record what is missing: hyperparameters, seeds, data filtering, code, annotation protocol, confidence intervals, or statistical tests.
7. Write a concise synthesis in your own words with page/section anchors; quote only when exact wording matters.

## Required output

A paper card: identity; one-sentence contribution; question; method; data; baselines; metrics; results; assumptions; limitations; reproducibility; relevance; confidence; and page/section anchors for each extracted fact.

## Integrity and safety gates

- Never invent page numbers or quote text not present in the supplied paper.
- Do not equate a reported benchmark gain with general capability improvement.
- Distinguish author-reported values from values independently reproduced.
- Treat OCR or extraction errors as uncertainty and inspect the rendered page when necessary.

## Related skills

`paper-triage`, `evidence-matrix-synthesis`, `citation-verification`, `results-to-claims`

## Example request

> Read these three papers and compare their datasets, baselines, reported accuracy, and evaluation limitations.
