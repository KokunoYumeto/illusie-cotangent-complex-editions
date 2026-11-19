"""Primary reviewer's p118 corrections and direct checks."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='118';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p118}'
ev='LNM239 scan PDF p136 / printed p118: both full 400-dpi halves and ten retained 800-dpi crops personally inspected (three crops enlarged again to include complete upper strokes). All three complete source spans and four prior entries read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','whole page','II.p118.upright-Latin','The Latin mathematical letters and all nested indices are upright, including the diagram labels.')
 ch(layer,r'\hbox{\text{#1}\hfill$\displaystyle #2$\hfill',r'\hbox to\linewidth{\text{#1}\hfill$\displaystyle #2$\hfill','three numbered formulas','II.p118.left-display-labels','The three formula labels are left aligned and separated from the formula; retain the named display macro.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 assert old.count('\\par\n\\noindent ')==10
 ch(layer,old,new,'ten prose line wraps','II.p118.join-false-paragraphs','The ten hard paragraph breaks in the supplied source occur inside continuous printed paragraphs: opening hypothesis, Hom adjunction, functoriality, its consequence, and inverse image.','structure')
 old=region(layer)[-180:];ch(layer,old,old+r'\clearpage'+'\n','physical boundary','II.p118.page-boundary','The inverse-image isomorphism and its period end the printed page.','structure')
old=region('corrected');new=old.replace('-module','-Module').replace("l'algèbre","l'Algèbre").replace("d'anneaux","d'Anneaux").replace(')-module',')-Module')
ch('corrected',old,new,'five object capitals','II.p118.withdraw-normalizations','The five printed capitals are not errors.','reading')
verdict(page,'ILL-SC-20260804-0115','No listed original correction','No original error found','The symmetric-algebra formulas, their functoriality and the inverse-image assertion are consistent and admit the direct checks recorded in CHECK_EVENTS.',ev)
verdict(page,'ILL-NORM-20260804-0146','Five capitalized object nouns','All five lower-case normalizations withdrawn','Rendered French layers agree on this page; source-only comment-language differences do not affect the edition.',ev)
verdict(page,'ILL-TX-20260804-0142','Nine anchors including page, named diagram and display macros','All preserved; upright Latin, left label placement and continuous paragraphs restored','The diagram has both vertical arrows upward, S_f(u) and f on the rightward arrows, and a comma at bottom right. All primes, subscripts and exponents inspected at 800 dpi.',ev)
verdict(page,'ILL-TR-20260804-0144','Symmetric algebra, underlying linear map, functoriality and inverse image','English prose retained; common layout corrections applied','Meaning is complete and the terms, including resp. and inverse image, conform to the supplied standard. No stylistic revision.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.1.3.1-2','An A-linear map h:M->I extends to a derivation on the tensor algebra by d(m1...mn)=sum_j m1...m_(j-1) h(mj) m_(j+1)...mn. The symmetric commutation relations have zero image because I is a module over the commutative symmetric algebra, so the derivation descends to S_A(M). Its restriction is h; the Leibniz rule forces this extension uniquely. Consequently Der_A(S_A(M),I)=Hom_A(M,I)=Hom_B(B tensor_A M,I). The representing isomorphism Omega(S_A(M)/A)->S_A(M) tensor_A M sends d(m) to 1 tensor m, which checks the printed direction and both tensor subscripts without a projectivity or flatness hypothesis.'),('II.p118.symmetric-algebra-functoriality','For f:A->A-prime and an A-linear u:M->M-prime, the induced ring map S_f(u) restricts to f on A and u on M, so the displayed square commutes. Under the checked differential identification, d(m) maps to d(u(m)) and thus 1 tensor m maps to 1 tensor u(m); S_A(M)-linearity gives s tensor m -> S_f(u)(s) tensor u(m). This is exactly the printed S_f(u) tensor_A u, followed by the canonical A-prime balancing implicit in its target.'),('II.1.1.4.1','The inverse-image functor of a geometric morphism preserves finite limits and all colimits. It therefore preserves the tensor product presentation, the multiplication map B tensor_A B->B and its kernel I, as well as the image defining I squared and the quotient I/I squared. The resulting identification is f^{-1}(I/I squared)=(f^{-1}I)/(f^{-1}I)^2, which is Omega(f^{-1}B/f^{-1}A). The construction commutes with maps of ring arrows, proving the claimed canonical functorial isomorphism.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p118_*.png')):f.write(f'| evidence/{p.name} | Printed p118, 800-dpi crop inspected during the first reading. |\n')
print('Page 118 edits and three direct checks recorded.')
