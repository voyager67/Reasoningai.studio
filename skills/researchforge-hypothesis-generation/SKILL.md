---
name: researchforge-hypothesis-generation
description: >-
  Generate testable hypotheses from a literature map and mechanism model, including operational predictions, rival explanations, and falsification criteria.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Hypothesis Generation

## Purpose

Move from an interesting idea to predictions that can be disproved by data. Keep exploratory hypotheses distinct from preregistered confirmatory hypotheses.

## Input

Bring any material already available: research question, evidence matrix, theory or mechanism, available data, measures, and constraints. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. State the phenomenon and proposed mechanism without assuming the mechanism is true.
2. Generate a small set of alternative explanations, including a null or baseline explanation.
3. Express each hypothesis as a directional or non-directional prediction with population, conditions, comparator, outcome, and time horizon where relevant.
4. Operationalize constructs and choose measurements that do not simply encode the desired result.
5. Specify what observation would support, weaken, or falsify each hypothesis.
6. Identify confounders, mediators, moderators, and plausible failure cases.
7. Label whether each hypothesis is confirmatory, exploratory, or post hoc and align the analysis plan accordingly.

## Required output

Hypothesis table with rationale and citations; measurable variables; predicted outcomes; rival explanations; falsification criteria; and confirmatory/exploratory status.

## Integrity and safety gates

- Do not present a post hoc explanation as a preregistered prediction.
- Do not turn correlation into mechanism without a causal design.
- Do not generate only hypotheses that predict the preferred method will win.
- Include null and adverse predictions where plausible.

## Related skills

`research-question-framing`, `research-gap-analysis`, `experimental-design`, `statistical-analysis-plan`

## Example request

> Generate three competing hypotheses for why a lightweight detector may generalize better under image compression.
