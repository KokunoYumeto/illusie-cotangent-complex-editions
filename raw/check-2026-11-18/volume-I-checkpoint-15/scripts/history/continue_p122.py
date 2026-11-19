"""Primary reviewer's p122 audit of compatibility and diagonal notation."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='122';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p122}'
ev='LNM239 scan PDF p140 / printed p122: both complete 400-dpi halves and eight retained 800-dpi crops personally inspected; all three complete source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','body and triangle','II.p122.upright-Latin','Latin letters and indices, including the underlined associated-sheaf functor a, are upright.')
 ch(layer,r'\hbox{\text{#1}\hfill',r'\hbox to\linewidth{\text{#1}\hfill','three numbered isomorphisms','II.p122.left-display-labels','All three labels are at the left margin, separate from the centered formulas.')
 old=region(layer);new=old.replace(r'\varinjlim_\lambda',r'\varinjlim')
 ch(layer,old,new,'formula (1.2.1.3)','II.p122.unprinted-limit-indices','evidence/I_p122_filtered-isomorphism.png shows no separate lambda under any of the three limit operators. Lambda remains on A and B. Remove the three supplied implicit indices in all layers.','reading')
 old=region(layer);new=old.replace(r'\xrightarrow{\ \sim\ }',r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}',2)
 ch(layer,old,new,'formulas (1.2.1.3) and (1.2.1.4)','II.p122.unheaded-isomorphisms','The first two isomorphisms have unheaded horizontal bars; the third, (1.2.1.5), has a right arrowhead and is retained. See evidence/I_p122_filtered-isomorphism.png, evidence/I_p122_inverse-image.png and evidence/I_p122_associated-sheaf.png.')
 ch(layer,'baseline=(current bounding box.center)','baseline=(P.base)','diagonal triangle','II.p122.triangle-baseline','The label (1.2.2.1) aligns with the top P-to-B row; all three arrow directions and the lower-right period are confirmed.')
 old=region(layer);new=old.replace(r'\makebox[\dimexpr\linewidth-8bp\relax][s]',r'\makebox[\linewidth][s]').replace(r'\raisebox{22bp}[0pt][0pt]{(1.2.2.1)}','(1.2.2.1)').replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})')
 ch(layer,old,new,'triangle label and both note markers','II.p122.labels-and-note-baselines','Use full-width top-row alignment, and baseline parentheses around a raised note numeral in the diagram and footnote; see evidence/I_p122_diagonal-triangle.png and evidence/I_p122_footnote.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace(r'\vspace{5bp}\hspace*{18bp}',r'\vspace{5bp}\noindent\hspace*{38bp}')
 ch(layer,old,new,'continuous prose and two paragraph indents','II.p122.prose-layout','All supplied internal paragraph breaks are ordinary printed line wraps. The Soit and Enfin paragraphs have approximately 38bp first-line indents, not 18bp.','structure')
 old=region(layer);new=old.replace('"',r'\textquotedbl{}').replace('“',r'\textquotedbl{}').replace('”',r'\textquotedbl{}')
 if old!=new:ch(layer,old,new,'quoted functor names','II.p122.straight-quotes','The original functor names use straight double quotation marks; see evidence/I_p122_local-system.png.')
 old=region(layer);a=old.index(r'\phantomsection\hypertarget{illusie:I:ch1:p122:footnote-1}');seg=old[a:];new=seg.replace(r'\noindent\rule{72bp}{0.35bp}',r'\vfill'+'\n'+r'\noindent\rule{72bp}{0.35bp}')
 assert new.endswith('\\vspace{5bp}\n');new=new[:-len('\\vspace{5bp}\n')]+r'\clearpage'+'\n'
 ch(layer,seg,new,'footnote and page boundary','II.p122.footnote-layout','Retain the short rule and one continuous bottom footnote, then enforce the printed boundary.','structure')
old=region('corrected');new=region('as-printed').replace('% DÉBUT DU FICHIER SOURCE','% BEGIN SOURCE').replace('% FIN DU FICHIER SOURCE','% END SOURCE')
ch('corrected',old,new,'normalization-only differences','II.p122.withdraw-normalizations','The complete enlarged page supports the printed object capitals, straight quotes and spaces before the indicated punctuation. No original error requires any of the fourteen recorded normalization events; restore the diplomatic reading, preserving the corrected file comments.','reading')
ch('English','we obtain a','one obtains a','diagonal construction','II.p122.impersonal-register.1','French on a is impersonal; render it with one under STANDARDS_20261119.md rather than authorial we.','terminology')
ch('English','For brevity, we write','For brevity, one writes','footnote','II.p122.impersonal-register.2','French on ecrit is impersonal, as distinguished from nous in the supplied standard.','terminology')
verdict(page,'ILL-SC-20260804-0119','No original mathematical misprint identified','No new original correction adopted','The filtered/local inductive-limit, inverse-image, associated-sheaf and diagonal constructions are well typed. Missing arrowheads in the first two isomorphisms and suppressed limit indices are actual printed notation, not errors to regularize.',ev)
verdict(page,'ILL-NORM-20260804-0150','Fourteen capitalization, quotation and punctuation-spacing normalizations','All withdrawn','These are printed conventions, and no necessary correction is justified. French layers now differ here only in source comments.',ev)
verdict(page,'ILL-TX-20260804-0146','Twelve anchors including page, named display and triangle macros','All preserved; two unheaded bars, suppressed limit indices, upright notation, prose, indents and note placement restored','All lambdas, inverse-image exponents, degree indices, Delta positions, underline scopes and note markers were enlarged and compared.',ev)
verdict(page,'ILL-TR-20260804-0148','Inductive limits, inverse image, associated sheaf and diagonal construction','Terminology confirmed; two impersonal on constructions repaired','No other meaning change is needed. Diagonal subobjects follows the original wording; no claim of a literal inclusion of the entire bisimplicial object is added.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.p122.filtered-and-local-limits','For a filtered system (A_i->B_i), each polynomial uses finitely many coefficients and generators, so it comes from a common stage, and equality is detected after passing to a later common stage. Thus colim A_i[B_i] identifies with (colim A_i)[colim B_i]. Repeating this argument gives the resolution degree by degree, compatibly with evaluation and free-generator maps. For a locally filtered system over the topos, the same finite lifting and equality arguments hold after a common cover; associated sheaves identify the result. The use of locally filtered here agrees with the category described in the proof of I 4.2.1.3 on the previously reviewed p100; that prior proposition is not reproved by this check.'),('II.p122.inverse-image-and-associated-sheaf','A geometric inverse image preserves finite products and all colimits. The free algebra is formed from finite strings/monomials, coproducts and the algebraic relations, so f^{-1}(A[S]) identifies naturally with f^{-1}(A)[f^{-1}(S)]. Recursion gives (1.2.1.4), and naturality preserves faces, degeneracies and augmentation. The associated-sheaf functor is likewise left exact and colimit preserving, giving (1.2.1.5) by the same construction.'),('II.p122.bisimplicial-and-diagonal-types','For simplicial A->B, forming the free resolution in Simpl(T) gives components P_{A_n}(B_n)_m. Fixing m gives the printed A-algebra row P_A(B)_m; fixing n gives the simplicial A_n-algebra column P_{A_n}(B_n). The original A and B are constant in the new vertical resolution direction. Taking diagonal n=m yields the three displayed ring maps A->P_A^Delta(B)->B and A->B, whose composite is the original structure map by augmentation compatibility. This checks the triangle, without pre-empting later claims about its augmentation.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p122_*.png')):f.write(f'| evidence/{p.name} | Printed p122, 800-dpi crop inspected during the first reading. |\n')
print('Page 122 edits and three mathematical checks recorded.')
