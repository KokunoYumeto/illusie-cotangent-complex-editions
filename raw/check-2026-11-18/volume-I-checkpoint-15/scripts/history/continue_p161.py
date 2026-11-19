"""Primary reviewer's page161 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='161';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p161}'
ev='LNM239 scan PDF p179 / printed p161: both complete400-dpi halves and ten800-dpi crops personally inspected; all three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace(r'$\mathcal Y$,',r'$\mathcal Y$ ,').replace('C-module variable','C-Module variable')
ch('corrected',old,new,'proof and remark','III.p161.withdraw-normalizations','Withdraw one optional capitalization and one punctuation-space change.','reading')
ch('corrected','A-extensions de C par un C-Module variable',r'C-extensions de $\Omega^1_{C/A}$ par un C-Module variable','remark1.1.9.1','III.1.1.9.1.category','The printed second category duplicates the algebra-extension category. By the explicit definitions on159, alg starts from C-module extensions of Omega_C/A and diff takes values there; the natural comparisons on160–161 establish precisely these quasi-inverse categories. Preserve the original in the diplomatic layer.','misprint of the original')
ch('English','$A$-extensions of $C$ by a variable $C$-module',r'$C$-extensions of $\Omega^1_{C/A}$ by a variable $C$-module','remark1.1.9.1','III.1.1.9.1.category','Follow the necessary corrected-French category repair justified by the domains of alg and diff on159 and their natural comparisons on160–161.','misprint of the original')
ch('as-printed',r'sous-jacents, $i^{-1}',r'sous-jacents de $i^{-1}','definition1.1.10','III.1.1.10.printed-de','The complete square-zero-condition crop clearly prints de, not a comma. Restore this original grammatical error diplomatically. Retain the supplied comma in corrected French and the independent English clause.','reading')
bar=r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}'
for layer in LAYERS:
 old=region(layer);assert old.count(r'\ReflowBodyFont ')==2
 ch(layer,old,old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath'),'page mathematics','III.p161.upright-Latin','Restore upright printed Latin mathematics in body, diagrams and footnotes.')
 old=region(layer);assert old.count(r'\mathcal Y')==4 and old.count(r'\mathcal O')==2
 ch(layer,old,old.replace(r'\mathcal Y','Y').replace(r'\mathcal O',r'\underline{\mathrm{O}}'),'extension and structure sheaves','III.p161.printed-letterforms','Restore four plain extension names Y and two underlined structure-sheaf O symbols.')
 ch(layer,r'd^1_{B/A}',r'd_{B/A}','comparison diagram','III.p161.derivation-degree','The top I-to-differentials arrow has d_B/A with no1 superscript in the print.','reading')
 ch(layer,r'\xrightarrow{\sim}',bar,'proof conclusion','III.p161.unheaded-isomorphism','The enlarged conclusion shows a tilde above an unheaded bar.')
 old=region(layer);new=old
 if layer=='English':new=new.replace(r'\uline{first-order infinitesimal $Y$-neighborhood}',r'\uline{first-order infinitesimal} $Y$-\uline{neighborhood}')
 else:new=new.replace(r'\uline{$Y$-voisinage infinitésimal d\'ordre un}',r'$Y$-\uline{voisinage infinitésimal d\'ordre un}')
 # Apostrophes are ordinary text in the TeX source.
 if layer!='English':new=old.replace("\\uline{$Y$-voisinage infinitésimal d'ordre un}","$Y$-\\uline{voisinage infinitésimal d'ordre un}")
 ch(layer,old,new,'definition emphasis','III.p161.underline-prefix','The Y- prefix is outside the printed underline; preserve the emphasized words and the separate extension underline.')
 old=region(layer);new=old.replace(r'\node at (294,0) {$,$};',r'\node[anchor=base] at ([xshift=13bp]ZbR.base) {$,$};')
 new=new.replace('    \\node[anchor=west] at (0,40) {(1.1.10.1)};\n','')
 new=new.replace(r'\node (X) at (171,40) {$X$};',r'\node (X) at (171,40) {$X$};'+'\n'+r'    \node[anchor=base west] at (0,0 |- X.base) {(1.1.10.1)};')
 new=new.replace(r'\node at (283,-3) {$,$};',r'\node[anchor=base] at ([xshift=112bp]Y.base) {$,$};')
 ch(layer,old,new,'comparison and triangle geometry','III.p161.diagram-baselines','Put both terminal commas on their respective lower-row baselines and the triangle number on the upper-row baseline. Preserve every arrow, label, node and native macro.')
 old=region(layer);assert old.count(r'\textsuperscript{(1)}')==2 and old.count(r'\textsuperscript{(2)}')==2
 new=old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})').replace(r'\textsuperscript{(2)}',r'(\textsuperscript{2})')
 new=new.replace(r'commutatif(\textsuperscript{1})',r'commutatif (\textsuperscript{1})').replace(r'diagram(\textsuperscript{1})',r'diagram (\textsuperscript{1})')
 new=new.replace(r'nul(\textsuperscript{2})',r'nul (\textsuperscript{2})').replace(r'kernel(\textsuperscript{2})',r'kernel (\textsuperscript{2})')
 ch(layer,old,new,'four footnote labels','III.p161.footnote-parentheses','Both body calls and both note labels on this page have raised numbers within baseline parentheses; preserve the spaces before body calls.')
 old=region(layer);new=old
 new=new.replace('donc on a\\par\n\n','donc on a\n').replace('so we have\\par\n\n','so we have\n').replace('hence we have\\par\n\n','hence we have\n')
 new=new.replace(r'\noindent\hspace*{1.5bp}$Y',r'$Y')
 new=new.replace('souvent\\par\n\n\\noindent\\hspace*{-0.5bp}{négligé dans la pratique.}', 'souvent négligé dans la pratique.')
 new=new.replace("$X'$\\par\n\n\\noindent\\hspace*{-0.5bp}{étaient les mêmes, $i$ étant l'identité sur ceux-ci.}","$X'$ étaient les mêmes, $i$ étant l'identité sur ceux-ci.")
 new=new.replace('often\\par\n\n\\noindent\\hspace*{-0.5bp}{suppressed in practice.}', 'often suppressed in practice.')
 new=new.replace('were\\par\n\n\\noindent\\hspace*{-0.5bp}{the same, with $i$ the identity on them.}', 'were the same, with $i$ the identity on them.')
 new=new.replace('\\vspace{5bp}\n\\phantomsection\\hypertarget{ILL-CCD:LNM239:CH3:S1:1:10:eq1:n1}', '\\vfill\n\\phantomsection\\hypertarget{ILL-CCD:LNM239:CH3:S1:1:10:eq1:n1}')+r'\clearpage'+'\n'
 ch(layer,old,new,'proof, footnotes and page boundary','III.p161.prose-flow','Join the artificial proof-conclusion paragraph and boxed footnote line fragments, retain all anchors and the two distinct notes, position the notes at the foot and preserve the printed page boundary.','structure')
old=region('English');new=old.replace('In fact we have shown','In fact it has been shown').replace('of $X$ we mean','of $X$ one means').replace('we shall often proceed','one will often proceed')
ch('English',old,new,'remark, definition and footnote','III.p161.impersonal-on','Preserve the impersonal on in all three clauses.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p161','Original A-extensions of C in remark; original de in definition silently changed to comma; one capitalized term and punctuation space','Same wrong category; existing comma corrects original de; optional normalization','Local source-comparison verdict, not a supplied decision-record ID. Correct the second category in1.1.9.1 to C-extensions of Omega_C/A in corrected French and English only. Restore printed de diplomatically, retain its necessary correction to comma in corrected French and the independent English clause. Withdraw optional capitalization and space normalizations. Shared derivation superscript, letterforms, underline scope, footnote shapes, prose and diagram baselines repaired. Footnote II1.1.4 correctly points to the ringed-topos convention on119, despite the duplicated earlier numbering; no renumbering.',ev+'evidence/I_p161_remark.png; evidence/I_p161_square-zero-complete.png; evidence/I_p161_footnotes-complete.png; evidence/I_p119_ringed-square.png; evidence/I_p119_footnote.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.9.diff-alg-comparison','For B=alg(Y), its local pairs (c,j) satisfy f(j)=dc. Projection delta(c,j)=j is an A-derivation, sends the included a in I to i(a), and satisfies f delta=dq. The induced u:Omega_B/A tensor_B C ->J therefore makes both squares of the printed diagram commute, with identities on I and Omega_C/A. Condition(L) makes its upper row exact, while Y is exact by definition. Thus u is an isomorphism; its inverse gives the printed unheaded isomorphism Y~diff(alg(Y)). Together with the comparison on160 this proves the asserted inverse group maps.'),('III.1.1.9.1.naturality-and-category','For a morphism of algebra extensions, including a varying kernel map, b->(q(b),db tensor1) commutes with it by naturality of universal differentials. For a morphism of C-module extensions of Omega_C/A, the induced map on alg is (c,j)->(c,v(j)); projection to J commutes with this map, so the universal maps u are natural too. The isomorphisms on160–161 are therefore natural over C-Mod, giving quasi-inverse equivalences between Exal_A(C,-) and C-module extensions of Omega_C/A. The printed second category of A-extensions of C merely repeats the first and cannot be the domain of alg; this verifies the necessary category correction.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p161_*.png')):f.write(f'| evidence/{p.name} | Page161 audit:800-dpi crop personally inspected; complete crops resolve the definition, square-zero clause and both complete footnotes. |\n')
 f.write('| evidence/I_p119_ringed-square.png; evidence/I_p119_footnote.png | Reinspected for161: the ringed-topos convention specifies the commutativity isomorphism, validating the footnote reference to II1.1.4 despite duplicate numbering. |\n')
print('Page161 edits, verdict and two proof checks recorded.')
