"""Primary reviewer's p128 invariance and differential comparison audit."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='128';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p128}'
ev='LNM239 scan PDF p146 / printed p128: both complete 400-dpi halves and ten retained 800-dpi crops personally inspected, with five recropped to include full upper extents; all three complete source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=region('as-printed')
ch('corrected',old,new,'six spacing and two normalization events','II.p128.withdraw-normalizations','The six punctuation spaces, Module capitalization and Eilenberg- Zilber spacing are printed conventions, not necessary mathematical or grammatical repairs. Restore them; the distinctive respée reading is also retained.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p128.upright-Latin','The entire proof uses upright Latin letters and indices; all Greek exponents and subscripts are retained.')
 ch(layer,r'\xrightarrow{\ \sim\ }',r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}','Corollary 1.2.6.3 display','II.p128.unheaded-isomorphism','The original isomorphism bar has no arrowhead; evidence/I_p128_corollary-map.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 ch(layer,old,new,'proofs, remark and corollaries','II.p128.prose-continuity','The source introduced paragraphs at ordinary typewritten line wraps. Preserve the actual breaks at b), headings and displays.','structure')
 if layer=='English':
  ch(layer,r'\uline{respectively. Then the}',r'\uline{respectively}. \uline{Then the}','Corollary 1.2.6.5','II.p128.underline-stop','The period between the two sentences is not underlined; evidence/I_p128_last-corollary.png.')
 else:
  ch(layer,r'\uline{respectivement. Alors la flèche}',r'\uline{respectivement}. \uline{Alors la flèche}','Corollary 1.2.6.5','II.p128.underline-stop','The period between the two sentences is outside the underline; evidence/I_p128_last-corollary.png.')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p128.boundary','The page ends at canonique; the statement continues on p129.','structure')
for layer in ['corrected','English']:
 ch(layer,r"L_{B'/A'}\quad .",r"L^\Delta_{B'/A'}\quad .",'Corollary 1.2.6.3 display','II.p128.missing-diagonal','The print has no Delta (evidence/I_p128_corollary-map.png), but B prime and A prime are simplicial rings, so L without Delta is bisimplicial and is not an object of the stated D.(B prime). The proof explicitly ends with the diagonal L^Delta and constructs the claimed isomorphism to it (evidence/I_p128_proof-end.png). Add the necessary Delta only in corrected French/English.','misprint of the original')
ch('English','as we have seen','as seen above','identification of (iii)_n','II.p128.impersonal-on','The French comme on a vu is impersonal under the supplied standard. Authorial Montrons remains Let us now show.','terminology')
old=region('English');new=old.replace('termwise free','free degreewise')
ch('English',old,new,'two corollaries and remark','II.p128.degreewise','Use degreewise for the same terme à terme condition already used in Proposition 1.2.5.3. The earlier term index also renders the computation degree by degree. Whole-volume consistency remains subject to the required recurrence review.','terminology')
verdict(page,'ILL-SC-20260804-0125','Six punctuation-space changes; respée retained','All six changes withdrawn; respée confirmed; missing Delta newly corrected','The printed respée designates the resp. variant of the assertion and needs no invented expansion. The actual mathematical defect is the absent diagonal superscript in Corollary 1.2.6.3.',ev)
verdict(page,'ILL-NORM-20260804-0156','Eilenberg--Zilber and module normalization','Both withdrawn','Preserve the printed spacing and capitalization in corrected French because neither creates ambiguity.',ev)
verdict(page,'ILL-TX-20260804-0152','Nine semantic anchors and two display macros','All retained; upright notation, unheaded bar, underline stop, prose and boundary restored','The corollary display genuinely lacks Delta in print; diplomatic preserves it. All three Kunneth references were checked against the already reviewed statements on pp86,90,93 and are relevant.',ev)
verdict(page,'ILL-TR-20260804-0154','Invariance and comparison proofs','Meaning confirmed; diagonal correction, impersonal on and degreewise consistency applied','The English corresponding assertion correctly refers to the resp. variant. No proof step or hypothesis is omitted.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.2.6.2a.completion','Let Q and Q prime be the two polynomial Z-algebras in the final map on p127. They are degreewise free over Z, and Q->Q prime is a quasi-isomorphism. Thus the ordinary products A tensor_Z Q and A prime tensor_Z Q prime compute the derived products, so the two tensor factors can be changed through quasi-isomorphisms; these are the horizontal and vertical maps of (1.2.1.2.1). Their composite is (i)_n. For (iii)_n, formula (1.2.3.3.1) is B tensor_Z Z^(P_A(B)_(n-1)) and its primed counterpart: the free-abelian factors are flat, their map is a quasi-isomorphism by the checked Whitehead application, and B->B prime is a quasi-isomorphism. The same derived-tensor argument applies. For (ii)_n replace B by the already checked P_A(B)_n and use the universal free basis for differentials. The cited I 3.3.5.2 and I 3.3.2.6 have exactly these flat-representative properties.'),('II.1.2.6.2b','The rowwise quasi-isomorphism of L gives a quasi-isomorphism on the diagonal by the first-quadrant bicomplex spectral sequence and Eilenberg--Zilber, as on p126. Since L^Delta is degreewise free over B, the map L^Delta -> L^Delta tensor_B B prime is a quasi-isomorphism for the quasi-isomorphism B->B prime, by I 3.3.4.6. Its composite with the base-change comparison is the first diagonal map; two-out-of-three proves the resp. variant.'),('II.1.2.6.3-and-1.2.6.4','Degreewise freeness of B over A implies both that L^Delta->Omega(B/A) is a quasi-isomorphism (1.2.5.3) and that Omega(B/A) is degreewise free over B. Both sides therefore compute their derived base changes along B->B prime, so tensoring this comparison with B prime preserves the quasi-isomorphism. The span Omega(B/A) tensor_B B prime <- L^Delta tensor_B B prime -> L^Delta_(Bprime/Aprime) has both arrows quasi-isomorphisms, giving the canonical isomorphism in D.(B prime). This proves the necessity of Delta in the conclusion and the sufficiency of the two weaker hypotheses in Remark 1.2.6.4. The latter are exactly the only uses of degreewise freeness in the argument.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p128_*.png')):f.write(f'| evidence/{p.name} | Printed p128, 800-dpi crop inspected during the first reading. |\n')
print('Page 128 edits and three proof checks recorded.')
