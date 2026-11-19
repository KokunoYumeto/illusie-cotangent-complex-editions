"""Primary reviewer's page155 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='155';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p155}'
ev='LNM239 scan PDF p173 / printed p155: both complete400-dpi halves, ten800-dpi page crops, two1600-dpi star-placement crops, and two800-dpi reference crops at printed114–115 personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected')
new=old.replace("d'anneaux","d'Anneaux").replace('B-modules','B-Modules').replace("l'algèbre","l'Algèbre").replace('$B$.','$B$ .').replace('[17],','[17] ,').replace('$M$,','$M$ ,').replace(r'$\mathcal X$,',r'$\mathcal X$ ,').replace('(loc. cit.) que','(loc. cit.)que')
assert new!=old
ch('corrected',old,new,'cofibered category and extensions prose','III.p155.withdraw-normalizations','Withdraw four capitalization changes, four punctuation-space normalizations, and the optional space after loc. cit.; these do not correct a demonstrated textual or mathematical error.','reading')
for layer in ['corrected','English']:
 ch(layer,'SGA 4 XVIII 1.4.2',r'SGA 4 XVIII\hspace{19bp}','Picard-definition reference','III.p155.withdraw-added-reference','The scan has a blank after XVIII. Restore the broad printed reference: adding 1.4.2 is an editorial precision, not an established necessary correction. No author erratum on this page.','reading')
ch('English',"an ``additively cofibered \ncategory''","an ``additive cofibered \ncategory''",'cofibered category designation','III.p155.additive-cofibered','GLOSSARY_SGA_EN_UNIFIED.tsv row132 fixes categorie cofibree additive as additive cofibered category.','terminology')
for layer in LAYERS:
 old=region(layer);assert old.count(r'\ReflowBodyFont ')==2
 ch(layer,old,old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath'),'Latin notation','III.p155.upright-Latin','Restore upright printed Latin mathematical letters in body and footnotes.')
 old=region(layer);assert old.count(r'\mathcal X')==3
 ch(layer,old,old.replace(r'\mathcal X','X'),'extension identifiers','III.p155.extension-symbols','Three plain upright X identifiers appear in the enlarged print, not calligraphic X.')
 old=region(layer)
 if layer=='corrected':
  assert old.count('« ')==4 and old.count(' »')==4
  new=old.replace('« ',r'\textquotedbl{}').replace(' »',r'\textquotedbl{}')
 else:
  assert old.count('``')==4 and old.count("''")==4
  new=old.replace('``',r'\textquotedbl{}').replace("''",r'\textquotedbl{}')
 ch(layer,old,new,'four quoted designations','III.p155.straight-quotes','Four pairs of straight quotation marks are visible in the print.')
 old=region(layer);assert old.count(r'\operatorname{pr}_{1*}')==1 and old.count(r'\operatorname{pr}_{2*}')==1 and old.count('$f_*\\ :\\')==1
 new=old.replace(r'\operatorname{pr}_{1*}',r'\operatorname{pr}_1*').replace(r'\operatorname{pr}_{2*}',r'\operatorname{pr}_2*').replace('$f_*\\ :\\','$f*\\ :\\')
 ch(layer,old,new,'product and direct-image functors','III.p155.baseline-stars','At1600dpi the stars have the text baseline; only 1 and 2 are lowered. Restore those positions without changing the direct-image notation or its meaning. evidence/I_p155_product-stars-1600.png; evidence/I_p155_direct-star-1600.png.')
 old=region(layer);assert old.count(r'\textsuperscript{(1)}')==2 and old.count(r'\textsuperscript{(2)}')==2
 new=old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})').replace(r'\textsuperscript{(2)}',r'(\textsuperscript{2})')
 new=new.replace(r'catégories(\textsuperscript{1})',r'catégories (\textsuperscript{1})').replace(r'categories(\textsuperscript{1})',r'categories (\textsuperscript{1})').replace(r'$.('+'\\textsuperscript{2})',r'$. (\textsuperscript{2})')
 ch(layer,old,new,'footnote calls and labels','III.p155.footnote-parentheses','Both body calls and both footnote labels have baseline parentheses around a raised digit; retain the printed separation before each body call.')
 old=region(layer)
 if layer=='English':
  new=old.replace('induces\\par\n\n\\noindent\\hspace*{1.0bp}{a functor}\\par','induces a functor\\par').replace('not need\\par\n\n\\noindent\\hspace*{-2.7bp}{this property.}\\par','not need this property.\\par')
  foot=r'\noindent\hspace*{-2.7bp}{(\textsuperscript{2}) A direct verification of these properties is moreover trivial.}\par'
  plain=r'(\textsuperscript{2}) A direct verification of these properties is moreover trivial.\par'
 else:
  new=old.replace('induit\\par\n\n\\noindent\\hspace*{1.0bp}{un foncteur}\\par','induit un foncteur\\par').replace("n'aurons\\par\n\n\\noindent\\hspace*{-2.7bp}{pas besoin de cette propriété.}\\par","n'aurons pas besoin de cette propriété.\\par")
  foot=r"\noindent\hspace*{-2.7bp}{(\textsuperscript{2}) La vérification directe de ces propriétés est d'ailleurs triviale.}\par"
  plain=r"(\textsuperscript{2}) La vérification directe de ces propriétés est d'ailleurs triviale.\par"
 assert foot in new
 new=new.replace(foot,plain).replace(r'\vspace{4.6bp}',r'\vfill'+'\n'+r'\vspace{4.6bp}')
 ch(layer,old,new,'introductory prose and two footnotes','III.p155.prose-and-footnote-placement','Join the two artificial mid-sentence paragraph breaks and remove the second-note line box; keep the two notes distinct and at the foot of the printed page.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p155.boundary','Retain the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p155','Four capitals, four punctuation spaces, no space after loc. cit., straight quotes and blank after SGA4 XVIII','Optional normalizations, guillemets, and inserted 1.4.2 locator','Local source-comparison verdict, not a supplied decision-record ID. Withdraw optional normalizations and added locator. No original mathematical error found. Retain English terminal category for categorie ponctuelle: the term denotes the one-object one-arrow category, not a translation of objet final. All math definitions, references to II1.1.1.3–4 and distinction of underlined category from un-underlined class group are preserved.',ev+'evidence/I_p155_picard-expanded.png; evidence/I_p155_class-group.png; evidence/I_p155_neutral-and-automorphisms.png; evidence/I_p155_splittings.png; evidence/I_p155_footnotes.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.5.cofibration-product','For a module map v:I->J, a map E->F of extensions over B whose kernel map is wv factors uniquely through E amalgamated-over-I J by [e,j]->f(e)+w(j); the defining relation and square-zero product verify this formula. Thus the pushout arrow is cocartesian. Over0 every extension is canonically B and every arrow is its identity. A quasi-inverse to the displayed product functor sends (E_M,E_N) to E_M times_B E_N. Its projection pushouts map to E_M and E_N by maps inducing identities on quotient and respective kernel, hence are isomorphisms. Conversely E->(pr1*E) times_B (pr2*E) induces identity on B and M times N, hence is an isomorphism. These maps commute with extension morphisms, so give natural quasi-inverses.'),('III.1.1.5.Picard-abelian-group','The Baer sum of E and F is the pushout of E times_B F along M direct-sum M ->M, (m,n)->m+n. Rebracketing tuples and permuting coordinates supply associativity and symmetry; both sides of each coherence diagram have the same representative tuple and summed kernel coordinate, hence agree. All extension morphisms fixing B,M are isomorphisms by the exact rows. The unit is B direct-sum M: (e,(bar(e),m)) maps to e+m and descends to the required unit isomorphism. The inverse is pushout by -id_M: the diagonal in E times_B E is killed on its kernel after the pushout by (m,n)->m-n, so factors through B and splits that sum. For E plus E, the difference between a pair and its flip is (m,-m), killed by summation, giving identity self-symmetry. These constructions prove the asserted Picard structure and abelian group of isomorphism classes.'),('III.1.1.5.automorphisms-splittings','If phi fixes kernel M and quotient B of E, delta=phi-id maps E to M, vanishes on M and factors uniquely as D:B->M. Multiplicativity and M^2=0 give D(bb-prime)=bD(b-prime)+b-prime D(b); the fixed A-map gives D|A=0. Conversely id_E+Dq is an extension automorphism with inverse id_E-Dq. Composition adds derivations. This canonical description requires no chosen splitting. On B direct-sum M it is the shear (b,m)->(b,m+D(b)); its restriction to b->(b,0) is the map b->b+D(b) printed in II(1.1.1.4), inspected again at800dpi. The square-zero algebra itself is II(1.1.1.3), also reinspected. If s:B->E is one splitting, every other is s+D and their differences are exactly A-derivations, proving the empty-or-torsor assertion and its identification with isomorphisms to the trivial extension.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p155_*.png')):f.write(f'| evidence/{p.name} | Page155 audit:800-dpi crop personally inspected; product-stars-1600 and direct-star-1600 at1600dpi; two reference crops from printed114–115. |\n')
print('Page155 edits, verdict and three mathematical checks recorded.')
