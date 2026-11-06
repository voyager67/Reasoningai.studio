# Research ecosystem and design references

This inventory records projects and services that informed the architecture. It is not a ranking, endorsement, or claim that ReasoningAI Studio reproduces their proprietary capabilities. Repository licenses were checked from their repository license files where stated below; service pricing and API availability can change.

## Skill and workflow repositories

| Project | What is useful to study | License checked | How ReasoningAI differs |
|---|---|---|---|
| [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) | Lightweight SKILL.md pattern, copy-ready prompt pack, focused academic editing principle. | MIT, checked from `LICENSE`. | We wrote a separate evidence-preserving editor; no original files or prose were copied. |
| [BESSER-PEARL/research-agent-skills](https://github.com/BESSER-PEARL/research-agent-skills) | Cross-agent skills.sh install pattern and structured manuscript review. | MIT, checked from `LICENSE`. | Expands to multiple stages and adds deterministic local utilities. |
| [kinqsradio/academic-research-skills](https://github.com/kinqsradio/academic-research-skills) | File-first evidence workflow, private research workspace guidance, validation and claim/source locators. | MIT, checked from `LICENSE`. | Ships its own compact CLI, tests, and 64 English-only skills. |
| [Boom5426/Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills) | End-to-end manuscript lifecycle, section-specific workflows, figure checks, rebuttal flow, example-driven documentation. | MIT, checked from `LICENSE`. | General research workflows rather than Nature-specific manuscript conventions. |
| [Future-House/paper-qa](https://github.com/Future-House/paper-qa) | Retrieval-augmented question answering over scientific papers. | Apache-2.0, checked from `LICENSE`. | Not bundled; evaluate it as an optional full-text retrieval component. |
| [ASReview](https://github.com/asreview/asreview) | Active-learning support for systematic-review screening and transparent review practice. | Apache-2.0, checked from `LICENSE`. | We provide a simple human-led screening ledger, not an active-learning screening engine. |
| [GROBID](https://github.com/kermitt2/grobid) | Scholarly PDF parsing and structured extraction; useful as an optional local service. | Official project page reports Apache-2.0 for software; re-check before bundling. | Not bundled; full PDF parsing is outside this lightweight CLI. |

| **ResearchForge Skills 1.0.0 (maintainer-authored)** | 30 focused research workflows, privacy-aware utility scripts, audit templates, and reusable prompts. | CC BY 4.0 for repository materials; two named anti-defensive prompt files retain MIT. | Included as the maintainer's own work; no standalone public source repository is claimed. |

## Scholarly metadata and standards

- [OpenAlex API](https://help.openalex.org/api/): default metadata search adapter; basic API access is available without an API key, subject to current usage limits. OpenAlex states that its data are CC0; still retain provenance and respect publisher rights in full-text files.
- [Crossref REST API](https://www.production.crossref.org/documentation/retrieve-metadata/rest-api/): DOI metadata lookup. Crossref says no sign-up is required for its public API.
- [Semantic Scholar Academic Graph API](https://api.semanticscholar.org/api-docs): optional search adapter; this project reads a key from `SEMANTIC_SCHOLAR_API_KEY` and never stores one.
- [PRISMA 2020](https://www.prisma-statement.org/prisma-2020): reporting guideline and flow diagram for systematic reviews. Use the official checklist and templates; the CLI only summarizes user-entered screening counts.
- [CONSORT 2025](https://www.bmj.com/content/389/bmj-2024-081123): current reporting statement for randomized trials; use the official guideline relevant to the study design.

## Commercial products to benchmark against

| Product | Paid/free capability worth benchmarking | Boundary for this release |
|---|---|---|
| [Elicit](https://elicit.com/pricing) | Paper discovery, paper chat, research reports, structured extraction, systematic-review workflows. | We provide prompt workflows, metadata search, and local CSV helpers; no licensed full-text corpus or equivalent hosted extraction service. |
| [Scite](https://scite.ai/pricing) | Smart Citation context (supporting/contrasting/mentioning), reference checks, alerts, and research assistant. | We do not provide Scite's citation-context corpus or trained classification system. |
| [Rayyan](https://www.rayyan.ai/pricing) | Collaborative review screening, duplicate detection, AI relevance predictions, PICO extraction. | We provide a portable ledger and arithmetic summary, not a multi-user cloud screening platform. |
| [Zotero](https://www.zotero.org/) | Reference library, capture, PDF annotation, citation integration. | Use Zotero as the reference manager; import/export CSV/BibTeX and use the DOI audit helpers alongside it. |

## License and reuse rules

All 64 project skills and the other project-authored materials are covered by CC BY 4.0, except the two prompt files identified in `licenses/MIT-EXCEPTIONS.txt`, which retain MIT. External projects in this inventory keep their own licenses; being listed here does not grant permission to copy their code, prompts, figures, or datasets. Re-check an external project's current license and attribution terms before adapting or redistributing its material.

## Video and hands-on references

- [ASReview LAB step-by-step screening tutorial (YouTube)](https://www.youtube.com/watch?v=O_Qh9HpwOeQ): a walkthrough of importing records and using active-learning-assisted title/abstract screening.
- [ASReview teaching materials](https://github.com/asreview/asreview-academy): public exercises for screening and simulations; the repository states CC BY 4.0 for its teaching materials.
- [OpenAlex tutorials](https://help.openalex.org/tutorials/): end-to-end API and literature-exploration tutorials, including systematic-review search strategies.
- [GROBID quick start](https://grobid.readthedocs.io/en/latest/getting_started/): setup and extraction walkthroughs for extracting structured metadata from scholarly PDFs.

These are third-party educational references, not demos of ReasoningAI Studio.
