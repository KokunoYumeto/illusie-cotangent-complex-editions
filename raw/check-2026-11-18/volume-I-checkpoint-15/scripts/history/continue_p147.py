"""Primary reviewer's page147 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='147';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p147}'
ev='LNM239 scan PDF p165 / printed p147: both complete400-dpi halves and nine800-dpi crops personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
ch('corrected','2-cartésien ([18]','2-cartésien ( [18]','footnote reference','II.p147.withdraw-spacing','Withdraw the optional reference-spacing normalization; preserve the necessary affine->affines agreement correction.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','II.p147.upright-Latin','Printed Latin mathematical and diagram letters are upright.')
 old=region(layer);assert old.count(r'\mathcal O')==2
 ch(layer,old,old.replace(r'\mathcal O',r'\underline{\mathrm{O}}'),'initial identifications','II.p147.structure-sheaves','The two structure-sheaf symbols are upright underlined O with X outside the underline.')
 old=region(layer);assert old.count(r'\xrightarrow{\sim}')==2
 ch(layer,old,old.replace(r'\xrightarrow{\sim}',r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}'),'two initial isomorphisms','II.p147.unheaded-isomorphisms','Both enlarged signs are plain horizontal bars with tilde and no arrowhead; preserve the genuine arrow in2.3.6.2.')
 old=region(layer);assert old.count(r'\textsuperscript{(1)}')==2
 ch(layer,old,old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})'),'note call and note label','II.p147.note-parentheses','The parentheses remain on the text baseline and only the digit1 is raised.')
 ch(layer,r'at (4.20,0.21) {.}',r'at ([xshift=1.20cm]Sp.base) {.}','base-change square period','II.p147.square-period','Align the terminal period with the bottom row baseline.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace('\\par\n\\phantomsection','\n\\phantomsection')
 for t in ["\\uline{d'homologie de}",r'\uline{of}',r'toute algèbre',r'algebra $B$']:new=new.replace('\\noindent '+t,t)
 ch(layer,old,new,'proofs and statements','II.p147.prose-continuity','Join printed line wraps and retained anchor boundaries; preserve statement/proof divisions and all displays.','structure')
 ch(layer,r'\phantomsection\hypertarget{illusie:I:ch1:p147:footnote-2.3.8-two-cartesian}',r'\par\vfill'+'\n'+r'\phantomsection\hypertarget{illusie:I:ch1:p147:footnote-2.3.8-two-cartesian}','footnote placement','II.p147.footnote-bottom','Keep the ruled note at the printed page foot.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p147.boundary','Retain the printed page boundary.','structure')
ch('English','we may suppose that $X$ and $Y$ are affine','one may suppose that $X$ and $Y$ are affine','2.3.7 proof','II.p147.impersonal-on','French on peut supposer is impersonal.','terminology')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p147','X et Y affine; reference space in footnote','X et Y affines; normalized reference space','Local source-comparison verdict, not a supplied decision-record ID. Confirm affine->affines as the required plural agreement for the coordinated subject X et Y; withdraw only the optional reference-space normalization.',ev+'evidence/I_p147_coherence-proof.png; evidence/I_p147_footnote.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.3.6.2-3','For the point inverse-image functor,1.2.1.4 identifies (L(B/A))_X with L(B_X/A_X). The associated-sheaf functor is M_X tensor_{B_X}O_X, exact because O_X is flat over B_X by localization. Applying2.3.1.1 to the p146 square therefore identifies L(B_X/A_X) tensor_{B_X}O_X with L(O_X/f^{-1}O_Y)=L(X/Y). This is precisely the canonical map2.3.6.2 and proves2.3.6.3. No derived-tensor mark is missing in the displayed ordinary tensors.'),('II.2.3.7.deduction','Locality2.3.0 reduces to affine X=Spec(B),Y=Spec(A). By2.3.6.3 and exactness of the associated-sheaf functor, H_n(L(X/Y)) is the sheaf associated with H_n(L(B/A)), proving quasi-coherence. Under the additional hypotheses, A is Noetherian and B is a finite-type A-algebra, hence Noetherian. Taking the finite-type degreewise polynomial resolution asserted in the cited Andre theorem,1.2.6.3 computes L(B/A) by Omega(P/A) tensor_P B. Each simplicial degree is a finite free B-module; its normalized degree is a direct summand and therefore finite projective. Over Noetherian B all kernels, images and homology modules are finitely generated, giving coherent associated sheaves. This verifies the deduction from the stated resolution-existence theorem; Andre[1]17.2 p69 was not independently consulted here.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p147_*.png')):f.write(f'| evidence/{p.name} | Page147 audit:800-dpi crop personally inspected. |\n')
print('Page147 edits, verdict and two proof/use checks recorded.')
