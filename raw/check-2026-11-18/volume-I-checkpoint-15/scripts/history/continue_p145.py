"""Primary reviewer's page 145 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='145';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p145}'
ev='LNM239 scan PDF p163 / printed p145: both complete 400-dpi halves and eight 800-dpi crops personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace("épimorphisme d'anneaux","épimorphisme d'Anneaux")
for a,b in [('travers $C$,','travers $C$ ,'),('$b\\in B$,','$b\\in B$ ,'),('$a\\in A$,','$a\\in A$ ,'),('$v(b)\\in C^*$,','$v(b)\\in C^*$ ,'),("f(a)\\in C'{}^*$,","f(a)\\in C'{}^*$ ,"),("$gu(X)\\subset C'{}^*$,","$gu(X)\\subset C'{}^*$ ,"),(r'$\bar gv=g$,',r'$\bar gv=g$ ,'),(r'A\xrightarrow{\sim}B$,',r'A\xrightarrow{\sim}B$ ,'),("$f^*B\\longrightarrow B'$,","$f^*B\\longrightarrow B'$ ,"),('([18]chap. III)','( [18]chap. III)')]:new=new.replace(a,b)
ch('corrected',old,new,'proof and proposition','II.p145.withdraw-normalizations','Restore the printed Anneaux capital and ten punctuation/reference spaces while preserving the necessary correction bar-g v=g.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','II.p145.upright-Latin','Printed Latin mathematical letters are upright; the one tilde isomorphism is headed.')
 old=region(layer);assert old.count(r'\mathcal O')==7
 ch(layer,old,old.replace(r'\mathcal O',r'\underline{\mathrm{O}}'),'2.3.4 structure sheaves','II.p145.structure-sheaves','All seven structure-sheaf symbols are upright underlined O, with their subscripts outside the underline.')
 old=region(layer);assert old.count(r'\widetilde X')==4
 ch(layer,old,old.replace(r'\widetilde X',r'X^{\sim}'),'2.3.4 spectrum notation','II.p145.spectrum-tilde','All four occurrences show the tilde raised to the right of X, including both structure-sheaf subscripts; restore this printed placement.')
 old=region(layer);new=old.replace('morphis-\\par\n\\vspace{4.6bp}\n\\noindent me','morphisme').replace('morphism\\par\n\\vspace{4.6bp}\n\\noindent of','morphism of')
 new=new.replace('\\par\n\\noindent ','\n').replace('\\par\n\\phantomsection','\n\\phantomsection')
 for t in [r'$v:f^*A',r'donc $f^*(\bar u)',r'Thus $f^*(\bar u)',r'ce qui prouve',r'which proves',r'$p^{-1}']:new=new.replace('\\noindent '+t,t)
 ch(layer,old,new,'proof and proposition paragraphs','II.p145.prose-continuity','Join false line paragraphs and anchor boundaries; remove the artificial gap and line-break hyphen in morphisme. Preserve proposition, proof and displayed assignment.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p145.boundary','Retain the printed page boundary.','structure')
ch('English','We have $f^*(X)','One has $f^*(X)','2.3.3(iv) converse','II.p145.impersonal-on','French on a is impersonal; retain that voice.','terminology')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p145','bar-g vu=gu implies bar-g v=v; Anneaux and ten spaces','bar-g v=g; lowercase anneaux and normalized spaces','Local source-comparison verdict, not a supplied decision-record ID. Confirm v->g as a necessary original-error repair: cancellation of epimorphism u gives equality of the two maps B->C-prime, namely bar-g v and g; the printed v instead has codomain C. Withdraw one capitalization and ten spacing normalizations.',ev+'evidence/I_p145_converse.png; evidence/I_p145_proposition.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.3.3.iii','For localization maps u and v, put Y=v^{-1}(C^*) and X=u^{-1}(Y). A map f:A->C-prime inverting X first factors over B because X contains u^{-1}(B^*). Locally b=x^{-1}a; if v(b) is a unit, vu(a)=vu(x)v(b) is a unit, so a belongs to X and the factor over B inverts Y. It therefore factors uniquely over C. Conversely, if vu is a localization and u is an epimorphism, a map g:B->C-prime inverting Y gives a unique bar-g:C->C-prime with bar-g vu=gu. Cancelling u yields bar-g v=g, confirming the printed v is wrong. Uniqueness follows since vu, hence v, is an epimorphism. This proves both assertions.'),('II.2.3.3.iv','Units can be represented by the finite-limit object of pairs (b,c) with bc=1; projection onto b is a monomorphism because inverses are unique. Thus both f_* and the left-exact f^* commute with units. Adjunction identifies maps from f^*A inverting f^*X with maps from A to f_*B-prime inverting X, hence with maps from B to f_*B-prime and finally from f^*B to B-prime. This proves preservation of localization. Conversely let X=u^{-1}(B^*). The comparison X^{-1}A->B becomes an isomorphism after f^*: f^*X is the full inverse image of units for the localization f^*u. A faithful functor reflects monomorphisms and epimorphisms; applying this on the underlying topoi, which are balanced, shows it reflects isomorphisms. Therefore the comparison was an isomorphism. The proof works for both the printed endomorphism and arbitrary distinct source and target topoi; it does not alone establish an obligatory prime on p144.'),('II.2.3.4.use-of-localization-lemma','For the presheaf construction stated in the text, every component O_X(U)->O_X(U)[s^{-1}] is localization at the multiplicative set generated by s. Applying2.3.3(i) to this presheaf morphism makes its associated sheaf map a localization. This verifies the stated deduction. Hakim [18], chapterIII, was not independently consulted here, so the external construction/locator is not claimed newly verified.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p145_*.png')):f.write(f'| evidence/{p.name} | Page145 audit:800-dpi crop personally inspected. |\n')
print('Page145 edits, verdict and three proof/use checks recorded.')
