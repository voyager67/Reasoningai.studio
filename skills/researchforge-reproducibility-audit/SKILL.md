---
name: researchforge-reproducibility-audit
description: >-
  Audit whether a computational research result can be rerun from available code, data provenance, environment, configuration, seeds, and documented commands.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Reproducibility Audit

## Purpose

Assess reproducibility evidence, not merely whether a repository contains code. Distinguish repeatability, reproducibility, and independent replication.

## Input

Bring any material already available: project directory, paper or result claim, code repository, dataset references, environment files, logs, and reported metrics. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Map each reported claim to the code, configuration, data version, run, and output that produced it.
2. Inspect repository structure, entry points, scripts, dependency versions, environment lockfiles, hardware assumptions, and data acquisition steps.
3. Check random seeds and nondeterministic operations; document which components cannot be made deterministic.
4. Verify split generation, preprocessing, leakage controls, training/evaluation separation, and metric implementations.
5. Check run logs and checkpoints for configuration, timestamps, code commit, dataset hash, and model artifact identity.
6. Attempt a clean-environment reproduction using documented commands when resources permit. Record exact commands and failures.
7. Compare reproduced metrics with reported values using appropriate tolerance and uncertainty; do not call a partial rerun a full reproduction.
8. Produce a gap list with severity and recommended fixes.

## Required output

Reproducibility matrix: claim; artifact; available evidence; rerun status; variance/tolerance; missing dependency; and confidence. Include exact rerun command and limitations.

## Integrity and safety gates

- Do not claim reproducibility from the presence of a README or requirements file alone.
- Do not report “reproduced” if data, model weights, or essential preprocessing are unavailable.
- Never paste secrets or access tokens into logs or a public report.
- Distinguish exact rerun, approximate rerun, and independent replication.

## Related skills

`dataset-audit`, `ml-experiment-planning`, `research-code-review`, `results-to-claims`

## Example request

> Audit this ML repository and tell me which published results can actually be rerun from its files.
