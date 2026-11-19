"""Primary reviewer's page171 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='171';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p171}'
ev='LNM239 scan PDF p189 / printed p171: both complete400-dpi halves and eleven800-dpi crops personally inspected; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old,new in [("d'anneaux","d'Anneaux"),('$A$-algèbres','$A$-Algèbres'),('$B$-module','$B$-Module'),('module des parties','Module des parties'),('$B$-algèbre','$B$-Algèbre')]:
 while old in region('corrected'):
  s=region('corrected');p=s.index(old);a=s.rfind('\n',0,p)+1;b=s.find('\n',p);before=s[a:b]
  ch('corrected',before,before.replace(old,new,1),'prose','III.p171.withdraw-capitalization','Withdraw optional capitalization normalization; retain printed usage. evidence/I_p171_definition.png; evidence/I_p171_algebra-case.png.','reading')
for old,new in [(r'\IllusiePrincipalPartsExtensionPOneSeventyOne{,}',r'\IllusiePrincipalPartsExtensionPOneSeventyOne{\hspace{3.0bp},}'),(r'\IllusiePrincipalPartsSplittingValuesPOneSeventyOne{image de}{}',r'\IllusiePrincipalPartsSplittingValuesPOneSeventyOne{image de}{\hspace{3.0bp}}'),('$M$. Tensorisant','$M$ . Tensorisant'),('$M$, on obtient','$M$ , on obtient'),(r'\IllusiePrincipalPartsSequenceMPOneSeventyOne{,}',r'\IllusiePrincipalPartsSequenceMPOneSeventyOne{\hspace{3.0bp},}'),('principales}. Soit','principales} . Soit'),(r'\otimes_B C$.',r'\otimes_B C$ .'),(r'\IllusiePrincipalPartsDerivationPOneSeventyOne{.}',r'\IllusiePrincipalPartsDerivationPOneSeventyOne{\hspace{3.0bp}.}')]:
 ch('corrected',old,new,'prose and displays','III.p171.withdraw-punctuation-spacing','Withdraw optional punctuation-spacing normalization. evidence/I_p171_extension.png; evidence/I_p171_values.png; evidence/I_p171_definition.png; evidence/I_p171_sequence-M.png; evidence/I_p171_algebra-case.png; evidence/I_p171_derivation.png.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p171.upright-Latin','Restore printed upright Latin mathematics.')
 ch(layer,r'd^1_{B/A}',r'd_{B/A}','lemma derivation','III.p171.unprinted-derivation-exponent','The print has d_B/A without a superscript1. evidence/I_p171_derivation.png.','reading')
 for x in [183,209]:
  ch(layer,rf'\node[anchor=west] at ({x},0) {{#1}};',r'\node[anchor=base west] at ([xshift=7bp]zr.base east) {#1};','exact-sequence punctuation','III.p171.punctuation-baseline','Restore the comma to the terminal-zero baseline, retaining the punctuation argument. evidence/I_p171_extension.png; evidence/I_p171_sequence-M.png.')
 old=region(layer);new=old.replace(r'    \node[anchor=west] at (0,0) {$j_1,\ j_2:$};'+'\n','')
 target=r'    \node (bb) at (47,0) {$B$};'
 new=new.replace(target,target+'\n'+r'    \node[anchor=base west] at ([xshift=-47bp]bb.base) {$j_1,\ j_2:$};')
 ch(layer,old,new,'splittings label','III.p171.splittings-label-baseline','Align j1,j2 and the colon with the baseline of B, preserving both parallel arrows. evidence/I_p171_splittings.png.')
 if layer=='English':
  ch(layer,'we have an\\par\n\n\\noindent A-extension','we have an A-extension','opening prose','III.p171.false-opening-paragraph','Remove the false paragraph inside the sentence; the scan shows a line wrap.','structure')
  ch(layer,'one obtains an\\par\n\n\\noindent exact sequence','one obtains an exact sequence','tensoring prose','III.p171.false-sequence-paragraph','Remove the false paragraph inside the sentence.','structure')
  ch(layer,'and the exact\\par\n\n\\noindent{sequence of principal parts}','and the exact sequence of principal parts','algebra-case prose','III.p171.false-algebra-case-paragraph','Restore continuous prose corresponding to the printed sentence.','structure')
  ch(layer,r'\uline{of the $A$-derivation}',r'\uline{of the} $A$-\uline{derivation}','lemma','III.p171.underline-scope','The mathematical A-prefix is outside the underline. evidence/I_p171_lemma.png.')
 else:
  ch(layer,"qu'on a une\\par\n\n\\noindent A-extension","qu'on a une A-extension",'opening prose','III.p171.false-opening-paragraph','Remove a false paragraph at a printed line wrap.','structure')
  ch(layer,'on obtient une\\par\n\n\\noindent suite exacte','on obtient une suite exacte','tensoring prose','III.p171.false-sequence-paragraph','Remove a false paragraph at a printed line wrap.','structure')
  old=region(layer);new=old.replace(r'\uline{Module des parties princi-}',r'\uline{Module des parties principales}').replace(r"\uline{pales d'ordre un de}",r"\uline{d'ordre un de}")
  ch(layer,old,new,'definition','III.p171.line-end-hyphen','Join the word principales across the print line break while retaining both anchors and the underlined definition. evidence/I_p171_definition.png.','structure')
  ch(layer,r'\uline{de la $A$-dérivation}',r'\uline{de la} $A$-\uline{dérivation}','lemma','III.p171.underline-scope','The mathematical A-prefix is outside the underline. evidence/I_p171_lemma.png.')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p171.page-boundary','Preserve the printed page boundary.','structure')
ch('English','that we have an A-extension','that one has an A-extension','opening','III.p171.impersonal-on','French qu-on a is impersonal; the opening Recall is retained.','translation')
for old,new in [(r'\IllusiePrincipalPartsExtensionPOneSeventyOne{,}',r'\IllusiePrincipalPartsExtensionPOneSeventyOne{\hspace{3.0bp},}'),(r'\IllusiePrincipalPartsSplittingValuesPOneSeventyOne{the image of}{}',r'\IllusiePrincipalPartsSplittingValuesPOneSeventyOne{the image of}{\hspace{3.0bp}}'),(r'\IllusiePrincipalPartsSequenceMPOneSeventyOne{,}',r'\IllusiePrincipalPartsSequenceMPOneSeventyOne{\hspace{3.0bp},}'),(r'\IllusiePrincipalPartsDerivationPOneSeventyOne{.}',r'\IllusiePrincipalPartsDerivationPOneSeventyOne{\hspace{3.0bp}.}')]:
 ch('English',old,new,'display punctuation','III.p171.English-formula-agreement','Keep English display punctuation/spacing aligned with the corrected French and print.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p171','Printed capitalization and spacing','Nine capitalization and eight spacing normalizations','Withdraw these optional normalizations. No original mathematical error identified. Restore the unprinted exponent on d, upright mathematics, underlining scope, punctuation/label baselines, continuous prose and page boundary. Underlined Exal is printed and retained as the extension category.',ev+'evidence/I_p171_lemma.png; evidence/I_p171_derivation.png; evidence/I_p171_definition.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.6.1-4.principal-parts','targeted proof check','The augmentation P1_B/A->B is split by j2 as a right B-module map. Hence tensoring with any M preserves its exact kernel sequence without assuming M flat. The left j1 action makes the result B-linear, and for a B-algebra C the tensor product is an algebra with square-zero ideal Omega1_B/A tensor_B C. This verifies the exactness and extension assertions in1.2.6.3 and1.2.6.4.'),('III.1.2.6.5.direct-comparison','targeted proof check','Personally reinspected the formula d(b)=1 tensor b-b tensor1 on115 (II1.1.2.5). In coordinates defined by the right splitting j2, P1_B/A is B plus Omega1_B/A and j1(b)=(b,-d(b)). Tensoring on the right with C gives C plus (Omega1_B/A tensor_B C), with left B-algebra structure b |-> (f(b),-d(b) tensor1). This is exactly partial(d_B/A tensor1) under the convention verified on170. The identification is canonical, is the identity on kernel and quotient, and proves the lemma directly; the author proof on172 remains unread at this moment.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p171_*.png')):f.write(f'| evidence/{p.name} | Page171 audit:800-dpi crop personally inspected. |\n')
 f.write('| evidence/I_p115_canonical-derivation.png | Personally reinspected for171: sign convention d=j2-j1. |\n')
print('Page171 edits, verdict and two checks recorded.')
