"""Primary reviewer's page175 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='175';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p175}'
ev='LNM239 scan PDF p193 / printed p175: both complete400-dpi halves and twelve800-dpi crops personally inspected. All three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old in ["un morphisme d'anneaux","Soient des morphismes d'anneaux"]:
 ch('corrected',old,old.replace('anneaux','Anneaux'),'statements','III.p175.withdraw-capitalization','Withdraw optional capitalization normalization. evidence/I_p175_lemma.png; evidence/I_p175_proposition.png.','reading')
for layer in ['corrected','English']:
 pairs=[(r'\IllusieSurjectionExtensionSequencePOneSeventyFive{.}',r'\IllusieSurjectionExtensionSequencePOneSeventyFive{\hspace{3.0bp}.}'),(r'\IllusieSurjectionHOnePOneSeventyFive{.}',r'\IllusieSurjectionHOnePOneSeventyFive{\hspace{3.0bp}.}'),(r'\IllusieSurjectionHomComparisonPOneSeventyFive{,}',r'\IllusieSurjectionHomComparisonPOneSeventyFive{\hspace{3.0bp},}'),(r'\IllusieSurjectionRingMorphismsPOneSeventyFive{,}',r'\IllusieSurjectionRingMorphismsPOneSeventyFive{\hspace{3.0bp},}'),(r'$H_0(L_{B/A})=0$,',r'$H_0(L_{B/A})=0$\hspace{3.0bp},'),(r'$H_0(L_{B/A})=0$.',r'$H_0(L_{B/A})=0$\hspace{3.0bp}.'),(r'$\Omega^1_{B/A}=0$,',r'$\Omega^1_{B/A}=0$\hspace{3.0bp},')]
 if layer=='corrected':pairs += [(r'\uline{surjectif de noyau $I$}.',r'\uline{surjectif de noyau $I$}\hspace{3.0bp}.'),(r'\uline{est surjectif de noyau $I$}.',r'\uline{est surjectif de noyau $I$}\hspace{3.0bp}.')]
 else:pairs += [(r'\uline{surjective with kernel $I$}.',r'\uline{surjective with kernel $I$}\hspace{3.0bp}.'),(r'\uline{is surjective with kernel $I$}.',r'\uline{is surjective with kernel $I$}\hspace{3.0bp}.')]
 for old,new in pairs:ch(layer,old,new,'formula punctuation','III.p175.punctuation-spacing','Withdraw optional corrected-French spacing changes and match the English formulas to the corrected French and print. evidence/I_p175_lemma.png; evidence/I_p175_extension.png; evidence/I_p175_corollary.png; evidence/I_p175_h-one.png; evidence/I_p175_proof-projection.png; evidence/I_p175_hom-comparison.png; evidence/I_p175_proposition.png.','reading' if layer=='corrected' else 'typesetting')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p175.upright-Latin','Restore upright printed Latin mathematics.')
 ch(layer,r'\operatorname{Ext}^1_B',r'\mathop{\mathbb E\mathrm{xt}}\nolimits^1_B','Hom comparison','III.p175.hyper-Ext','Restore the clearly doubled printed E. evidence/I_p175_hom-ext.png.','reading')
 terms=['surjective with kernel','is surjective with kernel'] if layer=='English' else ['surjectif de noyau','est surjectif de noyau']
 for term in terms:ch(layer,r'\uline{'+term+r' $I$}',r'\uline{'+term+r'} $I$','statement emphasis','III.p175.kernel-outside-underline','The kernel letter I is outside both printed underline spans. evidence/I_p175_lemma.png; evidence/I_p175_proposition.png.')
 old=region(layer);new=old
 if layer=='English':
  new=new.replace(r'\uline{Denote}\par'+'\n\n',r'\uline{Denote by}'+'\n').replace(r'\noindent\makebox[89.0bp][s]{by $U$\hfill\uline{the $A$-extension}}',r'$U$ \uline{the} $A$-\uline{extension}')
  new=new.replace(r'\uline{and a}\par'+'\n\n'+r'\noindent\uline{canonical functorial isomorphism}',r'\uline{and a canonical functorial isomorphism}')
  new=new.replace('one deduces a functorial'+r'\par'+'\n\n'+r'\noindent isomorphism','one deduces a functorial isomorphism')
 else:
  new=new.replace(r'\uline{Notons}\par'+'\n\n',r'\uline{Notons}'+'\n').replace(r'\noindent $U$\hspace{10.0bp}\uline{la A-extension}',r'$U$ \uline{la} $A$-\uline{extension}')
  new=new.replace(r'\uline{et un}\par'+'\n\n'+r'\noindent\uline{isomorphisme fonctoriel canonique}',r'\uline{et un isomorphisme fonctoriel canonique}')
  new=new.replace('on en déduit un isomorphisme'+r'\par'+'\n\n'+r'\noindent fonctoriel','on en déduit un isomorphisme fonctoriel')
 ch(layer,old,new,'statement and proof prose','III.p175.false-paragraphs-and-prefix','Join three line-wrap paragraph breaks, remove the fixed-width English phrase carrier, and leave A- outside the underline as printed; preserve every anchor. evidence/I_p175_lemma.png; evidence/I_p175_corollary.png; evidence/I_p175_hom-comparison.png.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p175.page-boundary','Preserve the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p175','Printed Anneaux and punctuation spacing','Two lowercase normalizations and nine removed spaces','Withdraw these optional normalizations. No original mathematical error identified. Restore hyper-Ext, upright Latin mathematics, the precise underline boundaries and continuous prose. All four headed isomorphisms, the baseline pushout star and the six formula carriers are retained.',ev+'evidence/I_p175_hom-ext.png; evidence/I_p175_pushout.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.8.extension-classification','independent re-proof','Given an A-extension E of B by M, its structural map h:A->E sends I into M and I squared to zero. Hence it induces a unique B-linear f:I/I squared->M and a morphism of extensions U->E. The pushout f*U->E is the identity on kernel M and quotient B, and is therefore an isomorphism. Conversely that pushout induces f, proving the claimed bijection; pushout and Baer sum give additivity and functoriality. This supplies a direct proof without inspecting the external EGA18.3.8 citation.'),('III.1.2.8.1.canonical-H1','targeted proof check','Surjectivity gives B tensor_A B=B and Omega1_B/A=0, hence H0(L_B/A)=0 by II1.2.4.2, personally reinspected on125. The cotangent complex has nonnegative homological degrees; truncation at degree1 therefore induces Hom_B(H1(L),M)=Hom_D(L,M[1]) by the standard t-structure vanishing. Combining this natural isomorphism with1.2.3 and1.2.8 gives Hom_B(I/I squared,M)=Hom_B(H1(L),M), so Yoneda gives the canonical H1(L)->I/I squared isomorphism in the printed direction. No projectivity of I/I squared is required.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p175_*.png')):f.write(f'| evidence/{p.name} | Page175 audit:800-dpi crop personally inspected. |\n')
 f.write('| evidence/I_p125_h-zero.png | Personally reinspected for175: the canonical H0 identification in II1.2.4.2. |\n')
print('Page175 repairs, verdict and two proof checks recorded.')
