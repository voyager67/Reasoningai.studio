---
name: researchforge-research-ethics-and-data-governance
description: >-
  Review research plans for consent, privacy, data rights, institutional approval, risk minimization, security, and responsible release of datasets and models.
license: CC-BY-4.0
metadata:
  project: ResearchForge-Skills
  version: "1.0.0"
---

# Research Ethics And Data Governance

## Purpose

Surface ethical and legal questions early enough to change the research design, not as a final checkbox.

## Input

Bring any material already available: research protocol, data sources, participant or subject context, collection method, intended analysis, storage, collaborators, and release plan. If an essential item is absent, state the gap and proceed with a clearly labelled provisional plan rather than repeatedly asking for information that is already present.

## Workflow

1. Map data subjects, data types, sensitivity, collection pathway, controller/steward, and intended recipients.
2. Check consent, notice, lawful access, data license, institutional approval, and terms of use; route jurisdiction-specific questions to qualified authorities.
3. Assess re-identification, linkage, model memorization, biometric or sensitive inference, and downstream misuse risks.
4. Apply data minimization, access controls, retention limits, encryption, pseudonymization, and safe deletion where applicable.
5. Review dataset and model release decisions separately; consider whether weights, prompts, examples, or metadata leak protected information.
6. Assess dual-use implications and whether mitigations, staged access, or non-release is appropriate.
7. Document accountability, incident response, researcher responsibilities, and any unresolved approvals before data collection.

## Required output

Ethics and data-governance checklist with data inventory, consent/rights evidence, privacy risks, mitigations, approval dependencies, retention, release decision, and open questions for institutional/legal review.

## Integrity and safety gates

- Do not provide legal certainty where jurisdiction or institutional policy is unknown.
- Do not publish personal, sensitive, or restricted data to make a benchmark reproducible.
- Do not bypass review-board approval or consent requirements.
- Treat model weights and embeddings as possible carriers of sensitive information.

## Related skills

`dataset-audit`, `ml-experiment-planning`, `reproducibility-audit`, `conference-submission-preflight`

## Example request

> Review whether this image dataset can be used and released for deepfake-detection research, including privacy and license risks.
