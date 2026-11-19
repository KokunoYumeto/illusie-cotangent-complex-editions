"""Primary reviewer's page156 audit; run once."""
import sys,csv,re
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='156';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p156}'
ev='LNM239 scan PDF p174 / printed p156: both complete400-dpi halves and nine800-dpi crops personally inspected; all three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('A-algèbres','A-Algèbres').replace("d'anneaux. Le foncteur","d'Anneaux. Le foncteur").replace('« restriction des scalaires »',r'\char34{}restriction des scalaires\char34{}').replace('« oubli »',r'\char34{}oubli\char34{}')
ch('corrected',old,new,'restriction and forgetting prose','III.p156.withdraw-normalizations','Withdraw two optional capitalizations and guillemets; the printed originals are not errors.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','III.p156.upright-Latin','Restore upright Latin mathematics, including the native ring triangle.')
 old=region(layer);assert old.count(r'\mathcal X')==2
 ch(layer,old,old.replace(r'\mathcal X','X'),'restriction-of-scalars assignment','III.p156.plain-X','Both extension identifiers are plain X in the enlarged scan.')
 ch(layer,'$f_* :','$f* :','1.1.5.2','III.p156.baseline-star','The star shares the f baseline, as on155; restore its position. evidence/I_p156_intro-and-fstar.png.')
 ch(layer,r'\node at (112,-4) {$,$};',r'\node[anchor=base] at ([xshift=86bp]A.base) {$,$};','1.1.6.1 terminal comma','III.p156.diagram-comma','Anchor the terminal comma at the bottom vertex baseline, as printed; all three arrow directions and the p label remain unchanged.')
 old=region(layer);pattern=r'\\noindent\\makebox\[0pt\]\[l\]\{([^\n]*)\}\\par'
 new,n=re.subn(pattern,lambda m:m.group(1)+' ',old);assert n==5
 new=new.replace(r'\noindent{de groupes}\par',r'de groupes\par').replace(r'\noindent{of groups}\par',r'of groups\par').replace('\\vspace{1.6bp}\n','')
 ch(layer,old,new,'three continuous prose sentences','III.p156.prose-continuity','Remove five full-line zero-width boxes and their artificial paragraph breaks, preserving the actual prose paragraphs, all displays and every anchor.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p156.boundary','Retain the printed page boundary.','structure')
old=region('English');assert old.count('additively cofibered categories')==2
ch('English',old,old.replace('additively cofibered categories','additive cofibered categories'),'restriction and forgetful functors','III.p156.additive-cofibered','Apply GLOSSARY_SGA_EN_UNIFIED.tsv row132 in both occurrences.','terminology')
old=region('English');assert old.count('``')==2 and old.count("''")==2
ch('English',old,old.replace('``',r'\textquotedbl{}').replace("''",r'\textquotedbl{}'),'restriction and forgetful names','III.p156.straight-quotes','Restore the printed straight quotes around the translated designations.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p156','A-Algèbres, Anneaux and straight quotes','Lowercased terms and guillemets','Local source-comparison verdict, not a supplied decision-record ID. Withdraw optional changes; no original mathematical error found. Seven displayed functor/group maps and the three arrows of1.1.6.1 have the printed types, primes, underlining and directions.',ev+'evidence/I_p156_intro-and-fstar.png; evidence/I_p156_restriction-setup.png; evidence/I_p156_restriction-prose.png; evidence/I_p156_forgetful-setup.png; evidence/I_p156_forgetful-prose.png; evidence/I_p156_triangle.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.5.2.pushout-additivity','For f:M->N, pushing the Baer sum along f equals pushing E times_B F along (m,m-prime)->f(m)+f(m-prime). Pushing the two extensions first and then summing yields the same extension by the pushout universal property and the natural product comparison. These identifications are coherent because f respects all finite sums. The trivial extension B direct-sum M pushes out to B direct-sum N. Thus the direct-image functor is additive between Picard categories and induces the printed homomorphism1.1.5.2.'),('III.1.1.5.3.restriction','For u:C->B and a B-module map v:M->N, the map (E times_B C) amalgamated-over-M N -> (E amalgamated-over-M N) times_B C sends [(e,c),n] to ([e,n],c). It respects ring products, A-maps and the defining relations; it induces identities on kernel N and quotient C, so is an isomorphism. Hence inverse image of extensions preserves cocartesian arrows above restriction of scalars. It also commutes with fiber products and takes the trivial extension to C direct-sum M. The Baer-sum construction therefore gives the asserted Picard functor and1.1.5.3 with source B and target C.'),('III.1.1.5.4.forgetting-base','Under A-prime->A, the underlying ring extension and B-module kernel are unchanged; only the structure map is precomposed. Pushouts (E direct-sum N)/(m,-v(m)), fiber products and the trivial extension remain the same rings and maps, now with their restricted A-prime structure. Cocartesian arrows and all Baer-sum coherences are therefore preserved over the identity on B-Mod, giving exactly the functor and group homomorphism from subscript A to subscript A-prime in1.1.5.4.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p156_*.png')):f.write(f'| evidence/{p.name} | Page156 audit:800-dpi crop personally inspected. |\n')
print('Page156 edits, verdict and three functoriality checks recorded.')
