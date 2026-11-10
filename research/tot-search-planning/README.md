# ToT research track — search and planning

**Status:** Planned  
**Last reviewed:** 11 November 2026  
**Results:** None published

## Motivation

Tree of Thoughts generalises a single linear reasoning trace into search over intermediate states. The central research question is not whether more branches can help, but when search improves solution quality enough to justify its evaluator error and compute cost.

## Candidate research questions

1. Which task structures benefit from explicit branching and backtracking?
2. How do branching factor, search depth, pruning, and evaluator choice affect quality?
3. Does ToT improve over CoT and self-consistency under matched model calls or token budgets?
4. When do graph-based combinations or heuristic search outperform tree search?
5. How robust are gains to evaluator perturbations, misleading intermediate states and task distribution shifts?

## Candidate study design

- Freeze the task suite and scoring rules before tuning search.
- Compare direct answer, CoT, self-consistency, and ToT under explicit compute budgets.
- Log every expanded state, score, prune/expand decision, tool call and final path.
- Include oracle-evaluator upper bounds only as diagnostic ceilings, never as deployable baseline.
- Report solved rate, cost per solved task, latency and evaluator calibration.
- Include ablations for branching, depth, backtracking and verifier components.

## Starting literature

- [Tree of Thoughts (NeurIPS 2023)](https://papers.nips.cc/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html)
- [Graph of Thoughts (AAAI 2024)](https://ojs.aaai.org/index.php/AAAI/article/view/29720)
- [Self-consistency (ICLR 2023)](https://research.google/pubs/self-consistency-improves-chain-of-thought-reasoning-in-language-models/)

## Next gate

Specify a reproducible state representation, candidate generator and independent state evaluator. Freeze the baseline prompts, total model-call/token budget and scoring harness before running comparisons.
