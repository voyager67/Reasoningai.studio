# Notices, provenance, and attribution

ReasoningAI Studio is an independent research workflow project. This unified
release combines original ReasoningAI Studio materials with a separately
licensed contribution from ResearchForge Skills 1.0.0. It is not affiliated
with or endorsed by the referenced projects.

## Included ResearchForge Skills contribution

Source: [voyager67/ResearchForge-Skills](https://github.com/voyager67/ResearchForge-Skills),
version 1.0.0, supplied as `ResearchForge-Skills-1.0.0.zip` (SHA-256: `4faa8c552e980292d9981bcf79ad9cbec18da2514f7fbf69c8c88c7db6f070bb`). The contribution's
30 English skills, English prompt, templates, sample files, and local Python
utilities are included. The 30 skills are namespaced as `researchforge-*` so that
they coexist with ReasoningAI skills without overwriting or silently replacing
workflows with similar names. Only the machine-readable `name` field was changed
for those skill files; their instructional text is retained. The Chinese prompt
was intentionally excluded because this release is English-only.

- Skills, prompt, templates, examples, and catalog-derived descriptions from
  ResearchForge retain **CC BY 4.0**. Attribution:
  ResearchForge Skills contributors, *ResearchForge Skills* (v1.0.0),
  https://github.com/voyager67/ResearchForge-Skills. License: https://creativecommons.org/licenses/by/4.0/.
- Imported ResearchForge Python utilities and their associated tests retain **MIT**.
  Their original license text is at `licenses/RESEARCHFORGE-CODE-LICENSE.txt`.
- The ResearchForge original content license and citation record are preserved in
  `licenses/RESEARCHFORGE-CONTENT-LICENSE.md` and
  `licenses/RESEARCHFORGE-CITATION.cff`. The mixed unified catalogs
  (`catalog/skills.json` and `docs/skill-catalog.md`) identify the applicable
  license for each skill; ResearchForge descriptions in those catalogs remain
  CC BY 4.0, while ReasoningAI skill descriptions remain CC BY-NC 4.0.

## Other research references

The original ReasoningAI Studio work was developed independently with workflow
inspiration from projects listed in `docs/research-ecosystem.md`, including
Adkid-Zephyr/anti-defensive-writing-Skill, BESSER-PEARL/research-agent-skills,
kinqsradio/academic-research-skills, and Boom5426/Nature-Paper-Skills. No source
files or prose from those references are bundled here. Their authors retain all
rights under their own licenses.

## License boundary

The root `LICENSE` applies to ReasoningAI Studio original materials only. It does
not override the ResearchForge CC BY 4.0 or MIT terms above, nor any third-party
terms for linked tools, APIs, standards, or services. Commercial use of
ReasoningAI-owned CC BY-NC 4.0 materials requires separate permission from the
rights holder. ResearchForge contribution materials retain their own CC BY 4.0
and MIT permissions.
