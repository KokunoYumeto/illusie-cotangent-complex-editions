"""Primary reviewer's p117 audit; original errors stay diplomatic."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='117';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p117}'
ev='LNM239 scan PDF p135 / printed p117: both complete 400-dpi halves and eleven retained 800-dpi crops personally inspected; all three full source regions and four prior entries read. '
bar=r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}'
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 old=region(layer);new=old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath').replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})')
 ch(layer,old,new,'body and footnote','II.p117.upright-and-note-calls','All Latin letters are upright; both note markers have baseline parentheses and a raised numeral, as shown in note-call.png and footnote.png.')
 old=r'\hspace*{-8bp}\hbox{\text{#1}\hfill$\displaystyle #2$\hfill'
 ch(layer,old,r'\hbox to\linewidth{\text{#1}\hfill$\displaystyle #2$\hfill','numbered sequences','II.p117.left-display-labels','Both sequence labels sit at the left margin, separated from the centered formula; preserve the existing named display macro.')
 for target in ['B[X]','S_B(M)']:
  ch(layer,r'C\xrightarrow{\sim}'+target,'C'+bar+target,'free-algebra isomorphisms','II.p117.unheaded-isomorphism.'+target,'The enlarged hypothesis and footnote show a tilde over an unheaded horizontal bar, not an arrow.')
 old=region(layer)
 a=old.index(r'\noindent\hspace{28bp}');b=old.index(r'\vspace{5bp}',a)
 para=old[a:b]
 new=para.replace('\\par\n\\noindent ', '\n').replace('\\par\n','\n').rstrip()+'\\par\n\n'
 ch(layer,para,new,'proof and inductive-limit paragraph','II.p117.join-proof-paragraph','The four printed lines form one paragraph beginning Ces assertions; the supplied hard paragraph breaks were line wraps. Original/corrected punctuation differences are retained.','structure')
 old=region(layer);a=old.index(r'\noindent des morphismes' if layer!='English' else r'\noindent be morphisms');b=old.index(r'\phantomsection',a)
 seg=old[a:b];new=seg.replace('\\par\n\\noindent ','\n')
 ch(layer,seg,new,'introduction to transitivity sequence','II.p117.join-sequence-intro','The line before suite de C-Modules is an ordinary line wrap, not a paragraph.','structure')
 old=region(layer);a=old.index(r'\noindent Cette suite' if layer!='English' else r'\noindent This sequence');b=old.index(r'\phantomsection',a)
 seg=old[a:b];new=seg.replace('\\par\n\\noindent ','\n')
 ch(layer,seg,new,'free-algebra hypothesis','II.p117.join-free-hypothesis','The quantified X continues the same paragraph after a printed line wrap.','structure')
 ch(layer,'\n\\noindent (1.1.2.12)','\n(1.1.2.12)','end of pointwise proof','II.p117.continuation-inline','The concluding references continue the same sentence and paragraph.')
 ch(layer,r'\noindent\rule{72bp}{0.35bp}',r'\vfill'+'\n'+r'\noindent\rule{72bp}{0.35bp}','footnote placement','II.p117.footnote-bottom','The short separator and note belong at the bottom of the page.')
 old=region(layer);a=old.index(r'\noindent\begin{minipage}');seg=old[a:];new=seg.replace('\\\\\n','\n')+r'\clearpage'+'\n'
 ch(layer,seg,new,'footnote and boundary','II.p117.footnote-flow-boundary','The note is one paragraph; remove arbitrary forced wraps and end the printed page after it.','structure')
old=region('corrected');new=old.replace("d'anneaux","d'Anneaux").replace('-modules','-Modules').replace('-algèbre','-Algèbre').replace('-module','-Module').replace('comme algèbre','comme Algèbre')
ch('corrected',old,new,'five object capitals','II.p117.withdraw-capital-normalizations','The five printed capitals are conventional and not errors.','reading')
old=region('English');new=old.replace('respectively,','resp.')
ch('English',old,new,'two parenthetical alternatives','II.p117.resp-standard','STANDARDS_20261119.md Rules 6 and English Kept require the printed abbreviation resp. to remain; both occurrences in the scan read resp.','terminology')
verdict(page,'ILL-SC-20260804-0114','EGA 2.5.5 and last term Omega(C/A) in 1.1.2.13','Omega(C/B) confirmed; EGA 20.5.5 retained provisionally for source-locator verification','The sequence repair is forced by 1.1.2.12 and the printed sectionwise polynomial sequence, and by the rank counterexample recorded in CHECK_EVENTS. The absent zero in the EGA locator is visible; the neighbouring references to section 20.5 support the supplied repair, but the exact external proposition has not been checked.',ev)
verdict(page,'ILL-NORM-20260804-0145','Five printed capitals, doubled closing parenthesis after EGA reference, and absent final period after definition','Five capitals restored; correction of unmatched closing parenthesis and missing sentence-final period retained','The parenthesis has only one opening and two closings; the final sentence has no stop before a new numbered assertion. These two punctuation repairs are justified original misprints, not changes of mathematical notation.',ev)
verdict(page,'ILL-TX-20260804-0141','Eleven anchors including page; two left labels and two unheaded isomorphism bars','All anchors and display macro preserved; false paragraphs, marker baselines and page ending corrected','All exponents, ring quotients, section arguments, zero terms, signs and references compared with enlarged images. Original C/A misprint deliberately preserved diplomatic.',ev)
verdict(page,'ILL-TR-20260804-0143','Inductive limits, exact sequence and flat symmetric-algebra footnote','Meaning retained; two expansions of resp. reversed to the required standard','No semantic omission found. The flat-module reduction is checked conditional on I 4.2.1.3; the cited external EGA text has not been read.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.1.2.10','For B-prime=B tensor_A A-prime, an A-derivation into a B-prime-module M is equivalent to an independent pair of A-derivations from B and A-prime. The extension is delta(b tensor a-prime)=a-prime delta_B(b)+b delta_A-prime(a-prime); balancing uses that both derivations vanish on A. The two summands of (1.1.2.10) represent these choices. The displayed canonical map is consequently an isomorphism, completing the assertion begun on p116. More generally a compatible family of derivations on a diagram of ring arrows extends uniquely over its inductive limit, so the same universal property verifies commutation with arbitrary inductive limits in the category of modules with varying base ring.'),('II.1.1.2.12-13','Quotient Omega(C/A) by the C-submodule generated by d(b) for b in B. Maps from the quotient to M are exactly B-derivations C->M, so it is Omega(C/B), proving right exactness. For C=B[X], a derivation is determined independently by its restriction to B and its values on X; hence Omega(C/A) is (Omega(B/A) tensor_B C) direct-sum C^(X), with Omega(C/B)=C^(X). This proves injectivity of the first map and exactness of the corrected short sequence, sectionwise and after exact sheafification.'),('II.1.1.2.13.printed-target','The printed last nonzero term Omega(C/A) is refuted already by A=k, B=k[t], C=k[t,x]. After tensoring with k(t,x), the putative exact sequence would have vector-space dimensions 1,2,2, which violate the alternating rank identity. Replacing the last term by Omega(C/B), of rank one, agrees with the preceding transitivity sequence and the printed sectionwise proof.','refuted, with the refined statement\'s id: II.1.1.2.13.corrected'),('II.p117.footnote-1','Using I 4.2.1.3 as the stated local filtered presentation of a flat module M by finite free modules M_i, the symmetric algebra S_B(M) is the filtered inductive limit of polynomial algebras S_B(M_i). The short transitivity sequences for these polynomial algebras form a compatible system. Their first terms have limit Omega(B/A) tensor_B S_B(M), while both differential terms commute with the limit by the checked universal property. Exactness of filtered inductive limits of sheaves of modules therefore gives the footnote assertion. This checks the reduction, not a fresh proof of I 4.2.1.3.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for event in events:
  sid,outcome,*typ=event;w.writerow([sid,now,who,typ[0] if typ else 'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p117_*.png')):f.write(f'| evidence/{p.name} | Printed p117, 800-dpi crop inspected during the first reading. |\n')
print('Page 117 edits and four targeted mathematical events recorded.')
