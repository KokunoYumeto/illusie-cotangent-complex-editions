"""Primary reviewer's page159 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='159';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p159}'
ev='LNM239 scan PDF p177 / printed p159: both complete400-dpi halves and nine800-dpi crops personally inspected; all three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('C-module','C-Module').replace('A-algèbre','A-Algèbre').replace(r'$P^1_{C/A}$-module',r'$P^1_{C/A}$-Module')
ch('corrected',old,new,'prose and note','III.p159.withdraw-capitalizations','Withdraw five optional capitalization normalizations.','reading')
for layer in ['corrected','English']:
 ch(layer,r'\mathcal Y\longmapsto\operatorname{alg}(\mathcal Y)',r'\mathcal Y\longmapsto\operatorname{Alg}(\mathcal Y)','functor name','III.p159.retain-Alg','The print has Alg in the functor sentence and alg in the displayed definitions. This harmless capitalization variation is not a necessary mathematical correction: the construction is unambiguous. Withdraw the unsupported uniformization.','reading')
for layer in LAYERS:
 old=region(layer);assert old.count(r'\ReflowBodyFont ')==2
 ch(layer,old,old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath'),'body and footnote mathematics','III.p159.upright-Latin','Restore upright printed Latin mathematical letters, including macro-defined formula carriers.')
 old=region(layer);assert old.count(r'\mathcal X')==3 and old.count(r'\mathcal Y')==6
 ch(layer,old,old.replace(r'\mathcal X','X').replace(r'\mathcal Y','Y'),'extension names','III.p159.plain-extension-names','Restore plain X and Y, with the printed prime retained; these letters are not calligraphic.')
 ch(layer,r'd^1_{C/A}(x)',r'd_{C/A}(x)','right structure formula','III.p159.derivation-degree','The enlarged right-structure line prints d with subscript C/A and no superscript1. The degree-free notation is valid for the universal derivation. Remove the unprinted exponent in all layers.','reading')
 old=region(layer);assert old.count(r'\textsuperscript{(1)}')==2
 new=old.replace(r'$I$\textsuperscript{(1)}',r'$I$ (\textsuperscript{1})').replace(r'\textsuperscript{(1)} $I$',r'(1) $I$')
 ch(layer,old,new,'body call and footnote label','III.p159.note-markers','The body has baseline parentheses around a raised1; the footnote itself has a baseline (1). Preserve that distinction, shown by the principal-parts and footnote crops.')
 old=region(layer);note=r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:1:8:Y-prime:n1}'
 new=old.replace(note,r'\vfill'+'\n'+note)+r'\clearpage'+'\n'
 ch(layer,old,new,'footnote position and page boundary','III.p159.foot-and-boundary','Keep the note at the page foot and retain the printed page boundary; the existing prose already follows continuous paragraphs.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p159','Five capitalized terms; Alg in the functor sentence; d^1 in supplied transcription','Optional term normalizations and Alg->alg; same added exponent','Local source-comparison verdict, not a supplied decision-record ID. Withdraw all five capitalization normalizations and the unsupported Alg uniformization. The printed capitalized functor name is unambiguous despite lowercase alg in the displays. Remove the shared unprinted derivation exponent in all layers. No necessary correction of the original found.',ev+'evidence/I_p159_right-structure.png; evidence/I_p159_alg-pullback.png; evidence/I_p159_footnote.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.7.3.diff-additivity','For C satisfying(L), every algebra extension gives an exact conormal extension. A morphism of algebra extensions induces a commutative conormal diagram. For a kernel map I->J and its algebra pushout, the induced map from the module pushout of the conormal extension to the new conormal extension is the identity on J and Omega_C/A; exactness therefore makes it an isomorphism. Similarly, for the fiber product of two algebra extensions, the conormal map into the fiber product of their conormal extensions is the identity on I1 direct-sum I2 and Omega_C/A, hence an isomorphism. Since Baer sum is fiber product followed by kernel addition, diff preserves it and induces the natural group homomorphism1.1.7.3.'),('III.1.1.8.alg-construction-additivity','Give C direct-sum J the square-zero multiplication (c,j)(cprime,jprime)=(ccprime,c jprime+cprime j). C-linearity of f makes id direct-sum f a surjective A-algebra map to C direct-sum Omega_C/A, with kernel (0,i(I)), whose square is zero. The map j2 sends x to (x,dx); Leibniz and d(A)=0 make it an A-algebra map. Its pullback is the algebra of pairs (x,j) satisfying f(j)=dx, with the same multiplication; it is an extension of C by I with the stated C-module action. Morphisms of module extensions induce morphisms of these algebras. Module pushout in I gives the corresponding algebra pushout by the canonical map, which is an isomorphism on kernel and quotient, and fiber products are preserved by the same explicit pair description. Thus the construction respects Baer addition and gives1.1.8.2, for arbitrary C, without imposing(L).')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p159_*.png')):f.write(f'| evidence/{p.name} | Page159 audit:800-dpi crop personally inspected; lower-page crop coordinates corrected before review. |\n')
print('Page159 edits, verdict and two proof checks recorded.')
