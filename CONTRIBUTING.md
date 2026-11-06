# Contributing

Contributions should improve a real research workflow and preserve evidence
integrity. This release is English-only; new skills, prompts, examples, and docs
should be written in English.

## Add a skill

1. Create `skills/<lowercase-hyphen-name>/SKILL.md`.
2. Add YAML frontmatter with a matching `name` and a useful `description`.
3. Specify required inputs, a task-specific procedure, a concrete output, and
   integrity/security boundaries.
4. Keep the workflow actionable; avoid generic prompt filler and unsupported
   claims about what tools can verify.
5. Add or update tests and the unified catalog in `catalog/skills.json` and
   `docs/skill-catalog.md`.
6. State the applicable license and provenance before including external text,
   code, assets, or examples. Never assume all third-party licenses are alike.

## Quality checks

```bash
python -m unittest discover -s tests -v
python -m compileall -q reasoningai scripts
python scripts/validate_skills.py
python -m reasoningai doctor
```

Do not submit secrets, private manuscripts, participant data, or unpublished
reviewer reports. Use synthetic fixtures. See `PRIVACY.md`, `SECURITY.md`,
and `NOTICE.md`.
