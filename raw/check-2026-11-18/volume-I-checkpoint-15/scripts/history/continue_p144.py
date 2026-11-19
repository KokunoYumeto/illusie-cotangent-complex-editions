"""Primary reviewer's page 144 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='144';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p144}'
ev='LNM239 scan PDF p162 / printed p144: both complete 400-dpi halves, thirteen 800-dpi crops and the 1600-dpi domain crop personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old
for a,b in [("un diagramme commutatif d'anneaux de","un diagramme commutatif d'Anneaux de"),("des morphismes d'anneaux de","des morphismes d'Anneaux de")]:new=new.replace(a,b)
new=new.replace("\\uline{morphisme d'anneaux de}","\\uline{morphisme d'Anneaux de}").replace('de la catégorie des anneaux','de la catégorie des Anneaux').replace(r'$C$-\uline{algèbre}',r'$C$-\uline{Algèbre}')
for a,b in [('$T$.','$T$ .'),(r'\operatorname{ob}T$,',r'\operatorname{ob}T$ ,'),("$C'$,","$C'$ ,"),(r'$f^*u$.',r'$f^*u$ .'),('unités de $B$,','unités de $B$ ,'),(r'\underline a B$.',r'\underline a B$ .'),("A\\otimes_C C'$,","A\\otimes_C C'$ ,"),("B\\otimes_C C'$.","B\\otimes_C C'$ ."),(r'v^{-1}(C^*)$,',r'v^{-1}(C^*)$ ,'),("C'{}^*$,","C'{}^*$ ,")]:new=new.replace(a,b)
ch('corrected',old,new,'lemma and proof','II.p144.withdraw-normalizations','Restore five printed capitals and thirteen punctuation spaces. The lowercase anneaux in part(i) is printed and remains lowercase.','reading')
for layer in LAYERS:
 ch(layer,r"f:T'\longrightarrow T",r'f:T\longrightarrow T','2.3.3(iv) domain','II.2.3.3.iv.printed-domain','The 1600-dpi crop evidence/I_p144_part-iv-domain-1600.png clearly has no prime. The endomorphism statement is meaningful and true; absent a demonstrated necessary repair, restore it in every layer. I-Q015 tracks whether subsequent context uniquely warrants the broader domain.','reading')
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','II.p144.upright-Latin','All printed Latin mathematical and diagram letters are upright; preserve the underlined sheafification symbol and all four headed tilde arrows.')
 old=region(layer);new=old.replace('\\uline{est de loca-}\\par\n\\noindent \\uline{lisation}',r'\uline{est de localisation}')
 new=new.replace('sous-\\par\n\\noindent préfaisceau','sous-préfaisceau').replace('sub-\\par\n\\noindent presheaf','sub-presheaf')
 new=new.replace('\\par\n\\noindent ','\n').replace('\\par\n\\phantomsection','\n\\phantomsection')
 for t in [r'\uline{alors le morphisme',r'\uline{then the associated',r'\uline{morphism of rings',r"$X'{}^{-1}"]:new=new.replace('\\noindent '+t,t)
 new=new.replace("\\noindent \\uline{morphisme d'Anneaux","\\uline{morphisme d'Anneaux")
 ch(layer,old,new,'lemma and proof paragraphs','II.p144.prose-continuity','Join printed line wraps, including retained anchor boundaries; remove the line-break hyphen in localisation and preserve lexical sous-/sub- hyphens. Preserve the four parts, displays and proof paragraph.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p144.boundary','Retain the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p144','All supplied layers add a prime in f:T-prime->T; C also normalizes five capitals and thirteen spaces','Same added prime; normalized capitals and spaces','Local source-comparison verdict, not a supplied decision-record ID. Restore the unprimed printed domain in all layers pending I-Q015: the printed statement is not false. Withdraw all five capitalization and thirteen spacing normalizations. No necessary original-error correction established on this page.',ev+'evidence/I_p144_part-iv-domain-1600.png; evidence/I_p144_part-ii.png; evidence/I_p144_proof-ii-expanded.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.3.3.i','Let X=u^{-1}(B^*) as a presheaf. Sectionwise locality identifies X^{-1}A with B. A map from the associated sheaf aA that inverts aX corresponds by sheafification adjunction to a presheaf map from A that inverts X, hence uniquely to a map from B. This proves (aX)^{-1}(aA)=aB by the universal property, with the displayed morphism au. No assumption that the topos has enough points is used.'),('II.2.3.3.ii','For every C-prime-algebra D, maps from B tensor_C C-prime to D are precisely C-algebra maps A->D that invert X, with the specified C-prime structure. These are precisely maps from A tensor_C C-prime that invert the image X-prime. Thus X-prime^{-1}(A tensor_C C-prime) is canonically B tensor_C C-prime. This proves the asserted base-change localization and requires no flatness of C-prime.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'READING_QUESTIONS.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['I-Q015','144','II.2.3.3(iv) domain','The print certainly has f:T->T, while all supplied layers insert a prime. The unprimed statement is true and the general statement is also true. Check the continuation and subsequent applications before deciding whether the author intended and requires a distinct source topos.','Printed f:T->T restored in all three layers; no unproved assertion of an original misprint.','scan reading resolved; scope/intent review pending','evidence/I_p144_part-iv-domain-1600.png; evidence/I_p144_part-iv.png'])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p144_*.png')):f.write(f'| evidence/{p.name} | Page144 audit: '+('1600' if '1600' in p.name else '800')+'-dpi crop personally inspected. |\n')
print('Page144 edits, verdict, scope question and two proof checks recorded.')
