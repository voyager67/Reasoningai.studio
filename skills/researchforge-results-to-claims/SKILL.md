---
name: researchforge-results-to-claims
description: >-
  Map every manuscript claim to the evidence that supports it, evaluate scope and uncertainty, and rewrite overbroad conclusions into defensible statements.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Results to Claims

## Purpose

Prevent claims from exceeding the actual design, sample, dataset, metric, or analysis. This skill is the final integrity gate before writing or submission.

## Input

Bring any material already available: draft manuscript, tables/figures, analysis outputs, protocols, and the exact claims or abstract under review. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Extract material claims from abstract, introduction, results, discussion, and conclusion.
2. For each claim, identify evidence source, analysis, sample, comparator, uncertainty, and whether it is direct or inferred.
3. Classify the claim as descriptive, comparative, predictive, causal, mechanistic, or generalization claim.
4. Check whether design and sampling justify the claim type and target population.
5. Inspect effect size, uncertainty, multiple testing, subgroup analysis, missing data, and plausible alternative explanations.
6. Narrow claims that exceed evidence; add missing qualifiers or identify the experiment needed to support them.
7. Check that tables, figures, abstract, and conclusion use consistent numbers and scope.
8. Produce a claim-evidence ledger and a prioritized repair list.

## Required output

Claim-evidence ledger with exact claim, source, support level, scope, uncertainty, alternative explanations, recommended revision, and missing evidence.

## Integrity and safety gates

- Do not convert absence of statistical significance into proof of no effect.
- Do not turn benchmark performance into universal capability claims.
- Do not remove relevant limitations to make a claim sound stronger.
- Keep negative, null, and contradictory evidence visible when it changes interpretation.

## Related skills

`statistical-analysis-plan`, `scientific-writing`, `anti-defensive-writing`, `peer-review`

## Example request

> Audit every major claim in this draft against the reported results and flag statements that overreach.
