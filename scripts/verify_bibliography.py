#!/usr/bin/env python3
"""Verify BibTeX DOI metadata against Crossref. Standard library only."""
from __future__ import annotations
import argparse, json, re, sys, time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)

def _split_top_level(value: str) -> list[str]:
    parts=[]; start=0; braces=0; parens=0; quoted=False; escaped=False
    for i,ch in enumerate(value):
        if escaped: escaped=False
        elif ch=='\\': escaped=True
        elif ch=='"' and braces==0: quoted=not quoted
        elif not quoted and ch=='{': braces+=1
        elif not quoted and ch=='}' and braces: braces-=1
        elif not quoted and braces==0 and ch=='(': parens+=1
        elif not quoted and braces==0 and ch==')' and parens: parens-=1
        elif not quoted and braces==0 and parens==0 and ch==',':
            parts.append(value[start:i].strip()); start=i+1
    parts.append(value[start:].strip())
    return parts

def _entry_body_end(text: str, start: int, opener: str) -> int | None:
    closer='}' if opener=='{' else ')'
    depth=1; braces=0; quoted=False; escaped=False
    for i in range(start,len(text)):
        ch=text[i]
        if escaped: escaped=False; continue
        if ch=='\\': escaped=True; continue
        if opener=='{':
            if ch=='"' and depth==1: quoted=not quoted
            elif not quoted and ch=='{': depth+=1
            elif not quoted and ch=='}':
                depth-=1
                if depth==0: return i
        else:
            if ch=='"' and braces==0: quoted=not quoted
            elif not quoted and ch=='{': braces+=1
            elif not quoted and ch=='}' and braces: braces-=1
            elif not quoted and braces==0 and ch=='(': depth+=1
            elif not quoted and braces==0 and ch==')':
                depth-=1
                if depth==0: return i
    return None

def _strip_outer(value: str) -> str:
    value=value.strip()
    if len(value)<2: return value
    if value[0]=='{' and value[-1]=='}':
        depth=0; escaped=False
        for i,ch in enumerate(value):
            if escaped: escaped=False
            elif ch=='\\': escaped=True
            elif ch=='{': depth+=1
            elif ch=='}':
                depth-=1
                if depth==0 and i!=len(value)-1: return value
        if depth==0: return value[1:-1]
    if value[0]=='"' and value[-1]=='"': return value[1:-1]
    return value

def parse_bibtex(text: str) -> list[dict[str, str]]:
    """Parse common BibTeX entries; preserve unknown syntax for manual review."""
    entries=[]; position=0
    while True:
        at=text.find('@',position)
        if at<0: break
        match=re.match(r'@([A-Za-z]+)\s*([{(])',text[at:])
        if not match:
            position=at+1; continue
        entry_type=match.group(1).lower(); opener=match.group(2)
        body_start=at+match.end(); body_end=_entry_body_end(text,body_start,opener)
        if body_end is None:
            # Keep earlier complete entries, but do not silently invent a partial one.
            break
        body=text[body_start:body_end]
        position=body_end+1
        if entry_type in {'comment','preamble','string'}: continue
        fields_parts=_split_top_level(body)
        if not fields_parts: continue
        key=fields_parts[0].strip()
        if not key: continue
        entry={'type':entry_type,'key':key}
        for field in fields_parts[1:]:
            if '=' not in field: continue
            field_name,raw_value=field.split('=',1)
            name=field_name.strip().lower()
            if not re.fullmatch(r'[a-z][a-z0-9_-]*',name): continue
            entry[name]=re.sub(r'\s+',' ',_strip_outer(raw_value)).strip()
        entries.append(entry)
    return entries

def norm(s: str) -> str:
    s=s.lower()
    s=re.sub(r'\\[a-zA-Z]+\s*',' ',s)
    s=re.sub(r'[^a-z0-9]+',' ',s)
    return ' '.join(s.split())

