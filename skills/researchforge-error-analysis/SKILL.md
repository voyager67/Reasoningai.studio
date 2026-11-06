---
name: researchforge-error-analysis
description: >-
  Turn model failures and unexpected results into a structured error taxonomy, representative cases, root-cause hypotheses, and targeted follow-up experiments.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Error Analysis

## Purpose

Move beyond a single average score to understand where, why, and for whom a system fails.

## Input

Bring any material already available: prediction logs, gold labels, examples, model/version metadata, task slices, and annotation guidance. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Validate the evaluation set and error labels before interpreting model failures.
2. Define an error taxonomy with mutually interpretable categories and a written assignment guide.
3. Sample failures and successes across classes, sources, demographics or contexts where ethically appropriate, difficulty, and confidence.
4. Annotate root-cause candidates separately from observed error type; use multiple annotators for subjective categories.
5. Quantify error frequency and uncertainty by slice; avoid cherry-picking vivid examples.
6. Identify plausible interventions and design targeted tests to distinguish them.
7. Prioritize errors by severity, frequency, user impact, and fixability; maintain a regression set.

## Required output

Error taxonomy; annotation guide; slice metrics; representative anonymized cases; root-cause hypotheses; prioritization; and regression tests.

## Integrity and safety gates

- Do not infer a causal root cause from a single example.
- Do not reveal sensitive records or demographic attributes unnecessarily.
- Do not hide common failure modes behind overall averages.
- Report annotator disagreement and ambiguous examples.

## Related skills

`llm-evaluation-design`, `dataset-audit`, `ml-experiment-planning`, `scientific-visualization`

## Example request

> Analyze model failures by class, image quality, source domain, and compression level, then propose discriminating tests.
