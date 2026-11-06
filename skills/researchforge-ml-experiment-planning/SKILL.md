---
name: researchforge-ml-experiment-planning
description: >-
  Plan compute-aware machine-learning experiments with credible baselines, fair comparisons, ablations, seeds, data splits, and decision rules.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# ML Experiment Planning

## Purpose

Make research results interpretable and reproducible while respecting hardware, time, and energy constraints.

## Input

Bring any material already available: research question, model candidates, dataset/splits, compute budget, library versions, baseline results, and target metrics. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Translate the question into a primary task, dataset, metric, and hypothesis. Freeze data splits before tuning.
2. Choose strong, relevant baselines and reproduce their protocol as closely as possible. Record deviations and inaccessible settings.
3. Define an experiment matrix: one primary comparison, mechanism ablations, robustness slices, and efficiency measures tied to the claim.
4. Estimate memory, training time, inference cost, storage, and number of runs before launching. Reduce scope transparently if budget is insufficient.
5. Control randomness and log seeds, configuration, data hashes, checkpoint identifiers, software and hardware details.
6. Separate training, validation, and final test use. Keep test labels out of model selection and prompt/model tuning.
7. Report mean and variation across appropriate independent runs; distinguish seed variability from data-sample variability.
8. Set stop/continue criteria based on scientific value and compute cost, not only leaderboard position.

## Required output

Experiment matrix; baseline protocol; compute estimate; configuration schema; run log; ablation plan; evaluation protocol; and a result table specification.

## Integrity and safety gates

- Do not claim SOTA without a comparable, current, fair evaluation.
- Do not compare models using mismatched data splits or hidden preprocessing differences.
- Do not describe one lucky seed as a robust improvement.
- Report failed runs and deviations when they affect conclusions.

## Related skills

`dataset-audit`, `experimental-design`, `statistical-analysis-plan`, `llm-evaluation-design`, `reproducibility-audit`

## Example request

> Plan a 7B model fine-tuning study that fits a single consumer GPU and includes fair baselines and ablations.
