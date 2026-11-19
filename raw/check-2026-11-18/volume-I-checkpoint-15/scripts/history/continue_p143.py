"""Primary reviewer's page 143 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='143';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p143}'
ev='LNM239 scan PDF p161 / printed p143: both complete 400-dpi halves and eight 800-dpi crops personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace("d'anneaux de","d'Anneaux de").replace('des anneaux et','des Anneaux et').replace("l'anneau de fractions","l'Anneau de fractions").replace('un anneau $','un Anneau $').replace('des anneaux est','des Anneaux est').replace('$T$.','$T$ .').replace("B'$.","B'$ .").replace('(cf. ([17]','(cf. ( [17]').replace('$u^{-1}(B^*)$.','$u^{-1}(B^*)$ .').replace('sur $A$,','sur $A$ ,')
ch('corrected',old,new,'corollary and localization prose','II.p143.withdraw-normalizations','Restore five printed capitals and five punctuation/reference spaces; preserve the necessary interchange of the derived-category arguments.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','II.p143.upright-Latin','All printed Latin mathematical and diagram letters are upright.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace('\\par\n\\vspace{4.7bp}\n\\noindent ','\n').replace('\\par\n\\vspace{1.5bp}\n\\noindent ','\n')
 new=new.replace('$.\\par\n\\phantomsection','$.\n\\phantomsection').replace('is a\\par\n\\phantomsection','is a\n\\phantomsection').replace('est un\\par\n\\phantomsection','est un\n\\phantomsection')
 for t in ["L'assertion",'The assertion',r'\uline{morphisme de localisation}',r'\uline{localization morphism}']:
  new=new.replace('\\noindent '+t,t)
 ch(layer,old,new,'corollary proof and localization definition','II.p143.prose-continuity','Join printed line wraps, including three spurious mid-sentence vertical gaps and the retained anchor boundaries. Preserve the corollary, proof and2.3.2 paragraph divisions.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p143.boundary','Retain the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p143','L(A-prime/A)=0 in D(B-prime), resp. L(B-prime/B)=0 in D(A-prime); five capitals and five spaces','Derived categories interchanged to D(A-prime), resp. D(B-prime); normalized capitals and spacing','Local source-comparison verdict, not a supplied decision-record ID. Confirm the category interchange: the cotangent complexes have coefficients in their numerator rings, as2.3.1 asserts. Withdraw the five capitalization and five spacing normalizations.',ev+'evidence/I_p143_proof.png, evidence/I_p143_hypothesis.png and evidence/I_p143_universal-property.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.3.1.1','By2.3.1 the two flat epimorphisms give L(A-prime/A)=0 in D(A-prime) and L(B-prime/B)=0 in D(B-prime), confirming the printed categories are interchanged. Transitivity for A->B->B-prime gives L(B/A) tensor_B^L B-prime isomorphic to L(B-prime/A). Transitivity for A->A-prime->B-prime gives L(B-prime/A) isomorphic to L(B-prime/A-prime). Their composite is the canonical comparison; flatness of B-prime over B identifies the derived tensor with the displayed ordinary tensor. This proves the corollary.'),('II.2.3.2.localization-properties','Replace X by the multiplicative subsheaf it generates; localization is given locally by fractions and then sheafification. A map from the localization is determined by the map from A, since inverses have unique images, proving the epimorphism property. For an injection M->N, if m/s maps to0 after localization, locally some allowed denominator t kills m in N, hence in M; therefore localization preserves injections. The natural identification M tensor_A X^{-1}A=X^{-1}M gives flatness. Finally Y=u^{-1}(B^*) contains X, and the universal maps B=X^{-1}A->Y^{-1}A->B are inverse by uniqueness. Every subsheaf of denominators realizing B lies in Y, so this is the largest such subsheaf. This argument does not assume enough points of the topos.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p143_*.png')):f.write(f'| evidence/{p.name} | Page143 audit:800-dpi crop personally inspected. |\n')
print('Page143 edits, verdict and two proof checks recorded.')
