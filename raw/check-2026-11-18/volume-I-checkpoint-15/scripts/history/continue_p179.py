"""Primary reviewer's page179 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='179';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p179}'
ev='LNM239 scan PDF p197 / printed p179: both complete400-dpi halves and eleven800-dpi crops personally inspected; cocartesian-square crop expanded upward and reinspected for the complete i-prime. All three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old,new in [('B-modules','B-Modules'),("d'anneaux","d'Anneaux")]:ch('corrected',old,new,'prose capitalization','III.p179.withdraw-capitalization','Withdraw optional capitalization normalization. evidence/I_p179_map-prose.png; evidence/I_p179_lemma-heading.png.','reading')
for layer in ['corrected','English']:
 pairs=[('(1.3.2.1):',r'(1.3.2.1)\hspace{3.0bp}:'),(r'$Q=P\otimes_A B$.',r'$Q=P\otimes_A B$\hspace{3.0bp}.')]
 for macro,mark in [('FunctorialComplexDefinition',','),('FunctorialRectangle',','),('FunctorialComplexMap',','),('AlmostFreeTriangle','.'),('AlmostFreeExactSequence',','),('AlmostFreeComplexMap',','),('CocartesianSquare',',')]:pairs.append((r'\Illusie'+macro+'POneSeventyNine{'+mark+'}',r'\Illusie'+macro+r'POneSeventyNine{\hspace{3.0bp}'+mark+'}'))
 for old,new in pairs:ch(layer,old,new,'formula punctuation','III.p179.punctuation-spacing','Withdraw optional corrected-French spacing normalization and align English formula punctuation. evidence/I_p179_definition.png; evidence/I_p179_functorial-prose.png; evidence/I_p179_rectangle.png; evidence/I_p179_map-prose.png; evidence/I_p179_triangle.png; evidence/I_p179_exact-sequence.png; evidence/I_p179_complex-map.png; evidence/I_p179_proof-opening.png; evidence/I_p179_cocartesian-square.png.','reading' if layer=='corrected' else 'typesetting')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','body mathematics','III.p179.upright-Latin','Restore upright printed Latin mathematics.')
 old='functorially on'+r'\par'+'\n\n'+r'\noindent (1.3.2.1)' if layer=='English' else 'fonctoriellement'+r'\par'+'\n\n'+r'\noindent de (1.3.2.1)'
 new='functorially on (1.3.2.1)' if layer=='English' else 'fonctoriellement de (1.3.2.1)'
 ch(layer,old,new,'functoriality prose','III.p179.false-paragraph','Join the continuous sentence at the printed line wrap. evidence/I_p179_functorial-prose.png.','structure')
 old=region(layer);new=old
 for letter,x in [('A','124'),('P','176'),('B','228')]:
  new=new.replace(r'\node (bottom'+letter+') at ('+x+r",4) {$"+letter+r"'$};",r'\node[anchor=base west] (bottom'+letter+r') at ([yshift=-54bp]top'+letter+r'.base west) {$'+letter+r"'$};",1)
  new=new.replace(r'([yshift=6bp]bottom'+letter+r'.north);',r'([yshift=6bp]top'+letter+r'.south |- bottom'+letter+r'.north);',1)
 assert new!=old
 ch(layer,old,new,'functoriality rectangle','III.p179.rectangle-column-alignment','Align each primed base letter below its unprimed letter and preserve three vertical comparison arrows. All seven arrows and the centered star tag remain. evidence/I_p179_rectangle.png.')
 for xy,gap in [('266,4','35'),('153,4','26'),('167,4','35')]:ch(layer,r'\node[anchor=west] at ('+xy+r') {#1};',r'\node[anchor=base] at ([xshift='+gap+r'bp]bottomB.base east) {#1};','diagram punctuation','III.p179.diagram-punctuation-baseline','Align the comma or period with the lower-row baseline. evidence/I_p179_rectangle.png; evidence/I_p179_triangle.png; evidence/I_p179_cocartesian-square.png.')
 if layer=='English':ch(layer,'which we leave to the reader to make explicit','which is left to the reader to make explicit','transitivity exercise','III.p179.impersonal-register','French on laisse is impersonal under the supplied standard. evidence/I_p179_map-prose.png.','translation')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p179.page-boundary','Preserve the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p179','Capital Modules/Anneaux and nine punctuation spaces','Lowercase words and omitted spaces','Withdraw these optional normalizations. No original mathematical error identified. Preserve all hypotheses, unlabelled differential and base-change arrows, fourteen diagram arrows, nine other displayed arrows, exact sequence endpoints and emphasis.',ev+'evidence/I_p179_map-prose.png; evidence/I_p179_hypotheses.png; evidence/I_p179_exact-sequence.png; evidence/I_p179_complex-map.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.3.2.functoriality-and-composition','targeted proof check','For a commutative triple (a:A->Aprime,p:P->Pprime,b:B->Bprime), p maps I=ker(P->B) into Iprime and I squared into Iprime squared, hence induces the degree1 map. In degree0 the map sends dx tensor z to d(p(x)) tensor b(z); the relative A relations and tensor relations vanish by commutativity. This is B-linear after restriction along b and commutes with the differential because both routes send the class of x in I to d(p(x)) tensor1. Composing triples composes these formulas literally, proving the identity and transitivity claimed without proof in the text.'),('III.1.3.3.proof-setup','targeted proof check','The maps P->Q=P tensor_A B, p|->p tensor1, and B->Q, b|->1 tensor b, form the displayed cocartesian square by the tensor-product universal property. Since i:A->B is surjective with kernel I, Q is P/IP and i-prime is surjective. The map Q->B induced by j:P->B and id_B is an augmentation with its canonical B-algebra section. These facts validate the setup for the author proof continuing on180; the full exactness assertion has not yet been certified on this page.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p179_*.png')):f.write(f'| evidence/{p.name} | Page179 audit: final800-dpi crop personally inspected. |\n')
print('Page179 repairs, verdict and two checks recorded.')
