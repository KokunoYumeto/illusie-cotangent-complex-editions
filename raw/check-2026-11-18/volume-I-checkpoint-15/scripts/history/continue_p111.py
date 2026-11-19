"""Reviewer-directed scan decisions for p111, including original diagram misprints."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='111';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p111}'
ev='LNM239 scan PDF p129 / printed p111: both complete 400-dpi halves and fifteen enlarged crops personally inspected (nine at 800 dpi, three at 1200 dpi, three at 1600 dpi), with all source regions and four prior records. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def change(layer,old,new,line,sid,why,kind='typesetting'):
 edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
bar=r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}'
for layer in LAYERS:
 change(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','throughout','I.p111.upright-Latin','Latin variables, functors, labels, degrees and shifts are upright throughout, including both diagram expansions.')
 old=region(layer);new=old.replace(r'\Lambda',r'\wedge')
 change(layer,old,new,'all exterior powers','I.p111.exterior-sign','All exterior signs in the proposition and both diagrams are plain wedges.','reading')
 old=region(layer);new=old.replace(r'\mathbf N',r'\mathbb N')
 change(layer,old,new,'n and m hypotheses','I.p111.natural-numbers','The double-stroked natural-number alphabet occurs in both quantified hypotheses; the stars are retained.')
 old=region(layer);new=old.replace(r'\xrightarrow{\ \sim\ }',bar).replace(r'\simeq',bar)
 change(layer,old,new,'isomorphisms and footnote','I.p111.isomorphism-bars','evidence/I_p111_isomorphisms.png and footnote.png show unheaded isomorphism bars with tildes.')
 change(layer,r'\begin{array}{rcl}',r'\begin{array}{l@{\hspace{14bp}}l}','(i), (ii)','I.p111.isomorphism-alignment','The two formula domains begin at the same left edge after the two left-aligned labels.')
 old=region(layer);new=old.replace('&'+bar,bar).replace(r'\\[2bp]',r'\\[12bp]')
 change(layer,old,new,'(i), (ii)','I.p111.isomorphism-alignment-complete','Keep each formula together in the second column and restore the printed gap between lines.')
 old=region(layer);new=old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})')
 change(layer,old,new,'body and bottom note markers','I.p111.note-markers','Both enlarged loci show baseline parentheses and a raised numeral 1.')
 if layer=='English':
  change(layer,r'\uline{Moreover, these are compatible with the pairings}',r'\uline{Moreover}, \uline{these are compatible with the pairings}','compatibility paragraph','I.p111.underline-compatibility','The first printed underline ends before the comma; the following words have a separate underline.')
  change(layer,r'\uline{that is, for}',r'\uline{that is}, \uline{for}','compatibility paragraph','I.p111.underline-explanation','Keep the punctuation between the explanatory words outside the underline, corresponding to the original separate spans.')
 else:
  change(layer,r'\uline{En outre, ceux-ci sont compatibles aux accouplements}',r'\uline{En outre}, \uline{ceux-ci sont compatibles aux accouplements}','compatibility paragraph','I.p111.underline-compatibility','The enlarged compatibility line shows separate underlines before and after the comma.')
  change(layer,r'\uline{i.e. pour}',r'\uline{i}.\uline{e}. \uline{pour}','compatibility paragraph','I.p111.underline-ie','The i, e and pour are underlined separately; both stops are outside the underline.')
 old=r'\ReflowDisplay{}{(*)\qquad0\longrightarrow E\xrightarrow{\operatorname{id}}E\longrightarrow C(E)'+'\n'+r'\longrightarrow E[1]\longrightarrow0,}'
 new=r'\par\vspace{5bp}\noindent\makebox[0pt][l]{(*)}\hspace*{105bp}\(0\longrightarrow E\longrightarrow C(E)\longrightarrow E[1]\longrightarrow0,\)\par\vspace{5bp}'
 change(layer,old,new,'sequence (*)','I.4.3.2.1.cone-sequence','evidence/I_p111_cone-sequence.png shows exactly 0 -> E -> C(E) -> E[1] -> 0, with no repeated E and no identity label. The inserted E/id is a transcription error, not an original error; remove it in all layers. Restore the left-margin (*) label at the same time.','reading')
 old=r'\ReflowDisplay{}{(**)\qquad0\longrightarrow KiE\longrightarrow KiC(E)\longrightarrow Ki(E[1])'+'\n'+r'\longrightarrow0.}'
 new=r'\par\vspace{5bp}\noindent\makebox[0pt][l]{(**)}\hspace*{105bp}\(0\longrightarrow KiE\longrightarrow KiC(E)\longrightarrow Ki(E[1])\longrightarrow0.\)\par\vspace{5bp}'
 change(layer,old,new,'sequence (**)','I.p111.Ki-sequence-label','evidence/I_p111_Ki-sequence.png places (**) at the left margin, separately from the formula; all printed terms and punctuation are already correct.')
 change(layer,r'\noindent\rule{120bp}{0.35bp}\par',r'\par\vfill\noindent\rule{74bp}{0.35bp}\par\vspace{4bp}','footnote rule','I.p111.footnote-rule','The bottom note is separated by a short rule approximately 74bp long.')
 old=region(layer)[-250:]
 if not old.endswith('\\vspace{5.0bp}\n'):raise ValueError('unexpected page ending')
 change(layer,old,old[:-len('\\vspace{5.0bp}\n')]+r'\clearpage'+'\n','physical boundary','I.p111.page-boundary','End the physical page after the complete Verdier footnote.','structure')
# Restore precisely the three original misprints only in the diplomatic layer.
change('as-printed',r'L\wedge^m(E)[m]\mathbin{\overset L\otimes}L\wedge^n(E)[n]',r'L\wedge^m(E)[m]\mathbin{\overset L\otimes}L\wedge(E)[n]','first square, lower-left vertex','I.4.3.2.1.missing-n','evidence/I_p111_first-exponents.png confirms m on the first factor and no exponent at all on the second wedge. Comparison with known m/n glyphs at 1600 dpi confirms the first m, which is retained. Corrected French/English retain the required n on the second factor, as dictated by (i) applied to LS^n(E[1]).','reading')
change('as-printed',r'L\Gamma^m(E)[m]\mathbin{\overset L\otimes}L\Gamma^n(E)[n]',r'L\Gamma^m(E)[m]\mathbin{\overset L\otimes}L\Gamma^m(E)[n]','second square, lower-left vertex','I.4.3.2.1.wrong-m','evidence/I_p111_second-exponent.png shows m on the second Gamma. Its corresponding upper factor has exponent n and map (ii) must land in Gamma^n shifted by n, so the other two layers rightly retain n.','reading')
change('as-printed',r'{$L\wedge^m(E[1])\mathbin{\overset L\otimes}L\wedge^n(E[1])$};',r'{$L\wedge^m(E[1])\mathbin{\overset L\otimes}L\wedge^n(E[1]$};','second square, upper-left vertex','I.4.3.2.1.missing-parenthesis','evidence/I_p111_missing-parenthesis.png confirms that the second factor lacks the closing round parenthesis after [1]. Retain that printed omission only here; the corrected layers already supply the necessary closing delimiter.','reading')
verdict(page,'ILL-SC-20260804-0108','First square second wedge lacks n; second square second Gamma has m; second upper wedge factor lacks a closing parenthesis','All three existing repairs retained in corrected French/English and now justified; diplomatic print restored','Reject the zero-error inventory for these original misprints. Separately remove the unprinted E/id in the cone sequence from every layer.',ev+'The two full square crops and three close-ups settle the readings; CHECK_EVENTS records the type constraints.')
verdict(page,'ILL-NORM-20260804-0139','No French textual normalization difference beyond nonprinting comments','No normalization withdrawal required','The original inventory has no entries here. The newly distinguished diagram differences are necessary corrections, not modernization.',ev)
verdict(page,'ILL-TX-20260804-0135','Eleven anchored units and both named diagram macros','All retained; exact diagram readings and cone sequence restored','The source had silently repaired three original diagram misprints while adding an extra identity term to the cone sequence. Fonts, alphabet, bars, underline spans, notes and labels restored.',ev)
verdict(page,'ILL-TR-20260804-0137','Shift formulas, functorial isomorphisms and proof opening','English meaning retained and formula transcription error removed','No terminology change required. Degreewise flat/bounded above and the sign warning express the French faithfully.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[
('I.4.3.2.1.diagram-types','The displayed map (i), with exponent n, has target (L wedge^n E)[n]. Thus the second factor at the lower-left of its product square must have exponent n, which the print omits. In the second square (ii), the upper second factor is L wedge^n(E[1]), so its target is (L Gamma^n E)[n], not the printed Gamma^m(E)[n]. These are forced degree/type repairs; the first factor in each lower row has m and remains m. The missing closing parenthesis in the upper second wedge factor is a delimiter omission. This checks the typing of the stated maps; it does not yet establish the full shift theorem or its product-sign compatibility, whose proof continues.'),
('I.4.3.2.1.cone-exactness','For a cochain complex E, take C(id_E)^q=E^(q+1) direct-sum E^q with d(a,b)=(-d_E a,a+d_E b). Inclusion b -> (0,b) and projection (a,b) -> a give the degreewise split exact sequence 0->E->C(id_E)->E[1]->0 shown in the scan. The transcription inserted E --id--> E before that inclusion; then the composite of these two arrows would be the nonzero inclusion, so it would not even be a complex for nonzero E. Removing the inserted term restores both the image and the mathematical sequence. Exactness after Ki uses the functors invoked by the text and is not independently re-proved here.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,body in events:w.writerow([sid,now,who,'targeted proof check',body])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p111_*.png')):
  dpi=1600 if p.stem.split('I_p111_',1)[1] in ['known-m','known-n','bottom-first-index'] else 1200 if p.stem.split('I_p111_',1)[1] in ['first-exponents','second-exponent','missing-parenthesis'] else 800
  f.write(f'| evidence/{p.name} | Printed p111, {dpi}-dpi crop inspected during the first reading. |\n')
print('Page 111 edits, three original-error verdicts and cone-sequence repair recorded.')
