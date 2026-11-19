"""Primary reviewer's page146 audit and evidence-based p144 scope refinement; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='146';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p146}'
ev='LNM239 scan PDF p164 / printed p146: both complete400-dpi halves and nine800-dpi crops personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('[18]chap. IV','[18]Chap. IV').replace('$-module quasi-cohérent','$-Module quasi-cohérent')
for a,b in [(r'\xrightarrow{p}Y$,',r'\xrightarrow{p}Y$ ,'),(r'D(\widetilde Y)$.',r'D(\widetilde Y)$ .'),(r'\longrightarrow Y$.',r'\longrightarrow Y$ .'),('$A$,','$A$ ,'),('$A$.','$A$ .'),(r'\longrightarrow B$.',r'\longrightarrow B$ .'),(r'\mathcal O_Y$,',r'\mathcal O_Y$ ,'),(r'\mathcal O_X$.',r'\mathcal O_X$ .')]:new=new.replace(a,b)
ch('corrected',old,new,'corollaries and affine comparison','II.p146.withdraw-normalizations','Restore the printed Chap./Module capitals and nine punctuation spaces; no original-error repair is needed in this page text.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','II.p146.upright-Latin','Printed Latin mathematical and diagram letters are upright.')
 old=region(layer);assert old.count(r'\mathcal O')==7
 ch(layer,old,old.replace(r'\mathcal O',r'\underline{\mathrm{O}}'),'structure sheaves','II.p146.structure-sheaves','Restore seven upright underlined O symbols, including the two square nodes; subscripts remain outside the underline.')
 old=region(layer);assert old.count(r'\widetilde Y')==6 and old.count(r'\widetilde M')==1
 ch(layer,old,old.replace(r'\widetilde Y',r'Y^{\sim}').replace(r'\widetilde M',r'M^{\sim}'),'spectrum and associated-sheaf notation','II.p146.right-side-tildes','All six Y and the one M have the printed tilde at upper right, including cotangent subscripts.')
 ch(layer,r'at (-4.68,2.48) {(2.3.6.1)}',r'at ([xshift=-4.68cm]BX.base) {(2.3.6.1)}','square tag','II.2.3.6.1.tag-baseline','The printed equation tag aligns with the top row baseline.')
 ch(layer,r'at (4.68,0) {,}',r'at ([xshift=1.81cm]fOY.base) {,}','square punctuation','II.2.3.6.1.comma-baseline','Align the printed comma with the bottom-row baseline, preserving its horizontal position.')
 old=region(layer);new=old.replace('locali-\\par\n\\noindent sation','localisation').replace('locali-\\par\n\\noindent zation','localization')
 new=new.replace('\\par\n\\noindent ','\n').replace('\\par\n\\phantomsection','\n\\phantomsection')
 for t in [r'\uline{La flèche canonique}',r'\uline{The canonical map}',r'résulte donc',r'therefore follows',r'a localization morphism by']:new=new.replace('\\noindent '+t,t)
 new=new.replace("\\noindent de localisation d'après","de localisation d'après")
 ch(layer,old,new,'corollaries and affine comparison','II.p146.prose-continuity','Join printed line wraps and retained anchor boundaries; remove the artificial line-break hyphen in localisation/localization. Preserve corollary, proof and numbered-paragraph divisions.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p146.boundary','Retain the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p146','Chap., Module; nine spaces; repeated2.3.6 numbering','chap., module; normalized spaces; same numbering','Local source-comparison verdict, not a supplied decision-record ID. Withdraw two capitalization and nine spacing normalizations. Retain both printed occurrences of2.3.6; I-Q016 tracks subsequent references before any numbering decision.',ev+'evidence/I_p146_corollary-235.png; evidence/I_p146_corollary-236.png; evidence/I_p146_affine-introduction.png; evidence/I_p146_module-identification.png.')
scope='The800-dpi evidence/I_p146_proof-236.png and evidence/I_p146_horizontal-localizations.png explicitly apply2.3.3(iv) to point inverse images and to f:X->Y for arbitrary affine schemes. These require a possibly distinct source topos. The proof personally checked on p145 works without any equality of source and target. Thus this later context supplies the previously missing necessity for the intended generality: restore T-prime only in corrected French/English, retaining the certain unprimed scan reading in D. This supersedes the provisional p144 scope disposition, not its scan reading.'
for layer in ['corrected','English']:
 edit_page(layer,r'\begin{illusiebodypage}{illusie:I:ch1:p144}',r'f:T\longrightarrow T',r"f:T'\longrightarrow T",'144','2.3.3(iv) domain after readingp146','II.2.3.3.iv.domain-required-by-use',ev+scope,'misprint of the original')
verdict('144','SUPPLIED-SOURCE-DIFF:I:p144:scope-after-p146','f:T->T, certain at1600dpi','f:T-prime->T in C/English','The explicit p146 applications and the checked p145 proof establish the intended generality. Confirm the supplied prime in C/English as the necessary scope repair; retain unprimed T in D. This supersedes the earlier provisional scope verdict.',scope)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.3.5','The localization p^{-1}O_Y->O_{Y-tilde} is a flat epimorphism, so2.3.1 gives L(Y-tilde/Y)=0. In the transitivity triangle2.1.5.6 for X->Y-tilde->Y, the derived pullback of this zero term is zero. Hence the canonical map L(X/Y)->L(X/Y-tilde) is an isomorphism in D(X), as asserted. This checks the deduction from2.3.4 without claiming an independent verification of Hakim chapterIV.'),('II.2.3.6.corollary-and-scope','At each prime of an affine scheme Spec(A), the stalk of A_X->O_X is A->A_p. Let S be the inverse image of O_X^*. Its stalk is A minus p, since inverse images commute with units. Thus (S^{-1}A_X)_p->O_{X,p} is the usual isomorphism A_p->A_p. Scheme sheaves have enough points, so S^{-1}A_X->O_X is an isomorphism. This proves the localization claim directly. The cited2.3.3(iv) can equivalently be applied to the jointly conservative family of all points, viewed as one morphism from the product topos of sets; it requires the general domain T-prime. The later f:X->Y use below the square independently requires that same generality.'),('II.2.3.6.1.square-and-module-identification','For X=Spec(B),Y=Spec(A), the two vertical maps are u_X and the structure sheaf map, so the square commutes by their construction. Its upper horizontal map is a localization by the corollary. The bottom is f^{-1}(A_Y->O_Y), with f^{-1}A_Y=A_X;2.3.3(iv) makes it a localization. For a B-module M, the canonical map M_X tensor_{B_X}O_X->M-tilde induces at p the identity M tensor_B B_p=M_p, so it is an isomorphism. This proves the displayed functor identification; the cited EGA Err I locators were preserved, not newly externally verified.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
q=ROOT/'READING_QUESTIONS.tsv'
with q.open(newline='') as f:reader=csv.DictReader(f,delimiter='\t');fields=reader.fieldnames;rows=list(reader)
for row in rows:
 if row['id']=='I-Q015':
  row['printed_page']='144–146';row['retained_reading']='D retains printed f:T->T; C/English have f:T-prime->T, now justified by the explicitp146 applications and the checkedp145 proof.';row['status']='first-reading scope resolved from subsequent use; mandatory second review pending';row['evidence']+='; evidence/I_p146_proof-236.png; evidence/I_p146_horizontal-localizations.png; CHECK_EVENTS II.2.3.3.iv and II.2.3.6.corollary-and-scope'
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
with q.open('a',newline='') as f:
 csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['I-Q016','146','Repeated2.3.6 number','The corollary and following affine-comparison paragraph both bear2.3.6. Review later citations and subordinate equation numbers before deciding whether any uniquely justified repair is needed.','Both printed numbers and all distinct anchors retained in every layer.','scan reading certain; reference disposition pending','evidence/I_p146_corollary-236.png; evidence/I_p146_affine-introduction.png; evidence/I_p146_square.png'])
with (ROOT/'CHECK_RECORD.md').open('a') as f:f.write('\n### Cross-page refinement during page146 — '+now+'\n\nPage1442.3.3(iv): '+scope+'\n')
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p146_*.png')):f.write(f'| evidence/{p.name} | Page146 audit:800-dpi crop personally inspected. |\n')
print('Page146 edits, p144 refinement, verdicts, questions and three proof checks recorded.')
