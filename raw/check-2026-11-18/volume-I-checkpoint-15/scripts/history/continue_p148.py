"""Primary reviewer's page148 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='148';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p148}'
ev='LNM239 scan PDF p166 / printed p148: both complete400-dpi halves and ten800-dpi crops, including the expanded top row, personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
ch('corrected',r'\mathcal O_S$-algèbre',r'\mathcal O_S$-Algèbre','proof opening','II.p148.withdraw-capitalization','Withdraw the optional lowercase normalization; the print has Algèbre.','reading')
for old,new in [("$A$. Alors","$A$ . Alors"),("_{S'}$. La flèche","_{S'}$ . La flèche"),("$A'$. La flèche","$A'$ . La flèche")]:
 ch('corrected',old,new,'proof punctuation','II.p148.withdraw-spacing','Withdraw optional punctuation-space normalization.','reading')
for layer in LAYERS:
 old=region(layer);assert old.count(r'\ReflowBodyFont ')==2
 ch(layer,old,old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath'),'Latin notation','II.p148.upright-Latin','Printed Latin mathematical and diagram letters are upright; cover both font sites.')
 old=region(layer);assert old.count(r'\mathcal O')==14
 ch(layer,old,old.replace(r'\mathcal O',r'\underline{\mathrm{O}}'),'fourteen structure-sheaf symbols','II.p148.structure-sheaves','Each structure-sheaf symbol is upright underlined O; subscripts remain outside its underline.')
 old=region(layer);assert old.count(r'\textsuperscript{(1)}')==2 and old.count(r'\textsuperscript{(2)}')==2
 new=old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})').replace(r'\textsuperscript{(2)}',r'(\textsuperscript{2})')
 new=new.replace(r'\uline{Preuve}(',r'\uline{Preuve} (').replace(r'\uline{Proof}(',r'\uline{Proof} (')
 new=new.replace("commutatif}(\\textsuperscript", "commutatif} (\\textsuperscript").replace("square}(\\textsuperscript", "square} (\\textsuperscript")
 ch(layer,old,new,'two calls and two labels','II.p148.note-parentheses','Only the note digits are raised; parentheses and the space preceding each text call are on the baseline.')
 ch(layer,r'at (3.77,-0.03) {,}',r'at ([xshift=1.16cm]BR.base) {,}','square punctuation','II.p148.square-comma','Align the terminal comma with the bottom-row baseline.')
 ch(layer,r'at (2.20,-0.03) {.}',r'at ([xshift=2.20cm]S.base) {.}','diamond punctuation','II.p148.diamond-period','Align the terminal period with the S baseline.')
 old=region(layer);body,notes=old.split(r'\noindent\rule{69bp}{0.4bp}',1)
 new=body.replace('\\par\n\\noindent ','\n').replace('\\par\n\\phantomsection','\n\\phantomsection')
 for t in ['donc (2.3.3','(2.3.3 (iii))','vertical arrow']:new=new.replace('\\noindent '+t,t)
 new+=r'\noindent\rule{69bp}{0.4bp}'+notes
 ch(layer,old,new,'proof and corollary','II.p148.prose-continuity','Join printed line wraps and retained body-anchor boundaries; retain separate footnotes and all displays.','structure')
 ch(layer,r'\noindent\rule{69bp}{0.4bp}',r'\par\vfill'+'\n'+r'\noindent\rule{69bp}{0.4bp}','footnote placement','II.p148.footnote-bottom','Keep both ruled notes at the page foot without merging their paragraphs.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p148.boundary','Retain the printed page boundary.','structure')
for layer in ['as-printed','corrected']:
 for old,new in [('(2.3.3 (iv) + (ii))','(2.3.3(iv) + (ii))'),('([18]chap. IV)','( [18]chap. IV)'),('([18] IV 3.1)','( [18] IV 3.1)')]:
  ch(layer,old,new,'reference spacing','II.p148.reference-spacing','Restore the reference spacing visible in the enlarged proof, corollary and footnote.','reading')
ch('English','we may suppose that $X$','one may suppose that $X$','proof opening','II.p148.impersonal-on','French on peut supposer is impersonal.','terminology')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p148','Algèbre; three punctuation spaces','algèbre; normalized punctuation spaces','Local source-comparison verdict, not a supplied decision-record ID. Withdraw the one capitalization and three optional spacing normalizations. No original mathematical error found on this page.',ev+'evidence/I_p148_proof-setup.png; evidence/I_p148_proof-conclusion.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.3.8.square','Put h=fu=vf-prime. On an affine-relative chart X=Spec_S(A), the stated base-change description gives X-prime=Spec_S-prime(A-prime), A-prime=v^{-1}A tensor_{v^{-1}O_S}O_S-prime. Inverse image preserves this tensor product, giving the top isomorphism h^{-1}A tensor_{h^{-1}O_S}f-prime^{-1}O_S-prime -> f-prime^{-1}A-prime. The two paths are induced by the same structure maps of the base-changed relative scheme; hence the displayed square commutes and every coefficient ring is correctly typed. The later corollary diamond has p:Z->X,q:Z->Y,f:X->S,g:Y->S and fp=gq.'),('II.2.3.8.proof','By2.3.4, f^{-1}A->O_X is a localization. Applying u^{-1} preserves localization by2.3.3(iv), and extending scalars along h^{-1}O_S->f-prime^{-1}O_S-prime preserves it by2.3.3(ii), so the left arrow is a localization. The right arrow is the relative-spectrum localization for A-prime by2.3.4; its composite with the top isomorphism is therefore a localization. Commutativity identifies this composite with the left arrow followed by(*); the converse direction of2.3.3(iii) implies that(*) is a localization. No flatness hypothesis is needed for this argument. The deduction uses the relative-spectrum/base-change description stated in the text; Hakim[18] was not independently consulted.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p148_*.png')):f.write(f'| evidence/{p.name} | Page148 audit:800-dpi crop personally inspected; expanded top row resolves its initial edge crop. |\n')
print('Page148 edits, verdict and two proof/use checks recorded.')
