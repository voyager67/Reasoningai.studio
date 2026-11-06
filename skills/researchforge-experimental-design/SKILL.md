---
name: researchforge-experimental-design
description: >-
  Design controlled, feasible experiments with valid comparators, randomization, measurement plans, sample-size reasoning, and threats-to-validity controls.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Experimental Design

## Purpose

Ensure that the experiment can distinguish the proposed explanation from plausible alternatives.

## Input

Bring any material already available: hypotheses, target population/system, data or apparatus, constraints, outcome measures, and baseline methods. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Map every hypothesis to one primary estimand or observable outcome.
2. Select an experimental, quasi-experimental, observational, or simulation design and justify why it identifies the intended effect.
3. Define treatment/intervention, comparator, inclusion criteria, sampling unit, assignment unit, and analysis unit.
4. Plan randomization, blinding, blocking, counterbalancing, or controls where appropriate.
5. Identify confounders, leakage channels, contamination, carryover, measurement error, and failure conditions.
6. Estimate sample size or power using explicit assumptions, effect size, variance, alpha, power, and attrition; label rough estimates as planning estimates.
7. Define stopping rules, exclusions, missing-data handling, and the analysis plan before inspecting confirmatory outcomes.
8. Pilot the protocol and document changes; keep pilot data separate if it influenced design decisions.

## Required output

Experiment protocol with design rationale, variables, sampling, controls, randomization, power assumptions, stopping/exclusion rules, analysis plan, resource estimate, and risk register.

## Integrity and safety gates

- Do not invent a power calculation when variance/effect-size assumptions are unknown.
- Do not treat repeated seeds on the same fixed dataset as independent datasets.
- Do not tune on the test set.
- Do not retroactively redefine primary outcomes without reporting the change.

## Related skills

`hypothesis-generation`, `statistical-analysis-plan`, `ml-experiment-planning`, `research-ethics-and-data-governance`

## Example request

> Design an ablation and generalization experiment that separates model quality from data leakage and preprocessing effects.
