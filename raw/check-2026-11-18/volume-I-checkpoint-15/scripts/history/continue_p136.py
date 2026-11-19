"""Primary reviewer's page 136 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='136';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p136}'
ev='LNM239 scan PDF p154 / printed p136: both complete 400-dpi halves and ten retained 800-dpi crops personally inspected. Full source regions read as-printed, corrected, English. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('« sont »',r'\textquotedbl{}sont\textquotedbl{}').replace(r'$\Omega^1_{B/A}\otimes_B C$.',r'$\Omega^1_{B/A}\otimes_B C$ .').replace('sur $A$,','sur $A$ ,').replace('sur $B$.','sur $B$ .')
ch('corrected',old,new,'opening, free case and corollary','II.p136.withdraw-normalizations','The guillemets and four closed punctuation spaces are editorial normalizations; restore the printed straight quotation marks and spacing.','reading')
ch('as-printed',r'\Omega^1_{C/B/A}\otimes_C',r'\Omega_{C/B/A}\otimes_C','final corollary isomorphism','II.p136.omitted-superscript','The scan has no superscript 1 here: evidence/I_p136_final-isomorphism.png. The diplomatic text must retain that omission. Corrected and English retain the supplied 1 because the object defined in 2.1.4 and used in (2.1.4.1) is the sequence Omega^1; the argument identifies exactly that sequence, not a newly defined Omega.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p136.upright-Latin','Latin variables and tensor/subscript rings are upright in the scan.')
 ch(layer,r'\xrightarrow{\ \sim\ }',r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}','final isomorphism','II.p136.unheaded-isomorphism','The final isomorphism sign is an unheaded bar with a tilde, not a directed arrow; evidence/I_p136_final-isomorphism.png.','reading')
 if layer!='English':
  ch(layer,'\\uline{sont des quasi-isomorphis-}\\par\n\\noindent \\uline{mes, la flèche canonique}',r'\uline{sont des quasi-isomorphismes}, \uline{la flèche canonique}','Proposition 2.1.3','II.p136.proposition-underline','Join the split word and keep the comma outside the printed underline; evidence/I_p136_proposition.png.')
  ch(layer,'\\uline{sont des}\\par\n\\noindent \\uline{quasi-isomorphismes, et que}',r'\uline{sont des quasi-isomorphismes}, \uline{et que}','Corollary 2.1.4.2','II.p136.corollary-underline','The comma after quasi-isomorphismes is outside the printed underline; evidence/I_p136_corollary.png.')
 else:
  ch(layer,'\\uline{are quasi-isomorphisms, the}\\par\n\\noindent \\uline{canonical arrow}',r'\uline{are quasi-isomorphisms}, \uline{the canonical arrow}','Proposition 2.1.3','II.p136.proposition-underline','Keep punctuation outside the corresponding emphasis, as in the scan.')
  old=region(layer);new=old.replace(r'\uline{are quasi-isomorphisms,}',r'\uline{are quasi-isomorphisms},').replace(r'\uline{degreewise, and that}',r'\uline{degreewise}, \uline{and that}').replace(r'\uline{degreewise. There is then}',r'\uline{degreewise}. \uline{There is then}')
  ch(layer,old,new,'Corollary 2.1.4.2','II.p136.corollary-underline','Keep punctuation outside the corresponding emphasis, as in the scan.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace('foncto-\nriel','fonctoriel')
 ch(layer,old,new,'continuous prose','II.p136.prose-continuity','These are printed line wraps within paragraphs, not new paragraphs. Join the divided fonctoriel and preserve all nine anchors.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p136.boundary','Retain the printed boundary after the corollary isomorphism.','structure')
ch('English',"``are''",r'\textquotedbl{}are\textquotedbl{}','opening phrase','II.p136.straight-quotes','Match the printed straight quotation marks.')
ch('English','(respectively, (2.1.1.6)\')','(resp. (2.1.1.6)\')','Proposition 2.1.3','II.p136.resp','Retain the source abbreviation resp. under the supplied terminology standard.','terminology')
ch('English','we obtain:','one obtains:','free-case conclusion','II.p136.impersonal','French on obtient is impersonal under the supplied register standard.','terminology')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p136','Straight quotes; four punctuation spaces; supplied sources all added a superscript 1 in the final formula','Guillemet and spacing normalizations withdrawn; final 1 retained only in corrected and English','Local source-comparison verdict, not a supplied decision-record ID. Missing 1 is an original notational omission: the defined sequence is Omega^1_{C/B/A}, and the corollary compares exactly that sequence after scalar extension. The diplomatic omission is restored.',ev+'evidence/I_p136_definition.png, evidence/I_p136_comparison-map.png, evidence/I_p136_final-isomorphism.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.1.2.H0-and-2.1.3','For constant rings, the cotangent complexes are connective. H_0(L_{B/A} tensor_B^L C)=H_0(L_{B/A}) tensor_B C, and H_0(L)=Omega^1 by 1.2.4.2. Therefore the end of the transitivity long exact sequence is precisely Omega^1_{B/A} tensor_B C -> Omega^1_{C/A} -> Omega^1_{C/B} -> 0, as in 1.1.2.12. For Proposition 2.1.3, apply 1.2.6.2(b) to all three ring pairs in the vertical quasi-isomorphism diagram. Degreewise flatness makes ordinary scalar extension on the displayed cotangent objects compute derived extension. Thus each of the three components is an isomorphism in the derived category; 2.1.2 and the true-triangle criterion I 3.2.4 give the assertion for the adjoint form as well.'),('II.2.1.4.free-sequence-and-corollary','If B is degreewise polynomial over A and C is degreewise polynomial over B, the differential sequence is degreewise split exact: choosing the polynomial variables identifies Omega^1_{C/A} with (Omega^1_{B/A} tensor_B C) direct-sum Omega^1_{C/B}. This proves the missing left injectivity in the general sequence; the printed leading zero and the explicit exception in the preceding sentence are therefore correct. The augmentation maps in 1.2.5.3 are quasi-isomorphisms on the three polynomial pairs, with the first additionally extended from B to C, which is degreewise free. Hence (2.1.4.1) is a quasi-isomorphism of true triangles. All its source and target modules are degreewise flat over C, so ordinary tensoring with C-prime computes derived extension and preserves this quasi-isomorphism. Compose its base change with the inverse of the adjoint quasi-isomorphism of 2.1.3 to obtain exactly the corollary in VT.(C-prime), including the unprimed Omega^1 sequence on the right. This verifies the missing-superscript correction without changing any ring index.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p136_*.png')):f.write(f'| evidence/{p.name} | Printed p136, 800-dpi crop inspected during the first reading. |\n')
print('Page 136 edits, source-difference verdict and two proof checks recorded.')
