"""Validate manuscript/bibliography/source-ledger consistency (no network needed)."""
import json
import re
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
text = '\n'.join(p.read_text(encoding='utf-8') for p in [ROOT/'paper.tex', *sorted((ROOT/'sections').glob('*.tex'))])
cited = {key.strip() for group in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', text) for key in group.split(',')}
bib = (ROOT/'refs.bib').read_text(encoding='utf-8')
keys = re.findall(r'@(?!(?:comment|string|preamble|IEEEtranBSTCTL)\b)\w+\s*\{\s*([^,]+),', bib, re.I)
ledger = json.loads((ROOT/'research'/'source_audit.json').read_text(encoding='utf-8'))
records = {r['key']:r for r in ledger['sources']}
errors=[]
if len(keys)!=len(set(keys)):errors.append('Duplicate BibTeX keys')
if cited-set(keys):errors.append('Missing BibTeX entries: '+str(sorted(cited-set(keys))))
if set(keys)-cited:errors.append('Uncited BibTeX entries: '+str(sorted(set(keys)-cited)))
if cited-set(records):errors.append('Missing source records: '+str(sorted(cited-set(records))))
for k in cited & records.keys():
    if not records[k].get('url','').startswith('https://'):errors.append('Missing primary URL: '+k)
    if not records[k].get('title') or not records[k].get('authors'):errors.append('Incomplete metadata: '+k)
    block=re.search(r'@\w+\s*\{'+re.escape(k)+r',.*?(?=\n\s*@|\Z)',bib,re.S)
    year=re.search(r'\byear\s*=\s*[{\"]?(\d{4})',block.group(0),re.I) if block else None
    if not year or str(records[k]['year'])!=year.group(1):errors.append('Bibliography/ledger year mismatch: '+k)
for filename in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',text):
    if not (ROOT/filename).exists():errors.append('Missing figure '+filename)
labels=re.findall(r'\\label\{([^}]+)\}',text)
refs=re.findall(r'\\(?:ref|eqref)\{([^}]+)\}',text)
if len(labels)!=len(set(labels)):errors.append('Duplicate labels')
if set(refs)-set(labels):errors.append('Undefined labels '+str(set(refs)-set(labels)))
if re.search(r'\b(?:TODO|FIXME|TBD)\b',text):errors.append('Unresolved drafting marker')
coverage_path=ROOT/'research'/'spreadsheet_coverage.csv'
if coverage_path.exists():
    with coverage_path.open(encoding='utf-8-sig',newline='') as stream:
        coverage=list(csv.DictReader(stream))
    if len(coverage)!=81 or len({r['excel_row'] for r in coverage})!=81:
        errors.append('Supplementary literature list must contain 81 unique mapped rows')
    for row in coverage:
        if row['citation_key'] not in cited:
            errors.append('Literature-list record not cited: '+row['excel_row'])
for heading in ['Scope, Retrieval, and Evidence Boundaries',
                'Data, Code, and Manuscript Preparation',
                'Limitations of This Survey']:
    if heading in text:errors.append('Removed process section returned: '+heading)
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(cited)} cited sources, {len(set(keys))} bibliography entries, {len(labels)} unique labels, all figure files present.')
print('This is a structural consistency check, not an independent replication or proof of claim correctness.')
