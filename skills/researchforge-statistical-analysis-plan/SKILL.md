---
name: researchforge-statistical-analysis-plan
description: >-
  Choose and document statistical analyses, estimands, assumptions, uncertainty estimates, multiplicity handling, and missing-data procedures before outcome inspection.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Statistical Analysis Plan

## Purpose

Make statistical conclusions interpretable and proportional to the design, rather than selecting tests after seeing which gives significance.

## Input

Bring any material already available: hypotheses, design, outcome definitions, sampling plan, data structure, and analysis environment. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Define the estimand: target population, treatment/comparison, outcome, handling of intercurrent events, and summary measure.
2. Identify outcome types, repeated measures, clustering, paired structure, censoring, and distributional features.
3. Choose candidate models/tests based on the design and assumptions; state diagnostics and fallback approaches.
4. Specify effect sizes and uncertainty intervals as primary reporting elements, not p-values alone.
5. Plan missing-data handling and sensitivity analyses. State when missingness mechanisms are unknown.
6. Define multiplicity control or hierarchical testing for multiple outcomes, comparisons, and subgroups.
7. For ML experiments, account for paired comparisons, seed variation, dataset-level variation, and uncertainty across examples.
8. Write the analysis plan in advance and record deviations, exploratory analyses, and robustness checks separately.

## Required output

A statistical analysis plan naming estimands, model/test, assumptions, diagnostics, effect sizes, confidence intervals, multiplicity strategy, missing-data plan, sensitivity analyses, and software/version.

## Integrity and safety gates

- Do not equate statistical significance with practical significance.
- Do not select tests solely because they yield smaller p-values.
- Do not use a confidence interval or significance test outside its assumptions without qualification.
- Do not fabricate sample size, degrees of freedom, or standard errors.

## Related skills

`experimental-design`, `ml-experiment-planning`, `llm-evaluation-design`, `results-to-claims`

## Example request

> Write a preregistered statistical analysis plan for paired model comparisons across repeated runs.
