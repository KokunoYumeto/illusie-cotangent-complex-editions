"""Primary reviewer's p115 display and notation corrections."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='115';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p115}'
ev='LNM239 scan PDF p133 / printed p115: both full 400-dpi halves and ten retained 800-dpi crops personally inspected. All source regions and four prior entries read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
def left(num,formula):return r'\ReflowDisplay{}{\hbox to\linewidth{\text{('+num+r')}\hfill$\displaystyle '+formula+r'$\hfill\phantom{\text{('+num+')}}}}'
def plain(formula):return r'\ReflowDisplay{}{'+formula+'}'
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','whole page','II.p115.upright-Latin','All mathematical Latin letters and their indices are upright in the print.')
 ch(layer,r'\mathbf N',r'\mathbb N','principal-parts index','II.1.1.2.N','evidence/I_p115_natural-n.png shows the double-stroked N.','reading')
 old=r'\ReflowDisplay{(1.1.1.4)}{\begin{aligned}'+'\n'+r'\operatorname{Der}_A(B,M)&\xrightarrow{\ \sim\ }'+'\n'+r'\operatorname{Hom}_{A\text{-}\mathrm{Alg}/B}(B,B\oplus M),\\'+'\n'+r'd&\longmapsto(x\longmapsto x+dx).'+'\n'+r'\end{aligned}}'
 new=left('1.1.1.4',r'\operatorname{Der}_A(B,M)\xrightarrow{\ \sim\ }\operatorname{Hom}_{A\text{-}\mathrm{Alg}/B}(B,B\oplus M),')+'\n'+plain(r'd\longmapsto(x\longmapsto x+dx).')
 ch(layer,old,new,'dual-number correspondence','II.1.1.1.4.left-label','The label is on the left of the upper isomorphism; the element assignment is a separate lower line ending in a period.','structure')
 old=r'\ReflowDisplay{(1.1.2.1)}{0\longrightarrow I\longrightarrow B\otimes_A B\longrightarrow B\longrightarrow0,'+'\n'+r'\qquad x\otimes y\longmapsto xy,}'
 new=left('1.1.2.1',r'0\longrightarrow I\longrightarrow B\otimes_A B\longrightarrow B\longrightarrow0')+'\n'+plain(r'x\otimes y\longmapsto xy,')
 ch(layer,old,new,'diagonal sequence','II.1.1.2.1.layout','evidence/I_p115_diagonal-sequence.png has the multiplication assignment below the sequence, no comma after the terminal zero, and a comma after xy; restore the left label.','structure')
 old=r'\ReflowDisplay{(1.1.2.2)}{j_1,j_2:B\rightrightarrows B\otimes_A B,'+'\n'+r'\qquad j_1(x)=x\otimes1,\qquad j_2(x)=1\otimes x.}'
 new=left('1.1.2.2',r'j_1,j_2:B\rightrightarrows B\otimes_A B')+'\n'+plain(r'j_1(x)=x\otimes1,\qquad j_2(x)=1\otimes x.')
 ch(layer,old,new,'two sections','II.1.1.2.2.layout','The two section formulas occupy a separate line; there is no comma after the upper target. Label is on the left.','structure')
 for num,formula in [('1.1.2.3',r'P^n_{B/A}=(B\otimes_A B)/I^{n+1},'),('1.1.2.4',r'0\longrightarrow\Omega^1_{B/A}\longrightarrow P^1_{B/A}\longrightarrow B'+'\n'+r'\longrightarrow0.')]:
  ch(layer,r'\ReflowDisplay{('+num+')}{'+formula+'}',left(num,formula),'single-line displays','II.'+num+'.left-label','The scan has the equation number on the left; the formula, degrees and punctuation are otherwise correct.')
 old=r'\ReflowDisplay{(1.1.2.5)}{d_{B/A}:B\longrightarrow\Omega^1_{B/A},'+'\n'+r'\qquad d_{B/A}(x)=1\otimes x-x\otimes1\pmod{I^2},}'
 new=left('1.1.2.5',r'd_{B/A}:B\longrightarrow\Omega^1_{B/A},')+'\n'+plain(r'd_{B/A}(x)=1\otimes x-x\otimes1\mathrel{\mathrm{mod}}I^2,')
 ch(layer,old,new,'canonical derivation','II.1.1.2.5.layout-and-mod','evidence/I_p115_canonical-derivation.png shows the element formula on its own line and mod I squared without parentheses. Both lines end in commas and the label is on the left.','structure')
 old=region(layer)[-190:];assert old.endswith('\\vspace{5.0bp}\n')
 ch(layer,old,old[:-len('\\vspace{5.0bp}\n')]+r'\clearpage'+'\n','physical boundary','II.p115.page-boundary','The canonical derivation formula and its comma end the printed page.','structure')
old=region('corrected');new=old.replace("d'anneaux","d'Anneaux").replace(r'\uline{anneau',r'\uline{Anneau').replace('-algèbre','-Algèbre').replace("L'idéal","L'Idéal").replace('-module','-Module').replace(r'\uline{module',r'\uline{Module')
ch('corrected',old,new,'seven object capitals','II.p115.withdraw-normalizations','The seven printed capitals are intact and not mathematical or grammatical errors.','reading')
for layer in ['as-printed','corrected']:
 ch(layer,r'\uline{Module des différentielles (de Kähler) de}',r'\uline{Module des différentielles} (\uline{de Kähler}) \uline{de}','Kähler terminology emphasis','II.p115.parentheses-not-underlined','evidence/I_p115_kahler-text.png shows separate underline spans; the parentheses are not underlined.')
verdict(page,'ILL-SC-20260804-0112','No listed original correction','No new original error established','Formulas and local algebra constructions agree with the scan; the differences repaired here belong to the transcription/layout.',ev)
verdict(page,'ILL-NORM-20260804-0143','Seven printed capitals','All seven lower-case normalizations withdrawn','No justification for these changes; rendered French layers now agree on this page.',ev)
verdict(page,'ILL-TX-20260804-0139','Ten anchors including page; left equation labels and separate element rows','All anchors preserved; display structure, punctuation, N and underline spans restored','All powers n,n+1,1,2, subscripts B/A and A, section indices, arrows and signs inspected at 800 dpi.',ev)
verdict(page,'ILL-TR-20260804-0141','Derivations, ring of principal parts, left/right structure, Kähler differentials','English meaning retained; common notation/display corrections applied','Terms agree with the supplied glossary and no overriding terminology change was identified. No English prose rephrasing.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.1.1.4','For an A-derivation d, d(1)=2d(1) implies d(1)=0, and A-linearity gives d(a)=0. The map x -> (x,d(x)) preserves products exactly because the dual-number product is (x,m)(y,n)=(xy,xn+ym); it is an A-algebra section of B direct-sum M -> B. Conversely any such section has that form, with additive A-linear second component satisfying Leibniz. These constructions are inverse and commute with the compatible restriction/base maps, proving the displayed canonical correspondence.'),('II.1.1.2.1-4','Multiplication mu:B tensor_A B -> B has ring sections j1 and j2, so it is surjective and has kernel I. Passing to the quotient by I squared gives exact 0->I/I squared->P^1->B->0. The ideal I/I squared has zero product, hence its module action factors through B. The two B-actions agree because (j2(b)-j1(b))I lies in I squared. The definition P^n=(B tensor B)/I^(n+1) is consistent for each nonnegative n.'),('II.1.1.2.5','Put delta(x)=j2(x)-j1(x) mod I squared. Additivity is immediate and delta(a)=0 for a in A. The difference delta(xy)-j1(x)delta(y)-j1(y)delta(x) is (j2(x)-j1(x))(j2(y)-j1(y)), which belongs to I squared. Thus the displayed sign order 1 tensor x minus x tensor 1 defines an A-derivation for the left B-action as asserted.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p115_*.png')):f.write(f'| evidence/{p.name} | Printed p115, 800-dpi crop inspected during the first reading. |\n')
print('Page 115 edits and three targeted checks recorded.')
