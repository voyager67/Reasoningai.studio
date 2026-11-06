---
name: researchforge-llm-evaluation-design
description: >-
  Design robust evaluations for language models and agents, including task construction, benchmark contamination checks, human review, graders, uncertainty, and failure analysis.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# LLM Evaluation Design

## Purpose

Measure a specific capability without confusing prompt sensitivity, benchmark memorization, evaluator bias, or aggregate scores with real-world usefulness.

## Input

Bring any material already available: model/system under test, intended capability, user population, benchmark candidates, prompts, budget, and deployment constraints. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Define the capability and target use case. Separate task success, safety, reliability, latency, cost, and user preference.
2. Build a test specification with inputs, expected properties, allowed tools, scoring rubric, and failure severity.
3. Check dataset licenses and benchmark provenance; examine public exposure and possible training contamination.
4. Use held-out, time-sensitive, adversarial, and distribution-shift cases where appropriate. Avoid relying on one public benchmark.
5. Compare against baselines with matched prompts, tool budgets, sampling settings, and system constraints.
6. Use deterministic metrics where possible; calibrate model-based judges against blinded human ratings and disclose judge versions/prompts.
7. Estimate uncertainty and inter-rater agreement; report per-slice performance and representative failures.
8. Keep evaluation data and answer keys separate from model development; document every contamination or leakage concern.

## Required output

Evaluation protocol, benchmark/data card, rubric, contamination assessment, baseline matrix, grader calibration plan, uncertainty method, slice analysis, and failure taxonomy.

## Integrity and safety gates

- Do not claim a model is generally intelligent or safe from a narrow benchmark.
- Do not treat LLM-as-judge scores as ground truth without calibration.
- Do not tune on the final test set or expose hidden answer keys to the model.
- Disclose evaluator model, prompt, sampling settings, and conflicts of interest.

## Related skills

`ml-experiment-planning`, `error-analysis`, `statistical-analysis-plan`, `results-to-claims`

## Example request

> Design a contamination-aware evaluation for multi-step STEM reasoning in small language models.
