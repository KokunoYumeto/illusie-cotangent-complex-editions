"""Primary reviewer's page169 audit; run once."""
import sys,csv,re
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='169';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p169}'
ev='LNM239 scan PDF p187 / printed p169: both complete400-dpi halves and eleven800-dpi crops personally inspected; six crops expanded and reinspected to complete clipped indices, labels or prose. Complete D/C/English regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old,new in [('$P$-modules','$P$-Modules'),("d'anneaux","d'Anneaux"),('$C$-module','$C$-Module'),("$M''=\\Omega^1_{P/A}$,","$M''=\\Omega^1_{P/A}$ ,"),('$T$,','$T$ ,')]:
 ch('corrected',old,new,'opening and setup','III.p169.withdraw-normalization','Withdraw optional capitalization or spacing normalization; the printed reading is coherent.','reading')
for layer in ['corrected','English']:
 ch(layer,r'\operatorname{Exal}_A(P,\Omega^1_{P/A})',r"\operatorname{Exal}_A(P,M')",'identity reduction, line5','III.1.2.4.3.identity-target','The coefficient in Exal is the kernel M-prime, not the quotient Omega=M-double-prime. Both composites in the preceding square end at Exal_A(P,M-prime). Retain the printed Omega only in D. evidence/I_p169_identity-source.png; evidence/I_p169_identity-target.png; evidence/I_p168_square2-bottom.png.','misprint of the original')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p169.upright-Latin','Restore upright printed Latin mathematics.')
 old=region(layer);new,n=re.subn(r'\\operatorname\{Ext\}(?=\^[i2]_C)',lambda m:r'\mathop{\mathbb E\mathrm{xt}}\nolimits',old);assert n==3,n
 ch(layer,old,new,'transitivity sequence and lead','III.p169.hyper-Ext','Restore the three enlarged double-stem E operators; the opening ordinary Ext_P is explicitly distinguished by the print and remains plain. evidence/I_p169_ordinary-Ext.png; evidence/I_p169_LES-lead.png; evidence/I_p169_LES2.png.')
 ch(layer,r'\draw[->] (T) -- (BL);',r'\draw[>->] (T) -- (BL);','transitivity triangle','III.p169.degree-one-arrow','Restore the printed tail mark on the degree-one arrow. It is not an extra shifted-object label. evidence/I_p169_triangle.png.')
 ch(layer,'baseline=(current bounding box.center)','baseline=(T.base)','transitivity triangle carrier','III.p169.triangle-baseline','The equation number is aligned with the upper vertex.')
 ch(layer,r'\raisebox{42.0bp}{(1.2.5.2)}',r'(1.2.5.2)','transitivity tag','III.p169.triangle-tag','Remove the hand raise after setting the actual top-vertex baseline.')
 ch(layer,r'\node at (239,-1) {$,$};',r'\node[anchor=base] at ([xshift=39bp]BR.base east) {$,$};','triangle comma','III.p169.triangle-comma','Align the comma to the lower formula baseline as printed.')
 ch(layer,r'\begin{minipage}{357bp}',r'\begin{minipage}[t]{357bp}','long sequence carrier','III.p169.sequence-baseline','Align the two-row carrier at its first row.')
 ch(layer,r'\raisebox{8.0bp}{(1.2.5.3)}',r'(1.2.5.3)','long sequence tag','III.p169.sequence-tag','Align the tag to the first row rather than a manual raise.')
 old=region(layer);new=old
 if layer!='English':
  new=new.replace('trivialement\\par\n\n','trivialement\n').replace('\\noindent des définitions','des définitions')
  new=new.replace('un triangle\\par\n\n','un triangle\n').replace('\\noindent distingué','distingué')
  new=new.replace("(1.2.5.2)\\par\n\n\\noindent s'écrit","(1.2.5.2) s'écrit")
 else:
  new=new.replace('trivially\\par\n\n','trivially\n').replace('\\noindent from the definitions','from the definitions')
  new=new.replace('a distinguished\\par\n\n','a distinguished\n').replace('\\noindent triangle','triangle')
  new=new.replace('(1.2.5.2)\\par\n\n\\noindent is written','(1.2.5.2) is written')
 new=new.replace('(cf.\\par\n\n\\noindent (II','(cf. (II')
 ch(layer,old,new,'proof conclusion, triangle lead and sequence prose','III.p169.paragraphs','Remove four false paragraph breaks inside printed sentences while preserving every intervening anchor.','structure')
 if layer!='English':ch(layer,'directe- \nment','directement','remark1.2.4.4','III.p169.line-hyphen','Join the printed line-end hyphenation; it is not a lexical hyphen.')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p169.page-boundary','Preserve the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p169','P-Modules; Anneaux; C-Module; two spaces before commas','lowercase; spaces omitted','Withdraw three capitalization and two spacing normalizations. Correct the newly identified original Exal target coefficient only in C/English. No other original error identified. The transitivity tensor is printed without a derived superscript and is valid for the degreewise flat standard cotangent complex; all five long-sequence labels are in their proper positions on this page.',ev+'evidence/I_p169_ordinary-Ext.png; evidence/I_p169_triangle-lead.png; evidence/I_p169_identity-target.png; evidence/I_p169_triangle.png; evidence/I_p169_LES1.png; evidence/I_p169_LES2.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.4.3.proof.identity-reduction','targeted proof check','For a general v:Omega->M-double-prime, pull the coefficient extension back along v. Naturality reduces the comparison to the identity map Omega->Omega, keeping its kernel M-prime unchanged. Both constructions then give alg of that pulled-back module extension, as explicitly checked by pairs on168. Thus the target is Exal_A(P,M-prime); replacing it by Exal_A(P,Omega) confuses quotient and kernel. Naturality of the augmentation/chi comparison and the coefficient connecting maps carries this ordinary square through1.2.1.1 and beta to the upper square, completing1.2.4.3 with this correction.'),('III.1.2.4.4.direct-exactness','targeted proof check','At Der(M), exactness is coefficient exactness. A derivation u:B->M-double-prime has zero boundary exactly when its pullback of B plus M splits, equivalently when u lifts to an M-valued derivation. If an M-prime extension becomes split after pushout to M, an isomorphism of that pushout with B plus M descends modulo M-prime to (id,u):B->B plus M-double-prime and identifies the original extension with its pullback. Finally, if an M extension E becomes split after pushout to M-double-prime, identify that pushout with B plus M-double-prime; the inverse image of B plus0 in E is an M-prime extension and pushes out to E. Its epimorphism onto B is verified locally by adjusting a lift with a section of M mapping to the unwanted M-double-prime component. These arguments prove every asserted exactness position through Exal_A(B,M), without asserting surjectivity of the next map.'),('III.1.2.5.3.transitivity','targeted proof check','The transitivity triangle in D(C), after applying RHom_C(-,M), gives the displayed sequence. Derived tensor/Hom adjunction identifies Ext_C(L_B/A tensor_B C,M) with Ext_B(L_B/A,M); the ordinary displayed tensor computes the derived tensor since the standard L_B/A is bounded below and degreewise flat. Degree0/1 classifications give the displayed Der/Exal groups. The map Der_A(C,M)->Der_A(B,M) is precomposition with f; forgetting the B-algebra structure gives Exal_B(C,M)->Exal_A(C,M), and pullback along f gives Exal_A(C,M)->Exal_A(B,M).'),('III.1.2.5.functoriality-references','used and rechecked in this run','Personally reinspected II1.1.2.8 on116 (differential base-change map), III1.1.5.3 and1.1.5.4 on156 (extension pullback and restriction of base), and the transitivity triangleII2.1.2.1 on134. Their directions agree with arrows1,2,4,5 and the triangle used here. No reference correction is needed.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p169_*.png')):f.write(f'| evidence/{p.name} | Page169 audit: final expanded800-dpi crop personally inspected. |\n')
 f.write('| evidence/I_p116_base-change-map.png; evidence/I_p134_triangle.png; evidence/I_p156_restriction-group.png; evidence/I_p156_forgetful-groups.png | Personally reinspected for the references used on169. |\n')
print('Page169 repairs, verdict and four mathematical checks recorded.')
