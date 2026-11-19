"""Update mechanical edit totals; never infer visual review or proof completion."""
import collections,csv,re
from pathlib import Path
root=Path(__file__).resolve().parent.parent
with (root/'CORRECTIONS.tsv').open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
counts=collections.Counter((r['layer'],r['kind']) for r in rows)
kinds=['reading','misprint of the original','translation','typesetting','structure','terminology']
unknown_kinds=collections.Counter(r['kind'] for r in rows if r['kind'] not in kinds)
if unknown_kinds:
    details=', '.join(f'{kind!r}: {count}' for kind,count in sorted(unknown_kinds.items(),key=lambda item:repr(item[0])))
    raise ValueError('Unknown CORRECTIONS.tsv kind values; CHECK_RECORD.md was not changed: '+details)
lines=['<!-- live-totals-start -->','These are current first-reading edit-row totals, not final certified error counts. A row may restore several instances within one explicitly identified source span.','', '| Layer | '+' | '.join(kinds)+' | Total |','|---|'+'---:|'*(len(kinds)+1)]
for layer in ['as-printed','corrected','English','build']:
 ns=[counts[layer,k] for k in kinds]
 lines.append('| '+layer+' | '+' | '.join(map(str,ns))+' | '+str(sum(ns))+' |')
lines+=['',f'Total recorded changes: **{len(rows)}**. Second visual readings remain pending. No-difference page counts will be consolidated from the page findings; absence of an edit does not establish absence of a difference.','<!-- live-totals-end -->']
section='\n'.join(lines)
p=root/'CHECK_RECORD.md';s=p.read_text()
if '<!-- live-totals-start -->' in s:s=re.sub(r'<!-- live-totals-start -->[\s\S]*?<!-- live-totals-end -->',lambda m:section,s)
else:s=s.replace('## Status and totals\n','## Status and totals\n\n'+section+'\n')
p.write_text(s)
print(f'Updated mechanical totals for {len(rows)} rows.')
