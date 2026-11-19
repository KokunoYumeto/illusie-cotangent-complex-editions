"""Primary reviewer's page 138 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='138';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p138}'
ev='LNM239 scan PDF p156 / printed p138: both complete 400-dpi halves and ten retained 800-dpi crops personally inspected; three left margins expanded and reinspected. Full source regions read as-printed, corrected, English. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace("d'anneaux simpliciaux", "d'Anneaux simpliciaux").replace('$T$.','$T$ .')
ch('corrected',old,new,'Proposition 2.2.1 hypothesis','II.p138.withdraw-normalizations','The capital Anneaux and the punctuation space are harmless printed conventions; restore both.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p138.upright-Latin','Latin variables and diagram letters are upright in the scan.')
 ch(layer,r'\draw[->] (LXY) -- (FLYZ);',r'\draw[>->] (LXY) -- (FLYZ);','(2.1.5.6) degree-one edge','II.p138.triangle-mark','The left descending edge has an initial forward-pointing head as well as its terminal head; evidence/I_p138_triangle.png.')
 old=region(layer);new=old.replace('baseline=(current bounding box.center)','baseline=(LXY.base)',1).replace(r'\raisebox{25.7bp}[0pt][0pt]{#1}',r'#1')
 ch(layer,old,new,'(2.1.5.6) number alignment','II.p138.triangle-baseline','Align the number with the top vertex baseline directly, removing the former compensating raise; evidence/I_p138_triangle.png.')
 ch(layer,r'\operatorname{Ext}',r'\mathop{\mathbb E\mathrm{xt}}\nolimits','(2.1.5.7)','II.p138.Ext-letterform','The initial E is visibly double-stroked, followed by ordinary upright xt; evidence/I_p138_kodaira-spencer-class.png.')
 ch(layer,r'\overset{\mathrm L}{\otimes}',r'\overset{\ell}{\otimes}','derived-pushout hypothesis','II.p138.derived-tensor-ell','The derived tensor mark is handwritten script ell, not an upright capital L; evidence/I_p138_hypothesis.png.')
 ch(layer,'Kodaira--Spencer','Kodaira-Spencer','name in definition','II.p138.name-hyphen','The printed proper-name separator is a single hyphen, not an en dash; evidence/I_p138_class-description.png.')
 old=region(layer);new=old
 if layer!='English':
  new=new.replace(r'\uline{un topos, et soit}',r'\uline{un topos}, \uline{et soit}').replace(r'\uline{est un isomorphisme.}',r'\uline{est un isomorphisme}.').replace('\\uline{Alors les flèches cano-}\\par\n\\noindent \\uline{niques :}',r'\uline{Alors les flèches canoniques} :')
 else:
  new=new.replace(r'\uline{be a topos, and let}',r'\uline{be a topos}, \uline{and let}').replace(r'\uline{is an isomorphism.}',r'\uline{is an isomorphism}.').replace(r'\uline{Then the canonical maps:}',r'\uline{Then the canonical maps}:')
 ch(layer,old,new,'proposition punctuation and divided word','II.p138.underline-endpoints','The top comma, sentence period and introducing colon lie outside the printed underline. Rejoin canoniques in French; evidence/I_p138_heading-proposition.png and evidence/I_p138_hypothesis.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 ch(layer,old,new,'opening, class definition and hypothesis prose','II.p138.prose-continuity','Join printed line wraps within paragraphs, preserving all nine anchors, the section destination, and every display boundary.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p138.boundary','Retain the printed boundary after the proposition conclusion.','structure')
for old,new,sid in [('We shall write','One will write','notation'),('as we shall see later','as will be seen later','later')]:ch('English',old,new,'Kodaira-Spencer definition','II.p138.impersonal-'+sid,'Render the corresponding French on impersonally under the supplied register standard.','terminology')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p138','Anneaux capital and space before the period after T','Both normalization changes withdrawn','Local source-comparison verdict, not a supplied decision-record ID. No original mathematical error is established on this page.',ev+'evidence/I_p138_hypothesis.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.1.5.6-7.triangle-and-class','Apply the ring transitivity triangle to the three structure sheaves identified on p137. Inverse-image compatibility identifies the first term with f-star L_{Y/Z}; the cotangent complex is degreewise flat, so this ordinary pullback represents its derived pullback. The other terms are L_{X/Z} and L_{X/Y}. Thus the degree-one arrow has source L_{X/Y} and target f-star L_{Y/Z}, giving exactly Ext^1(L_{X/Y},f-star L_{Y/Z}) under the previously checked suspension convention. The degree-zero arrows are the canonical cotangent maps. Taking H_0 of this connective triangle gives f-star Omega^1_{Y/Z}->Omega^1_{X/Z}->Omega^1_{X/Y}->0, agreeing with 1.1.4.5.'),('II.2.2.1.independent-resolution-check','The hypothesis identifies the ordinary pushout B-prime with the derived coproduct of B and A-prime over A. Choose degreewise polynomial simplicial A-resolutions P->B and Q->A-prime; the diagonal polynomial resolution construction is available from 1.2.6. Then P tensor_A Q represents that derived coproduct and maps by a quasi-isomorphism to B-prime. The polynomial differential identity Omega^1_{(P tensor_A Q)/A}=(Omega^1_{P/A} tensor_A Q) direct-sum (P tensor_A Omega^1_{Q/A}) gives, after extension to B-prime, exactly the two summands and the canonical map in (ii). For (i), P tensor_A A-prime represents the same derived pushout and is degreewise polynomial over A-prime; Omega^1_{(P tensor_A A-prime)/A-prime}=Omega^1_{P/A} tensor_A A-prime gives the displayed base-change comparison. The quasi-isomorphism invariance and free comparison of 1.2.6 identify both maps as quasi-isomorphisms. This is an independent check of the statement, its primes and tensor rings; the author\u2019s proof on subsequent pages has not yet been read.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p138_*.png')):f.write(f'| evidence/{p.name} | Printed p138, 800-dpi crop inspected during the first reading. |\n')
print('Page 138 edits, source-difference verdict and two mathematical checks recorded.')
