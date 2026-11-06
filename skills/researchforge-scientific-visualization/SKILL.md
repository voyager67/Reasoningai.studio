---
name: researchforge-scientific-visualization
description: >-
  Choose and produce scientific figures that communicate the measured result accurately, with appropriate scales, uncertainty, labels, annotations, and reproducible source data.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Scientific Visualization

## Purpose

Optimize interpretability without visually exaggerating effects or hiding inconvenient measurements.

## Input

Bring any material already available: data table, analysis outputs, target audience, intended claim, required venue style, and plotting environment. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. State the question the figure must answer and the comparison it should enable.
2. Choose chart form based on data type and estimand: distribution, paired comparison, time series, calibration, ablation, or qualitative examples.
3. Select scales and axes honestly; include zero baselines when relevant and explain any truncation or transformation.
4. Show uncertainty, sample sizes, and individual observations when they materially affect interpretation.
5. Use readable labels, color-safe palettes, consistent units, and accessible contrast; do not encode information by color alone.
6. Keep figure data and generation code traceable to the analysis output; preserve raw data separately.
7. Check figure captions, statistical annotations, and references against the actual dataset and method.
8. Review at expected print or screen size and create a concise alternative text description.

## Required output

Publication-ready figure(s), source code, source-data table, caption, alt text, units, and notes on transformations/uncertainty.

## Integrity and safety gates

- Do not crop or rescale to exaggerate differences.
- Do not omit outliers or failed runs without a justified, disclosed rule.
- Do not use 3D effects or decorative encoding that obscures quantities.
- Do not label correlation plots as causal effects.

## Related skills

`error-analysis`, `results-to-claims`, `scientific-writing`

## Example request

> Turn these repeated-run metrics into a clear paired comparison figure with uncertainty and a truthful caption.
