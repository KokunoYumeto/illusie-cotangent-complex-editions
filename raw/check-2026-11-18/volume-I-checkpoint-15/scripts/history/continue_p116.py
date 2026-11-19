"""Primary reviewer's p116 notation, layout and targeted algebra checks."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='116';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p116}'
ev='LNM239 scan PDF p134 / printed p116: both full 400-dpi halves and eleven 800-dpi crops personally inspected; all three full source regions and four prior entries read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
def left(num,formula):return r'\ReflowDisplay{}{\hbox to\linewidth{\text{('+num+r')}\hfill$\displaystyle '+formula+r'$\hfill\phantom{\text{('+num+')}}}}'
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','whole page','II.p116.upright-Latin','The mathematical Latin letters and indices are upright in the print.')
 old=r'\ReflowDisplay{(1.1.2.6)}{\begin{aligned}'+'\n'+r'\operatorname{Hom}_B(\Omega^1_{B/A},M)&\xrightarrow{\ \sim\ }'+'\n'+r'\operatorname{Der}_A(B,M),\\'+'\n'+r'u&\longmapsto u d_{B/A}.'+'\n'+r'\end{aligned}}'
 new=left('1.1.2.6',r'\operatorname{Hom}_B(\Omega^1_{B/A},M)\xrightarrow{\ \sim\ }\operatorname{Der}_A(B,M),')+'\n'+r'\ReflowDisplay{}{u\longmapsto u d_{B/A}.}'
 ch(layer,old,new,'universal property','II.1.1.2.6.left-label','The label is on the left at the upper isomorphism; the element assignment has its own lower line.','structure')
 ch(layer,'baseline=(current bounding box.center)','baseline=(B.base)','commutative square baseline','II.1.1.2.7.baseline','evidence/I_p116_square.png places the left label on the upper B-to-B-prime row; preserve the existing named diagram macro and its four arrows.')
 old=r'\begin{equation}\tag{1.1.2.7}'+'\n'+r'\IllusieDifferentialsBaseChangeSquare'+'\n'+r'\end{equation}'
 ch(layer,old,left('1.1.2.7',r'\IllusieDifferentialsBaseChangeSquare'),'commutative square label','II.1.1.2.7.left-label','Restore the printed label at the left of the upper row.','structure')
 for num,formula in [('1.1.2.8',r"\Omega^1_{B/A}\otimes_B B'\longrightarrow\Omega^1_{B'/A'}."),('1.1.2.10',r"(\Omega^1_{B/A}\otimes_B B')\oplus"+'\n'+r"(B'\otimes_{A'}\Omega^1_{A'/A})\longrightarrow\Omega^1_{B'/A}")]:
  ch(layer,r'\ReflowDisplay{('+num+')}{'+formula+'}',left(num,formula),'base-change displays','II.'+num+'.left-label','The scan has the number on the left; the powers, tensor subscripts, parentheses and punctuation are confirmed by the retained enlarged crops.')
 old=r"\operatorname{Hom}_{B'}(\Omega^1_{B'/A'},M)\longrightarrow"+'\n'+r"\operatorname{Hom}_{B'}(\Omega^1_{B/A}\otimes_B B',M)"
 new=r"\operatorname{Hom}(\Omega^1_{B'/A'},M)\longrightarrow"+'\n'+r"\operatorname{Hom}(\Omega^1_{B/A}\otimes B',M)"
 ch(layer,old,new,'Hom-tensor adjunction','II.p116.implicit-subscripts','evidence/I_p116_hom-adjunction.png shows no subscript on either of the first two Hom symbols or on the middle tensor symbol. The final Hom retains its B subscript. The extra subscripts are explanatory additions, not repairs to an original error.','reading')
 old=region(layer)[-190:];assert old.endswith('\\vspace{5.0bp}\n')
 ch(layer,old,old[:-len('\\vspace{5.0bp}\n')]+r'\clearpage'+'\n','physical boundary','II.p116.page-boundary','The direct-sum map (1.1.2.10), without final punctuation, ends this printed page; the sentence continues on p117.','structure')
old=region('corrected');new=old.replace('-module','-Module').replace('Le module','Le Module')
ch('corrected',old,new,'four object capitals','II.p116.withdraw-normalizations','The four printed Module capitals are intact and not errors.','reading')
for layer in LAYERS:
 old=r'\noindent The module' if layer=='English' else r'\noindent Le Module'
 new=r'\noindent\hspace*{2em}The module' if layer=='English' else r'\noindent\hspace*{2em}Le Module'
 ch(layer,old,new,'functoriality paragraph','II.p116.paragraph-indent','evidence/I_p116_functoriality-intro.png shows a new paragraph indented at Le Module.')
verdict(page,'ILL-SC-20260804-0113','No listed original correction','No new original error established','The implicit subscripts in the original are mathematically unambiguous in context; all three transcriptions had expanded them unnecessarily.',ev)
verdict(page,'ILL-NORM-20260804-0144','Four printed Module capitals','All four lower-case normalizations withdrawn','These are printed conventions, with no grammatical or mathematical defect.',ev)
verdict(page,'ILL-TX-20260804-0140','Eleven anchors including page and named square macro','All anchors and macro name preserved; left labels, implicit subscripts, indentation and upright Latin restored','All exponents, indices, primes, arrows, parentheses and small punctuation inspected in retained 800-dpi crops.',ev)
verdict(page,'ILL-TR-20260804-0142','Universal property, functoriality and cocartesian base change','English prose retained; common scan-based notation and layout corrections applied','Translation meaning agrees with the French; cocartesian and the differential terminology agree with the glossary. The final assertion is continued on p117.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.1.2.6','For an A-derivation delta:B->M, define phi:B tensor_A B->M by phi(b tensor c)=b delta(c). It is A-balanced and satisfies phi(zw)=mu(z)phi(w)+mu(w)phi(z), hence vanishes on I squared when restricted to I. It induces a B-linear map I/I squared->M sending 1 tensor x minus x tensor 1 to delta(x). Conversely composition with d is an A-derivation. If z=sum b tensor c is in I, then sum bc=0 and z=sum (b tensor 1)(1 tensor c minus c tensor 1), proving generation and uniqueness. These inverse constructions commute with restriction and sheafification, establishing the displayed natural bijection. This is an independent check of the construction; no claim is made to having read the cited EGA passage.'),('II.1.1.2.7-8','A commutative square with map f:B->B-prime gives the A-derivation b->d-prime(f(b)) into Omega(B-prime/A-prime), regarded as a B-module. The universal property gives the semilinear map and its B-prime-linear tensor adjoint (1.1.2.8). Precomposition on Hom sends a derivation delta-prime to delta-prime composed with f, which verifies the displayed restriction map and its directions. Identity and composition follow on the generators d(b).'),('II.1.1.2.9.first-claim','For the pushout B-prime=B tensor_A A-prime and a B-prime-module M, an A-derivation delta:B->M extends uniquely to an A-prime-derivation by delta-prime(b tensor a-prime)=a-prime delta(b). A-balancing uses delta(a)=0; the Leibniz rule follows directly on pure tensors. Restriction and extension are inverse and natural in M, so the representing base-change map Omega(B/A) tensor_B B-prime -> Omega(B-prime/A-prime) is an isomorphism. No flatness is used. The second assertion concerning (1.1.2.10) is not certified here because its predicate continues on p117.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p116_*.png')):f.write(f'| evidence/{p.name} | Printed p116, 800-dpi crop inspected during the first reading. |\n')
print('Page 116 edits and three targeted checks recorded.')
