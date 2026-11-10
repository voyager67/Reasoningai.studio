# ReasoningAI research programme

This directory is the canonical record of ReasoningAI's own research tracks. It is separate from the literature synthesis in [the evidence register](../docs/reasoning-evidence-register.md).

## Research tracks

| Track | Status | Focus |
|---|---|---|
| [CoT — Faithfulness and evaluation](cot-faithfulness/README.md) | Planned | When are verbalised reasoning traces faithful, useful and verifiable? |
| [ToT — Search and planning](tot-search-planning/README.md) | Planned | When does branching search and backtracking improve task success under a fixed compute budget? |
| [HRM — Hierarchical computation](hrm-hierarchical-reasoning/README.md) | Planned | Which gains come from recurrent/hierarchical computation versus refinement loops, data augmentation or extra compute? |

**No original experimental results are claimed in these project records yet.** Statuses will change only when protocols, code, logs and evidence support the change.

## Standard project layout

When a track moves into implementation, use this structure:

~~~text
research/<track>/
├── README.md                 # question, scope, status, links
├── protocol.md               # frozen design and decision rules
├── method.md                 # implementation and exact method
├── results/
│   ├── runs.csv              # run-level metrics and metadata
│   ├── summary.md            # analysed results and uncertainty
│   └── failures.md           # error taxonomy and negative findings
├── artifacts/
│   └── README.md             # paths, hashes and release notes
└── paper/
    ├── outline.md
    └── claims.md             # claim-to-evidence map
~~~

Do not commit large checkpoints, private datasets, credentials or restricted artifacts. Keep external datasets at their licensed source and record immutable identifiers, hashes and access conditions. Use Git LFS or a suitable data registry only after checking the storage and license implications.

## Working templates

- [Reasoning experiment protocol](../templates/reasoning-experiment-protocol.md)
- [Research finding record](../templates/research-finding-record.md)
- [Existing experiment plan](../templates/researchforge-experiment-plan.md)
- [Existing research protocol](../templates/researchforge-research-protocol.md)
- [Evidence matrix CSV](../templates/researchforge-evidence-matrix.csv)
- [Claim-evidence ledger CSV](../templates/researchforge-claim-evidence-ledger.csv)

## Research governance

Use the [publication standard](../docs/research-publication-standard.md). External literature results belong in the evidence register; only ReasoningAI-run experiments belong in these project folders.
