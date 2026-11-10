# Research publication standard

This document defines how ReasoningAI records research work and decides what may appear on the website, in a repository release, or in a paper.

## 1. Separate the kinds of work

Every public item must be identified as one of the following:

- **Literature note:** a synthesis of external research with linked sources.
- **Research proposal:** a question, hypothesis and planned method; no results are implied.
- **Experiment protocol:** a frozen plan for data, baseline, metrics and execution.
- **Internal result:** a completed run not yet independently checked.
- **Reproduced result:** a result rerun using a documented method, with deviations stated.
- **Research finding:** a claim supported by an analysed result and its uncertainty.
- **Preprint / submitted paper / published paper:** manuscript status must be accurate and linked to the relevant version.

A literature result must never be presented as a ReasoningAI experiment. A project marked planned must not have fabricated progress metrics, benchmark results or impact claims.

## 2. Project lifecycle

Use the following status vocabulary consistently:

| Status | Meaning | Website treatment |
|---|---|---|
| Planned | Topic selected; protocol not frozen | “Planned research track” |
| Protocol design | Question and experimental design being specified | “Protocol in development” |
| Implementation | Code or test harness exists; no validated result implied | “Implementation underway” |
| Running | Experiments are actively executing | “Experiments running” only if true |
| Internal analysis | Runs completed; checks and interpretation ongoing | “Internal analysis” |
| Reproduced | A documented run has been repeated from frozen artifacts | “Reproduced under stated setup” |
| Submitted | Manuscript submitted to a named venue | Name the venue and date only if verifiable |
| Published | Accepted/published with persistent paper link | “Published” with DOI/venue |
| Archived | Work stopped or superseded; preserve why | State the reason and final status |

Status is a factual field. Update it only when repository artifacts support the change.

## 3. Minimum evidence package

Before a result is promoted from internal analysis to a public research finding, record:

- exact research question and falsifiable hypothesis;
- model name, checkpoint/revision, tokenizer and inference configuration;
- dataset provenance, license, version, split, filtering and contamination analysis;
- baseline and justification for comparability;
- prompt, system instructions, tools, code and dependency versions;
- number of runs, random seeds, sample counts and stopping rules;
- compute budget, token budget, tool calls, latency and hardware;
- primary and secondary metrics with aggregation rules;
- uncertainty intervals or variance where applicable;
- ablations, robustness slices and failure analysis;
- deviations from the frozen protocol;
- artifact locations, hashes and reproduction instructions;
- limitations, threats to validity and what was not tested.

## 4. Required comparisons

For inference-time methods, compare at least:
1. a direct or minimal baseline;
2. a strong standard baseline (for example, CoT where appropriate);
3. the proposed method;
4. a compute-matched comparison or an explicit quality-versus-cost curve.

For architecture or training claims, add capacity-aware controls:
- parameter-matched baseline;
- training-data and training-step comparison;
- training-compute disclosure;
- inference-compute comparison;
- ablations that isolate each proposed component.

Do not present comparisons across papers as if they were one controlled experiment.

## 5. Website claim policy

The website has two separate content types:

- **State of the field:** reported results from papers and independent benchmark evaluators. Always label the source and avoid first-person ownership of those results.
- **ReasoningAI research:** our own projects. Link to the corresponding research folder, protocol and result artifacts. Mark planned or unpublished work clearly.

Every numerical headline needs a source, a comparator, an exact metric, an evaluation setting and a date/version. Avoid “state of the art”, “breakthrough”, “outperforms” or “validated” unless a defensible comparison supports that wording.

## 6. Publication checklist

Before publication, complete the [finding record](../templates/research-finding-record.md) and check:

- [ ] Claims map to exact tables, figures, logs or source passages.
- [ ] Primary sources and dataset versions are linked.
- [ ] Baselines are fair and compute is disclosed.
- [ ] Test contamination and leakage were assessed.
- [ ] Negative results and failed runs are not hidden.
- [ ] Uncertainty and limitations appear next to the headline.
- [ ] Data and model licenses permit the planned release.
- [ ] Privacy, consent, security and research ethics were reviewed.
- [ ] Reproduction instructions were tested by someone other than the original author where feasible.
- [ ] Website copy distinguishes external literature from ReasoningAI's own results.

## 7. Source and version management

Prefer DOI, proceedings, official dataset repositories and archived benchmark records. Save a bibliographic record and access date. If a paper is updated, preserve the version used for the claim. Never cite a search result as if it were the paper itself.

The publication standard applies to research records and web copy. It does not replace venue requirements, institutional approval, ethics review or domain-specific standards.
