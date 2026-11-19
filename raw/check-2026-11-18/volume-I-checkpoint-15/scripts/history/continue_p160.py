"""Primary reviewer's page160 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='160';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p160}'
ev='LNM239 scan PDF p178 / printed p160: both complete400-dpi halves and ten800-dpi crops personally inspected; all three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('A-algèbre','A-Algèbre').replace('C-modules','C-Modules').replace('$I$.','$I$ .').replace('$J$,','$J$ ,').replace(r'\longrightarrow J$,',r'\longrightarrow J$ ,')
ch('corrected',old,new,'proposition and proof prose','III.p160.withdraw-normalizations','Withdraw two optional capitalizations and three punctuation-space changes.','reading')
bar=r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}'
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p160.upright-Latin','Restore upright printed Latin variables in body and both diagrams.')
 old=region(layer);assert old.count(r'\mathcal X')==4 and old.count(r'\mathcal Y')==3
 ch(layer,old,old.replace(r'\mathcal X','X').replace(r'\mathcal Y','Y'),'extension names','III.p160.plain-extension-names','Restore the seven plain upright X/Y occurrences.')
 old=region(layer);assert old.count('d^1_')==3
 ch(layer,old,old.replace('d^1_','d_'),'three vertical-arrow labels','III.p160.derivation-degrees','Both diagrams print d_B/A or d_C/A without a degree superscript. Remove all three unprinted1 exponents, supported by the two label crops and complete second diagram.','reading')
 ch(layer,r'\xrightarrow{\sim}',bar,'X comparison','III.p160.unheaded-isomorphism','The enlarged alg-diff line shows a tilde above an unheaded bar, not an arrow.')
 old=region(layer)
 if layer=='English':new=old.replace(r'\uline{A-algebra satisfying condition}',r'A-\uline{algebra satisfying condition}')
 else:new=old.replace(r'\uline{A-Algèbre vérifiant la condition}',r'A-\uline{Algèbre vérifiant la condition}')
 ch(layer,old,new,'proposition emphasis','III.p160.underline-prefix','The underline starts at Algèbre, after the A- prefix.')
 old=region(layer);new=old
 new=new.replace(r'\node (bM)  at (177,0)',r'\node[anchor=west] (bM) at (98,0)')
 new=new.replace(r'\node (bN)  at (298,0)',r'\node[anchor=west] (bN) at (253,0)')
 new=new.replace(r'\node (bM)  at (180,0)',r'\node[anchor=west] (bM) at (159,0)')
 new=new.replace(r'\node (bN)  at (260,0)',r'\node[anchor=west] (bN) at (215,0)')
 new=new.replace(r'\draw[->] (tB) -- node[right,xshift=1bp]',r'\draw[->] (tB.south) -- node[right,xshift=1bp]')
 new=new.replace(r'\draw[->] (tC) -- node[right,xshift=1bp]',r'\draw[->] (tC.south) -- node[right,xshift=1bp]')
 new=new.replace(r'\binom{f}{d_{B/A}\otimes1}',r'\left(\begin{array}{@{}l@{}}f\\[8bp]d_{B/A}\otimes1\end{array}\right)')
 new=new.replace(r'\binom{\mathrm{id}}{d_{C/A}}',r'\left(\begin{array}{@{}l@{}}\mathrm{id}\\[8bp]d_{C/A}\end{array}\right)')
 new=new.replace(r'\right)$} (bM);',r'\right)$} (tB.south |- bM.north);')
 new=new.replace(r'\right)$} (bN);',r'\right)$} (tC.south |- bN.north);')
 new=new.replace(r'\draw[->] (tB) -- (bM);',r'\draw[->] (tB.south) -- (tB.south |- bM.north);')
 new=new.replace(r'\node at (378,-1) {$,$};',r'\node[anchor=base] at ([xshift=28bp]b0b.base) {$,$};')
 new=new.replace(r'\node at (350,-1) {$.$};',r'\node[anchor=base] at ([xshift=21bp]b0b.base) {$.$};')
 assert new!=old
 ch(layer,old,new,'both commutative diagrams','III.p160.diagram-geometry','Restore the four printed vertical B/C arrows with column projections and lower-node left alignment; the three two-row arrow labels are left-aligned with their printed row separation. Put the comma and period on the lower-row baseline. All sixteen horizontal and seven downward arrows and their endpoints/labels are retained; final geometry awaits the required build/PDF check.')
 old=region(layer);new=old.replace('$A$-exten-\\par\n\n\\noindent\\hspace*{0.3bp}sions','$A$-extensions')+r'\clearpage'+'\n'
 ch(layer,old,new,'morphism sentence and boundary','III.p160.prose-flow','Join the line-end split inside A-extensions and retain the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p160','Two capitalized terms and three punctuation spaces; supplied added derivation superscripts','Optional normalizations; same added superscripts','Local source-comparison verdict, not a supplied decision-record ID. Withdraw optional normalizations. Remove three shared unprinted derivation exponents; restore diagram geometry, unheaded comparison and emphasis. No original mathematical error found. The proposition proof continues on161.',ev+'evidence/I_p160_diagram-one.png; evidence/I_p160_diagram-two.png; evidence/I_p160_alg-diff.png; evidence/I_p160_proposition.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.9.alg-diff-comparison','For E=Omega_B/A tensor_B C, the map B->C direct-sum E is b->(f(b),db tensor1). Leibniz makes it an A-algebra map. Its composite with C direct-sum E ->C direct-sum Omega_C/A equals j2 f, since differentials commute with f. On I it is i->(0,di), the kernel inclusion in the extension built from diff(X); hence the induced map X->alg(diff(X)) is the identity on kernel I and quotient C and is an isomorphism of extensions. This verifies the first composite on this page.'),('III.1.1.9.reverse-comparison-setup','The defining pullback alg(Y)->Yprime supplies B->C direct-sum J over C. Projection to J is an A-derivation because multiplication in C direct-sum J is square-zero; the B-action on J is through C. By the universal property of differentials it gives precisely the C-linear u:Omega_B/A tensor_B C ->J asserted at the page end. The subsequent diagram and conclusion are on161 and are not counted as read or checked here.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p160_*.png')):
  if p.name!='I_p160_derivation.png':f.write(f'| evidence/{p.name} | Page160 audit:800-dpi crop personally inspected; complete crops supply the Y exponent, continuation and terminal reference. |\n')
 f.write('| evidence/I_p157_footnote.png; evidence/I_p158_footnote.png | Reinspected while checking159: these labels have raised1, unlike the baseline1 in the footnote label on159. No blanket normalization is valid. |\n')
print('Page160 edits, verdict and two partial-proof checks recorded.')
