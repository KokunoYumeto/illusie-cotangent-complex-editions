"""Primary reviewer's page150 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='150';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p150}'
ev='LNM239 scan PDF p168 / printed p150: both complete400-dpi halves (lower half blank), four800-dpi formula/prose crops and one1600-dpi punctuation crop personally inspected. All three source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old,new in [(r'$U\ni x$,',r'$U\ni x$ ,'),(r'$V\ni y$,',r'$V\ni y$ ,'),(r'$f(U)\subset W$,',r'$f(U)\subset W$ ,')]:
 ch('corrected',old,new,'indexing clause','II.p150.withdraw-spacing','Withdraw optional comma-space normalization.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','II.p150.upright-Latin','Printed Latin mathematical letters are upright.')
 old=region(layer);assert old.count(r'\mathcal O')==18
 ch(layer,old,old.replace(r'\mathcal O',r'\underline{\mathrm{O}}'),'eighteen structure-sheaf symbols','II.p150.structure-sheaves','All eighteen structure-sheaf symbols are upright underlined O; all their subscripts remain outside the underline.')
 ch(layer,r'\mathcal T\!or_i^S',r'\underline{\operatorname{Tor}}_i^S','second formula','II.p150.sheaf-Tor','The sheaf Tor operator is upright and underlined, with i,S outside the underline.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 ch(layer,old,new,'indexing clause','II.p150.prose-continuity','Join the printed line wrap in the single indexing sentence.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p150.boundary','Retain the page boundary and the substantial printed blank remainder.','structure')
ch('English','the direct limit being taken','the inductive limit being taken','indexing clause','II.p150.inductive-limit','Use the established translation inductive limit for limite inductive.','terminology')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p150','Three comma spaces; omitted tensor base','Three normalized comma spaces; same omitted tensor base','Local source-comparison verdict, not a supplied decision-record ID. Withdraw the optional spaces. Retain the omitted tensor base as determinate shorthand for O(X,x) tensor_{O(S,s)} O(Y,y); no original mathematical correction is needed. The faded first terminal punctuation is retained provisionally as semicolon and logged for second reading.',ev+'evidence/I_p150_indexing.png; evidence/I_p150_sheaf-Tor.png; evidence/I_p150_first-punctuation-1600.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.3.12.three-comparisons','Stalk inverse image is exact and preserves tensor products and flatness, giving the first formula Tor over h^{-1}O_S at z = Tor over O(S,s) of O(X,x),O(Y,y). Set R=O(X,x) tensor_{O(S,s)}O(Y,y). The local ring O(Z,z) is the corresponding localization of R, so flat localization of the affine Tor module gives the second formula; its unlabelled tensor is over R. The triples of affine neighborhoods U,V,W with f(U),g(V) contained in W form a filtered neighborhood basis. Their coordinate rings and modules have colimits O(S,s),O(X,x),O(Y,y). Functorial free resolutions and exactness of filtered colimits give the third Tor/inductive-limit formula, including variation of the coefficient ring.'),('II.2.3.12.vanishing-equivalence','The forward implication follows by tensoring the vanishing stalk Tor groups in the second formula. For the converse, suppose the quasi-coherent sheaf Tor_i^S vanishes on Z for i>0. On each affine product U times_W V its associated module is Tor_i^{O_S(W)}(O_X(U),O_Y(V)), which must vanish because the affine associated-sheaf functor is faithful. Taking the filtered limit in the third displayed formula gives every raw stalk Tor group zero, hence the sheaf in2.3.11 is zero. This proves the asserted global equivalence without incorrectly treating any single localization R->O(Z,z) as faithfully flat. The EGA/SGA exact bibliography locators were not independently consulted.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'READING_QUESTIONS.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['I-Q017','150','II.2.3.12 first Tor comparison','The terminal mark is faint: the1600-dpi crop does not securely distinguish semicolon from colon.','Retain the supplied semicolon provisionally; no mathematical claim depends on this mark.','first reading retained; second reading pending','evidence/I_p150_stalk-Tor.png; evidence/I_p150_first-punctuation-1600.png'])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p150_*.png')):f.write(f'| evidence/{p.name} | Page150 audit:personally inspected at the resolution in the filename, otherwise800dpi; first terminal punctuation remains provisional. |\n')
print('Page150 edits, verdict, two proof checks and punctuation question recorded.')
