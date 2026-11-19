"""Primary reviewer's page 139 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='139';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p139}'
ev='LNM239 scan PDF p157 / printed p139: both complete 400-dpi halves and nine retained 800-dpi crops personally inspected; opening and freeness crops expanded and reinspected. Full source regions read as-printed, corrected, English. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old
for a,b in [(r'P_A^{\Delta}(B)=P$,',r'P_A^{\Delta}(B)=P$ ,'),(r"P_{A'}^{\Delta}(B')=P'$,",r"P_{A'}^{\Delta}(B')=P'$ ,"),(r"$P\otimes_A A'=P^1$.",r"$P\otimes_A A'=P^1$ ."),(r'$(*)$,',r'$(*)$ ,'),('sur $A$,','sur $A$ ,'),(r'$R=P\otimes_A Q$,',r'$R=P\otimes_A Q$ ,')]:
 assert new.count(a)==1,(a,new.count(a));new=new.replace(a,b)
ch('corrected',old,new,'six punctuation spaces','II.p139.withdraw-normalizations','Withdraw six optional punctuation-spacing normalizations; retain the justified Delta addition in R-prime.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p139.upright-Latin','Latin variables and all diagram letters are upright in the scan.')
 ch(layer,r'\overset{\mathrm L}{\otimes}',r'\overset{\ell}{\otimes}','derived-pushout hypothesis','II.p139.derived-tensor-ell','The derived tensor mark is script ell. The following tilde arrow has a printed arrowhead and is retained; evidence/I_p139_hypothesis.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 new=new.replace("$A'$.\\par\n\\vspace{5bp}\n\\noindent ","$A'$.\n")
 if layer!='English':
  new=new.replace('quasi-\nisomorphisme','quasi-isomorphisme')
  new=new.replace('Prouvons\\par\n\\phantomsection\\hypertarget{illusie:I:ch1:p139:proof-base-change-map-ii-setup}{}%\n\\noindent maintenant','Prouvons\n\\phantomsection\\hypertarget{illusie:I:ch1:p139:proof-base-change-map-ii-setup}{}%\nmaintenant')
 else:
  new=new.replace('a quasi-\\par\n\\phantomsection\\hypertarget{illusie:I:ch1:p139:proof-base-change-map-ii-setup}{}%\n\\noindent isomorphism','a\n\\phantomsection\\hypertarget{illusie:I:ch1:p139:proof-base-change-map-ii-setup}{}%\nquasi-isomorphism')
 ch(layer,old,new,'continuous proof paragraphs','II.p139.prose-continuity','Join printed line wraps and divided quasi-isomorphism, including the anchor inside the transition to part (ii). Preserve all eight anchors, every display, and both diagram macros.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p139.boundary','Retain the printed boundary after the second diagram.','structure')
old=region('English');new=old.replace('termwise free','degreewise free');ch('English',old,new,'two freeness assertions','II.p139.degreewise','Use the established degreewise term for terme a terme in both occurrences; evidence/I_p139_freeness.png.','terminology')
old=region('English');new=old.replace('We have a commutative','There is a commutative');ch('English',old,new,'two diagram introductions','II.p139.impersonal-on','Both source introductions use impersonal on; retain authorial We now prove for Prouvons.','terminology')
old=region('English');new=old.replace('There are canonical maps','Of the canonical maps').replace('\\noindent The first is an isomorphism','\\noindent the first is an isomorphism');ch('English',old,new,'sentence enclosing differential display','II.p139.differential-sentence','Restore the source sentence structure Des fleches ... la premiere, whose display ends in a comma; the supplied English leaves two independent clauses around that comma.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p139',r"R'=P_A(B'); six printed punctuation spaces",r"R'=P_A^{\Delta}(B'); spacing restored",'Local source-comparison verdict, not a supplied decision-record ID. Retain the missing-Delta correction: the argument needs the diagonal simplicial resolution of the simplicial A-algebra B-prime, as already specified for P and Q. Withdraw six optional spacing changes.',ev+'evidence/I_p139_proof-ii-setup.png confirms the omitted Delta; evidence/I_p139_proof-i.png confirms that (1.1.2.9) DOES have its closing parenthesis, so no parenthesis correction is made.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.2.1.proof-i','P is degreewise free over A and resolves B, so the derived-pushout hypothesis makes P1=P tensor_A A-prime->B-prime a quasi-isomorphism. The augmentation P-prime->B-prime is a quasi-isomorphism, so commutativity of (*) gives P1->P-prime by two-out-of-three. Both are degreewise free over A-prime. The first differential map is the ordinary base-change isomorphism of 1.1.2.9. For the second, the scalar-extended variant of 1.2.6.5 gives Omega(P1/A-prime) tensor_{P1} P-prime->Omega(P-prime/A-prime) as a quasi-isomorphism of degreewise free P-prime-modules. Kunneth I 3.3.2 therefore allows extension to B-prime. Identifying Omega(P/A) tensor_P B with L(B/A) gives exactly map (i). This supplies the intermediate ring-change step compressed in the printed argument; it does not assume ordinary tensor preserves arbitrary quasi-isomorphisms.'),('II.2.2.1.proof-ii-setup','Q=P_A^Delta(A-prime) and P=P_A^Delta(B) are simplicial polynomial A-resolutions. Thus R=P tensor_A Q models B derived-tensor_A A-prime and maps to B-prime. Functoriality supplies P->R-prime and Q->R-prime for R-prime=P_A^Delta(B-prime); the tensor-product universal property gives R->R-prime. Each edge of (**) has the printed source and target, and both augmentations to B-prime commute. The missing Delta in the printed R-prime definition would leave the bisimplicial resolution P_A(B-prime), incompatible with the stated simplicial comparison; the retained correction is necessary. The continuation of the author proof on p140 is not yet read.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p139_*.png')):f.write(f'| evidence/{p.name} | Printed p139, 800-dpi crop inspected during the first reading. |\n')
print('Page 139 edits, source-difference verdict and two mathematical checks recorded.')
