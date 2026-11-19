"""Primary reviewer's page 134 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page
page='134';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p134}'
ev='LNM239 scan PDF p152 / printed p134: both complete 400-dpi halves and eleven 800-dpi crops personally inspected; full source regions read as-printed, corrected, English. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('C-modules','C-Modules').replace("$C'$-modules","$C'$-Modules").replace('$P$,','$P$ ,').replace('$A$,','$A$ ,')
ch('corrected',old,new,'opening, proof and footnote','II.p134.withdraw-normalizations','The three Module capitals and two spaces before commas are printed conventions, not necessary corrections.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','II.p134.upright-Latin','Printed Latin variables, primes and tensor indices are upright.')
 ch(layer,r'\draw[->] (T) -- (L);',r'\draw[>->] (T) -- (L);','distinguished triangle left edge','II.p134.triangle-arrow-mark','The scan has a second forward-pointing arrowhead at the beginning of the descending left edge, in addition to its terminal arrowhead. Restore this visible marking without adding an unprinted degree label or shift; evidence/I_p134_triangle.png.','reading')
 ch(layer,r'$\chi$',r'$\underline{\chi}$','Proposition 2.1.2 functor','II.p134.underlined-chi','The functor chi is underlined in the scan, agreeing with the notation in I 3.2.4; evidence/I_p134_proposition.png.','reading')
 old=region(layer);new=old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})')
 ch(layer,old,new,'note call and footnote marker','II.p134.note-markers','Only the numeral is raised; both parentheses sit on the text baseline, in the call and the footnote.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace('\\par\n\\vspace{2.0bp}\n\\noindent ','\n')
 ch(layer,old,new,'opening, theorem and proof prose','II.p134.prose-continuity','Ordinary line wraps, including De meme/comme, are not paragraph breaks. Preserve all nine semantic anchors.','structure')
 ch(layer,r'\vspace{0.5bp}',r'\vfill','footnote placement','II.p134.footnote-bottom','The footnote follows a bottom-of-page rule, separate from the continuing proof.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p134.boundary','Retain the boundary after the footnote; the proof continues on the next page.','structure')
for layer in ['as-printed','corrected']:
 ch(layer,r"\uline{s'écrit, à isomorphisme canonique fonctoriel près}",r"\uline{s'écrit}, \uline{à isomorphisme canonique fonctoriel près}",'Proposition 2.1.2 punctuation','II.p134.comma-outside-underline','The comma following ecrit is outside the underline; evidence/I_p134_proposition.png.')
 ch(layer,r'\uline{des flèches canoniques.}',r'\uline{des flèches canoniques}.','Proposition ending','II.p134.period-outside-underline','The closing period is outside the underline; evidence/I_p134_degree-zero.png.')
ch('English',r'\uline{is, up to canonical functorial isomorphism}',r'\uline{is}, \uline{up to canonical functorial isomorphism}','Proposition punctuation','II.p134.comma-outside-underline','Match the printed division around the comma.')
ch('English',r'\uline{of the canonical maps.}',r'\uline{of the canonical maps}.','Proposition ending','II.p134.period-outside-underline','Match the printed exclusion of the closing period.')
ch('English','we have a canonical functorial commutative','there is a canonical functorial commutative','proof opening','II.p134.impersonal-have','On a is impersonal under the supplied standard.','terminology')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.1.1.6-prime-and-footnote','Each degree of P is a free algebra over A, and Q is a free algebra over P; hence Q is also free over A. The three differential modules in (2.1.1.3) are degreewise free, so their scalar extensions to C are degreewise flat C-modules. In particular the quotient remains flat and tensoring the short exact sequence with C-prime preserves its injection. The semilinear map (2.1.1.6), viewed by restriction as a C-module map, is adjoint to the C-prime-linear map (2.1.1.6) prime. Thus both source and target in that formula really are exact sequences, as the footnote requires.'),('II.2.1.2.diagram-and-vertical-maps','Naturality of the augmentation L^Delta->Omega^1 in both ring variables makes both squares of (*) commute. The lower row is the transitivity sequence already checked on p133. Proposition 1.2.5.3, reread on p126, applies to Q over P and to P over A because both are degreewise free polynomial algebras (free modules of generators satisfy its flatness hypothesis). It gives exactly the right vertical quasi-isomorphism and L^Delta_{P/A}->Omega^1_{P/A} asserted here. Extension by Q and the remaining comparison needed for the distinguished triangle continue on p135; they are not certified by this partial proof event.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p134_*.png')):f.write(f'| evidence/{p.name} | Printed p134, 800-dpi crop inspected during the first reading. |\n')
print('Page 134 edits and two proof checks recorded.')
