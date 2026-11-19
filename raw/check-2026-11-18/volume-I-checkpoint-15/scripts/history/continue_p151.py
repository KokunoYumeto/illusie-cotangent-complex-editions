"""Primary reviewer's page151 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='151';anchor=r'\begin{illusiebodypage}{illusie:I:ch3:p151}'
ev='LNM239 scan PDF p169 / printed p151: both complete400-dpi halves, thirteen800-dpi crops and one1600-dpi extension-symbol crop personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');assert old.count("d'algèbres")==3 and old.count('B-module')==2
new=old.replace("d'algèbres","d'Algèbres").replace("commutatif d'anneaux","commutatif d'Anneaux").replace('un idéal $I$','un Idéal $I$').replace('B-module','B-Module').replace('$I$. Les','$I$ . Les')
ch('corrected',old,new,'definitions and heading','III.p151.withdraw-normalizations','Withdraw seven optional capitalizations and one punctuation-space normalization; the introductory anneaux remains lowercase as printed.','reading')
for layer in LAYERS:
 old=region(layer);assert old.count(r'\ReflowBodyFont ')==4
 ch(layer,old,old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath'),'Latin notation','III.p151.upright-Latin','Printed Latin mathematical letters are upright at all four font sites.')
 old=region(layer);assert old.count(r'\mathcal X')==2
 ch(layer,old,old.replace(r'\mathcal X','X'),'extension object symbol','III.p151.extension-symbol','The enlarged prose glyph and triangle label are plain X, not a calligraphic character. evidence/I_p151_extension-symbol-1600.png; evidence/I_p151_triangle.png.')
 if layer=='English':
  pairs=[(r'\uline{$A$-extension of}',r'$A$-\uline{extension of}'),(r'\uline{by the $B$-module}',r'\uline{by the} $B$-\uline{module}')]
 else:pairs=[(r'\uline{$A$-extension de}',r'$A$-\uline{extension de}'),(r'\uline{par le B-Module}',r'\uline{par le} B-\uline{Module}')]
 for old,new in pairs:ch(layer,old,new,'extension terminology','III.p151.underline-scope','The prefixes A- and B- are outside the printed underlines; preserve the emphasized words.')
 old=region(layer);assert old.count(r'\textsuperscript{(1)}')==2
 ch(layer,old,old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})'),'note call and note label','III.p151.note-parentheses','The note parentheses are on the baseline; only the digit is raised.')
 ch(layer,r'\node at (160,-1) {$;$};',r'\node[anchor=base] at ([xshift=31.4bp]A.base) {$;$};','triangle punctuation','III.p151.semicolon-baseline','Align the printed semicolon with the bottom A baseline.')
 old=region(layer);new=old.replace('\\par\n\n\\vspace{1.6bp}\n','\n')
 ch(layer,old,new,'category lead-in','III.p151.prose-continuity','Remove the artificial paragraph and gap within the sentence introducing the category.','structure')
 ch(layer,r'\phantomsection\hypertarget{illusie:I:ch3:S1:1:1:eq1:n1}',r'\par\vfill'+'\n'+r'\phantomsection\hypertarget{illusie:I:ch3:S1:1:1:eq1:n1}','footnote placement','III.p151.footnote-bottom','Keep the complete ruled note at the printed page foot.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p151.boundary','Retain the printed chapter-opening page boundary.','structure')
old=region('English');assert old.count('A chain of results on algebra extensions')==2
ch('English',old,old.replace('A chain of results on algebra extensions','Sorites on algebra extensions'),'section heading and destination title','III.1.1.Sorites','Apply the established glossary sorite -> sorites and the p114 decision consistently, retaining all destination identifiers.','terminology')
for old,new in [('in $T$ we mean a commutative diagram','in $T$ one means a commutative diagram'),('We say that $X$','One says that $X$')]:ch('English',old,new,'definition','III.p151.impersonal-on','French on entend and On dit are impersonal; retain We review for Nous passons en revue.','terminology')
ch('English',"In view of this chapter's heading",'In view of the opening convention of this chapter','footnote','III.p151.chapeau','Le chapeau coiffant ce chapitre refers to the opening convention that rings are commutative and unital, which removes ambiguity in Exal; heading incorrectly directs the reader to the title.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p151','Seven capitalized technical words and one punctuation space','Lowercase technical words and normalized space','Local source-comparison verdict, not a supplied decision-record ID. Withdraw these optional normalizations; no original mathematical error found. Restore the plain extension symbol X in all layers and the glossary heading in English.',ev+'evidence/I_p151_headings.png; evidence/I_p151_definition-expanded.png; evidence/I_p151_kernel.png; evidence/I_p151_extension-terminology.png; evidence/I_p151_extension-symbol-1600.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
outcome='For p:E->B an epimorphism of ring sheaves with kernel I and I^2=0, a local section b of B has local lifts x to E. Define b*y=xy for y in I. Two lifts differ by i in I, so their products differ by iy=0; hence the local actions agree and glue. Additivity, associativity and the unit law descend from the E-action. The same local-lift argument forces uniqueness. This uses sheaf-local surjectivity and does not assume that E(U)->B(U) is surjective on every object U. The triangle correctly records A->E->B with its given A->B composite.'
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['III.1.1.1.kernel-module',now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p151_*.png')):f.write(f'| evidence/{p.name} | Page151 audit:personally inspected at1600dpi where named, otherwise800dpi; expanded definition resolves initial lower edge. |\n')
print('Page151 edits, verdict and kernel-module proof check recorded.')
