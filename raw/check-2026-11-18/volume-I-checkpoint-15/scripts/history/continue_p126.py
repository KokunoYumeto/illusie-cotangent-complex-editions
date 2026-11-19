"""Primary reviewer's p126 diagonal-construction audit."""
import sys,csv,re
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='126';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p126}'
ev='LNM239 scan PDF p144 / printed p126: both complete 400-dpi halves and eight retained 800-dpi crops personally inspected; all three complete source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace("d'anneaux","d'Anneaux").replace('comme anneau','comme Anneau').replace('-module','-Module').replace(r'\uline{module}',r'\uline{Module}')
ch('corrected',old,new,'ten capitalization events','II.p126.withdraw-capitalizations','The ten object-name capitalization normalizations are optional and do not repair an original error.','reading')
old=region('corrected');new=old.replace('$T$.','$T$ .').replace('$T$,','$T$ ,').replace('$B_o$,','$B_o$ ,').replace('$P=P_A(B)$.','$P=P_A(B)$ .').replace(r'\Omega^1_{B/A}$,',r'\Omega^1_{B/A}$ ,')
ch('corrected',old,new,'six of seven punctuation events','II.p126.withdraw-punctuation-normalizations','The six deletions of spaces before punctuation normalize the typewritten convention. Preserve the seventh event, which correctly excludes the comma after N from the underline; evidence/I_p126_proposition.png.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p126.upright-Latin','Latin letters and indices in the diagonal construction, proof and square are upright.')
 ch(layer,r'\mathbf N',r'\mathbb N','Proposition 1.2.5.3','II.p126.natural-numbers','The initial stem is double-stroked; evidence/I_p126_proposition.png.')
 ch(layer,r'\xrightarrow{\sim}',r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}','Proposition 1.2.5.3','II.p126.unheaded-isomorphism','The B_n-to-symmetric-algebra isomorphism uses an unheaded bar; evidence/I_p126_proposition.png.')
 ch(layer,'baseline=(current bounding box.center)','baseline=(B.base)','square (1.2.6.1)','II.p126.square-baseline','The equation number shares the baseline of the top B row; evidence/I_p126_base-change-square.png.')
 ch(layer,r'\raisebox{34bp}[0pt][0pt]{(1.2.6.1)}','(1.2.6.1)','square (1.2.6.1)','II.p126.square-label','Remove the compensated raised label after fixing the diagram baseline.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 for suffix in ['bisimplicial-cotangent-complex','diagonal-augmentation-restriction']:
  marker=r'\phantomsection\hypertarget{illusie:I:ch1:p126:'+suffix+'}{}%'
  new=new.replace('\\par\n'+marker+'\n\\noindent ','\n'+marker+'\n')
 ch(layer,old,new,'continuous definitions, proposition and proof','II.p126.prose-continuity','Join scan line wraps, including the two midparagraph semantic anchors; retain all anchors and the genuine paragraph/display divisions.','structure')
 old=region(layer);new=old
 if layer=='English':
  pairs=[(r'\uline{Suppose that, for every}',r'\uline{Suppose that}, \uline{for every}'),(r'\uline{(this is the case, for example, if}',r'(\uline{this is the case, for example, if}'),(r'\uline{degreewise). Then}',r'\uline{degreewise}). \uline{Then}'),(r'\uline{is a quasi-isomorphism.}',r'\uline{is a quasi-isomorphism}.')]
 else:
  pairs=[(r'\uline{Supposons que, pour chaque}',r'\uline{Supposons que}, \uline{pour chaque}'),(r'\uline{(c\'est le cas par exemple si}',r'(\uline{c\'est le cas par exemple si}'),(r'\uline{terme à terme). Alors}',r'\uline{terme à terme}). \uline{Alors}'),(r'\uline{est un quasi-isomorphisme.}',r'\uline{est un quasi-isomorphisme}.')]
  pairs[1]=( "\\uline{(c'est le cas par exemple si}","(\\uline{c'est le cas par exemple si}")
  if layer=='as-printed':pairs.append((r'$n\in\mathbb N$ \uline{, il existe un}',r'$n\in\mathbb N$ , \uline{il existe un}'))
 for a,b in pairs:
  assert a in new,a
  new=new.replace(a,b)
 ch(layer,old,new,'Proposition 1.2.5.3','II.p126.underline-stops','Commas separating the initial clauses, the explanatory parentheses, and full stops are outside underlining; evidence/I_p126_proposition.png. English follows the same emphasis boundaries.')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p126.boundary','The sentence describing square (1.2.6.1) ends this printed page.','structure')
verdict(page,'ILL-SC-20260804-0123','Seven punctuation/space events','Six optional spacing changes withdrawn; underline-comma repair retained and propagated to diplomatic','The scan has the comma after N outside the underline. This is a transcription repair, not an original mathematical error. No original mathematical error found.',ev)
verdict(page,'ILL-NORM-20260804-0154','Ten object-name capitalization events','All withdrawn','Printed capitalization is deliberate and grammatically adequate.',ev)
verdict(page,'ILL-TX-20260804-0150','Twelve anchors and diagram/display macros','All preserved; letterforms, unheaded bar, underlining, diagram baseline and prose restored','Every formula and small sign was enlarged. The constant-object subscript o is retained: the typewritten round glyph does not establish a different mathematical index.',ev)
verdict(page,'ILL-TR-20260804-0152','Diagonal construction and degreewise free-algebra criterion','Meaning confirmed','The translation preserves the constant case, flatness, columnwise quasi-isomorphism and first-quadrant spectral-sequence argument. Set already renders impersonal On pose adequately.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.2.5.flatness','In degree n, the diagonal resolution is P_(A_n)(B_n)_n, a polynomial A_n-algebra. Its differentials are free over that algebra; tensoring with B_n gives a free, hence flat, B_n-module. If A and B are constant simplicial rings, the resolution is constant in the horizontal direction, so taking the diagonal recovers the previously defined ordinary cotangent complex. Restriction of the bisimplicial augmentation consequently has the stated source and target.'),('II.1.2.5.3','For each fixed horizontal degree n, the hypothesis B_n is a symmetric algebra on a flat A_n-module lets Proposition 1.2.4.4 identify the vertical column augmentation with a quasi-isomorphism. Normalize and take its mapping cone: all vertical-column homology vanishes. The first-quadrant bicomplex filtration converges because each total degree has only finitely many terms; its total complex is acyclic. Eilenberg--Zilber compares the total complex with the diagonal, so the diagonal augmentation is a quasi-isomorphism. This checks the applicability and convergence of the cited results, not a new proof of the general Eilenberg--Zilber theorem.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p126_*.png')):f.write(f'| evidence/{p.name} | Printed p126, 800-dpi crop inspected during the first reading. |\n')
print('Page 126 edits and two proof checks recorded.')
