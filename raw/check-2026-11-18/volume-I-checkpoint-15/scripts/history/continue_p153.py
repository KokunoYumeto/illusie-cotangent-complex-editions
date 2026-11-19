"""Primary reviewer's page153 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='153';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p153}'
ev='LNM239 scan PDF p171 / printed p153: both complete400-dpi halves and nine800-dpi crops personally inspected, including an expanded functoriality line. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old
for a,b,n in [('B-module','B-Module',2),("d'anneaux","d'Anneaux",1),('un anneau','un Anneau',1),("d'algèbres","d'Algèbres",1),('A$-algèbres','A$-Algèbres',2),('C-module','C-Module',1),('$B$. Enfin,','$B$ . Enfin,',1),('$I$, les','$I$ , les',1),('$A$, $B$','$A$ , $B$',1),('$I$.\\par','$I$ .\\par',1),('$T$, et','$T$ , et',1),('$_A$, dont','$_A$ , dont',1),('$(u,\\operatorname{id}_I)$.','$(u,\\operatorname{id}_I)$ .',1),('« image de $\\mathcal X$ par $u$ »',r'\char34{}image de $\mathcal X$ par $u$\char34{}',1)]:
 assert new.count(a)==n,(a,new.count(a));new=new.replace(a,b)
ch('corrected',old,new,'definitions and pullback','III.p153.withdraw-normalizations','Withdraw eight optional capitalizations, seven punctuation-space normalizations and guillemets; the print has straight quotation marks.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','III.p153.upright-Latin','Printed Latin mathematical letters are upright.')
 old=region(layer);assert old.count(r'\mathcal X')==7
 ch(layer,old,old.replace(r'\mathcal X','X'),'extension identifiers','III.p153.extension-symbol','Restore all seven plain upright X identifiers; the enlarged extension, pullback and associativity displays agree with pp151–152.')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p153.boundary','Retain the printed page boundary.','structure')
ch('English','“image of $X$ under $u$”',r'\textquotedbl{}image of $X$ under $u$\textquotedbl{}','pullback designation','III.p153.straight-quotes','Restore the straight quotation marks enclosing the translated designation.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p153','Eight capitalized technical words, seven punctuation spaces and straight quotes','Lowercase words, normalized spaces and guillemets','Local source-comparison verdict, not a supplied decision-record ID. Withdraw the optional normalizations. No original mathematical error found. Preserve every sequence arrow, the headed associativity isomorphism, its primes, and all category subscripts.',ev+'evidence/I_p153_variable-category.png; evidence/I_p153_fixed-category.png; evidence/I_p153_extension.png; evidence/I_p153_u-and-quote.png; evidence/I_p153_pullback-sequence.png; evidence/I_p153_module-and-map.png; evidence/I_p153_functoriality-expanded.png; evidence/I_p153_cocycle-isomorphism.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.3.pullback','For E->B with square-zero kernel I and u:C->B, E times_B C->C is locally surjective: a local lift of u(c) pairs with c. Its kernel is i->(i,0), hence I, and the product of two kernel elements is zero. For a local lift (e,c), multiplication on (i,0) gives (ei,0), which equals u(c)i under the original B-action. Thus the induced C-action is restriction by u. The first projection is an A-algebra morphism of extensions, inducing u on quotients and id_I on kernels, so pi sends it to (u,id_I). The categories with fixed A,B and then fixed I are closed under composition/identity by their defining conditions.'),('III.1.1.3.associativity','For u-prime:C-prime->C, the canonical map E times_B C-prime -> (E times_B C) times_C C-prime sends (e,c-prime) to ((e,u-prime(c-prime)),c-prime). The inverse forgets the forced middle coordinate. Both maps preserve A, C-prime and I and are ring maps; therefore the displayed arrow is an isomorphism in Exal_A(C-prime,I). For u-double-prime:C-double-prime->C-prime, both composites insert the same coordinates u-prime u-double-prime(c-double-prime), u-double-prime(c-double-prime), c-double-prime. This proves the claimed cocycle condition by the fiber-product universal property, without assuming global sections of E->B are surjective.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p153_*.png')):f.write(f'| evidence/{p.name} | Page153 audit:800-dpi crop personally inspected; expanded functoriality crop supplies the complete top edge. |\n')
print('Page153 edits, verdict and two pullback/coherence checks recorded.')
