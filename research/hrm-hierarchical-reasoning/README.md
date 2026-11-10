# HRM research track — hierarchical and recurrent computation

**Status:** Planned  
**Last reviewed:** 11 November 2026  
**Results:** None published

## Motivation

Hierarchical and recurrent architectures are proposed as ways to allocate computation across levels or repeated refinement steps. A credible evaluation must isolate the architecture's contribution from extra compute, outer-loop refinement, task augmentation, training data and evaluation-time search.

## Candidate research questions

1. Does recurrence or hierarchical coupling improve performance over a parameter- and compute-matched transformer?
2. What gains remain after controlling for outer-loop refinement and task augmentation?
3. How do adaptive depth, recurrence count and halting criteria affect accuracy, latency and memory?
4. Do improvements transfer to new task families or mainly fit the training/evaluation task distribution?
5. Which intermediate states are stable and useful for diagnosing failures?

## Candidate study design

- Begin with a small, tractable architecture and a transparent training/inference budget.
- Compare against parameter-matched and compute-matched baselines.
- Ablate recurrence, high/low-level coupling, outer-loop refinement and data augmentation independently.
- Report training and inference compute separately.
- Use multiple seeds and held-out task families; analyse transfer and memorisation.
- Do not infer biological plausibility from a high-level architectural analogy.

## Starting literature

- [Hierarchical Reasoning Model paper (2025)](https://arxiv.org/abs/2506.21734)
- [ARC Prize independent HRM evaluation and ablations (2025)](https://arcprize.org/blog/hrm-analysis)
- [Survey of frontiers in LLM reasoning (TMLR 2025)](https://mlanthology.org/tmlr/2025/ke2025tmlr-survey/)

## Next gate

Choose an architecture and benchmark scope that fit the available compute. Freeze matched baselines and ablation plan before training. The initial project should test the smallest claim that can distinguish recurrence/hierarchy from simply spending more computation.
