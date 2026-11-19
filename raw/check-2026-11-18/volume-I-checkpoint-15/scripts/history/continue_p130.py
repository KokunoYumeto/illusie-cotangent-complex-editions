"""Primary reviewer's p130 derived-functor and adjunction audit."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='130';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p130}'
ev='LNM239 scan PDF p148 / printed p130: both complete 400-dpi halves and ten 800-dpi crops personally inspected; all three full source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
with (ROOT/'CORRECTIONS.tsv').open(newline='') as f:
 done={(r['layer'],r['statement']) for r in csv.DictReader(f,delimiter='\t') if r['printed_page']==page}
def ch(layer,old,new,line,sid,why,kind='typesetting'):
 if (layer,sid) not in done:edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=region('as-printed').replace('parcout les','parcourt les').replace('surjectif dégré','surjectif degré')
ch('corrected',old,new,'Scholium, dual-number paragraph, proposition and proof','II.p130.withdraw-normalizations','Withdraw eleven punctuation/reference-spacing changes and two capitalization changes. Retain parcout -> parcourt and degre with the erroneous first acute removed: both original spelling errors are visible in evidence/I_p130_constancy.png and require grammatical/orthographic repair.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p130.upright-Latin','The print uses upright Latin symbols, including the indexed module and algebra categories. Both displayed isomorphisms have arrowheads and are retained as arrows.')
 ch(layer,r"\text{``}\!\varprojlim\!\text{''}",r'\text{\textquotedbl{}}\!\varprojlim\!\text{\textquotedbl{}}','pro-object display','II.p130.straight-quotes','The projective-limit notation uses straight double quotation marks; evidence/I_p130_pro-object.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 middle=r'\phantomsection\hypertarget{illusie:I:ch1:p130:cotangent-complex-derived-notation}{}%'
 new=new.replace('\\par\n'+middle+'\n\\noindent ','\n'+middle+'\n')
 ch(layer,old,new,'Scholium and proposition prose','II.p130.prose-continuity','Ordinary typewritten wraps were converted into paragraphs, including the middle of the sentence before the cotangent notation anchor. Join them while retaining that anchor, the genuine new indented paragraph, and all displays.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p130.boundary','The page ends after the ordinary dual-number adjunction (*); the proof continues on p131.','structure')
verdict(page,'ILL-SC-20260804-0127','Thirteen existing events','Two spelling repairs confirmed; eleven spacing changes withdrawn','Parcout lacks the necessary r of parcourt; degre has an erroneous acute on its first e in print. All other events merely normalize printed spaces.',ev)
verdict(page,'ILL-NORM-20260804-0158','Two capitalization changes','Both withdrawn','A-Algebre and Algebre are conventional printed capitals and are retained.',ev)
verdict(page,'ILL-TX-20260804-0154','Nine semantic anchors and three display calls','All retained; upright Latin, straight quotes, prose and boundary restored','The pro-object index is C prime -> C, both differential exponents are 1, both cotangent superscripts are Delta, and both isomorphism bars genuinely have arrowheads.',ev)
verdict(page,'ILL-TR-20260804-0156','Scholium conclusion and Proposition 1.2.6.7 opening','Meaning confirmed; no meaning or terminology edit necessary','Left derived functor, right fractions, essentially constant, the dual-number construction, and both Hom formulas agree with corrected French. The proposition proof continues on the next page.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.2.6.6.left-derived','For each quasi-isomorphism C prime -> C with C prime fibrant over B, the canonical resolution P_A^Delta(C prime)->C prime is again an admissible quasi-isomorphism: it is surjective degreewise and hence fibrant, so its composite to B is fibrant. These replacements refine the indexing system by algebras free degreewise over A. On that subsystem 1.2.5.3 compares differentials with the diagonal cotangent complex, and 1.2.6.5 makes the transition maps quasi-isomorphisms. Tensoring the comparisons with B is justified by degreewise freeness of both differential and cotangent modules. The common value is L^Delta(C/A) tensor_C B by 1.2.6.2. Thus the pro-object is essentially constant and the cited criterion I 1.4.4 yields the left derived functor. The already reviewed definitions on pp14 and62 were reread; retained crops of their notation and relative category were inspected again.'),('II.1.2.6.7.dual-number-functor','As an underlying simplicial abelian sheaf, the square-zero algebra B plus M is the direct sum B direct-sum M. For a quasi-isomorphism M->M prime, the induced map is id_B direct-sum f. Normalization preserves finite sums and its homology is the direct sum of the two homologies. Hence the induced algebra map is a quasi-isomorphism and the construction descends to the localized categories.'),('II.1.2.6.7.ordinary-adjunction-star','Fix the structure map g:C->B. A map of A-algebras over B from C to B plus F has the form c |-> (g(c),d(c)). The square-zero multiplication says exactly d(cc prime)=g(c)d(c prime)+g(c prime)d(c), with d zero on A. Thus these maps are A-derivations C->F, represented by Hom_C(Omega(C/A),F), which tensor-Hom adjunction identifies with Hom_B(Omega(C/A) tensor_C B,F). These assignments commute with the simplicial operators and with maps in C,F, proving the printed canonical functorial bijection (*). This checks the opening step, not the still-continuing derived adjunction proof.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p130_*.png')):f.write(f'| evidence/{p.name} | Printed p130, 800-dpi crop inspected during the first reading. |\n')
print('Page 130 edits and three targeted proof checks recorded.')
