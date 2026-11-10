# CoT research track — faithfulness and evaluation

**Status:** Planned  
**Last reviewed:** 11 November 2026  
**Results:** None published

## Motivation

Chain-of-thought prompting can improve performance on selected tasks, but a readable rationale is not necessarily a faithful account of the factors that caused the model's answer. Research in this area now includes instance-level faithfulness benchmarks and surveys.

## Candidate research questions

1. Under what conditions do verbalised rationales track answer-relevant model behaviour?
2. How sensitive are rationale and answer to controlled changes in prompt framing, evidence order, and irrelevant-but-plausible distractors?
3. Can independent checks—counterfactual tests, logit-based methods, process verifiers or external evidence—detect unfaithful trajectories?
4. How do faithfulness, answer accuracy, cost and robustness trade off?

## Candidate study design

- Define trace faithfulness operationally before choosing metrics.
- Separate answer correctness, step validity, external consistency and causal faithfulness.
- Use models and datasets with documented versions and rights.
- Include adversarial and counterfactual controls.
- Compare self-judging against independent evaluators; calibrate human annotation.
- Include a negative-control condition in which the rationale is perturbed without changing the answer, where the protocol permits it.

## Starting literature

- [Turpin et al. — Language Models Don't Always Say What They Think](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html)
- [Lanham et al. — Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702)
- [FaithCoT-Bench (ICLR 2026)](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6c7154e394e24c69409256ccf8bf0804-Abstract-Conference.html)
- [The Mirage of Explainability (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.614/)
- [When Must Faithful Chain-of-Thought Fail? (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.1823/)

## Next gate

Freeze a measurable research question, choose lawful datasets and models, write protocol.md from the [experiment template](../../templates/reasoning-experiment-protocol.md), and define what constitutes a faithful trace before any benchmark run.
