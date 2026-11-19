"""Primary reviewer's p123 audit of the cotangent-complex definition."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='123';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p123}'
ev='LNM239 scan PDF p141 / printed p123: complete 400-dpi page and both halves, followed by ten retained 800-dpi crops, personally inspected; all three complete source regions and all four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','body and square','II.p123.upright-Latin','The displayed and inline Latin letters, subscripts and diagram nodes are upright in the print; see all retained formula and square crops.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 ch(layer,old,new,'opening paragraph, definition and tensor construction','II.p123.prose-continuity','The supplied internal paragraph breaks divide ordinary printed line wraps, including the underlined definition. Restore continuous paragraphs without changing their words.','structure')
 old=region(layer);new=old+r'\clearpage'+'\n'
 ch(layer,old,new,'page boundary','II.p123.page-boundary','Keep the complete adjunction sentence on this printed page and enforce its boundary.','structure')
for layer in ('as-printed','corrected'):
 ch(layer,"et l'on note $L_{B/A}$, le","et l'on note $L_{B/A}$ le",'definition before (1.2.3.1)','II.p123.unprinted-comma','evidence/I_p123_definition-text.png shows no comma after L_{B/A}. The coordinated French verbs share their following object; no grammatical correction is required. The English apposition has different syntax and keeps its comma.','reading')
old=region('corrected');new=region('as-printed').replace('% DÉBUT DU FICHIER SOURCE','% BEGIN SOURCE').replace('% FIN DU FICHIER SOURCE','% END SOURCE')
ch('corrected',old,new,'five normalization-only differences','II.p123.withdraw-normalizations','The five lowercased object names are printed with capitals: Algèbre, Anneaux (twice), Module and Modules. No original error justifies these changes; restore the printed conventions.','reading')
verdict(page,'ILL-SC-20260804-0120','No original mathematical correction recorded','No new original correction adopted','The diagonal augmentation and the definition and functorial maps of the cotangent complex are well typed; the additional comma in both supplied French files was a transcription difference.',ev)
verdict(page,'ILL-NORM-20260804-0151','Five capitalization normalizations','All withdrawn','The corrected French now agrees with the as-printed text except for file comments; no necessary correction justifies the five normalizations.',ev)
verdict(page,'ILL-TX-20260804-0147','Ten anchors and named diagram/display macros','All retained','Compared every prime, subscript, exponent, underline scope, arrow and punctuation mark; retained the existing numbered-display and square macros, repaired upright notation, internal paragraph breaks and the boundary.',ev)
verdict(page,'ILL-TR-20260804-0149','Cotangent complex and its canonical maps','Meaning and terminology confirmed','English accurately distinguishes the B-linear map from its B-prime-linear adjoint. Degreewise free and cotangent complex are consistent terms. No English meaning or terminology change is required.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.p123.diagonal-quasi-isomorphism','For the bisimplicial underlying additive object P, take normalization in both nonnegative directions. Each vertical augmented column is the free resolution of B_n already checked on p121, hence has vertical homology B_n in degree zero and zero in positive degrees. The first-quadrant spectral sequence therefore identifies the homology of the total normalized complex with that of B. Each total degree has finitely many summands, so this use has no unbounded-totalization convergence issue. Applying the Eilenberg--Zilber comparison cited by the text gives the quasi-isomorphism from the diagonal to B. Degree n of the diagonal is P_{A_n}(B_n)_n, free over A_n by the recursive construction. This checks the application, not a new proof of the general Eilenberg--Zilber theorem.'),('II.p123.cotangent-functoriality-and-adjunction','Write phi:P->P-prime and beta:B->B-prime for the maps induced by the commutative ring square, with epsilon-prime phi=beta epsilon. The universal derivation gives the P-linear map Omega(P/A)->Omega(P-prime/A-prime), dp |-> d(phi(p)). The map on cotangent complexes sends dp tensor b to d(phi(p)) tensor beta(b); augmentation compatibility makes it balanced over P. It commutes with faces, degeneracies and composition by naturality of universal derivations and the resolution. Extension/restriction-of-scalars adjunction gives the displayed B-prime-linear map L_(B/A) tensor_B B-prime -> L_(B-prime/A-prime), without a flatness assumption or an assertion that it is an isomorphism.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p123_*.png')):f.write(f'| evidence/{p.name} | Printed p123, 800-dpi crop inspected during the first reading. |\n')
print('Page 123 edits and two mathematical checks recorded.')
