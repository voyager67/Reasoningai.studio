#!/usr/bin/env python3
"""Local CSV/JSONL dataset audit. Reports aggregate counts and duplicate locations, not raw rows."""
from __future__ import annotations
import argparse, csv, hashlib, json, sys
from collections import Counter, defaultdict
from pathlib import Path

def stable_hash(value: str) -> str:
    return hashlib.sha256(value.strip().encode('utf-8',errors='replace')).hexdigest()

def read_records(path: Path, fmt: str):
    if fmt=='csv':
        with path.open('r',encoding='utf-8-sig',newline='') as f:
            yield from csv.DictReader(f)
    else:
        with path.open('r',encoding='utf-8') as f:
            for line_no,line in enumerate(f,1):
                if not line.strip(): continue
                try: item=json.loads(line)
                except json.JSONDecodeError as exc: raise ValueError(f'Invalid JSON on line {line_no}: {exc.msg}')
                if not isinstance(item,dict): raise ValueError(f'Line {line_no} is not a JSON object')
                yield item

def audit(records, id_col='id', text_col='text', label_col='label', split_col='split'):
    total=0; missing=Counter(); labels=defaultdict(Counter); split_counts=Counter()
    row_hashes=defaultdict(list); text_hashes=defaultdict(list); ids=Counter(); keys=set(); duplicate_ids=0
    columns=set()
    for idx,row in enumerate(records,1):
        total+=1; columns.update(map(str,row.keys()))
        for col in (id_col,text_col,label_col,split_col):
            if col and (col not in row or row.get(col) is None or str(row.get(col)).strip()==''):
                missing[col]+=1
        ident=str(row.get(id_col,'')).strip() if id_col else ''
        split=str(row.get(split_col,'')).strip() if split_col else ''
        label=str(row.get(label_col,'')).strip() if label_col else ''
        text=str(row.get(text_col,'')).strip() if text_col else ''
        if ident:
            ids[ident]+=1
            if ids[ident]>1: duplicate_ids+=1
        if split: split_counts[split]+=1
        if split and label: labels[split][label]+=1
        rh=stable_hash(json.dumps(row,sort_keys=True,ensure_ascii=False,default=str))
        row_hashes[rh].append({'row':idx,'split':split})
        if text: text_hashes[stable_hash(text)].append({'row':idx,'split':split})
    duplicate_rows=[{'count':len(v),'row_numbers':[x['row'] for x in v[:20]]} for v in row_hashes.values() if len(v)>1]
    cross_split=[]
    for h,items in text_hashes.items():
        splits=sorted({x['split'] for x in items if x['split']})
        if len(splits)>1: cross_split.append({'splits':splits,'count':len(items)})
    return {'record_count':total,'columns':sorted(columns),'missing_values':dict(missing),
            'duplicate_id_rows_beyond_first':duplicate_ids,'duplicate_row_groups':len(duplicate_rows),
            'duplicate_row_examples':duplicate_rows[:50],'cross_split_exact_text_groups':cross_split[:100],
            'split_counts':dict(split_counts),'label_counts_by_split':{s:dict(c) for s,c in labels.items()},
            'notes':['Exact-text checks do not detect semantic or near-duplicate leakage.','Inspect split strategy for subject, source, temporal, and group leakage.','Raw row values are not included in this report.']}

def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('dataset',type=Path)
    ap.add_argument('--format',choices=['csv','jsonl'],default=None)
    ap.add_argument('--id-column',default='id'); ap.add_argument('--text-column',default='text')
    ap.add_argument('--label-column',default='label'); ap.add_argument('--split-column',default='split')
    ap.add_argument('--output',type=Path)
    args=ap.parse_args(argv)
    if args.output and args.output.resolve()==args.dataset.resolve():
        ap.error('--output must not overwrite the source dataset')
    fmt=args.format or ('jsonl' if args.dataset.suffix.lower() in {'.jsonl','.ndjson'} else 'csv')
    try:
        report=audit(read_records(args.dataset,fmt),args.id_column,args.text_column,args.label_column,args.split_column)
    except (OSError,ValueError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr); return 2
    report['source_file']=args.dataset.name; report['format']=fmt
    rendered=json.dumps(report,indent=2,ensure_ascii=False)+'\n'
    if args.output: args.output.write_text(rendered,encoding='utf-8')
    else: print(rendered,end='')
    return 0
if __name__=='__main__': raise SystemExit(main())
