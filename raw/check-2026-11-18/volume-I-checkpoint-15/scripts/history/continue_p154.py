"""Primary reviewer's page154 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='154';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p154}'
ev='LNM239 scan PDF p172 / printed p154: both complete400-dpi halves, eleven800-dpi crops and one1600-dpi pushout-sign crop personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');assert old.count('B-modules')==2
new=old.replace('B-modules','B-Modules').replace('$_A$. On','$_A$ . On').replace('« image de $\\mathcal X$ par $v$ »',r'\char34{}image de $\mathcal X$ par $v$\char34{}')
ch('corrected',old,new,'pushout and comparison prose','III.p154.withdraw-normalizations','Withdraw two optional capitalizations, one punctuation-space normalization and replacement of printed straight quotes by guillemets.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','III.p154.upright-Latin','Printed Latin mathematical letters are upright.')
 old=region(layer);assert old.count(r'\mathcal X')==11 and old.count(r'\mathcal Y')==5
 ch(layer,old,old.replace(r'\mathcal X','X').replace(r'\mathcal Y','Y'),'extension identifiers','III.p154.extension-symbols','Restore eleven plain X and five plain Y identifiers, including the morphism diagram; enlarged glyphs agree throughout.')
 ch(layer,r'\mathop{\oplus}\limits^{I}',r'\oplus^{I}','pushout expression','III.p154.pushout-superscript','The I is an upper-right superscript, not a centered limit. Retain the supplied oplus glyph provisionally because its vertical stroke is badly faded; question I-Q018 records the uncertainty.')
 old=region(layer)
 prefix=r'\noindent\makebox[0pt][l]{\hspace*{0.2bp}'
 assert old.count(prefix)==1
 if layer=='English':suffix='morphism}\\par\nof $B$-modules';joined='morphism\nof $B$-modules'
 else:suffix='morphisme}\\par\nde B-Modules';joined='morphisme\nde B-Modules'
 assert old.count(suffix)==1
 ch(layer,old,old.replace(prefix,'',1).replace(suffix,joined,1),'pushout functoriality prose','III.p154.prose-continuity','Remove the zero-width full-line box and artificial paragraph inside the single printed sentence; permit normal reflow.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p154.boundary','Retain the printed page boundary.','structure')
ch('English','“image of $X$ under $v$”',r'\textquotedbl{}image of $X$ under $v$\textquotedbl{}','pushout designation','III.p154.straight-quotes','Restore the straight quotation marks enclosing the translated designation.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p154','Two B-Modules capitals, one punctuation space and straight quotes','Lowercase modules, normalized space and guillemets','Local source-comparison verdict, not a supplied decision-record ID. Withdraw optional normalizations; source comments require no editorial verdict. No original mathematical error found. All twelve arrows in the extension diagram, both headed isomorphisms and the three factorization references agree with the print.',ev+'evidence/I_p154_pushout.png; evidence/I_p154_pushout-sign-1600.png; evidence/I_p154_functoriality.png; evidence/I_p154_associativity-expanded.png; evidence/I_p154_extension-diagram.png; evidence/I_p154_comparison.png; evidence/I_p154_factorization.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.3.pushout','Give E direct-sum J the square-zero semidirect ring multiplication (e,j)(e-prime,j-prime)=(ee-prime,bar(e)j-prime+bar(e-prime)j). B-linearity of v makes {(i,-v(i)):i in I} an ideal: multiplying by (e,j) yields (ei,-v(ei)), since I acts trivially on J. Its quotient E amalgamated-over-I J maps locally surjectively to B. The injection j->[0,j] is monic, and [i,j]=[0,v(i)+j] identifies its image with the kernel, which is square-zero. The canonical e->[e,0] induces id_B and v. Thus (1.1.3.4)–(1.1.3.5) are valid, with the A-structure induced from E.'),('III.1.1.3.pushout-associativity','For v-prime:J->J-prime, the map from the single pushout for v-prime v to the iterated pushout sends [e,j-prime] to [[e,0],j-prime]. Its inverse sends [[e,j],j-prime] to [e,v-prime(j)+j-prime]. The defining relations, multiplication, A-map, quotient B and kernel J-prime are preserved. For a third module map, either route sends a representative to the same sum of successive images of its kernel coordinates; hence the usual cocycle condition holds.'),('III.1.1.4.comparison-factorization','For the displayed morphism f with E->F, u:B->C and v:I->J, regard J as a B-module by u. The map E amalgamated-over-I J -> F times_C B sends [e,j] to (f(e)+j,bar(e)). The relation (i,-v(i)) maps to zero, and the map respects products because J^2=0. It induces identity maps on J and B, hence is an isomorphism of extensions. Explicitly, locally lift b to e and represent (a,b) by [e,a-f(e)]; changing e by i changes the representative by (i,-v(i)), so these inverses glue. Composing E->[e,0], this isomorphism, and projection to F gives f(e). All three referenced arrows therefore have the claimed order and types.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'READING_QUESTIONS.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['I-Q018','154','III.1.1.3.4 pushout sign','The circle and horizontal stroke are clear, but the vertical stroke is largely absent even at1600dpi; tiny central remnants are consistent with a faded plus. Review the glyph and later recurrences on the second reading.','Retain supplied oplus in all three layers provisionally. The upper-right I placement is certain and restored. The pushout construction is independently verified.','first reading retained; second reading pending','evidence/I_p154_pushout.png; evidence/I_p154_pushout-sign-1600.png'])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p154_*.png')):f.write(f'| evidence/{p.name} | Page154 audit:800-dpi crop personally inspected, except pushout-sign-1600 at1600dpi; expanded crops resolve edges. |\n')
print('Page154 edits, verdict, three construction checks and one reading question recorded.')
