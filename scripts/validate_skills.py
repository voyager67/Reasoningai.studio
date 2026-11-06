#!/usr/bin/env python3
"""Validate local Agent Skills metadata, structure, and relative Markdown links."""
from __future__ import annotations
import re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SKILLS=ROOT/'skills'
NAME_RE=re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')

def parse_frontmatter(path: Path):
    text=path.read_text(encoding='utf-8')
    if not text.startswith('---\n'): raise ValueError('missing opening YAML frontmatter')
    end=text.find('\n---\n',4)
    if end<0: raise ValueError('missing closing YAML frontmatter')
    fm=text[4:end]
    vals={}
    for line in fm.splitlines():
        if line.startswith('  '): continue
        m=re.match(r'^([a-z][a-z0-9_-]*):\s*(.*)$',line)
        if m: vals[m.group(1)]=m.group(2).strip().strip('"\'')
    return vals,text[end+5:]

def validate(root: Path=ROOT):
    errors=[]; skills_root=root/'skills'; skill_dirs=sorted(p for p in skills_root.iterdir() if p.is_dir()) if skills_root.exists() else []
    if not skill_dirs: errors.append('no skill directories found')
    for folder in skill_dirs:
        path=folder/'SKILL.md'
        if not path.is_file(): errors.append(f'{folder.name}: missing SKILL.md'); continue
        try: fm,body=parse_frontmatter(path)
        except (OSError,ValueError) as exc: errors.append(f'{folder.name}: {exc}'); continue
        name=fm.get('name',''); desc=fm.get('description','')
        if not NAME_RE.fullmatch(name): errors.append(f'{folder.name}: invalid name {name!r}')
        if name!=folder.name: errors.append(f'{folder.name}: frontmatter name does not match directory')
        if not desc or len(desc)>1024: errors.append(f'{folder.name}: description missing or longer than 1024 characters')
        if len(body.strip())<400: errors.append(f'{folder.name}: skill body is unexpectedly short')
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',body):
            if target.startswith(('http://','https://','#','mailto:')): continue
            target=target.split('#',1)[0]
            if not target: continue
            resolved=(path.parent/target).resolve()
            try: resolved.relative_to(root.resolve())
            except ValueError: errors.append(f'{folder.name}: link escapes repository: {target}'); continue
            if not resolved.exists(): errors.append(f'{folder.name}: broken relative link: {target}')
    return len(skill_dirs),errors

def main():
    count,errors=validate()
    if errors:
        print(f'FAIL: {len(errors)} issue(s) across {count} skills')
        for e in errors: print(f'- {e}')
        return 1
    print(f'PASS: {count} skill folders have valid frontmatter, descriptions, body length, and local links.')
    return 0
if __name__=='__main__': raise SystemExit(main())
