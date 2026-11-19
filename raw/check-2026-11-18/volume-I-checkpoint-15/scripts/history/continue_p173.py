"""Primary reviewer's page173 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='173';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p173}'
ev='LNM239 scan PDF p191 / printed p173: both complete400-dpi halves and fourteen800-dpi detail crops personally inspected; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old,new in [("d'anneaux","d'Anneaux"),('$B$-algèbres','$B$-Algèbres'),('$B$-algèbre par','$B$-Algèbre par')]:ch('corrected',old,new,'prose','III.p173.withdraw-capitalization','Withdraw optional capitalization normalization.','reading')
for old,new in [('$j_1$,','$j_1$ ,'),(r'\partial(d_{B/A}\otimes1)$.',r'\partial(d_{B/A}\otimes1)$ .'),(r'\IllusiePrincipalPartsMorphismPOneSeventyThree{,}',r'\IllusiePrincipalPartsMorphismPOneSeventyThree{\hspace{3.0bp},}'),(r'\IllusiePrincipalPartsLemmaDiagramPOneSeventyThree{,}',r'\IllusiePrincipalPartsLemmaDiagramPOneSeventyThree{\hspace{3.0bp},}'),(r'\IllusiePrincipalPartsCanonicalSequencePOneSeventyThree{).}',r'\IllusiePrincipalPartsCanonicalSequencePOneSeventyThree{\hspace{3.0bp})\hspace{3.0bp}.}')]:ch('corrected',old,new,'prose/display punctuation','III.p173.withdraw-punctuation-spacing','Withdraw optional punctuation-spacing normalization. evidence/I_p173_proof-top.png; evidence/I_p173_proof-opposite.png; evidence/I_p173_morphism.png; evidence/I_p173_lemma-bottom.png; evidence/I_p173_canonical-sequence.png.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p173.upright-Latin','Restore upright printed Latin mathematics.')
 for i in range(2):
  old=region(layer);ch(layer,old,old.replace('(***)','(**)',1),'proof reference','III.p173.two-star-reference','The print has two stars in both references, pointing to diagram(**) on172. All supplied source layers add a third star. evidence/I_p173_proof-top.png; evidence/I_p173_proof-opposite.png.','reading')
 ch(layer,r'\draw[->] (181,65) -- (181,47);',r'\draw[|->] (181,65) -- (181,47);','element assignment','III.p173.mapsto-bar','Restore the printed initial bar on the vertical element-assignment arrow. evidence/I_p173_ring-map.png.','reading')
 old=region(layer);new=old.replace('(tpp.south) -- (bca.north);','(tpp.south) -- (tpp.south |- bca.north);').replace('(tcc.south) -- (bcb.north);','(tcc.south) -- (tcc.south |- bcb.north);')
 ch(layer,old,new,'lemma diagram','III.p173.vertical-comparison-arrows','Restore the two vertical comparison arrows while preserving the printed left-edge alignment of the unequal lower formulas. evidence/I_p173_lemma-arrows.png; evidence/I_p173_lemma-top.png; evidence/I_p173_lemma-bottom.png.')
 ch(layer,r'\binom{\mathrm{id}}{d_{C/B}}',r'\left(\begin{array}{l}\mathrm{id}\\[9bp]d_{C/B}\end{array}\right)','right vertical label','III.p173.two-row-label','Restore the tall, left-aligned two-row label, retaining id and the subscript C/B. evidence/I_p173_lemma-arrows.png.')
 ch(layer,r'\node[anchor=west] at (330,4) {#1};',r'\node[anchor=base west] at ([xshift=10bp]bzr.base east) {#1};','lemma diagram comma','III.p173.comma-baseline','Restore the comma after the lower terminal zero on its baseline. evidence/I_p173_lemma-bottom.png.')
 if layer=='English':
  ch(layer,r'\uline{$B$-linear diagram}',r'$B$-\uline{linear diagram}','lemma heading','III.p173.underline-scope','The B-prefix is outside the printed underline. evidence/I_p173_lemma-heading.png.')
  ch(layer,'that had\\par\n\n\\noindent to be proved.','that had to be proved.','proof conclusion','III.p173.false-proof-paragraph','Join the continuous sentence across a printed line wrap.','structure')
  ch(layer,'(1.2.6.4)\\par\n\n\\noindent (respectively','(1.2.6.4) (respectively','lemma conclusion','III.p173.false-lemma-paragraph','Join continuous prose before the final display.','structure')
 else:
  ch(layer,r'\uline{$B$-linéaire}',r'$B$-\uline{linéaire}','lemma heading','III.p173.underline-scope','The B-prefix is outside the printed underline. evidence/I_p173_lemma-heading.png.')
  ch(layer,"qu'il\\par\n\n\\noindent fallait démontrer.","qu'il fallait démontrer.",'proof conclusion','III.p173.false-proof-paragraph','Join the continuous sentence across a printed line wrap.','structure')
  ch(layer,'(1.2.6.4)\\par\n\n\\noindent (resp.','(1.2.6.4) (resp.','lemma conclusion','III.p173.false-lemma-paragraph','Join continuous prose before the final display.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p173.page-boundary','Preserve the printed page boundary.','structure')
ch('English','we indeed obtain','one indeed obtains','proof conclusion','III.p173.impersonal-on','French on a is impersonal; the opening passive and There is in the lemma already follow this rule.','translation')
for i in range(2):
 old=region('English');ch('English',old,old.replace('respectively','resp.',1),'lemma conclusion','III.p173.resp','Retain the printed abbreviation resp.','translation')
for old,new in [(r'\IllusiePrincipalPartsMorphismPOneSeventyThree{,}',r'\IllusiePrincipalPartsMorphismPOneSeventyThree{\hspace{3.0bp},}'),(r'\IllusiePrincipalPartsLemmaDiagramPOneSeventyThree{,}',r'\IllusiePrincipalPartsLemmaDiagramPOneSeventyThree{\hspace{3.0bp},}'),(r'\IllusiePrincipalPartsCanonicalSequencePOneSeventyThree{).}',r'\IllusiePrincipalPartsCanonicalSequencePOneSeventyThree{\hspace{3.0bp})\hspace{3.0bp}.}')]:ch('English',old,new,'display punctuation','III.p173.English-formula-agreement','Match English display punctuation/spacing to corrected French and print.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p173','Printed capitalization and spacing','Three capitalization and five spacing normalizations','Withdraw the optional normalizations. Restore the two-star references and missing mapsto bar in all layers. No original mathematical error identified. A-extension in the opening is printed and remains true for the underlying A-extension; the explicit maps establish the stronger B-extension compatibility, so no change of A to B is necessary.',ev+'evidence/I_p173_proof-top.png; evidence/I_p173_proof-opposite.png; evidence/I_p173_ring-map.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.6.5.proof.completed','targeted proof check','In j1 coordinates the upper extension of172 has B-map b |-> (f(b),1 tensor d(b)), the opposite of partial(d tensor1), whose B-map has negative derivation. The sigma comparison has -id on the kernel and id on the quotient, so the lower principal-parts extension is the opposite of the upper and hence canonically partial(d tensor1). This completes the author proof and agrees with the independent direct comparison on171. The references are(**), as printed. The term A-extension is true upon restriction and does not require an editorial substitution.'),('III.1.2.6.6.construction','targeted proof check','The displayed algebra map on triple tensors is x tensor y tensor z |-> f(x) tensor f(y)z. It respects balancing and sends the diagonal ideal from B into the diagonal ideal from C, so descends to principal parts. Identifying P1_C/A with C plus Omega1_C/A via its first splitting gives the explicit map [x tensor y tensor z] |-> (f(x)f(y)z, f(x)d(f(y)z)). For b tensor1 tensor1 it gives(f(b),0), verifying the stated B-algebra structure and formula1.2.6.6.'),('III.1.2.6.7.diagram','targeted proof check','On d_B/A(b) tensor c, the formula1.2.6.6 gives(0,c d_C/A(f(b))), so the left square commutes with positive identity on the differential module. Applying id plus j to its second component gives f(x)f(y)d_C/B(z)=d_C/B(f(x)f(y)z), verifying the right square with the column(id,d_C/B). That column is B-linear since d_C/B kills B. The lower row is exact because its kernel is0 plus ker(j), the image of Omega1_B/A tensor C, and j is surjective. Personally reinspected II1.1.2.12 on117; it is exactly the cited differential sequence. The author proof of this lemma on174 remains unread.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p173_*.png')):f.write(f'| evidence/{p.name} | Page173 audit:800-dpi crop personally inspected. |\n')
 f.write('| evidence/I_p117_transitivity.png | Personally reinspected for173: exact reference II1.1.2.12. |\n')
print('Page173 repairs, verdict and three checks recorded.')
