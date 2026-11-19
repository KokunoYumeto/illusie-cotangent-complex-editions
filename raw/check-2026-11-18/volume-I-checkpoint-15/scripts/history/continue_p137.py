"""Primary reviewer's page 137 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='137';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p137}'
ev='LNM239 scan PDF p155 / printed p137: both complete 400-dpi halves and eleven retained 800-dpi crops personally inspected; coefficient and ending crops expanded and reinspected. Full source regions read as-printed, corrected, English. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('-modules simpliciaux','-Modules simpliciaux').replace("d'anneaux de", "d'Anneaux de").replace('$,','$ ,').replace('« composé »',r'\textquotedbl{}composé\textquotedbl{}')
ch('corrected',old,new,'definition and coefficient prose','II.p137.withdraw-normalizations','Two capitals, six punctuation spaces and straight quotes are printed conventions, not original errors; restore them. Retain the grammatical repair deux diagrammes.','reading')
for layer in ('corrected','English'):
 ch(layer,r'C=u^{-1}(\mathcal O_Z)',r'C=u^{-1}(\mathcal O_X)','definition of C after (2.1.5.4)','II.p137.structure-sheaf-index','The scan really prints Z: evidence/I_p137_coefficients-first.png. But u has source X-prime and target X, so u^{-1} acts on sheaves on X, and the ring C in the pulled-back triple is u^{-1}(O_X). O_Z is a sheaf on Z and cannot be its argument here. The definition (2.1.5.2), the arrow C->C-prime and the u-star map (2.1.5.5) independently force X.','misprint of the original')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p137.upright-Latin','Printed Latin variables and diagram labels are upright.')
 old=region(layer);new=old.replace(r'\mathcal O',r'\underline{\mathrm{O}}')
 ch(layer,old,new,'all structure sheaves','II.p137.structure-sheaf-font','Each structure sheaf is an underlined upright O, not a calligraphic O; every subscript and inverse-image exponent checked in the retained crops.')
 old=region(layer);new=old.replace('baseline=(current bounding box.center)','baseline=(X.base)',1).replace('baseline=(current bounding box.center)','baseline=(A.base)',1)
 ch(layer,old,new,'(2.1.5.3) and (2.1.5.4) labels','II.p137.diagram-baselines','Both diagram numbers align with the top row in the scan; all arrow directions, labels, empty labels and final comma are retained.')
 old=region(layer);new=old
 for space in ('3.5','1.6','2.0'):new=new.replace('\\par\n\\vspace{'+space+'bp}\n\\noindent ','\n')
 new=new.replace('à (2.1.5.1).\\par\n','à (2.1.5.1).\n').replace('to (2.1.5.1).\\par\n','to (2.1.5.1).\n')
 new=new.replace('\\noindent Elle dépend','Elle dépend').replace('\\noindent It depends','It depends')
 ch(layer,old,new,'definition, coefficients, composition and ending','II.p137.prose-continuity','The scan has continuous paragraphs at these line wraps, including the definition followed by its functoriality sentence. Remove false paragraph breaks and their inserted interline spaces while preserving all ten anchors.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p137.boundary','Retain the printed boundary before the continued distinguished triangle.','structure')
ch('English','For a composite of two diagrams',r'For a \textquotedbl{}composite\textquotedbl{} of two diagrams','composition sentence','II.p137.quotation-omission','The author marks composite with quotation marks; restore this omitted qualification in the English.','translation')
ch('English','which we leave','which is left','composition sentence','II.p137.impersonal','French qu\u2019on laisse is impersonal, not the authors\u2019 nous.','terminology')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p137','deux diagramme; Module and Anneaux capitals; six punctuation spaces and straight quotes','deux diagrammes retained; nine normalization differences withdrawn','Local source-comparison verdict, not a supplied decision-record ID. The plural diagrammes is required after deux; the other differences are unsupported normalization. A newly established mathematical correction replaces O_Z by O_X in C in corrected and English only.',ev+'evidence/I_p137_composition.png and evidence/I_p137_coefficients-first.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.1.5.coefficient-types-and-pullback','The ring triple on X is (gf)^{-1}O_Z -> f^{-1}O_Y -> O_X. Apply u^{-1} to obtain A->B->C on X-prime. Commutativity of the two squares and the ringed-topos structure maps give A->A-prime, B->B-prime, C->C-prime, with primed objects exactly as displayed. This checks all six coefficient types and forces C=u^{-1}O_X. The inverse-image comparison 1.2.3.5 identifies u^{-1}L_{X/Y/Z} with the transitivity sequence of that unprimed triple. Extend scalars along C->C-prime and apply (2.1.1.6)-prime. Since u-star M=u^{-1}M tensor_C C-prime, the resulting map is exactly (2.1.5.5).'),('II.2.1.5.composition-left-to-reader','Write alpha_u:u-star L_{X/Y/Z}->L_{X-prime/Y-prime/Z-prime} for one commutative diagram and alpha_v:v-star L_{X-prime/Y-prime/Z-prime}->L_{X-double-prime/Y-double-prime/Z-double-prime} for a second. Under the canonical inverse-image and tensor-associativity identification (uv)-star=v-star u-star, the required transitivity is alpha_{uv}=alpha_v composed with v-star(alpha_u). This follows degree by degree from the functorial free polynomial resolution maps: a generator is carried first to its image under the first ring map and then under the second, exactly its image under the composite; taking relative differentials and extending scalars preserves the equality. The same applies to all three terms and both maps of the exact sequence, so it is an equality of maps of true triangles, not merely of their derived isomorphism classes. Identity diagrams induce identities. This makes explicit the assertion left to the reader.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p137_*.png')):f.write(f'| evidence/{p.name} | Printed p137, 800-dpi crop inspected during the first reading. |\n')
print('Page 137 edits, source-difference verdict and two proof checks recorded.')
