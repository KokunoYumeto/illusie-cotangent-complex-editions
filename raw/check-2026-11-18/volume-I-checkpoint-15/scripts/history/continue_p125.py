"""Primary reviewer's p125 audit of augmentation, H0 and flat symmetric algebras."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='125';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p125}'
ev='LNM239 scan PDF p143 / printed p125: both complete 400-dpi halves and twelve retained 800-dpi crops personally inspected; all three complete source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p125.upright-Latin','The augmentation, homology, free/symmetric algebras and differential modules all use upright Latin letters and indices.')
 ch(layer,r'\operatorname{Ext}',r'\mathop{\mathbb E\mathrm{xt}}\nolimits','Corollary 1.2.4.3','II.p125.Ext-letterform','evidence/I_p125_ext-der.png clearly shows a double-stroked initial E, followed by ordinary upright xt, as independently verified here rather than inferred from p91.')
 old=region(layer);new=old.replace(r'\xrightarrow{\sim}',r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}')
 ch(layer,old,new,'Proposition 1.2.4.4 and its proof','II.p125.unheaded-isomorphisms','Both B~S_A(E) and B~A[X] use unheaded bars. The Ext-to-Der map has an arrowhead and is retained; see evidence/I_p125_symmetric-proposition.png and evidence/I_p125_flat-reduction.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 ch(layer,old,new,'opening, proof and statement continuations','II.p125.prose-continuity','Every internal line-end paragraph break in these continuous statements and proofs is a transcription artifact. Retain the genuine divisions at headings and displays.','structure')
 old=region(layer);new=old.replace('``',r'\textquotedbl{}').replace("''",r'\textquotedbl{}').replace('« ',r'\textquotedbl{}').replace(' »',r'\textquotedbl{}')
 ch(layer,old,new,'name of the forgetful functor','II.p125.straight-quotes','The functor name is enclosed in straight double quotes, confirmed in evidence/I_p125_free-homotopy.png.')
 if layer=='English':
  changes=[(r'\uline{is an isomorphism.}',r'\uline{is an isomorphism}.'),(r'\uline{module. There is a functorial canonical}',r'\uline{module}. \uline{There is a functorial canonical}'),(r'\uline{module.}',r'\uline{module}.'),(r'\uline{is a quasi-isomorphism.}',r'\uline{is a quasi-isomorphism}.')]
 else:
  word='Module' if layer=='as-printed' else 'module'
  changes=[(r'\uline{est un isomorphisme.}',r'\uline{est un isomorphisme}.'),(r'\uline{'+word+r'. Il existe un isomorphisme canonique}',r'\uline{'+word+r'}. \uline{Il existe un isomorphisme canonique}'),(r'\uline{'+word+r' plat.}',r'\uline{'+word+r' plat}.'),(r'\uline{est un quasi-isomorphisme.}',r'\uline{est un quasi-isomorphisme}.')]
 old=region(layer);new=old
 for a,b in changes:
  assert a in new,a
  new=new.replace(a,b)
 ch(layer,old,new,'three statements','II.p125.underline-stops','Underlining stops before the full stops, including between Module and Il in the corollary; confirmed in the proposition and corollary crops.')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p125.boundary','The final tensor-product argument and cqfd end this page.','structure')
old=region('corrected');new=region('as-printed')
ch('corrected',old,new,'eight normalization events','II.p125.withdraw-normalizations','Seven object-name capitalization changes and the quotation normalization have no mathematical or grammatical necessity. Restore the printed conventions.','reading')
ch('English','we may therefore suppose','one may therefore suppose','flat-module reduction','II.p125.impersonal-on.1','French on peut is impersonal; the supplied standard distinguishes it from authorial nous.','terminology')
ch('English','We\nthen have','One\nthen has','free-algebra reduction','II.p125.impersonal-on.2','French On a is impersonal and is rendered with one under the supplied standard.','terminology')
verdict(page,'ILL-SC-20260804-0122','No original correction recorded','Confirmed: no original error found on this page','The H0 identification, Ext-zero corollary and flat symmetric-algebra proposition are checked with their stated hypotheses. No mathematical wording is altered.',ev)
verdict(page,'ILL-NORM-20260804-0153','Eight capitalization/quotation events','All withdrawn','These are optional normalizations of printed conventions.',ev)
verdict(page,'ILL-TX-20260804-0149','Ten anchors and two display macros','All preserved; upright Latin, double-stroked Ext, unheaded bars, underline stops and prose restored','Every displayed and inline index, exponent, reference and small sign was enlarged; the corollary underline was recropped to include its second line.',ev)
verdict(page,'ILL-TR-20260804-0151','Meaning of the augmentation proofs','Confirmed; two impersonal on clauses corrected','Retain the glossary rendering cokernel for conoyau; here of the two maps means their categorical coequalizer. Homotopy equivalence renders homotopisme, and inductive limits follows the supplied standard.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.2.4.2','For a B-module M, a map H0(L)->M is a map Omega(P0/A) tensor_(P0) B -> M equalizing the two face-induced maps from degree one. By universal derivations this is a derivation P0->M equalizing P1=>P0. Since B is their coequalizer as an A-algebra, these are exactly Der_A(B,M)=Hom_B(Omega(B/A),M). Yoneda identifies H0(L) with Omega(B/A), and the identification is induced by the augmentation.'),('II.1.2.4.3','The cotangent complex is in nonnegative homological degrees and M is in degree zero. The degree-zero derived Hom is therefore Hom_B(H0(L),M), by the standard truncation property (or the degree-zero cycles of Hom into an injective resolution). Combining the preceding checked identification with the universal property of Omega gives Ext^0_B(L,M)=Der_A(B,M), naturally in M.'),('II.1.2.4.4','Use the cited local Lazard--Deligne presentation of flat E by free modules. Symmetric algebra and the previously checked cotangent construction commute with this local inductive system; local exactness lets the claimed quasi-isomorphism be checked on the free stages. For B=A[X], the free-algebra adjunction supplies a split extra degeneracy, hence P_A(B)->B is a simplicial A-algebra homotopy equivalence. Applying the functor Omega(-/A) preserves the simplicial homotopy identities, so Omega(P/A)->Omega(B/A) is a quasi-isomorphism. Each Omega(P_n/A) is a free P_n-module. Thus tensoring the quasi-isomorphism P->B with the flat simplicial P-module Omega(P/A) gives a quasi-isomorphism Omega(P/A)->Omega(P/A) tensor_P B. The augmentation triangle and two-out-of-three prove the final assertion. This is the use of I 3.3.4.6, whose statement and unit argument on the already reviewed p92 were reread; no new proof of the general local Lazard--Deligne theorem is claimed.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p125_*.png')):f.write(f'| evidence/{p.name} | Printed p125, 800-dpi crop inspected during the first reading. |\n')
q=ROOT/'READING_QUESTIONS.tsv'
rows=list(csv.reader(q.open(),delimiter='\t'))
for row in rows:
 if row and row[0]=='I-Q008':
  row[1]='91;125';row[4]+=' Printed p125 independently confirms and restores the same double-stroked initial E in Corollary 1.2.4.3.';row[6]+='; evidence/I_p125_ext-der.png'
with q.open('w',newline='') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows)
print('Page 125 edits and three proof checks recorded.')
