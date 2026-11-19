"""Primary reviewer's page167 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='167';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p167}'
ev='LNM239 scan PDF p185 / printed p167: both complete400-dpi halves and fourteen800-dpi crops personally inspected, including two expanded crops completing initially clipped indices; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
ch('corrected','$B$-modules','$B$-Modules','last paragraph','III.p167.withdraw-capitalization','Withdraw the optional capitalization normalization.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p167.upright-Latin','Restore upright printed Latin mathematics.')
 old=region(layer);n=old.count(r'\mathcal Y');ch(layer,old,old.replace(r'\mathcal Y','Y'),'extension names','III.p167.plain-Y',f'Restore the {n} plain printed Y identifiers.')
 ch(layer,r'*P',r'*p','projection relation','III.p167.augmentation-p','The printed pullback is along lowercase augmentation p, not the algebra P.','reading')
 ch(layer,r'Y)*(H_0p)^{-1}*p',r'Y)\mathbin{\raisebox{-4bp}{$*$}}H_0p^{-1}*p','projection relation','III.p167.projection-notation','Remove unprinted parentheses around H_0p in this display and reproduce its visibly lowered, full-size first star; retain the actual parentheses in the diagram arrow label. No inverse direction changes.')
 ch(layer,r'D_{\bullet}(P)',r'\operatorname{D.}(P)','derived inverse identity','III.p167.derived-category-dot','The print has an upright D with a baseline period, not a subscript bullet.')
 old=region(layer);new=old
 for node,x in [('BN',132),('BE',190),('BP',247)]:
  oldx={'BN':137,'BE':195,'BP':252}[node];new=new.replace(f'\\node ({node}) at ({oldx},0)',f'\\node[anchor=west] ({node}) at ({x},0)')
 new=new.replace(r'{$v$} (BN);',r'{$v$} (TN |- BN.north);').replace(r'(TE) -- (BE);',r'(TE) -- (TE |- BE.north);').replace(r'{$(H_0p)^{-1}p$} (BP);',r'{$(H_0p)^{-1}p$} (TP |- BP.north);')
 ch(layer,old,new,'morphism diagram','III.p167.diagram-column-alignment','The lower homology expressions start with H below the upper N,E,P columns. Align their left edges and make the three arrows vertical at the upper-node abscissas. Preserve the two extension labels, all eleven arrows, both arrow labels and all macro/node names; final geometry requires the build.')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p167.page-boundary','Preserve the printed page boundary without adding or removing a prose paragraph.','structure')
ch('English',r'\text{dans }',r'\text{in }','derived inverse identity','III.p167.untranslated-dans','Translate the accidentally retained French word in the English display.','translation')
ch('English','But we have','But one has','homology identity lead','III.p167.impersonal-on','Preserve impersonal on.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p167','B-Modules','B-modules','Local source-comparison verdict, not a supplied record ID. Withdraw the optional capitalization. No original mathematical error identified. Restore lowercase augmentation p, remove unprinted projection-formula parentheses, reproduce the lowered first star, plain Y and upright D with a baseline dot, diagram-column alignment and page boundary. Translate the retained French dans in the English formula.',ev+'evidence/I_p167_projection-relation.png; evidence/I_p167_derived-inverse.png; evidence/I_p167_diagram-lower.png; evidence/I_p167_bottom-reference.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.3.proof.projection-relation','The canonical simplicial projection alg(Y)->H_0alg(Y) maps the kernel N by v:N->H_0N and the quotient P by its projection P->H_0P=(H_0p)^(-1)p. Applying the extension comparison1.1.4.1, directly reinspected on154, identifies v*alg(Y) with the pullback of H_0alg(Y) along this composite. This is precisely H_0alg(Y)*H_0p inverse*p. Parentheses omitted in the print are harmless conventional inverse notation; the trailing p must remain lowercase.'),('III.1.2.3.proof.alpha-beta-completion','The previous relation, compatibility of diff with kernel pushout, and chi pushout naturality give alpha beta(y)=sigma((H_0s)^(-1)v)chi(diff alg(Y)). The equivalence1.1.9 identifies diff alg(Y) with Y. Since M is constant and v is the canonical homology projection, vs=H_0s as actual maps M->H_0N. Hence ((H_0s)^(-1)v)s=id_M; s is invertible in D.(P), so (H_0s)^(-1)v=s^(-1) there. Therefore alpha beta(y)=sigma s^(-1)chi(Y)=y. Combined with the independent beta alpha check on166, this completes the stated bijection; its group-homomorphism property was checked at164.'),('III.1.2.4.references','Reinspected II1.2.4.3 on125: its canonical isomorphism Ext_B^0(L_B/A,M)=Der_A(B,M), together with the now checked extension classification1.2.3 in degree1, has the required coefficient variance to identify the first two degrees of the long exact sequence associated to0->M-prime->M->M-double-prime->0. This checks the two references and setup only; the actual sequence and its boundary description are on168 and not yet certified.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'used and rechecked in this run' if sid.endswith('references') else 'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p167_*.png')):f.write(f'| evidence/{p.name} | Page167 audit:800-dpi crop personally inspected; full versions complete the initial chi and final-identity crops. |\n')
 f.write('| evidence/I_p125_ext-der.png; evidence/I_p154_comparison.png | Personally reinspected for167: degree-zero classification and the canonical extension comparison. |\n')
print('Page167 repairs, verdict and three checks recorded.')
