"""Primary reviewer's p113 decisions; faded formula readings remain qualified."""
import sys,csv
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='113';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p113}'
ev='LNM239 scan PDF p131 / printed p113: both 400-dpi halves and eight enlarged crops personally inspected (six at 800 dpi; faded diagram base and sign formula at 1200 dpi). All three entire source spans and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def change(layer,old,new,line,sid,why,kind='typesetting'):
 edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 change(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','whole page','I.p113.upright-Latin','Surviving printed Latin mathematical letters are upright throughout; this includes the diagram, whose macro expands after the font activation.')
 for suffix,var in [('resolution-induced-shifts-u-v','u'),('tensor-resolution-map-w','w')]:
  mark=r'\phantomsection\hypertarget{illusie:I:ch1:p113:'+suffix+r'}{}%'
  old='\n\n'+mark+'\n'+r'\noindent $'+var
  new='\n'+mark+'\n$'+var
  change(layer,old,new,'continuous concluding paragraph','I.p113.join-'+var,'evidence/I_p113_shift-arrows.png and evidence/I_p113_tensor-resolution.png show continuous prose at notons u and si w. Remove source-added paragraph breaks while keeping both anchors.','structure')
 change(layer,r'\vspace{5.0bp}',r'\clearpage','physical page boundary','I.p113.page-boundary','The canonical-isomorphism sentence ends the printed page, followed by the chapter boundary.','structure')
old=region('corrected');new=old.replace('de modules plats','de Modules plats')
change('corrected',old,new,'two occurrences','I.p113.withdraw-normalizations','Both printed occurrences of Modules are capitalized; no defect justifies the lower-case normalization.','reading')
change('English','whose verification is left to the reader:','whose verification is left as an exercise to the reader:','first sentence','I.p113.exercise-omission','The original explicitly says laissée en exercice au lecteur. Restore the omitted characterization as an exercise.','translation')
verdict(page,'ILL-SC-20260804-0110','No previously listed source correction','No new mathematical correction established','The supplied formulas agree with surviving strokes, but the final formula and canonical-isomorphism line have faded delimiters; retain provisionally under I-Q012 rather than certify invisible details.',ev+'evidence/I_p113_sign-identity.png; evidence/I_p113_canonical-shift-left.png; evidence/I_p113_canonical-shift-right.png')
verdict(page,'ILL-NORM-20260804-0141 / ILL-TCI-20260813-0132 / ILL-TCI-20260813-0133','Two printed Modules capitals','Both lower-case normalizations withdrawn','Neither capitalization is a misprint.',ev+'evidence/I_p113_paragraph-start.png; evidence/I_p113_shift-arrows.png')
verdict(page,'ILL-TX-20260804-0137','Six anchored units including page; product square followed by continuous prose','All anchors and named diagram macro retained; two false paragraph breaks removed','Top and bottom product degrees and arrows inspected; the lower row is faint but compatible. Small signs and negative exponents in prose inspected. Faded final delimiters remain provisional.',ev)
verdict(page,'ILL-TR-20260804-0139','The fact is explicitly left as an exercise','English restores as an exercise; otherwise meaning retained','No terminology-standard change needed on this page; flat modules, resolution and canonical isomorphism agree with the terminology in use.',ev)
with (ROOT/'READING_QUESTIONS.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['I-Q012','113','4.3.2.1 final sign comparison and canonical tensor-shift identification','The sign formula and final identification are severely faded in horizontal bands. Surviving strokes support the supplied expressions, including mn and the derived tensor mark, but do not independently establish all parentheses. Revisit at the second reading; retain any genuinely unrecoverable details as such. The sign exercise also requires checking the precise earlier tensor-shift convention before a full proof is claimed.','Supplied formulas retained provisionally; no silent replacement of unreadable glyphs.','faded delimiters unresolved; full sign proof pending','evidence/I_p113_sign-identity.png (1200 dpi); evidence/I_p113_canonical-shift-left.png and evidence/I_p113_canonical-shift-right.png (800 dpi).'])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p113_*.png')):f.write(f'| evidence/{p.name} | Printed p113, {1200 if p.stem.endswith(("sign-identity","diagram-lower")) else 800}-dpi crop inspected during first reading. |\n')
print('P113 edits, prior verdicts and faded-reading question recorded; no full sign-proof claim.')
