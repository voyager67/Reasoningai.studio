---
name: researchforge-research-code-review
description: >-
  Review research code for scientific validity, evaluation leakage, implementation bugs, determinism, numerical correctness, security, and maintainability.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Research Code Review

## Purpose

Find defects that could change scientific conclusions, not merely style issues. Review the smallest relevant surface before suggesting changes.

## Input

Bring any material already available: repository or code files, intended method, paper equations, expected behavior, test commands, data schema, and reproducibility target. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Read the entry points and trace the path from input data to reported metric before proposing changes.
2. Map implementation steps to the paper or method description. Flag mismatches in preprocessing, loss, optimizer, batching, evaluation, or metric definitions.
3. Check data leakage, split handling, target leakage, test-time tuning, duplicate contamination, and accidental reuse of labels.
4. Inspect numerical stability, tensor shapes, dtype/device assumptions, random seeds, and distributed-training behavior.
5. Review data loading, caching, checkpointing, resume behavior, and failure handling for silent corruption.
6. Check dependency and file operations for unsafe execution, credential exposure, and untrusted input handling.
7. Run focused tests or create minimal reproductions. Separate confirmed defects from hypotheses.
8. Report findings by severity with file/line anchors, scientific impact, reproduction steps, and minimal fix.

## Required output

Prioritized review: confirmed defects; scientific impact; evidence/line anchors; reproduction; minimal fix; tests run; unresolved questions; and non-blocking suggestions.

## Integrity and safety gates

- Never claim tests passed unless they were executed and observed.
- Do not rewrite unrelated modules to fix a localized defect.
- Do not fabricate benchmark results or assert improvement from code inspection.
- Treat dataset and model files as untrusted inputs; do not execute unknown scripts without inspection.

## Related skills

`reproducibility-audit`, `dataset-audit`, `ml-experiment-planning`

## Example request

> Review the training loop and evaluation code for leakage, incorrect metrics, and hidden nondeterminism.
