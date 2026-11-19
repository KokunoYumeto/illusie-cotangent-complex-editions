"""Primary reviewer's p132 ringed-topos cotangent functoriality audit."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='132';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p132}'
ev='LNM239 scan PDF p150 / printed p132: both complete 400-dpi halves and ten retained 800-dpi crops personally inspected, with four crops expanded to include complete indices, exponents and labels; all three full source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace(r'$\mathcal O_X$-module',r'$\mathcal O_X$-Module').replace('en $f$, dans','en $f$ , dans')
ch('corrected',old,new,'opening definition and augmentation paragraph','II.p132.withdraw-normalizations','The printed Module capital and space before the comma after f are harmless conventions, not original misprints.','reading')
for layer in ['corrected','English']:
 ch(layer,r'\IllusieCotangentRingedTopoiSquareCorrected\par',r'\IllusieCotangentRingedTopoiSquareDiplomatic\par','first commutative square','II.p132.withdraw-added-v','The lower arrow is unnamed in the scan (evidence/I_p132_topoi-square.png). It is a valid commutative square without a letter on that arrow; no formula on this page uses an undefined v, and the explicit reference to (1.1.4.2) supplies the comparison with the previously named square. Adding v is optional annotation, not a mathematically necessary correction. Restore the printed diagram in both layers while preserving both macro definitions.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p132.upright-Latin','All Latin variables, superscript inverse-image symbols and indices are upright in the scan.')
 old=region(layer);new=old.replace(r'\mathcal O',r'\underline{\mathrm{O}}')
 ch(layer,old,new,'definition prose and (1.2.7.1)','II.p132.structure-sheaf','The structure sheaf is an underlined upright O, not a script O; evidence/I_p132_opening.png and evidence/I_p132_definition.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 ch(layer,old,new,'definition and coherence prose','II.p132.prose-continuity','The source makes paragraphs at ordinary typewritten wraps, including the continuation Avec la notation. Restore continuous prose while preserving all headings and displays.','structure')
 oldcomment='% The diplomatic witness omits v from the lower horizontal arrow of the\n% first square; the corrected and English lanes restore it from (1.1.4.2).'
 newcomment='% The printed lower horizontal arrow is unnamed. All layers use the\n% diplomatic macro after review; the historical corrected macro is retained.'
 ch(layer,oldcomment,newcomment,'diagram-carrier comment','II.p132.diagram-comment','Keep the source comment accurate after withdrawing the optional added v; no macro name or definition is removed.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p132.boundary','The page ends after the H_0 comparison (1.2.7.4).','structure')
for layer in ['as-printed','corrected']:
 ch(layer,'compte tenu de (1.2.3.5)','compte tenu de(1.2.3.5)','coherence paragraph','II.p132.printed-reference-spacing','The print has no space between de and this parenthesized reference; evidence/I_p132_coherence.png.')
ch('English','We call the','One calls the','opening definition','II.p132.impersonal-call','On appelle is impersonal under the supplied register standard.','terminology')
ch('English','we leave to the reader','one leaves to the reader','coherence paragraph','II.p132.impersonal-leave','On laisse is impersonal under the supplied register standard.','terminology')
verdict(page,'ILL-SC-20260804-0129','Added v and removed punctuation space','Both withdrawn','An unnamed lower arrow is valid and unambiguous in the cited commutative square. A v label is not necessary to repair a mathematical error. The printed punctuation space is also harmless.',ev)
verdict(page,'ILL-NORM-20260804-0160','Module capitalization','Withdrawn','Retain the printed capital in corrected French.',ev)
verdict(page,'ILL-TX-20260804-0156','Eleven semantic anchors, two squares and four numbered formulas','All retained; upright letters, underlined structure sheaves, reference spacing and prose restored','All diagram arrows and the final H_0 isomorphism have arrowheads as printed. No punctuation is added after either square. Both historical first-square macros remain defined.',ev)
verdict(page,'ILL-TR-20260804-0158','Ringed-topos cotangent construction','Meaning confirmed; unnecessary diagram annotation withdrawn and two impersonal forms applied','The construction uses ordinary structure rings, so L without Delta is the intended simplicial complex. The English formulas follow corrected French.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.2.7.2','Inverse image identifies u^{-1}L_{X/Y} with the cotangent complex for u^{-1}O_X over u^{-1}f^{-1}O_Y by 1.2.3.5. The ring square induced by the given topos square then gives the map after tensoring over u^{-1}O_X with O_Xprime, exactly u^*L_{X/Y}->L_{Xprime/Yprime} by 1.2.3.2 prime. An explicit name for the lower topos arrow is unnecessary to define that square or its induced ring maps.'),('II.1.2.7.transitivity-cocycle','For two successive squares, identify u_prime^*u^* with (u u_prime)^* by inverse-image composition and tensor associativity. At each stage of the canonical polynomial resolution the functorial map sends a generator to the generator indexed by its image. The composite of two such assignments equals the assignment for the composite ring map. Functoriality of differentials and associativity of scalar extension give the same equality for the induced cotangent maps under the canonical pullback identification. For three squares both parenthesizations send every generator and coefficient through the same three ring maps; the canonical inverse-image and tensor associators agree by their universal properties. This supplies the transitivity isomorphism and its cocycle compatibility left to the reader.'),('II.1.2.7.3-and-1.2.7.4','The augmentation of the canonical algebra resolution is natural in every ring map, and taking its universal differential commutes with the map of resolutions. Extending scalars therefore gives the displayed commuting augmentation square, whose bottom map is the differential comparison of 1.1.4.3. Its H_0 identification is the already checked 1.2.4.2 applied to O_X over f^{-1}O_Y, so H_0(L_{X/Y}) is Omega^1_{X/Y}.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p132_*.png')):f.write(f'| evidence/{p.name} | Printed p132, 800-dpi crop inspected during the first reading. |\n')
print('Page 132 edits and three targeted proof checks recorded.')
