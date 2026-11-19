"""Primary reviewer's page 142 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='142';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p142}'
ev='LNM239 scan PDF p160 / printed p142: both complete 400-dpi halves and seven 800-dpi crops personally inspected, with three expanded crops reread to include edge signs. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('$f$.','$f$ .').replace(r'\mathcal O_X$,',r'\mathcal O_X$ ,').replace('$T$.','$T$ .').replace('sur $A$,','sur $A$ ,').replace("d'anneaux de","d'Anneaux de").replace('des anneaux de','des Anneaux de')
ch('corrected',old,new,'localization and epimorphism prose','II.p142.withdraw-normalizations','Restore four harmless printed punctuation spaces and two Anneaux capitals; retain the necessary F->f and ia->la corrections.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','II.p142.upright-Latin','Printed Latin mathematical and diagram letters are upright.')
 old=region(layer);new=old.replace(r'\mathcal O_',r'\underline{\mathrm{O}}_')
 ch(layer,old,new,'four structure sheaves in localization proof','II.p142.structure-ring-font','Each printed structure-ring symbol is an underlined upright O; evidence/I_p142_localization-proof-expanded.png.')
 ch(layer,r'(A) -- node[below] {$u$} (Bb)',r'(A) -- node[above] {$u$} (Bb)','lower arrow of pushout square','II.p142.lower-u-position','The lower horizontal u is above its arrow; evidence/I_p142_pushout-square.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace('$T$ .\\par\n','$T$ .\n').replace('$T$.\\par\n','$T$.\n').replace('$A$.\\par\n','$A$.\n').replace('=0$),\\par\n','=0$),\n')
 new=new.replace('\\noindent \\uline{On suppose','\\uline{On suppose').replace('\\noindent \\uline{Suppose','\\uline{Suppose').replace('\\noindent \\uline{Alors on a}','\\uline{Alors on a}').replace('\\noindent \\uline{Then we have}','\\uline{Then we have}').replace("\\noindent d'où l'assertion.","d'où l'assertion.").replace('\\noindent whence the assertion.','whence the assertion.')
 ch(layer,old,new,'statement and proof prose','II.p142.prose-continuity','Remove line-wrap paragraph breaks, including those adjoining retained anchors; keep the separate statements, proofs and diagrams.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p142.boundary','Retain the printed end of page.','structure')
ch('English','Then we have','Then one has','vanishing conclusion','II.p142.impersonal','French Alors on a takes the impersonal register under the supplied standard.','terminology')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p142','F; ia flèche; two Anneaux capitals; four punctuation spaces','f; la flèche; normalized capitals and spacing','Local source-comparison verdict, not a supplied decision-record ID. Confirm F->f: the only inducing morphism is the f:X->Y of the preceding page and diagram. Confirm ia->la as a grammatical printed typo. Withdraw the two capitalization and four spacing normalizations.',ev+'evidence/I_p142_original-slips.png and evidence/I_p142_flat-epi-hypothesis-expanded.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.3.0','Localization pulls the two structure sheaves back exactly: O(X-prime)=u^{-1}O(X), and f-prime^{-1}O(Y-prime)=u^{-1}f^{-1}O(Y). Thus the defining ring map is the inverse image of the original one. The standard cotangent construction commutes with inverse image, giving1.2.3.5; since u^*=u^{-1} for the induced structure ring, this is the asserted canonical isomorphism. F in the print must denote the already defined f; no uppercase F is introduced.'),('II.2.3.1','For an epimorphism of commutative ring objects A->B, the two maps B->B tensor_A B coincide, so multiplication B tensor_A B->B is inverse to either map; conversely the pushout identity forces cancellation and hence the epimorphism property. Flatness gives vanishing of higher Tor, so2.2.1 applied to the displayed pushout yields L(B/A)->L(B/B) as a quasi-isomorphism. B=S_B(0), with0 flat, so1.2.4.4 applies and L(B/B) is quasi-isomorphic to Omega^1(B/B)=0. This proves the stated vanishing in D(B).')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p142_*.png')):f.write(f'| evidence/{p.name} | Page142 audit:800-dpi crop personally inspected; expanded crops resolve edge clipping. |\n')
print('Page142 edits, verdict and two proof checks recorded.')
