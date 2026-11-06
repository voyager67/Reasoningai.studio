---
name: researchforge-research-decision-gate
description: >-
  Evaluate whether a research idea or experiment should proceed, be narrowed, be redesigned, or be stopped using scientific value, evidence, feasibility, and resource constraints.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Research Decision Gate

## Purpose

Help researchers avoid spending months on an idea with no credible measurement path, while preserving promising work that needs a smaller test.

## Input

Bring any material already available: research brief, current evidence, proposed method, expected contribution, compute/time/data budget, risks, and alternatives. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Restate the claim the proposed work would establish and identify who would care if it were true.
2. Check whether the literature gap and intended contribution are supported by a documented search.
3. Test the measurement path: can the outcome be observed, compared, and independently checked?
4. Estimate data, compute, time, skill, ethics, and infrastructure requirements with explicit assumptions.
5. Identify the smallest discriminating experiment that could change the decision.
6. Define go, revise, pause, and stop conditions before running that experiment.
7. Compare the idea with the best alternative use of the same resources and record the reasoning.

## Required output

Decision memo with decision (go/revise/pause/stop), evidence, assumptions, minimum test, resource estimate, risks, decision thresholds, and review date.

## Integrity and safety gates

- Do not use confidence or enthusiasm as substitutes for evidence.
- Do not claim a proposal is novel from a narrow search.
- Do not keep a failing experiment alive by changing success criteria after observing outcomes.
- A stop decision is a useful result when the evidence supports it.

## Related skills

`research-gap-analysis`, `research-question-framing`, `experimental-design`, `ml-experiment-planning`

## Example request

> Assess whether this 4-week student research project is feasible on one 16 GB GPU and define a minimal decisive experiment.
