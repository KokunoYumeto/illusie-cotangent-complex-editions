"""Primary reviewer's p127 invariance proof and citation audit."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='127';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p127}'
ev='LNM239 scan PDF p145 / printed p127: both complete 400-dpi halves and nine retained 800-dpi crops personally inspected; all three complete source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p127.upright-Latin','All ring, resolution and row indices are upright; the three Z letterforms remain double-stroked.')
 old=region(layer);new=old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})')
 ch(layer,old,new,'note call and footnote','II.p127.note-markers','Only the numeral is raised; parentheses are on the baseline. See evidence/I_p127_statement.png and evidence/I_p127_footnote.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 if layer=='English':new=new.replace('hypothe-\nsis,','hypothesis,').replace("$B\\longrightarrow B'$).\n\n\\noindent For","$B\\longrightarrow B'$).\nFor").replace('(I 2.2.3)\n\n\\noindent it','(I 2.2.3)\nit')
 else:new=new.replace('récur-\nrence,','récurrence,').replace("$B\\longrightarrow B'$),\n\n\\noindent Pour","$B\\longrightarrow B'$),\nPour").replace('(I 2.2.3)\n\n\\noindent il','(I 2.2.3)\nil')
 ch(layer,old,new,'statement and induction paragraph','II.p127.prose-continuity','Join ordinary scan wraps and artificial paragraph breaks; reconstruct the divided word recurrence/hypothesis.','structure')
 if layer=='English':
  ch(layer,r'\uline{Suppose that the horizontal arrows in (1.2.6.1) are}',r'\uline{Suppose that the horizontal arrows in} (1.2.6.1) \uline{are}','proposition heading','II.p127.reference-underline','The displayed reference is excluded from the underlining in evidence/I_p127_statement.png.')
  ch(layer,r'\uline{is a quasi-isomorphism.}',r'\uline{is a quasi-isomorphism}.','part b conclusion','II.p127.statement-stop','The period is outside the underline; evidence/I_p127_diagonal.png.')
 else:
  ch(layer,r'\uline{On suppose que les flèches horizontales de (1.2.6.1) sont des}',r'\uline{On suppose que les flèches horizontales de} (1.2.6.1) \uline{sont des}','proposition heading','II.p127.reference-underline','The reference is not underlined; evidence/I_p127_statement.png.')
  ch(layer,r'\uline{est un quasi-isomorphisme,}',r'\uline{est un quasi-isomorphisme}.','part b conclusion','II.p127.statement-period','The original ends with a period outside the underline, not the supplied comma; evidence/I_p127_diagonal.png.','reading')
  ch(layer,"$B\\longrightarrow B'$),","$B\\longrightarrow B'$).",'convention for n=-1','II.p127.convention-period','The scan has a full stop after the closing parenthesis; evidence/I_p127_convention.png.','reading')
 old=region(layer);new=old
 # Preserve the named macro for subsequent formulas; only the first three rows
 # have the common printed left start.
 rows=[r"\text{(i)}\quad P_A(B)\longrightarrow P_{A'}(B')\quad ,",r"\text{(ii)}\quad"+'\n'+r"\Omega^1_{P_A(B)/A}\longrightarrow\Omega^1_{P_{A'}(B')/A'}\quad ,",r"\text{(iii)}\quad L_{B/A}\longrightarrow L_{B'/A'}\quad ."]
 for expr in rows:
  a=r'\IllusiePoneTwentySevenMap{'+expr+'}'
  assert a in new,a
  new=new.replace(a,r'\noindent\hspace*{133bp}$\displaystyle '+expr+r'$\par')
 ch(layer,old,new,'maps (i), (ii), (iii)','II.p127.map-alignment','All three labels begin at the same printed horizontal position; independent centering lost this alignment. See evidence/I_p127_maps.png.')
 old=region(layer);new=old.replace(r'\phantomsection\hypertarget{illusie:I:ch1:p127:footnote-1}',r'\vfill'+'\n'+r'\phantomsection\hypertarget{illusie:I:ch1:p127:footnote-1}')+r'\clearpage'+'\n'
 ch(layer,old,new,'footnote and page boundary','II.p127.bottom-note','Keep the note at the printed foot and end the page after it; the main proof continues on p128.','structure')
for layer in ['corrected','English']:
 ch(layer,'(I 4.2.2.5)','(I 4.2.2.1)','symmetric-algebra step','II.p127.symmetric-citation','The original clearly cites 4.2.2.5 (evidence/I_p127_symmetric.png), but that proposition on p104 concerns Tor amplitude. Lemma 4.2.2.1 on the already reviewed p102 is the precise preservation-of-quasi-isomorphisms result used here. Its flatness, upper boundedness and local inductive-limit hypotheses are checked in CHECK_EVENTS.','misprint of the original')
ch('English',r'\text{(respectively,}',r'\text{(resp.}','part b parenthesis','II.p127.resp','The supplied standard retains the source abbreviation resp.','terminology')
ch('English','(We agree that','(The convention is that','n=-1 convention','II.p127.impersonal-on.1','French on convient is impersonal; preserve the convention without replacing it by authorial we.','terminology')
ch('English','we deduce that','one deduces that','symmetric-algebra step','II.p127.impersonal-on.2','French on en deduit is impersonal. Montrons remains We show because it is authorial first person.','terminology')
verdict(page,'ILL-SC-20260804-0124',"Par l'hypothèses de; point after hypothèse",'Singular hypothesis correction confirmed; earlier period alignment confirmed','The definite singular article requires hypothèse; the print has the period already restored after the base-case hypothesis. Add the independently verified cross-reference repair 4.2.2.5 to 4.2.2.1 in corrected/English.',ev)
verdict(page,'ILL-NORM-20260804-0155','One initial-capital event: (on to (On','Retained as an orthographic correction','The parenthetical is a separate sentence after a full stop; the sentence-initial capital is a necessary orthographic repair rather than optional object-name normalization. Diplomatic retains on.',ev)
verdict(page,'ILL-TX-20260804-0151','Twelve anchors; source formulas and footnote','All anchors retained; two comma misreadings repaired','Upright Latin, note-call baselines, reference underline, three-row alignment, divided-word joining and bottom note restored. The original mistaken citation remains diplomatic.',ev)
verdict(page,'ILL-TR-20260804-0153','Induction and two diagonal maps','Meaning confirmed; resp. and two impersonal clauses repaired','Both diagonal variants and the n=-1 convention agree with corrected French. The induction has only been checked through the last map on this page; continuation is not yet certified.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.2.6.2a.Whitehead','The base case n=-1 is B->B prime, a quasi-isomorphism by hypothesis. For the induction step, the map P_A(B)_(n-1)->P_Aprime(Bprime)_(n-1) is a map of simplicial rings and therefore of their additive simplicial abelian sheaves. Consequently hypothesis (ii) of I 2.2.2, reread on p25, applies to Corollary I 2.2.3 on p26; no assumption that the topos has enough points is needed. The induced map of free abelian sheaves is a quasi-isomorphism.'),('II.1.2.6.2a.symmetric-functor','Both sides of (*) are degreewise free abelian sheaves. Their normalized complexes are bounded above in the cohomological convention (degrees <=0) and flat termwise, since normalized terms are direct summands. The full symmetric-algebra functor commutes with local inductive limits, being assembled from finite tensor products, coinvariants and direct sums. Lemma I 4.2.2.1 on p102 therefore shows that S_Z(*) is a quasi-isomorphism. Its nonpositive case involves ordinary simplicial normalization, so the unbounded two-sided totalization concern in I-Q009 is not used. The printed I 4.2.2.5 is the Tor-amplitude proposition, and is a wrong cross-reference; corrected French/English cite 4.2.2.1. This verifies only the portion of the induction printed on p127.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p127_*.png')):f.write(f'| evidence/{p.name} | Printed p127, 800-dpi crop inspected during the first reading. |\n')
print('Page 127 edits and two targeted proof checks recorded.')
