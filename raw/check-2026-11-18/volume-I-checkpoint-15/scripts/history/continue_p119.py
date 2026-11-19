"""Primary reviewer's p119 audit, including two original index/target defects."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='119';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p119}'
ev='LNM239 scan PDF p137 / printed p119: both complete 400-dpi halves and nine retained 800-dpi crops personally inspected; two crops regenerated with complete margins and reread. All three full source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 old=region(layer);new=old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath').replace(r'\mathcal O',r'\underline{\mathrm{O}}')
 ch(layer,old,new,'body, diagrams and principal parts','II.p119.upright-and-structure-sheaf','The four structure-sheaf O symbols in evidence/I_p119_principal-parts.png are underlined upright O, not script O. Other Latin variables and indices are upright.')
 ch(layer,r'\hbox{\text{#1}\hfill$\displaystyle #2$\hfill',r'\hbox to\linewidth{\text{#1}\hfill$\displaystyle #2$\hfill','principal-parts label','II.p119.left-display-label','The displayed definition has its number at the left, apart from the centered formula.')
 old=region(layer);a=old.index(r'\providecommand{\IllusieRingedTopoiSquare}');b=old.index('% FIN DU' if layer=='as-printed' else '% END SOURCE',a);seg=old[a:b]
 ch(layer,seg,seg.replace('baseline=(current bounding box.center)','baseline=(X.base)'),'ringed square label alignment','II.p119.square-baseline','The number (1.1.4.2) aligns with the upper X row, not the square center; preserve both named diagram macros and all arrow directions.')
 ch(layer,r'\makebox[\dimexpr\linewidth-16bp\relax][s]',r'\makebox[\linewidth][s]','ringed square label','II.p119.square-linewidth','The diagram label occupies the same left margin as the other numbered display.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 ch(layer,old,new,'prose and footnote wraps','II.p119.join-line-wraps','The supplied paragraph breaks before de T, Simpl(T), appliquée, u, s’identifie, le topos, dans la diagonale, de X and the final note reference are ordinary printed line wraps.','structure')
 old=region(layer);a=old.index(r'\phantomsection\hypertarget{illusie:I:ch1:p119:inverse-image-differentials-cont}');b=old.index(r'\phantomsection\hypertarget{illusie:I:ch1:p119:simplicial-transition-square}',a);seg=old[a:b]
 new=seg.replace('\\par\n\n','\n').replace(r'\noindent qui','qui').replace(r'\noindent which','which')
 ch(layer,seg,new,'opening paragraph across anchor','II.p119.join-opening','Autre exemple, qui nous sera utile is one continuous sentence. Preserve the internal semantic anchor without adding a paragraph.','structure')
 old=region(layer);new=old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})')
 ch(layer,old,new,'both note markers','II.p119.note-marker-baselines','Both note markers have baseline parentheses and a raised numeral, as shown in the definitions and footnote crops.')
 old=region(layer);a=old.index(r'\phantomsection\hypertarget{illusie:I:ch1:p119:footnote-1}');seg=old[a:]
 new=seg.replace(r'\noindent\rule{72bp}{0.35bp}',r'\vfill'+'\n'+r'\noindent\rule{72bp}{0.35bp}').replace(r'\begin{minipage}{\dimexpr\linewidth-16bp\relax}',r'\begin{minipage}{\linewidth}').replace('``',r'\textquotedbl{}').replace("''",r'\textquotedbl{}')
 assert new.endswith('\\vspace{5bp}\n');new=new[:-len('\\vspace{5bp}\n')]+r'\clearpage'+'\n'
 ch(layer,seg,new,'footnote and boundary','II.p119.note-layout','The note uses straight double quotation marks, is a single paragraph below a short rule, and ends the page; restore full text width and bottom placement.','structure')
ch('as-printed',r'$\Omega^1_{B_n/A_n}$ (via',r'$\Omega^1_{B^n/A^n}$ (via','first degree-component formula','II.p119.simplicial-superscript-misprint','evidence/I_p119_degree.png clearly has superscript n on B and A here, unlike the later subscripted component maps and diagram. Restore the original defect diplomatically. Corrected/English subscript n is necessary for simplicial degree evaluation.','reading')
old=region('corrected');new=old.replace("d'anneaux","d'Anneaux").replace('-module','-Module').replace("l'anneau","l'Anneau").replace('le module','le Module').replace('À un carré','A un carré')
ch('corrected',old,new,'five capitals and initial A','II.p119.withdraw-normalizations','Five capitalizations and the unaccented sentence-initial A are printed conventions; none is a necessary correction.','reading')
ch('English','fibers. Another example,','stalks. Another example,','opening sentence','II.p119.stalk-standard','This is the inverse image of a sheaf at a point; STANDARDS_20261119.md requires stalk for the fibre of a sheaf, and fiber for a morphism.','terminology')
ch('English','which will be useful below,','which will be useful to us below,','simplicial example','II.p119.restore-nous','The French explicitly says qui nous sera utile; restore the authorial us omitted by the supplied English.','translation')
ch('English',r'We call $P^n_{X/Y}$ the ring',r'$P^n_{X/Y}$ is called the ring','first definition','II.p119.impersonal-register.1','The French On dit que is impersonal; the supplied standard requires the passive or one for on and reserves we for nous.','terminology')
ch('English',r'We call $\Omega^1_{X/Y}$ the module',r'$\Omega^1_{X/Y}$ is called the module','second definition','II.p119.impersonal-register.2','The same explicit impersonal-register rule applies to the second On dit que.','terminology')
verdict(page,'ILL-SC-20260804-0116','f:X->X','f:X->Y retained and confirmed','The displayed O_Y and relative X/Y objects require f to have target Y; an arbitrary endomorphism of X would not even define f^{-1}(O_Y). Add the previously unrecorded superscript n defect in the first simplicial differential term: diplomatic restored; corrected and English subscript n retained.',ev)
verdict(page,'ILL-NORM-20260804-0147','Five printed object capitals and unaccented A','All six normalizations withdrawn','No grammatical or mathematical defect justified these changes.',ev)
verdict(page,'ILL-TX-20260804-0143','Nine anchors including page and two named squares','All preserved; original first superscripts, underlined O, label alignment, continuous prose and note typography restored','Both squares and all small signs inspected. The second occurrence of 1.1.4 and its formula number 1.1.4.1 genuinely repeat p118; numbering is retained pending cross-reference audit, not silently regularized.',ev)
verdict(page,'ILL-TR-20260804-0145','Stalks of sheaves, simplicial components, ringed topoi and specified isomorphism','Stalk terminology and impersonal definitions corrected under the standard; omitted us restored','Other meanings remain faithful. The last square begins a sentence continued on p120; no completion is invented.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.p119.simplicial-components','Evaluation at [n] in the simplicial topos preserves the limits and colimits involved in I/I squared, so the degree-n component is Omega(B_n/A_n). A simplex map u:[m]->[n] induces ring maps B_n->B_m and A_n->A_m; functoriality of differentials gives the printed direction from degree n to degree m. This checks all four diagram indices and shows why the first printed B^n/A^n is an index-placement error.'),('II.p119.ringed-target','For a morphism f:X->Y, f^{-1} has source Y and target X, so f^{-1}(O_Y)->O_X is the required ring arrow and defines both relative principal parts and differentials. With the printed f:X->X, an independent O_Y is outside the domain of f^{-1}. The corrected target Y is therefore necessary, as also witnessed by the adjacent square.'),('II.p119.stalks-and-square-types','Applying the inverse-image result of p118 to a point p:Set->T gives the asserted stalk compatibility. For the ringed square, u^* f^* and f-prime^* v^* both go from modules on Y to modules on X-prime. Thus the specified isomorphism in the note is correctly typed; the claimed consequence for diagram (1.1.4.4) is deferred until that diagram is read.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'READING_QUESTIONS.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['I-Q014','118–119','II.1.1.4 and (1.1.4.1), duplicated','The two distinct paragraphs and formulas are both numbered 1.1.4 and 1.1.4.1 in the print. Inspect the later references before deciding whether any uniquely justified numbering repair is possible.','Both printed numberings retained in all layers; page-specific anchors distinguish them','scan reading resolved; cross-reference disposition pending','evidence/I_p118_inverse-image-text.png; evidence/I_p118_inverse-image-formula.png; evidence/I_p119_ringed-hypothesis.png; evidence/I_p119_principal-parts.png.'])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p119_*.png')):f.write(f'| evidence/{p.name} | Printed p119, 800-dpi crop inspected during the first reading. |\n')
print('Page 119 edits, three checks and numbering follow-up recorded.')
