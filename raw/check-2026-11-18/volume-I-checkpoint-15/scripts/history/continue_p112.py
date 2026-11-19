"""Primary-reviewer decisions for p112; right-edge uncertainty is explicit."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='112';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p112}'
ev='LNM239 scan PDF p130 / printed p112: both full 400-dpi halves and twelve enlarged crops personally inspected (eleven at 800 dpi and clipped terminal zero at 1600 dpi). All source regions and four prior entries read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def change(layer,old,new,line,sid,why,kind='typesetting'):
 edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 change(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','throughout','I.p112.upright-Latin','The mathematical Latin variables, functors, powers, signs and reference labels are upright.')
 old=region(layer);change(layer,old,old.replace(r'\Lambda',r'\wedge'),'all exterior powers','I.p112.exterior-sign','All exterior-power signs are plain wedges in the exact sequences and prose formulas.','reading')
 old=region(layer);change(layer,old,old.replace(r'\cdots',r'\ldots'),'four exact sequences','I.p112.ellipsis','All ellipses have baseline dots.')
 change(layer,r'\longrightarrow\ldots\\[-2bp]',r'\longrightarrow\ldots\longrightarrow\\[10bp]','(ii)-prime continuation','I.p112.continuation-arrow','evidence/I_p112_second-sequence.png shows an arrow after the ellipsis at the end of the first line, and another at the beginning of the continuation line. The source omitted the former.','reading')
 old=region(layer);new=old.replace('0,\\\\\n','0,\\\\[12bp]\n').replace('\\ ,\\\\\n','\\ ,\\\\[12bp]\n')
 change(layer,old,new,'sequence separation','I.p112.sequence-spacing','The two sets of labelled sequences have a visible vertical gap between their members.')
 old=r'\ReflowDisplay{}{S^n(E[1])\longrightarrow\wedge^nE[n]'+'\n'+r'\qquad\text{(resp. }\wedge^n(E[1])\longrightarrow\Gamma^nE[n]\text{)}}'
 new=r'\ReflowDisplay{}{S^n(E[1])\longrightarrow\wedge^nE[n]}'+'\n'+r'\par\vspace{8bp}\noindent(resp. $\wedge^n(E[1])\longrightarrow\Gamma^nE[n]$)\par\vspace{8bp}'
 change(layer,old,new,'shift arrows','I.p112.separate-resp-line','The main shift arrow is centered; the resp. arrow is a separate left-aligned line, not beside it.','structure')
 mark=r'\phantomsection\hypertarget{illusie:I:ch1:p112:product-compatibility-square-intro}{}%'
 word='For' if layer=='English' else 'Pour'
 old='\n\n'+mark+'\n'+r'\noindent '+word
 new='\n'+mark+'\n'+word
 change(layer,old,new,'last paragraph','I.p112.paragraph-join','evidence/I_p112_paragraph-join.png shows Pour la dernière partie continuing the same paragraph after the resolution parenthesis. Preserve the anchor without introducing a paragraph break.','structure')
 old=region(layer)[-250:]
 if not old.endswith('\\vspace{5.0bp}\n'):raise ValueError('unexpected ending')
 change(layer,old,old[:-len('\\vspace{5.0bp}\n')]+r'\clearpage'+'\n','physical boundary','I.p112.page-boundary','The page ends after carré commutatif, whose diagram follows on the next page.','structure')
# Reading of the scan-edge zero is explicitly less certain than intact glyphs.
change('as-printed',r'S^nKiC(E)\longrightarrow S^nKi(E[1])\longrightarrow\ ,',r'S^nKiC(E)\longrightarrow S^nKi(E[1])\longrightarrow0,','(i)-prime right edge','I.p112.clipped-terminal-zero','evidence/I_p112_clipped-zero.png shows the left curved stroke of the terminal 0 at the scan boundary. Its mathematical role is also forced by exactness. Restore the recognisable, partially clipped zero in diplomatic French as a reconstruction. Punctuation after it lies outside the image: the supplied comma is provisionally retained, not certified as seen (I-Q011).','reading')
change('as-printed',r'\wedge^{n-1}(Ki(E[1]))',r'\wedge^{n-1}(Ki(E[1])','(ii)-prime continuation','I.4.3.2.1.seq-parenthesis','evidence/I_p112_second-sequence.png shows only one closing round parenthesis after [1], although two were opened. Preserve this original omission diplomatically; the corrected and English sources already supply the missing delimiter.','reading')
change('as-printed',r'\noindent(resp. $\wedge^n(E[1])\longrightarrow',r'\noindent(resp. $\wedge^n(E[1]\longrightarrow','resp. shift arrow','I.4.3.2.1.resp-parenthesis','evidence/I_p112_resp-shift.png shows no round closing parenthesis after E[1]. The corrected layers already supply the syntactically necessary delimiter.','reading')
old=region('corrected');new=old.replace('exacte de modules','exacte de Modules').replace('comme anneau','comme Anneau').replace("d'algèbres","d'Algèbres")
change('corrected',old,new,'opening and last paragraph','I.p112.withdraw-normalizations','Three capitalizations Modules, Anneau, Algèbres are printed and cause no defect. Restore them; retain the justified announced-isomorphism gender repair.','reading')
# The helper defaults to high; this scan-edge reconstruction is expressly medium.
p=ROOT/'CORRECTIONS.tsv'
with p.open(newline='') as f:r=list(csv.DictReader(f,delimiter='\t'));fields=list(r[0])
for row in r:
 if row['printed_page']==page and row['statement']=='I.p112.clipped-terminal-zero':row['confidence']='medium (first reading; 0 partly clipped; following punctuation unverified; second reading pending)'
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(r)
verdict(page,'ILL-SC-20260804-0109 / ILL-TCI-20260813-0130','annoncée modifying the masculine isomorphisme','annoncé retained in corrected French','Confirm necessary grammatical agreement repair, as the enlarged resolution paragraph shows. No corresponding English gender issue.',ev+'evidence/I_p112_resolution.png')
verdict(page,'ILL-TCI-20260813-0129','Terminal zero partly clipped at the right scan edge; following punctuation outside the image','Reconstructed zero retained in C/E and now supplied in D','The visible left arc and sequence identify 0 with medium visual confidence; this is scan reconstruction, not an original mathematical error. The supplied comma remains provisional in all layers (I-Q011).',ev+'evidence/I_p112_clipped-zero.png')
verdict(page,'I.p112.pre-existing-delimiter-repairs','Missing closing parenthesis in (ii)-prime and in the resp. shift arrow','Both necessary closing parentheses retained in corrected French/English','The diplomatic sources had silently supplied both; their printed omissions are now restored. These original errors were absent from the earlier inventory.',ev+'evidence/I_p112_second-sequence.png; evidence/I_p112_resp-shift.png')
verdict(page,'ILL-NORM-20260804-0140','Modules, Anneau, Algèbres','Three lower-case normalizations withdrawn','Capitalization is printed and not an error.',ev)
verdict(page,'ILL-TX-20260804-0136','Eight anchored units; continuation arrow, separate resp. line, same final paragraph','All anchors retained; missing arrow, structure and typography restored','Every degree n, n-1, n-p, p, the negative n, inverse f, integral-normalization notation and all sequence terms were enlarged and checked.',ev)
verdict(page,'ILL-TR-20260804-0138','Contractibility argument, finite resolution and product-square introduction','English meaning retained; common formula/structure repairs applied','Contractible expresses homotopiquement trivial for complexes; no additional glossary or supplied-standard change is required.',ev)
with (ROOT/'READING_QUESTIONS.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['I-Q011','112','4.3.2.1, (i)-prime right edge','The scan cuts through the terminal zero. Its left arc is visible, but any punctuation beyond it is outside the image. Revisit the original pixel boundary at the second reading; do not claim that the supplied comma has been seen.','Terminal 0 reconstructed in all layers; supplied following comma provisionally retained.','medium reconstruction; punctuation unresolved; second reading pending','evidence/I_p112_clipped-zero.png (1600 dpi); evidence/I_p112_first-sequence.png (800 dpi).'])
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['I.4.3.2.1.acyclic-middle-shift',now,who,'targeted proof check','For an exact sequence of complexes 0->A->T1->...->Tn->B->0 with all Ti acyclic, form the finite total complex X=[A->T1->...->Tn], with A in horizontal degree -n. Its augmentation f:X->B is a quasi-isomorphism by exactness of the finite rows. Projection X->A[n] is also a quasi-isomorphism: its kernel has a finite filtration with shifted acyclic Ti as quotients. Thus projection composed with f inverse gives B isomorphic to A[n], exactly the resolution convention stated here. If a middle tensor factor C is contractible via h, the tensor homotopy on x tensor y is (-1)^degree(x) x tensor h(y); the two cross terms cancel and dH+Hd=id. This verifies the formal final step of the printed proof. Homotopy invariance of the particular nonlinear S/Gamma/exterior constructions and the normalization comparison (4.1.3.5)/(4.2.3.3) are cited dependencies, not independently re-proved by this event.'])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p112_*.png')):f.write(f'| evidence/{p.name} | Printed p112, {1600 if "clipped-zero" in p.name else 800}-dpi crop inspected during the first reading. |\n')
print('Page 112 edits and qualified scan-edge question recorded.')
