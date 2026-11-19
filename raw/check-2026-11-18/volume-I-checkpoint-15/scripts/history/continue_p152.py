"""Primary reviewer's page152 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='152';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p152}'
ev='LNM239 scan PDF p170 / printed p152: both complete400-dpi halves and twelve800-dpi page crops personally inspected, plus an800-dpi reread of I3.1.2 on p57. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');assert old.count("d'algèbres")==1 and old.count('B-module')==2 and old.count("d'anneaux")==2
new=old.replace("d'algèbres","d'Algèbres").replace('B-module','B-Module').replace("d'anneaux","d'Anneaux").replace('un anneau $A$','un Anneau $A$').replace('$A$. Pour','$A$ . Pour')
ch('corrected',old,new,'definitions','III.p152.withdraw-normalizations','Withdraw six optional capitalizations and one punctuation-space normalization.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','III.p152.upright-Latin','Printed Latin mathematical letters are upright.')
 ch(layer,r'\mathcal X','X','underlying pair','III.p152.extension-symbol','The extension identifier is printed as plain upright X, consistent with the enlarged p151 symbol.')
 old=region(layer);new=old.replace('    \\draw[->] (Bp) -- (B);\n','',1)
 new=new.replace('    \\draw[->] (A) -- (B);\n    \\node at (120.2,-4.5)', '    \\draw[->] (A) -- (B);\n    \\draw[->,preaction={draw=white,line width=8bp}] (Bp) -- (B);\n    \\node at (120.2,-4.5)',1)
 ch(layer,old,new,'extension-morphism diagram crossing','III.p152.crossing-gap','The horizontal B-prime->B passes over the vertical A->E with a visible gap and no vertex. Draw its white preaction last; retain the separately visible faint A-prime->B-prime arrow and every label.')
 ch(layer,r'\node at (120.2,-4.5) {$.$};',r'\node[anchor=base] at ([xshift=47.1bp]A.base) {$.$};','extension diagram punctuation','III.p152.period-baseline','Align the terminal period with the bottom A baseline.')
 if layer=='English':old='\\par\n\n\\vspace{1.8bp}\\noindent\\hspace*{0.2bp}\\makebox[43.0bp][s]{square}';new='\nsquare'
 else:old='\\par\n\n\\vspace{1.8bp}\\noindent\\hspace*{0.2bp}{commutatif}';new='\ncommutatif'
 ch(layer,old,new,'commutative-square lead-in','III.p152.prose-continuity','Join the single printed sentence and remove the artificial paragraph, spacing and stretched word.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p152.boundary','Retain the printed page boundary.','structure')
ch('English','we shall be especially interested','one will be especially interested','1.1.2 opening','III.p152.impersonal-on','French on s\'intéressera is impersonal.','terminology')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p152','Six capitalized technical words and one punctuation space','Lowercase words and normalized space','Local source-comparison verdict, not a supplied decision-record ID. Withdraw the optional normalizations. No original mathematical error found. Confirm the faint diagonal arrow from A-prime to B-prime, preserve all diagram edges, and restore the nonvertex crossing gap.',ev+'evidence/I_p152_extension-diagram.png; evidence/I_p152_underlying-pair.png; evidence/I_p152_algmod-definition.png; evidence/I_p152_subcategory.png; evidence/I_p152_final-expanded.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.1.pi','A commutative morphism of extension triangles sends I-prime=ker(E-prime->B-prime) into I=ker(E->B). For a local lift e-prime of b-prime and y in I-prime, the induced map t satisfies t(b-prime*y)=t(e-prime*y)=g_E(e-prime)t(y)=g_B(b-prime)t(y). Thus t is B-prime-linear over B-prime->B. Restriction to kernels respects identities and composites, so the displayed association is a functor pi:Exal->Algmod. All nine arrows of the extension diagram and four arrows of the ring square have the stated sources/targets.'),('III.1.1.1.algmod-and-1.1.2','For B-prime->B, extension/restriction of scalars identifies Hom_{B-prime}(I-prime,I) with Hom_B(I-prime tensor_{B-prime}B,I): t maps to i tensor b -> b*t(i), with inverse evaluated at i tensor1. This is exactly the variable-ring module convention in I3.1.2, personally reread on p57. The extra commutative A-square is independent compatible data. Requiring the A-component to be the identity defines Exal_A as a subcategory closed under identities/composition; it is generally not full in Exal, since morphisms with a nonidentity A-endomorphism remain possible in the ambient category.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p152_*.png')):f.write(f'| evidence/{p.name} | Page152 audit:800-dpi crop personally inspected; expanded crops resolve initial edges; ref-p057 is the cited variable-ring module definition. |\n')
print('Page152 edits, verdict and two functor/definition checks recorded.')
