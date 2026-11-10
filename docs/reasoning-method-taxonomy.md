# Reasoning method taxonomy

**Purpose:** provide a working map of reasoning methods relevant to modern AI systems.  
**Scope reviewed:** 11 November 2026.  
**Status:** literature-oriented reference; not an exhaustive survey and not a claim that ReasoningAI implements every method below.

The public-facing companion is the [ReasoningAI Methods Atlas](https://reasoningai.tech/methods.html).

## 1. How to read this taxonomy

The word *reasoning* is used for several different things in AI papers. Do not treat every named technique as the same kind of object.

| Layer | What it describes | Examples |
|---|---|---|
| Reasoning form | The kind of inference or problem-solving being performed | Deduction, induction, abduction, causal inference |
| Inference-time procedure | How a model is prompted, decoded, or orchestrated for one task | CoT, self-consistency, least-to-most, ToT, GoT |
| Search algorithm | How candidate states or plans are explored | BFS, DFS, beam search, best-first search, MCTS |
| External computation | A specialised engine used to calculate, retrieve, execute, or prove | Python, SQL, SAT/SMT, theorem prover, retrieval system |
| Training objective | The signal used to change model behaviour | SFT, preference optimisation, outcome reward, process reward, RLVR |
| Architecture | The computational structure used inside or around a model | Transformer, recurrent/looped model, hierarchical modules, latent reasoning |
| Evaluation method | How a claimed capability is tested | Exact-answer verifier, process labels, hidden tests, perturbation, human review |

A technique may span multiple layers. For example, Tree of Thoughts is an inference-time search framework; it is not a new base-model architecture. GRPO is an optimisation algorithm, not a standalone reasoning method. A chain-of-thought trace is generated text and should not automatically be interpreted as a faithful record of internal computation.

## 2. Classical and formal reasoning

### Deductive inference
Derive a conclusion that follows from premises under explicit inference rules. Includes propositional logic, first-order logic, resolution, natural deduction and proof construction. Exactness depends on valid formalisation and sound inference.

### Inductive inference
Infer a general rule or pattern from finite observations. Conclusions are defeasible and depend on sample coverage, distribution assumptions and uncertainty.

### Abductive inference
Propose one or more plausible explanations for observations, then compare them with evidence. Abduction is hypothesis generation, not proof.

### Analogical and case-based reasoning
Map structural relationships from a known problem or case to a new one, retrieve relevant precedents, and adapt the solution. Similar surface wording is not enough; the relational mapping must be justified.

### Causal and counterfactual reasoning
Represent causal assumptions with graphs or structural models, distinguish observation from intervention, and reason about counterfactual outcomes. A predictive association alone does not identify a causal effect.

### Probabilistic and Bayesian inference
Represent uncertainty with distributions and update beliefs using evidence. Report priors, likelihood assumptions, calibration and sensitivity where they matter.

### Symbolic reasoning and theorem proving
Operate over explicit symbols, predicates, rules and proof obligations. Includes SAT/SMT solving, constraint solving, logic programming and proof assistants. The solver can verify the encoded problem, not whether the encoding captured the real-world intent.

### Constraint solving and program synthesis
Find assignments or programs that satisfy formal constraints, examples or specifications. Use test suites, proof obligations and sandboxing to validate generated programs.

## 3. Prompting and inference-time decomposition

### Chain-of-Thought (CoT)
Generate intermediate natural-language steps before an answer. Variants include few-shot CoT (worked demonstrations) and zero-shot CoT (an instruction to reason step by step). CoT can improve performance on some multi-step tasks, but the trace may be incomplete or unfaithful.

### Self-consistency
Sample multiple CoT paths and aggregate final answers, commonly by majority vote. It is a decoding/selection procedure, not a training objective. Report sample count and added compute.

### Least-to-most prompting
Decompose a difficult task into ordered subproblems and solve them sequentially, using earlier results to condition later steps. It was designed to improve compositional generalisation beyond the complexity of prompt examples.

### Plan-and-Solve
Ask for a plan before executing its substeps. Planning and execution must be evaluated separately; a coherent plan can still be incomplete or followed incorrectly.

### Self-Ask and question decomposition
Generate intermediate questions, answer them, and assemble the final response. External search can ground subanswers, but every retrieved fact still needs provenance and source validation.

### Program-of-Thoughts (PoT)
Represent a mathematical computation as executable code, using a runtime for deterministic arithmetic or data operations. Code generation errors and runtime safety remain separate issues.

### Program-Aided Language models (PAL)
Use a language model to translate and decompose a problem into a program, then delegate exact execution to an interpreter. The generated program is an artifact to test, not an oracle.

### Structured scratchpads and intermediate representations
Use tables, typed state, equations, schemas or other explicit intermediate objects to make dependencies inspectable. This is a design family rather than one standard algorithm.

## 4. Search and test-time compute

### Tree of Thoughts (ToT)
Represent partial solutions as branches, generate candidate continuations, evaluate states and use search strategies such as breadth-first or depth-first exploration with backtracking. Performance depends on state definition, branching factor, evaluator quality and compute budget.

### Graph of Thoughts (GoT)
Represent intermediate outputs as a graph with dependencies, allowing combination, transformation and iterative refinement. Graph orchestration can reuse or merge partial results but adds coordination complexity.

### Beam search
Keep a bounded number of high-scoring partial candidates at each step. It controls width and cost but can prune the correct path if the scoring heuristic is weak.

### Best-first search
Expand the currently most promising state according to a priority function. The heuristic controls search behaviour and may not reflect the true value of a partial solution.

### Breadth-first and depth-first search
Explore shallower states first or pursue one branch deeply before backtracking. These are general search strategies that can be paired with model-generated candidates.

### Monte Carlo Tree Search (MCTS)
Allocate simulations across a decision tree using exploration/exploitation rules and accumulated value estimates. Useful when actions can be simulated or evaluated; quality depends on rollout and value-estimation fidelity.

### Test-time compute scaling
Allocate more inference budget through longer deliberation, sampling, search, verifier-guided selection or iterative refinement. Compare methods using accuracy-versus-compute curves, not accuracy alone.

## 5. Agents, tools and retrieval

### ReAct
Interleave reasoning-oriented decisions with external actions and observations. A loop can retrieve information, execute a tool, inspect the result and choose the next action.

### Retrieval-Augmented Generation (RAG)
Retrieve documents or records and condition a response on them. RAG is a grounding architecture pattern, not proof of correct synthesis or citation faithfulness.

### Multi-hop and iterative retrieval
Use intermediate answers to generate follow-up queries, chaining evidence acquisition across sources. Track which claim is supported by which retrieved passage.

### Tool calling and learned tool use
Select and invoke calculators, search engines, APIs, databases, compilers and other tools. Evaluate tool selection, argument validity, execution reliability, permissions and output interpretation separately.

### Code execution and external solvers
Delegate deterministic subproblems to Python, SQL, symbolic engines or theorem provers. Treat the runtime boundary as a security boundary; use least privilege and sandboxing.

### Multi-agent collaboration
Assign agents distinct roles such as proposer, critic, researcher or verifier. Measure whether agent diversity adds value over a single model with an equal total compute budget. Agreement is not independent corroboration when agents share model biases or sources.

## 6. Verification, feedback and critique

### Self-Refine
Generate, critique and revise an answer in one or more rounds. Improvements depend on whether feedback is informative and discriminates real errors from stylistic preferences.

### Reflexion
Store verbal feedback from previous agent attempts and use it to guide later attempts. This is useful in repeated environments, but memory can preserve an incorrect diagnosis.

### Debate and adversarial critique
Generate competing proposals or critiques. Evaluate whether the method improves truth-tracking under matched compute; debate can otherwise reward persuasion or consensus.

### Outcome reward models (ORMs)
Score completed outputs or final answers. An ORM does not necessarily identify which intermediate step is wrong.

### Process reward models (PRMs)
Score intermediate reasoning steps. Process labels can provide denser supervision, but are costly and can be ambiguous; learned verifiers can be exploited.

### External verification
Use unit tests, property-based tests, compilers, theorem provers, trusted databases, independent evidence or expert review. This is usually a stronger check than asking the same model to reconsider its own answer, but still depends on specification and verifier validity.

## 7. Training paradigms and architectures

### Reasoning supervised fine-tuning (SFT) and distillation
Train on curated examples, solution traces or trajectories produced by a stronger teacher. Record the teacher, data provenance, trace filtering and contamination controls.

### Process supervision
Provide training labels for intermediate steps, rather than only final outcomes. Separate the effects of data quality, label policy, reward model architecture and search-time selection.

### Outcome supervision
Provide feedback on final answers or completed tasks. It can scale in domains with verifiable outcomes, but may not teach the model how to avoid bad intermediate steps.

### Reinforcement learning with verifiable rewards (RLVR)
Optimise a policy with rewards from deterministic or programmatic checks such as exact answers, unit tests or compilers. PPO and GRPO are optimisation choices used in some implementations; report reward definition, sampling, compute, and failure analysis.

### Preference optimisation
Use human preferences or learned reward models to shape outputs. Preference improvements are not equivalent to better mathematical or logical validity.

### Continuous or latent-space reasoning
Maintain intermediate reasoning state in hidden representations rather than verbalising every step. This raises questions about interpretability, faithfulness, controllability and evaluation.

### Recurrent and hierarchical computation
Reuse model computation across recurrent steps, loops or levels of abstraction. Compare against parameter- and compute-matched baselines to establish whether a proposed architecture—not just additional refinement—produces the gain.

### Multimodal and embodied reasoning
Combine language with visual, spatial, audio, video or action-conditioned state. Evaluate perception, grounding, planning and action execution as separate sources of error.

## 8. Evaluation dimensions

A reasoning experiment should not collapse capability into one headline accuracy number. Select measures according to the task:

- **Correctness:** exact-match, executable success, proof validity, task success.
- **Robustness:** paraphrase, numeric substitutions, irrelevant clauses, distribution shifts, adversarial inputs.
- **Process quality:** step correctness, trace faithfulness, dependency validity, verifier precision/recall.
- **Calibration:** confidence versus empirical correctness, selective prediction, abstention quality.
- **Efficiency:** tokens, FLOPs where available, tool calls, wall-clock latency, energy or monetary cost.
- **Reproducibility:** seeds, variance, environment, data version, code and artifact availability.
- **Generalisation:** held-out composition, unseen domains, fresh tasks and external validation.

See the [research evidence register](research-evidence-register.md), [experiment protocol](../templates/reasoning-experiment-protocol.md), and [finding record](../templates/research-finding-record.md).

## 9. Selected starting literature

- Wei et al. (2022), [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903).
- Wang et al. (2023), [Self-Consistency Improves Chain of Thought Reasoning](https://research.google/pubs/self-consistency-improves-chain-of-thought-reasoning-in-language-models/).
- Zhou et al. (2023), [Least-to-Most Prompting Enables Complex Reasoning](https://arxiv.org/abs/2205.10625).
- Yao et al. (2023), [Tree of Thoughts](https://papers.nips.cc/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html).
- Besta et al. (2024), [Graph of Thoughts](https://ojs.aaai.org/index.php/AAAI/article/view/29720).
- Yao et al. (2023), [ReAct](https://arxiv.org/abs/2210.03629).
- Gao et al. (2023), [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435).
- Lightman et al. (2023), [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050).
- Ke et al. (2025), [A Survey of Frontiers in LLM Reasoning](https://mlanthology.org/tmlr/2025/ke2025tmlr-survey/).
- Zhang et al. (2025), [A Survey on Test-Time Scaling in LLMs](https://arxiv.org/abs/2503.24235).
- Jin et al. (2026), [The Mirage of Explainability: A Survey on CoT Faithfulness](https://aclanthology.org/2026.emnlp-main.614/).

## 10. Maintenance policy

Add a method only when its primary source, conceptual layer, intended task, evaluation setup and known limitations can be stated. Keep method descriptions distinct from claims about ReasoningAI implementations. When results are added, cite the source and use the [research finding record](../templates/research-finding-record.md). Do not copy figures, tables or substantial paper text without checking reuse rights.
