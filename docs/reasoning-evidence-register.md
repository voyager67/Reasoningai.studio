# Reasoning research evidence register

**Evidence snapshot:** 11 November 2026  
**Purpose:** record selected findings that inform ReasoningAI's research agenda.  
**Interpretation rule:** every metric below is attributed to the cited paper or independent evaluator. None is a result produced or independently reproduced by ReasoningAI unless a record explicitly says so.

This is a curated evidence register, not a systematic review or leaderboard. It is deliberately mixed: positive results, robustness failures, faithfulness concerns and independent verification are all included.

## Evidence classes

| Class | Meaning |
|---|---|
| Primary-paper result | Reported by the authors on their stated model, dataset, metric and protocol |
| Independent evaluation | A separate evaluator ran or audited a method on a stated split or environment |
| Limitation / counter-evidence | Evidence that narrows the interpretation or identifies a failure mode |
| Research synthesis | Survey or synthesis that organises prior evidence; not a new benchmark result |

## Selected findings

### E-001 — Self-consistency on reasoning benchmarks
- **Class:** Primary-paper result
- **Method:** sample diverse chain-of-thought paths and aggregate the final answers.
- **Reported result:** +17.9% on GSM8K, +11.0% on SVAMP, +12.2% on AQuA, +6.4% on StrategyQA and +3.9% on ARC-Challenge versus the paper's CoT baseline.
- **Source:** Wang et al., *Self-Consistency Improves Chain of Thought Reasoning in Language Models* (ICLR 2023). [Google Research publication](https://research.google/pubs/self-consistency-improves-chain-of-thought-reasoning-in-language-models/).
- **Interpretation boundary:** paper-specific models, sampling configuration and baselines. Sampling increases inference cost; correlated samples can share errors.
- **ReasoningAI replication:** not conducted.

### E-002 — Tree of Thoughts on Game of 24
- **Class:** Primary-paper result
- **Method:** branch over intermediate states, evaluate candidates and backtrack.
- **Reported result:** GPT-4 with CoT solved 4% of Game of 24 tasks in the original comparison; ToT with beam width 5 reached 74%. The paper's table also reports 7.3% for direct input and 9.0% for CoT self-consistency at k=100.
- **Source:** Yao et al., *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* (NeurIPS 2023). [Conference paper and abstract](https://papers.nips.cc/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html); [paper PDF](https://papers.nips.cc/paper/2023/file/271db9922b8d1f4dd7aaef84ed5ac703-Paper-Conference.pdf).
- **Interpretation boundary:** one highly structured planning puzzle and one model/protocol. The paper itself shows large gaps between search widths and baselines. Do not generalise 4%→74% to all reasoning tasks.
- **ReasoningAI replication:** not conducted.

### E-003 — Least-to-most prompting on SCAN
- **Class:** Primary-paper result
- **Method:** decompose a task into ordered, simpler subproblems and solve sequentially.
- **Reported result:** with code-davinci-002 and 14 exemplars, the paper reports at least 99% accuracy on SCAN splits including the length split, compared with 16% for CoT.
- **Source:** Zhou et al., *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models* (ICLR 2023). [arXiv](https://arxiv.org/abs/2205.10625).
- **Interpretation boundary:** historical model, controlled compositional benchmark and specific prompting setup. Not evidence of equivalent gains on modern open-ended tasks.
- **ReasoningAI replication:** not conducted.

### E-004 — Program-Aided Language Models
- **Class:** Primary-paper result
- **Method:** have the model translate a problem into executable code and delegate computation to a Python interpreter.
- **Reported result:** the paper reports PAL with Codex exceeding PaLM-540B with CoT by 15 absolute accuracy points on GSM8K.
- **Source:** Gao et al., *PAL: Program-aided Language Models* (2023). [arXiv](https://arxiv.org/abs/2211.10435).
- **Interpretation boundary:** model, benchmark, interpreter and prompt setup are specific to the study. Generated code must be validated and executed safely.
- **ReasoningAI replication:** not conducted.

### E-005 — Process supervision on MATH
- **Class:** Primary-paper result
- **Method:** supervise intermediate solution steps rather than only the final answer.
- **Reported result:** the process-supervised model solved 78% of a representative subset of the MATH test set. The work released PRM800K, approximately 800,000 step-level human feedback labels.
- **Source:** Lightman et al., *Let's Verify Step by Step* (ICLR 2024). [arXiv](https://arxiv.org/abs/2305.20050); [PRM800K dataset](https://github.com/openai/prm800k).
- **Interpretation boundary:** this result depends on the paper's model, best-of-N selection and MATH subset. Process labels have costs and annotation policy matters.
- **ReasoningAI replication:** not conducted.

### E-006 — Graph of Thoughts on sorting
- **Class:** Primary-paper result
- **Method:** represent intermediate outputs as a graph, with operations for combining, transforming and refining nodes.
- **Reported result:** for the paper's sorting setup at P=128, GoT reduced median error by approximately 62% compared with ToT and reduced costs by more than 31%.
- **Source:** Besta et al., *Graph of Thoughts: Solving Elaborate Problems with Large Language Models* (AAAI 2024). [AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/view/29720).
- **Interpretation boundary:** result is for the paper's sorting configuration, metric and cost accounting; it is not a general 62% accuracy gain across tasks.
- **ReasoningAI replication:** not conducted.

### E-007 — DeepSeek-R1-Zero and verifiable-reward RL
- **Class:** Primary-paper result
- **Method:** reinforcement learning with rule-based accuracy and format rewards for reasoning-oriented tasks.
- **Reported result:** the Nature article reports AIME 2024 pass@1 rising from 15.6% to 77.9% during DeepSeek-R1-Zero RL training; self-consistency decoding raised the reported score to 86.7%.
- **Source:** DeepSeek-AI, *DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning*, Nature 645, 633–638 (17 September 2025). [Nature](https://www.nature.com/articles/s41586-025-09422-z).
- **Protocol detail:** the article describes 16 sampled outputs per question for the cited self-consistency setup, with a maximum output length of 32,768 tokens.
- **Interpretation boundary:** benchmark, training run, model and sampling configuration are specific. RLVR requires a reliable reward function and can be vulnerable to reward hacking or distribution shift.
- **ReasoningAI replication:** not conducted.

### E-008 — HRM independent ARC evaluation and ablations
- **Class:** Independent evaluation / limitation
- **Method:** Hierarchical Reasoning Model with recurrent high- and low-level modules.
- **Original claim context:** the HRM paper reported 41% on ARC-AGI-1 with a 27M-parameter model and a small number of training tasks.
- **Independent result:** ARC Prize reports 32% on the ARC-AGI-1 semi-private set and 2% on ARC-AGI-2.
- **Ablation finding:** ARC Prize reports that the hierarchical architecture had minimal impact compared with a similarly sized transformer; the outer-loop refinement process drove substantial performance, and transfer benefits were limited.
- **Sources:** Wang et al., [HRM paper](https://arxiv.org/abs/2506.21734); ARC Prize, [The Hidden Drivers of HRM's Performance on ARC-AGI](https://arcprize.org/blog/hrm-analysis) (15 August 2025).
- **Interpretation boundary:** independent evaluator's datasets and reproduction protocol should be read directly. This result illustrates why architectural claims need component ablations.
- **ReasoningAI replication:** not conducted.

### E-009 — CoT faithfulness is not guaranteed
- **Class:** Limitation / counter-evidence
- **Finding:** controlled studies show that a verbalised chain of thought can omit influential information or fail to faithfully represent factors that changed the model's answer.
- **Sources:** Turpin et al., [Language Models Don't Always Say What They Think](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html); Lanham et al., [Measuring Faithfulness in Chain-of-Thought Reasoning](https://arxiv.org/abs/2307.13702).
- **Interpretation boundary:** distinguish behavioural transparency, internal faithfulness and answer correctness. A readable trace is not causal access to a model's internal computation.
- **ReasoningAI replication:** not conducted.

### E-010 — FaithCoT-Bench (ICLR 2026)
- **Class:** Primary benchmark contribution
- **Finding:** introduces FINE-CoT, an expert-annotated collection of 1,000+ trajectories from four representative LLMs across four domains, including 300+ unfaithful instances with fine-grained causes and step-level evidence; evaluates eleven detection methods.
- **Source:** Shen et al., [FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6c7154e394e24c69409256ccf8bf0804-Abstract-Conference.html).
- **Interpretation boundary:** benchmark-level results do not automatically transfer to all models, domains or deployment contexts.
- **ReasoningAI replication:** not conducted.

### E-011 — Self-correction without external feedback
- **Class:** Limitation / counter-evidence
- **Finding:** intrinsic self-correction can fail to improve reasoning and may degrade performance when the model has no external feedback signal.
- **Source:** Huang et al., [Large Language Models Cannot Self-Correct Reasoning Yet](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html).
- **Interpretation boundary:** distinguish intrinsic revision from correction guided by tests, retrieval, tools, formal checkers or human feedback.
- **ReasoningAI replication:** not conducted.

### E-012 — GSM-Symbolic robustness
- **Class:** Limitation / counter-evidence
- **Finding:** changing numerical values and adding clauses can cause substantial performance degradation; the paper reports drops of up to 65% under its added-clause perturbation setting.
- **Source:** Mirzadeh et al., [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ec2e7a896f8250986b3907f57621ce94-Abstract-Conference.html); [Apple ML Research summary and dataset links](https://machinelearning.apple.com/research/gsm-symbolic).
- **Interpretation boundary:** the 65% figure is the maximum reported drop under a specific perturbation, not a universal average decline.
- **ReasoningAI replication:** not conducted.

### E-013 — 2026 CoT faithfulness survey
- **Class:** Research synthesis
- **Finding:** organises CoT faithfulness around internal alignment and external consistency, and reviews post-hoc rationalisation, sycophancy, metrics, benchmarks and mitigation strategies.
- **Source:** Jin et al., [The Mirage of Explainability: A Survey on Chain-of-Thought Faithfulness in Large Language Models](https://aclanthology.org/2026.emnlp-main.614/) (EMNLP 2026).
- **Interpretation boundary:** a survey synthesises a body of research; it is not a new controlled experiment.

### E-014 — Information-theoretic limits and empirical faithfulness (EMNLP 2026)
- **Class:** Primary theoretical and empirical study
- **Finding:** derives a capacity bound for when faithful traces would be impossible, but reports that none of the evaluated benchmark settings were provably in the above-capacity regime. The authors attribute observed unfaithfulness to training rather than a binding token-interface limit in the tested settings.
- **Source:** Wu, Guo and Yiu, [When Must Faithful Chain-of-Thought Fail? An Information-Theoretic Bound and Its Empirical Limits](https://aclanthology.org/2026.emnlp-main.1823/) (EMNLP 2026).
- **Interpretation boundary:** do not simplify the paper to “CoT can never be faithful”; its abstract explicitly finds the proposed capacity bound does not bind on the evaluated benchmarks.

## Synthesis: implications for ReasoningAI

1. **Decomposition is a useful control surface, not a correctness guarantee.** CoT, least-to-most, plans and intermediate representations should be evaluated against direct baselines.
2. **Search can help on tasks with meaningful branches and backtracking.** ToT/GoT experiments must disclose state representation, evaluator, branching, depth, pruning and total compute.
3. **Execution can provide stronger checks than prose.** Use code, tests, solvers or verified data when tasks admit objective checks; validate the generated program and the specification.
4. **More compute must be priced.** Report quality alongside tokens, model calls, latency and compute costs.
5. **Process traces need a faithfulness claim of their own.** A valid final answer does not prove the trace is faithful; a trace that sounds coherent does not prove the answer.
6. **Architecture claims require ablation.** Compare recurrent or hierarchical models with capacity- and compute-matched controls, and isolate outer-loop refinement, data augmentation and training effects.
7. **Negative results belong in the record.** Failed hypotheses, unstable runs, robustness regressions and null ablations are publishable evidence when methods are transparent.

## Updating this register

Use [research-finding-record.md](../templates/research-finding-record.md) for each new claim. Add the exact paper/version, model snapshot, dataset split, baseline, metric, uncertainty, compute budget and evidence class. Mark a result as independently reproduced only after another execution of the documented protocol; do not convert a paper-reported result into a ReasoningAI result by paraphrasing it.
