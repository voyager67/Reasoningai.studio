# Reasoning experiment protocol

> Copy this file into research/<track>/protocol.md. Complete and review it before running experiments. Record all deviations rather than silently editing a frozen protocol.

## 1. Study identity

- Project / track:
- Protocol version:
- Status: Planned / Frozen / Amended / Completed
- Owner(s):
- Date frozen:
- Repository and code commit:
- Related literature:
- Funding / compute source, if relevant:

## 2. Research question and hypotheses

- Primary research question:
- Motivation and evidence gap:
- Primary hypothesis:
- Operational prediction:
- Null hypothesis:
- Rival explanations:
- Falsification criterion:
- Secondary hypotheses:

## 3. Task definition and scope

- Task family:
- Input / output specification:
- Unit of analysis:
- Success definition:
- Exclusions:
- Intended deployment boundary:
- Out-of-scope claims:

## 4. Methods under comparison

| Arm | Method | Model / checkpoint | Prompt or config | Role |
|---|---|---|---|---|
| A | Direct / minimal baseline | | | |
| B | Strong standard baseline (e.g. CoT) | | | |
| C | Proposed method | | | |
| D | Compute-matched or ablation control | | | |

For each method, record the exact algorithm, model calls, sampling, branching, search, tools, verifier, stopping rule and fallback behaviour.

## 5. Models and runtime

- Model name and immutable revision:
- Weights/tokenizer source and license:
- Quantization / precision:
- Inference framework and version:
- Decoding parameters:
- Context and output limits:
- System / developer prompts:
- Tool versions and permissions:
- Hardware:
- Software environment / lockfile:
- Randomness sources and seeds:

## 6. Dataset and provenance

| Dataset | Version / commit | License | Split | Count | Hash / immutable ID | Transformations |
|---|---|---|---|---:|---|---|

- Access date and source:
- Inclusion / exclusion rules:
- Deduplication:
- Train/test leakage checks:
- Benchmark contamination checks:
- Privacy / consent / ethics review:
- Data retention and release plan:

## 7. Experimental design

- Study design:
- Baseline selection rationale:
- Randomisation or sampling plan:
- Number of seeds / independent runs:
- Number of samples per item:
- Stopping criteria:
- Hyperparameter search budget:
- Order effects / caching controls:
- Failure and timeout handling:
- Deviations policy:

## 8. Compute and cost budget

| Arm | Model calls | Max tokens / call | Total token budget | Tool calls | Wall-clock budget | Hardware |
|---|---:|---:|---:|---:|---:|---|

Record prompt, completion and reasoning tokens separately where available. Report actual consumption, not only the planned budget.

## 9. Metrics and analysis plan

### Primary endpoint
- Metric and formula:
- Aggregation unit:
- Exact scoring script / version:
- Statistical comparison:
- Uncertainty interval:
- Minimum practically meaningful effect:

### Secondary endpoints
- Correctness / task success:
- Robustness / perturbation:
- Process or trace validity:
- Calibration / verifier quality:
- Latency:
- Token and tool cost:
- Memory / compute:
- Failure categories:

### Analysis controls
- Multiple comparisons:
- Missing or invalid runs:
- Outlier policy:
- Confidence interval method:
- Subgroup / difficulty slices:
- Exploratory versus confirmatory analysis:

## 10. Ablations and negative controls

| Component | Ablation / control | Expected diagnostic | Result |
|---|---|---|---|
| Search / decomposition | Remove or reduce | Isolate structural contribution | |
| Verifier / reward | Disable or replace | Isolate evaluator contribution | |
| Extra compute | Match or remove | Separate quality from budget | |
| Data augmentation | Remove / vary | Test data contribution | |
| Architecture | Parameter/compute matched baseline | Isolate architecture contribution | |

Add task-specific controls, adversarial cases and known-answer checks.

## 11. Reproducibility and artifacts

- Code commit:
- Commands:
- Environment / dependency lock:
- Config files:
- Dataset IDs and hashes:
- Raw result location:
- Logs / traces:
- Checkpoints:
- Artifact storage and access:
- Independent rerun plan:

## 12. Decision rules

- Continue if:
- Stop if:
- Redesign if:
- Claim supported if:
- Claim not supported if:

## 13. Deviations and decision log

| Date | Version / run | Change | Reason | Impact on interpretation | Approved by |
|---|---|---|---|---|---|

## 14. Sign-off

- Protocol reviewed by:
- Date:
- Frozen commit:
