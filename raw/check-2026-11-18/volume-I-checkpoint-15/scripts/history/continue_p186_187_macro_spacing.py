"""Primary local typesetting follow-up; run once after pages186-188."""
import sys
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page
for page,names in [('186',['IllusieProblemSquareLowerArrowPOneEightySix']),('187',['IllusieFlatTorsorGroupPOneEightySeven','IllusieFlatAutomorphismExtPOneEightySeven'])]:
 anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p'+page+'}'
 for layer in LAYERS:
  for name in names:
   old='\\'+name+('\n(' if page=='186' else ' (')
   new='\\'+name+'{} ('
   evidence='Primary typesetting follow-up: keep an explicit word boundary after the no-argument inline carrier when joining its former false paragraph; otherwise TeX consumes the whitespace after the control word. Printed separating space personally inspected in evidence/I_p186_opening.png or evidence/I_p187_torsor.png and evidence/I_p187_automorphisms.png as applicable. No mathematical or lexical change.'
   edit_page(layer,anchor,old,new,page,'inline carrier boundary','III.p'+page+'.inline-carrier-space',evidence,'typesetting')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'CHECK_RECORD.md').open('a') as f:f.write('\n### Typesetting follow-up after page188 — '+now+'\n\nExplicit spaces after three inline formula carriers on pp.186–187 were retained by terminating their TeX control words with empty braces. This prevents whitespace consumption after joining the already-reviewed continuous prose. Nine immediate correction rows record the three-layer changes; no new page completion or mathematical check is inferred.\n')
print('Recorded nine explicit inline-carrier spaces on186-187.')
