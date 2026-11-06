#!/usr/bin/env python3
"""Heuristic, read-only reproducibility preflight for a research project."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

CHECKS=[
 ('project_readme',['README.md','README.rst']),
 ('license_or_data_terms',['LICENSE','LICENSE.md','COPYING','DATA_LICENSE.md']),
 ('dependency_manifest',['requirements.txt','pyproject.toml','environment.yml','environment.yaml','conda-lock.yml','uv.lock','poetry.lock']),
 ('data_provenance',['DATASET.md','DATASHEET.md','data_card.md','data/README.md']),
 ('training_or_analysis_entrypoint',['train.py','main.py','run_experiment.py','analysis.py','notebooks/']),
 ('evaluation_entrypoint',['evaluate.py','eval.py','test.py']),
 ('configuration',['config.yaml','config.yml','config.json','configs/']),
 ('run_logs_or_results',['logs/','results/','metrics.json','metrics.csv']),
 ('model_or_artifact_manifest',['MODEL_CARD.md','model_card.md','artifacts/','checkpoints/README.md']),
]
SEED_RE=re.compile(r'\b(seed|manual_seed|random_state|deterministic)\b',re.I)
COMMAND_RE=re.compile(r'python\s+[^\n`]+|uv\s+run\s+[^\n`]+|conda\s+run\s+[^\n`]+',re.I)

def check(root: Path):
    present=[]; missing=[]
    for label,candidates in CHECKS:
        found=[c for c in candidates if (root/c).exists()]
        item={'check':label,'found':found}
        (present if found else missing).append(item)
    readmes=[root/'README.md']
    readme_text='\n'.join(p.read_text(encoding='utf-8',errors='replace') for p in readmes if p.is_file())
    seed_files=[]; command_examples=[]
    for base in (root/'src',root/'scripts',root/'configs',root):
        if not base.exists(): continue
        for p in base.rglob('*'):
            if not p.is_file() or any(part in {'.git','.venv','venv','node_modules','__pycache__'} for part in p.parts): continue
            if p.suffix.lower() not in {'.py','.md','.txt','.yaml','.yml','.toml','.json'}: continue
            try: content=p.read_text(encoding='utf-8',errors='replace')
            except OSError: continue
            if SEED_RE.search(content): seed_files.append(str(p.relative_to(root)))
            if p.name.lower()=='readme.md': command_examples.extend(COMMAND_RE.findall(content))
            if len(seed_files)>100: break
        if len(seed_files)>100: break
    return {'project':root.name,'assessment':'heuristic_preflight_not_a_reproduction',
            'present_checks':present,'missing_checks':missing,
            'seed_or_determinism_mentions':sorted(set(seed_files)),
            'documented_command_examples':command_examples[:30],
            'limitations':['This script inspects filenames and text heuristically; it does not execute project code.','A detected seed mention does not prove deterministic execution.','A missing filename does not prove the artifact is absent under another name.','Only a clean rerun can provide direct reproduction evidence.']}

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('project',type=Path); ap.add_argument('--output',type=Path)
    args=ap.parse_args(argv)
    if not args.project.is_dir(): ap.error(f'not a directory: {args.project}')
    report=check(args.project.resolve()); rendered=json.dumps(report,indent=2,ensure_ascii=False)+'\n'
    if args.output: args.output.write_text(rendered,encoding='utf-8')
    else: print(rendered,end='')
    return 0
if __name__=='__main__': raise SystemExit(main())
