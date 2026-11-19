"""Primary reviewer's page174 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='174';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p174}'
ev='LNM239 scan PDF p192 / printed p174: both complete400-dpi halves, nine800-dpi crops and a1600-dpi underline crop personally inspected; boundary crop expanded and reinspected to include all exponents. All three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old,new in [(r'\IllusiePrincipalPartsCompositePOneSeventyFour{,}',r'\IllusiePrincipalPartsCompositePOneSeventyFour{\hspace{3.0bp},}'),(r'\IllusiePrincipalPartsDerivationRowPOneSeventyFour{correspond à la $A$-dérivation}{,}',r'\IllusiePrincipalPartsDerivationRowPOneSeventyFour{correspond à la $A$-dérivation}{\hspace{3.0bp},}')]:ch('corrected',old,new,'formula punctuation','III.p174.withdraw-spacing','Withdraw optional punctuation-spacing normalization. evidence/I_p174_composite.png; evidence/I_p174_final-proof.png.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p174.upright-Latin','Restore upright printed Latin mathematics.')
 for i in range(4):
  s=region(layer);start=s.index(r'\providecommand{\IllusiePrincipalPartsBoundaryMapPOneSeventyFour}');p=s.index(r'\operatorname{Ext}',start);n=s[:p]+s[p:].replace(r'\operatorname{Ext}',r'\mathop{\mathbb E\mathrm{xt}}\nolimits',1)
  ch(layer,s,n,'corollary1.2.7 and proof','III.p174.hyper-Ext','Restore the printed doubled-E hyper-Ext in the two boundary terms, corollary statement and proof prose. Ordinary Ext in the alg map remains plain. evidence/I_p174_boundary.png; evidence/I_p174_statement.png; evidence/I_p174_final-proof.png; evidence/I_p174_alg-map.png.','reading')
 ch(layer,r'$0_{\mathrm{IV}}$\par'+'\n\n'+r'\noindent 20.2.2))',r'$0_{\mathrm{IV}}$ 20.2.2))','remark reference','III.p174.false-reference-paragraph','Join the reference split by a print line wrap; retain its doubled parentheses. evidence/I_p174_remark.png.','structure')
 oldmacro=r'''  \makebox[377bp][s]{%
    \IllusiePrincipalPartsCanonicalArrowPOneSeventyFour\hfill
    #1\hfill
    $d_{B/A}\otimes1:B\longrightarrow\Omega^1_{B/A}\otimes_B C#2$%
  }%'''
 newmacro=r'''  \IllusiePrincipalPartsCanonicalArrowPOneSeventyFour\ #1
  $d_{B/A}\otimes1:B\longrightarrow\Omega^1_{B/A}\otimes_B C#2$%'''
 ch(layer,oldmacro,newmacro,'final proof sentence','III.p174.unwrap-derivation-row','Restore inline prose and formulas rather than a fixed-width box; preserve the reusable carrier and its two arguments. evidence/I_p174_final-proof.png.','structure')
 old=region(layer);new=old
 lead='canonical arrow' if layer=='English' else 'flèche canonique'
 new=new.replace(lead+' \n\n\n'+r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:2:7:proof:canonical-arrow}',lead+'\n'+r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:2:7:proof:canonical-arrow}')
 new=new.replace(r'\IllusiePrincipalPartsCanonicalArrowPOneSeventyFour\quad ',r'\IllusiePrincipalPartsCanonicalArrowPOneSeventyFour\ ')
 new=new.replace(lead+r'\par'+'\n\n\n\n'+r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:2:7:proof:derivation}',lead+'\n'+r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:2:7:proof:derivation}')
 new=new.replace(r'\noindent\IllusiePrincipalPartsDerivationRowPOneSeventyFour',r'\IllusiePrincipalPartsDerivationRowPOneSeventyFour')
 new=new.replace(r'\par'+'\n'+r'\vspace{3.36bp}'+'\n'+r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:2:7:proof:conclusion}','\n'+r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:2:7:proof:conclusion}')
 ch(layer,old,new,'proof prose','III.p174.false-proof-paragraphs','Join continuous proof sentences around the canonical-arrow carriers, retaining all anchors and mathematical displays. evidence/I_p174_proof-canonical.png; evidence/I_p174_final-proof.png.','structure')
 if layer!='English':
  for old,new in [('conjonc- \ntion','conjonction'),('directe- \nment','directement')]:ch(layer,old,new,'proof and remark prose','III.p174.line-end-hyphen','Join the word split at a printed line end. evidence/I_p174_proof-end.png; evidence/I_p174_remark.png.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p174.page-boundary','Preserve the printed page boundary.','structure')
for old,new in [(r'\IllusiePrincipalPartsCompositePOneSeventyFour{,}',r'\IllusiePrincipalPartsCompositePOneSeventyFour{\hspace{3.0bp},}'),(r'\IllusiePrincipalPartsDerivationRowPOneSeventyFour{corresponds to the $A$-derivation}{,}',r'\IllusiePrincipalPartsDerivationRowPOneSeventyFour{corresponds to the $A$-derivation}{\hspace{3.0bp},}')]:ch('English',old,new,'formula punctuation','III.p174.English-formula-agreement','Match English formula punctuation/spacing to corrected French and print.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p174','Printed punctuation spacing','Two removed spaces','Withdraw both optional spacing normalizations. No original mathematical error identified. Restore four hyper-Ext symbols per layer while preserving the ordinary Ext of the alg map. The1600-dpi check confirms that the full phrase via l-isomorphisme is underlined, so that source scope is retained. Restore continuous prose and line-end words.',ev+'evidence/I_p174_alg-map.png; evidence/I_p174_boundary.png; evidence/I_p174_via-underline1600.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.6.8.and-1.2.5.4-completion','targeted proof check','The preceding lemma is explicitly left as an exercise; its diagram and exactness were proved directly in the173 event. Under the additional injectivity in1.2.6.8, the alg extension is the pullback of C plus Omega1_C/A along(id,d_C/B). Diagram1.2.6.7 gives a map from principal parts to that pullback, identical on kernel and quotient, hence an isomorphism of B-extensions. Combining this with1.2.6.5 gives alg(*)=partial(d tensor1) in the free-resolution case of170, and the stated covariance reduction completes1.2.5.4. This also agrees with the independent algebra calculation recorded on170.'),('III.1.2.6.9.direct-exactness','targeted proof check','Restriction has kernel Der_B(C,M). The boundary of u is C plus M with B-map(f,-u); it is split as a B-extension exactly when there is an A-derivation delta:C->M with delta f=-u, proving exactness at Der_A(B,M). A B-extension which becomes split over A, after choosing an A-splitting, has B-map(f,v) and is the boundary of-v; this proves exactness at Exal_B(C,M). An A-extension of C pulls back to the trivial A-extension of B exactly when f lifts to an A-algebra map B->E; such a lift is exactly a B-algebra structure on E. This proves exactness through Exal_A(C,M), as claimed. The external EGA reference itself has not been inspected.'),('III.1.2.7.boundary-class','targeted proof check','For the transitivity triangle K->L_C/A->L_C/B->K[1], K=L_B/A tensor_B C, the boundary of the canonical map K->N, N=Omega1_B/A tensor_B C, is its shifted composite with L_C/B->K[1]. Under the derivation identification that canonical map corresponds to d_B/A tensor1. Compatibility1.2.5.4 and lemma1.2.6.5 therefore identify this composite with the principal-parts extension class, with the positive sign stated. The standard cotangent model is degreewise flat, so its ordinary tensor computes the required scalar extension here. Personally reinspected II1.2.4.1 on125 and theoremIII1.2.3 on164; both are the cited maps.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p174_*.png')):f.write(f'| evidence/{p.name} | Page174 audit: final800-dpi crop or1600-dpi underline crop personally inspected. |\n')
 f.write('| evidence/I_p125_augmentation.png; evidence/I_p164_theorem.png | Personally reinspected for174: canonical augmentation and extension-class isomorphism. |\n')
print('Page174 repairs, verdict and three proof checks recorded.')