def extract_doi(entry: dict[str,str]) -> str | None:
    raw=entry.get('doi','') or entry.get('url','')
    m=DOI_RE.search(raw)
    return m.group(0).rstrip('.,);]') if m else None

def crossref_lookup(doi: str, timeout: float=12.0) -> dict:
    url='https://api.crossref.org/works/'+quote(doi,safe='')
    req=Request(url,headers={'User-Agent':'ResearchForgeSkills/1.0 (public DOI metadata verification)'})
    with urlopen(req,timeout=timeout) as response:
        payload=json.loads(response.read().decode('utf-8'))
    msg=payload.get('message',{})
    titles=msg.get('title') or []
    authors=msg.get('author') or []
    return {'doi':msg.get('DOI',''),'title':titles[0] if titles else '',
            'first_author':authors[0].get('family','') if authors else '',
            'year':(msg.get('published-print') or msg.get('published-online') or msg.get('created') or {}).get('date-parts',[[None]])[0][0],
            'container':(msg.get('container-title') or [''])[0]}

def audit_entries(entries: list[dict[str,str]], offline: bool=False, delay: float=0.1) -> list[dict]:
    out=[]
    for e in entries:
        doi=extract_doi(e)
        row={'key':e['key'],'title':e.get('title',''),'doi':doi,'status':'no_doi','metadata_match':None,'registry':None}
        if not doi:
            row['status']='manual_lookup_required'; out.append(row); continue
        if offline:
            row['status']='not_checked_offline'; out.append(row); continue
        try:
            meta=crossref_lookup(doi)
            title_match=not e.get('title') or not meta.get('title') or norm(e['title'])==norm(meta['title'])
            author_match=True
            if e.get('author') and meta.get('first_author'):
                first=re.split(r'\s+and\s+|,',e['author'],maxsplit=1,flags=re.I)[0].strip()
                family=re.split(r'\s+',first)[-1].strip('{} ')
                author_match=norm(family)==norm(meta['first_author'])
            year_match=True
            if e.get('year') and meta.get('year'):
                y=re.search(r'\d{4}',e['year']); year_match=(not y or int(y.group())==int(meta['year']))
            row['registry']=meta
            row['metadata_match']=bool(title_match and author_match and year_match)
            row['status']='verified_metadata_match' if row['metadata_match'] else 'metadata_mismatch_review'
        except HTTPError as exc:
            row['status']='not_found_or_registry_error' if exc.code==404 else f'http_error_{exc.code}'
        except (URLError,TimeoutError,ValueError,KeyError) as exc:
            row['status']='lookup_unavailable'; row['error_type']=type(exc).__name__
        out.append(row)
        time.sleep(max(0.0,delay))
    return out

def main(argv=None) -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('bibtex',type=Path)
    ap.add_argument('--output',type=Path,help='Write JSON report to this path (default: stdout)')
    ap.add_argument('--offline',action='store_true',help='Parse references but do not send DOI lookups')
    ap.add_argument('--delay',type=float,default=0.1,help='Delay between Crossref requests in seconds (default: 0.1)')
    args=ap.parse_args(argv)
    if args.output and args.output.resolve()==args.bibtex.resolve():
        ap.error('--output must not overwrite the source bibliography')
    try: text=args.bibtex.read_text(encoding='utf-8')
    except OSError as exc: ap.error(str(exc))
    entries=parse_bibtex(text)
    if not entries:
        print('No BibTeX entries parsed.',file=sys.stderr); return 2
    report={'source_file':args.bibtex.name,'entry_count':len(entries),'mode':'offline' if args.offline else 'crossref','results':audit_entries(entries,args.offline,args.delay)}
    rendered=json.dumps(report,indent=2,ensure_ascii=False)+'\n'
    if args.output: args.output.write_text(rendered,encoding='utf-8')
    else: print(rendered,end='')
    return 0
if __name__=='__main__': raise SystemExit(main())
