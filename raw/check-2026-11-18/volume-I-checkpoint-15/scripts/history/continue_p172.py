"""Primary reviewer's page172 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='172';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p172}'
ev='LNM239 scan PDF p190 / printed p172: both complete400-dpi halves, fifteen800-dpi detail crops and a1600-dpi right-edge crop personally inspected. The diamond-label crop was expanded and reinspected to include the complete lower indices. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old,new in [("d'anneaux","d'Anneaux"),('$B$-algèbre','$B$-Algèbre')]:ch('corrected',old,new,'prose','III.p172.withdraw-capitalization','Withdraw optional capitalization normalization. evidence/I_p172_opening.png; evidence/I_p172_caption.png.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p172.upright-Latin','Restore printed upright Latin mathematics.')
 ch(layer,r'\draw[->] (187,70) -- (187,49);',r'\draw[|->] (187,70) -- (187,49);','first diagram element assignment','III.p172.mapsto-bar','The vertical element-assignment arrow has a printed initial bar. Restore it without changing the other arrows. evidence/I_p172_ring-map.png.','reading')
 old=region(layer);new=old.replace(r'    \node[anchor=west] at (0,58) {$(*)$};'+'\n','').replace(r'    \node[anchor=west] at (0,76) {$(**)$};'+'\n','')
 for target,newline in [(r'    \node (bb) at (74,58) {$B$};',r'    \node[anchor=base west] at ([xshift=-74bp]bb.base) {$(*)$};'),(r'    \node (tzl) at (66,85) {$0$};',r'    \node[anchor=base west] at ([xshift=-66bp]tzl.base) {$(**)$};')]:new=new.replace(target,target+'\n'+newline)
 ch(layer,old,new,'diagram tags','III.p172.tag-baselines','Align(*) with B and(**) with the upper-row initial zero, as printed. evidence/I_p172_diamond-tag.png; evidence/I_p172_morphism-tag.png.')
 ch(layer,r'\node[anchor=west] at (345,8) {$,$};',r'\node[anchor=base west] at ([xshift=30bp]bzr.base east) {$,$};','last diagram comma','III.p172.comma-baseline','Place the comma after the final zero on its baseline with the printed separation. evidence/I_p172_morphism-bottom.png.')
 if layer=='English':
  ch(layer,'is regarded as a\n\\par\n\\noindent $B$-algebra','is regarded as a $B$-algebra','final caption','III.p172.false-paragraph','Join the continuous final sentence.','structure')
 else:
  s=region(layer);line=next(x for x in s.splitlines() if x.startswith(r'\noindent\makebox[0pt][l]{{où '))
  new=line[len(r'\noindent\makebox[0pt][l]{{'):-2]
  ch(layer,line,new,'final caption','III.p172.false-prose-box','Remove the zero-width box around continuous prose so the caption can reflow. Preserve every word, resp. and all formulas. The source terminal period is retained provisionally because it lies beyond the clipped scan edge (Q019).','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p172.page-boundary','Preserve the printed page boundary.','structure')
ch('English','We have','One has','sigma lead','III.p172.impersonal-on','French On a is impersonal.','translation')
for i in range(2):
 old=region('English');ch('English',old,old.replace('respectively','resp.',1),'final caption','III.p172.resp','Retain the source abbreviation resp.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p172','Anneaux; B-Algèbre','anneaux; B-algèbre','Withdraw both optional capitalization normalizations. No original mathematical error identified. Restore the missing mapsto bar and printed diagram tag/punctuation baselines, upright Latin mathematics and continuous final prose. Preserve the minus sign, factor order, epsilon/sigma labels and both resp. abbreviations. Final period is retained without a decision because the scan clips the right edge.',ev+'evidence/I_p172_ring-map.png; evidence/I_p172_sigma.png; evidence/I_p172_caption-edge1600.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.6.5.proof.flip','targeted proof check','The map x tensor y tensor z |-> z tensor y tensor x respects the balancing relations: the C-action on the first B-factor of the upper tensor product becomes the last B-factor action on the lower tensor product. It is an involutive A-algebra isomorphism, commutes with both maps from B and both product maps to C, and sends the diagonal ideal to the diagonal ideal. Thus it descends modulo the square of that ideal to the displayed sigma map in(*).'),('III.1.2.6.5.proof.kernel-sign','targeted proof check','Using d(y)=1 tensor y-y tensor1, the flip sends x tensor d(y) to y tensor1 tensor x-1 tensor y tensor x=-d(y) tensor x. Hence the map on the differential kernel is minus the canonical tensor symmetry, written -id after that identification. The quotient map is id_C, so(**) is a commutative morphism of B-extensions with exactly the displayed signs and structures 1 tensor j2 / j1 tensor1. This checks the author proof through172; its continuation on173 remains unread.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'READING_QUESTIONS.tsv').open('a',newline='') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['Q019','172','III.1.2.6.5.final-caption','The authority scan clips the closing parenthesis at the right edge of the final caption; a following period cannot be seen even at1600dpi.','Retain the supplied terminal period provisionally; do not infer its absence from the clipping.','Open; no low-confidence change applied.','evidence/I_p172_caption.png; evidence/I_p172_caption-edge1600.png'])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p172_*.png')):f.write(f'| evidence/{p.name} | Page172 audit: final800-dpi detail or1600-dpi edge crop personally inspected. |\n')
print('Page172 repairs, verdict, Q019 and two proof checks recorded.')
