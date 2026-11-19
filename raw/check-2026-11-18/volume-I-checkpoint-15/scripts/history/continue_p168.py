"""Primary reviewer's page 168 audit; run once."""
import sys,csv,re
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='168';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p168}'
ev='LNM239 scan PDF p186 / printed p168: both complete 400-dpi halves, fourteen 800-dpi crops and the second-square double-prime detail at 1600 dpi personally inspected; complete D/C/English source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=r"""0\longrightarrow\operatorname{Der}_A(B,M')
      \xrightarrow{\,1\,}\operatorname{Der}_A(B,M)
      \xrightarrow{\,2\,}\operatorname{Der}_A(B,M'')
      \xrightarrow{\,3\,}\operatorname{Exal}_A(B,M')"""
new=r"""0\xrightarrow{\,1\,}\operatorname{Der}_A(B,M')
      \xrightarrow{\,2\,}\operatorname{Der}_A(B,M)
      \xrightarrow{\,3\,}\operatorname{Der}_A(B,M'')
      \longrightarrow\operatorname{Exal}_A(B,M')"""
ch('as-printed',old,new,'first row of (1.2.4.2)','III.1.2.4.2.printed-arrow-labels','evidence/I_p168_LES1.png unambiguously places 1 on 0->Der(M-prime), 2 on Der(M-prime)->Der(M), and 3 on Der(M)->Der(M-double-prime). Restore these printed positions. The supplied corrected and English positions are retained: Proposition1.2.4.3 identifies 3 with the boundary Der(M-double-prime)->Exal(M-prime), and 1,2 are the coefficient functoriality maps.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p168.upright-Latin','Restore upright printed Latin mathematics.')
 old=region(layer);new,n=re.subn(r'\\operatorname\{Ext\}(?=(?:\^[i012])?_B)',lambda m:r'\mathop{\mathbb E\mathrm{xt}}\nolimits',old)
 assert n==6,n
 ch(layer,old,new,'opening, long sequence, first square and proof prose','III.p168.hyper-Ext','Restore six individually enlarged double-stem E operators; the second square has ordinary Ext_P of the module Omega and its plain E is retained. evidence/I_p168_opening.png; evidence/I_p168_LES2.png; evidence/I_p168_square1-top.png; evidence/I_p168_square-prose.png; evidence/I_p168_square2-top.png.')
 ch(layer,r'\mathop{\mathbb E\mathrm{xt}}\nolimits_B$',r'\mathop{\mathbb E\mathrm{xt}}\nolimits$','proof prose after first square','III.p168.unprinted-Ext-subscript','The prose says the exact sequence of hyper-Ext without a B subscript; remove the unprinted subscript. evidence/I_p168_square-prose.png.','reading')
 ch(layer,r'\begin{minipage}{349bp}',r'\begin{minipage}[t]{349bp}','(1.2.4.2) carrier','III.p168.sequence-baseline','Align the sequence carrier with the first row, where the printed equation tag lies.')
 ch(layer,r'\raisebox{8.0bp}{(1.2.4.2)}',r'(1.2.4.2)','(1.2.4.2) tag','III.p168.sequence-tag','Remove the artificial tag raise after giving the carrier its first-row baseline.')
 # Match the printed left edges, upright vertical maps, and baseline commas.
 old=region(layer);new=old
 for name,x,y in [('TL',12,80),('TR',156,80),('BL',12,3),('BR',156,3)]:
  ox=46 if name in ('TL','BL') else 196
  new=new.replace(f'\\node ({name}) at ({ox},{y})',f'\\node[anchor=west] ({name}) at ({x},{y})')
 for name,x,y in [('TL',14,91),('TR',152,91),('BL',14,3),('BR',152,3)]:
  ox=49 if name in ('TL','BL') else 201
  new=new.replace(f'\\node ({name}) at ({ox},{y})',f'\\node[anchor=west] ({name}) at ({x},{y})')
 new=new.replace(r'(TL) -- (BL);',r'([xshift=24bp]TL.south west) -- ([xshift=24bp]BL.north west);')
 new=new.replace(r'(TR) -- (BR);',r'([xshift=25bp]TR.south west) -- ([xshift=25bp]BR.north west);')
 new=new.replace(r'(TR) -- node[right=8bp] {$\operatorname{alg}$} (BR);',r'([xshift=25bp]TR.south west) -- node[right=8bp] {$\operatorname{alg}$} ([xshift=25bp]BR.north west);')
 new=new.replace(r'\node at (245,-2) {$,$};',r'\node[anchor=base] at ([xshift=30bp]BR.base east) {$,$};')
 new=new.replace(r'\node at (251,-2) {$,$};',r'\node[anchor=base] at ([xshift=30bp]BR.base east) {$,$};')
 ch(layer,old,new,'two commutative squares','III.p168.square-alignment','Restore the shared left edges of each column and vertical arrows under the operator/argument junction, instead of centering expressions of unequal width. Put each comma on the lower formula baseline. Preserve all eight arrows, both partial labels, alg, and macro/node names. All six square crops inspected; final geometry requires the build.')
 ch(layer,r'\uline{$u$}',r'$u$','proposition','III.p168.plain-u','The mathematical u is not underlined. evidence/I_p168_prop-body.png.')
 ch(layer,r'\uline{$X$}',r'$X$','proposition','III.p168.plain-X','The mathematical X is not underlined. evidence/I_p168_prop-body.png.')
 if layer!='English':
  ch(layer,r'\uline{une $A$-dérivation de $B$}',r'\uline{une} $A$-\uline{dérivation de} $B$','proposition','III.p168.derivation-underline','The underline excludes the A-prefix and final B. evidence/I_p168_prop-body.png.')
  ch(layer,r'\uline{est la $A$-extension}',r'\uline{est la} $A$-\uline{extension}','proposition','III.p168.extension-underline','The underline excludes the A-prefix. evidence/I_p168_prop-body.png.')
  ch(layer,'canonique\\par\n\n\\noindent fonctoriel','canonique fonctoriel','opening prose','III.p168.opening-paragraph','Join the typographic line break inside one printed sentence.','structure')
  needle="\\uline{coïncide avec l'homomorphisme}\\par\n\n\n\\vspace{5bp}\n"
  replacement="\\uline{coïncide avec l'homomorphisme} \n"
 else:
  ch(layer,r'\uline{be an $A$-derivation of $B$}',r'\uline{be an} $A$-\uline{derivation of} $B$','proposition','III.p168.derivation-underline','Follow the printed scope of emphasis, excluding the mathematical A-prefix and B. evidence/I_p168_prop-body.png.')
  ch(layer,r'\uline{is the $A$-extension}',r'\uline{is the} $A$-\uline{extension}','proposition','III.p168.extension-underline','Follow the printed emphasis, excluding the mathematical A-prefix. evidence/I_p168_prop-body.png.')
  ch(layer,'functorial\\par\n\n\\noindent canonical','functorial canonical','opening prose','III.p168.opening-paragraph','Join the line break inside one printed sentence.','structure')
  needle='\\uline{coincides with the homomorphism}\\par\n\n\n\\vspace{5bp}\n'
  replacement='\\uline{coincides with the homomorphism} \n'
 ch(layer,needle,replacement,'proposition boundary-map lead','III.p168.inline-boundary-lead','The boundary map continues the proposition in the same paragraph; remove the invented display break and spacing while retaining its anchor. evidence/I_p168_prop-body.png.','structure')
 ch(layer,r'\noindent\hspace*{18.0bp}$\partial:',r'$\partial:','proposition boundary map','III.p168.inline-boundary-map','The map is inline in the proposition.','structure')
 ch(layer,"\\operatorname{Exal}_A(B,M')$\n\\par\n\n\\vspace{5bp}\n","\\operatorname{Exal}_A(B,M')$ \n",'proposition after boundary map','III.p168.inline-boundary-continuation','Continue directly with defined as follows, keeping its anchor.','structure')
 old=region(layer)
 if layer=='English':new=old.replace('with the notation\\par\n\n','with the notation\n').replace('\\noindent of (1.2.3),','of (1.2.3),')
 else:new=old.replace('avec les notations\\par\n\n','avec les notations\n').replace('\\noindent de (1.2.3),','de (1.2.3),')
 ch(layer,old,new,'lead to second square','III.p168.proof-paragraph','Join the false paragraph inside the proof sentence; preserve the intervening anchor. evidence/I_p168_square-prose.png.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p168.page-boundary','Preserve the printed page boundary.','structure')
ch('English','the exact sequence of $','of $','opening','III.p168.duplicated-sequence','The preceding page already ends with the exact sequence. Remove its duplicated English continuation; the French continues la suite / exacte des.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p168:first-square','Ext^0_B(L_B/A,M)','Ext^0_B(L_B/A,M-double-prime)','Confirm the existing corrected/English coefficient M-double-prime. The vertical identification with Der_A(B,M-double-prime) and the boundary of the coefficient sequence require this module. Diplomatic M is printed and retained.',ev+'evidence/I_p168_square1-top.png; evidence/I_p168_square1-bottom.png.')
verdict(page,'SUPPLIED-SILENT-REPAIR:I:p168:arrow-labels','First row labels 1,2,3 on its first,second,third arrows','First row labels 1,2,3 on its second,third,fourth arrows','Restore the printed label positions only in the diplomatic layer. Confirm the already supplied corrected/English intended positions as an original misprint repair: 3 must be the boundary explicitly described by Proposition1.2.4.3, while 1,2 are coefficient functoriality. No added correction row is fabricated for unchanged corrected/English bytes.',ev+'evidence/I_p168_LES1.png; evidence/I_p168_prop-heading.png; evidence/I_p168_prop-body.png. The last-square lower-left module has two primes, confirmed at 1600 dpi, and is retained in all layers.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.4.2.coefficient-sequence','targeted proof check','Applying RHom_B(L_B/A,-) to the coefficient short exact sequence gives the displayed long exact sequence. The nonnegative homological degrees of L and the degree-zero module give vanishing negative Ext. The checked degree-zero and degree-one identifications yield Der and Exal; coefficient functoriality identifies the first two nontrivial Der maps and the two Exal maps. The printed first-row labels1,2,3 are shifted one arrow left; correcting them is necessary for the explicit identification of arrow3 with the connecting map in1.2.4.3.'),('III.1.2.4.3.ordinary-square','targeted proof check','For v:Omega^1_P/A->M-double-prime, the module boundary is the pullback J={(m,w):f(m)=v(w)} of the coefficient extension. The algebra alg(J) consists of pairs (b,(m,w)) with w=d(b); it is canonically {(b,m):f(m)=v(d(b))}. Writing u=v composed with d, this is exactly the pullback of P plus M -> P plus M-double-prime along (id,u). The formulas preserve multiplication because u is an A-derivation and the square-zero product has cross terms bm-prime+b-prime m. Thus the lower square commutes with the positive boundary convention; no global projectivity of Omega is needed.'),('III.1.2.4.3.first-square-types','targeted proof check','The first square must start at Ext^0_B(L_B/A,M-double-prime): its vertical map is the coefficient-preserving degree-zero identification and its horizontal map is the connecting morphism to Ext^1_B(L_B/A,M-prime). The printed unprimed M fails both types. The right vertical composite, inverse of1.2.1.1 followed by beta1.2.3.1, has the correct direction. Compatibility with the simplicial comparison is not yet certified here; the author proof continues on169.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p168_*.png')):f.write(f'| evidence/{p.name} | Page168 audit: personally inspected; 800 dpi except the named1600-dpi double-prime detail. |\n')
print('Page168 repairs, two verdicts and three targeted checks recorded.')
