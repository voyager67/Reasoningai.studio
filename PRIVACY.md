# Privacy and data handling

ReasoningAI Studio is a local-first toolkit. The CLI does not upload manuscript
text, PDFs, datasets, credentials, or screening decisions to a ReasoningAI
Studio server. There is no hosted backend, user account, analytics, telemetry,
or remote storage in this release.

## Network behavior

Network calls are explicit: scholarly search and DOI-verification commands use
OpenAlex, Crossref, or optional Semantic Scholar; the imported
`scripts/verify_bibliography.py` performs Crossref lookups unless `--offline`
is supplied. These calls send search terms or DOI identifiers plus ordinary
request metadata. They do not upload local manuscripts, entire bibliographies,
or dataset rows. Avoid queries that contain confidential research details.

## Local data handling

The dataset audit reads CSV or JSONL locally. It reports schema names, aggregate
counts, split and label distributions, and duplicate row positions. It does not
include raw row text in its report; content hashes are used transiently for
duplicate detection. The reproducibility preflight scans filenames and selected
text files locally and does not execute project code. Skill validation reads
Markdown metadata and local links.

## Credentials

No API key is required for the default OpenAlex or Crossref paths. The optional
Semantic Scholar key is read from `SEMANTIC_SCHOLAR_API_KEY`. Never paste keys
into source files, prompts, issue reports, screenshots, or committed `.env`
files. `.env` is ignored by Git. A local environment variable or secret manager
is preferable.

## Research and host privacy

Keep manuscripts, unpublished results, human-subject data, private notes, and
project-specific exports outside the public repository. The included `.gitignore`
excludes common research files, but it is not a data-loss prevention system. An
AI agent reading files or using a connected browser/search tool is still subject
to that provider's own processing and retention policies. Review those terms
before supplying confidential material.

## Limits

The utilities do not create a secure enclave or enforce model-provider privacy
settings. A skill file cannot override the host agent's permissions or privacy
policies. Inspect every report and keep a clean copy of important source data.
