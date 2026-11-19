"""Primary reviewer's page185 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='185';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p185}'
ev='LNM239 scan PDF p203 / printed p185: both complete400-dpi halves and eleven800-dpi crops personally inspected, with three upper-edge expansions reinspected; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
ch('corrected',"d'anneaux","d'Anneaux",'lemma','III.p185.withdraw-capitalization','Restore the printed capitalized noun; no necessary correction is involved. evidence/I_p185_lemma.png.','reading')
for layer in ['corrected','English']:
 for old,new in [(r'$B$,',r'$B$\hspace{3.0bp},'),(r'$)=(f_o,u)$.',r'$)=(f_o,u)$\hspace{3.0bp}.'),(r'$u$,',r'$u$\hspace{3.0bp},'),(r'$f_o$,',r'$f_o$\hspace{3.0bp},')]:
  ch(layer,old,new,'formula punctuation','III.p185.inline-punctuation','Restore printed formula punctuation spacing. evidence/I_p185_lemma.png; evidence/I_p185_condition.png; evidence/I_p185_explanation.png.','reading' if layer=='corrected' else 'typesetting')
 for macro in ['AlgmodPair','Square']:
  ch(layer,r'\IllusieFlatness'+macro+'POneEightyFive{,}',r'\IllusieFlatness'+macro+r'POneEightyFive{\hspace{3.0bp},}','display punctuation','III.p185.display-punctuation','Restore the printed terminal comma spacing. evidence/I_p185_pair.png; evidence/I_p185_square.png.','reading' if layer=='corrected' else 'typesetting')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','body','III.p185.upright-Latin','Restore upright printed Latin mathematics.')
 s=region(layer);ch(layer,s,s.replace(r'\operatorname{Ext}',r'\mathop{\mathbb E\mathrm{xt}}\nolimits'),'square lower row','III.p185.hyper-Ext','Both lower-row Ext symbols have a doubled E in the print. evidence/I_p185_square.png.')
 if layer=='English':
  pairs=[(r'\uline{Let, as above,}',r'\uline{Let}, \uline{as above},'),(r'\uline{be a morphism of $A$-extensions}',r'\uline{be a morphism of} $A$-\uline{extensions}'),(r'cocartesian.}',r'cocartesian}.'),(r'\uline{Then, with the preceding}',r'\uline{Then}, \uline{with the preceding}'),(r'\uline{notation,}',r'\uline{notation},'),(r'\uline{be an isomorphism.}',r'\uline{be an isomorphism}.')]
 else:
  pairs=[(r'\uline{Soit, comme plus haut,}',r'\uline{Soit}, \uline{comme plus haut},'),(r'\uline{un morphisme de A-extensions}',r'\uline{un morphisme de} A-\uline{extensions}'),(r'cocartésien.}',r'cocartésien}.'),(r'\uline{Alors, avec les notations}',r'\uline{Alors}, \uline{avec les notations}'),(r'\uline{précédentes,}',r'\uline{précédentes},'),(r'\uline{soit un isomorphisme.}',r'\uline{soit un isomorphisme}.')]
 for old,new in pairs:ch(layer,old,new,'lemma emphasis','III.p185.underline-scope','Preserve the printed underline scope, leaving the A-prefix and punctuation outside it. evidence/I_p185_lemma.png.')
 s=region(layer);a=s.index(r'  \begin{tikzpicture}');b=s.index(r'  \end{tikzpicture}',a);old=s[a:b];new=old
 for node,x,y in [('TL',0,82),('TR',170,82),('BL',0,3),('BR',170,3)]:
  import re
  new=re.sub(r'\\node \('+node+r'\) at \([^)]*\)',lambda m:r'\node[anchor=base west] ('+node+f') at ({x},{y})',new)
 new=new.replace('(TL) -- node[above] {$(*)$} (TR)',r'([xshift=3bp,yshift=3bp]TL.base east) -- node[above] {$(*)$} ([xshift=-3bp,yshift=3bp]TR.base west)')
 new=new.replace('(BL) -- (BR)',r'([xshift=3bp,yshift=3bp]BL.base east) -- ([xshift=-3bp,yshift=3bp]BR.base west)').replace('(TL) -- (BL)','(32,70) -- (32,18)').replace('(TR) -- (BR)','(202,70) -- (202,18)')
 new=new.replace('at (-12,38)','at (-3,41)').replace(r'\node at (33,38) {$\sim$};',r'\node at (38,44) {\rotatebox{90}{$\sim$}};').replace(r'\node at (227,38) {$\sim$};',r'\node at (208,44) {\rotatebox{90}{$\sim$}};').replace('at (278,38)','at (245,41)')
 new=new.replace(r'\node[anchor=west] at (288,0) {#1};',r'\node[anchor=base] at ([xshift=18bp]BR.base east) {#1};')
 ch(layer,old,new,'comparison square','III.p185.square-geometry','Align both rows and the vertical arrows under the leading function arguments; restore the two vertical single-tilde labels on the right of their arrows and the comma baseline. Preserve all four directed edges and reference labels. evidence/I_p185_square.png.')
 if layer=='English':
  ch(layer,'Now there is a'+r'\par'+'\n\n','Now there is a\n','square introduction','III.p185.false-prose-paragraph','Join a false paragraph across a printed line wrap, preserving the anchor. evidence/I_p185_explanation.png.','structure')
  ch(layer,r'\vspace{1.68bp}'+'\n'+'commutative square','commutative square','square introduction','III.p185.false-prose-space','Remove the associated false vertical break. evidence/I_p185_explanation.png.','structure')
 else:
  ch(layer,'un carré'+r'\par'+'\n\n','un carré\n','square introduction','III.p185.false-prose-paragraph','Join a false paragraph across a printed line wrap, preserving the anchor. evidence/I_p185_explanation.png.','structure')
  ch(layer,r'\vspace{1.68bp}'+'\n'+r'\noindent{commutatif}','commutatif','square introduction','III.p185.false-prose-space','Remove the associated false vertical break. evidence/I_p185_explanation.png.','structure')
 s=region(layer);ch(layer,s,s+r'\clearpage'+'\n','page boundary','III.p185.page-boundary','Preserve the printed page boundary.','structure')
for old,new in [(r'$)$:',r'$)$\hspace{3.0bp}:'),('background role):','background role)'+r'\hspace{3.0bp}:'),('as follows:','as follows'+r'\hspace{3.0bp}:')]:
 ch('English',old,new,'prose colons','III.p185.English-colon-spacing','Align the printed colon spacing already retained in corrected French. evidence/I_p185_algmod-introduction.png; evidence/I_p185_problem-introduction.png; evidence/I_p185_reformulation.png.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p185','Anneaux; six punctuation spaces; peut-être','anneaux; omitted spaces; peut être','Withdraw optional capitalization and punctuation normalization. Retain removal of the original erroneous hyphen: peut être is the modal verb followed by the infinitive, not the adverb peut-être.',ev+'evidence/I_p185_lemma.png; evidence/I_p185_reformulation.png; evidence/I_p185_pair.png; evidence/I_p185_explanation.png; evidence/I_p185_square.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.2.1.1.1.flatness','targeted proof check','The cocartesian hypothesis gives J=IC and C0=C tensor_B B0. If C is B-flat, base change makes C0 B0-flat, and tensoring0->I->B->B0->0 identifies I tensor_B0 C0 with IC=J, hence v is an isomorphism. Conversely, v injective implies Tor_1^B(B0,C)=0 from this exact sequence. For any B0-module N, the first-quadrant change-of-rings Tor sequence and flatness of C0 give Tor_1^B(N,C)=0: both total-degree1 terms vanish. For any B-module M, both IM and M/IM are B0-modules since I^2=0; their short exact sequence then gives Tor_1^B(M,C)=0. This proves B-flatness, locally for the ringed topos, without a noetherian assumption.'),('III.2.1.2.1.reformulation','targeted proof check','A B-extension of C0 by J includes the required structural B->C map and hence an A-extension map. Pull it back along f0:B0->C0 to obtain a B-extension of B0 by J. Under1.2.8 this pullback is the pushout of0->I->B->B0->0 along the induced I->J (I^2=0), so its class maps to precisely f restricted to I. The condition that (*) equal the prescribed u is therefore exactly the original problem. Personally reinspected the1.2.8 statement and Hom-to-Exal formula on175.'),('III.2.1.2.1.square','targeted proof check','The bottom arrow is contravariance of hyper-Ext under L_{B0/B} tensor_B0 C0->L_{C0/B}. The right vertical map is the canonical identification through H1(L_{B0/B})=I, tensor-Hom derived adjunction and the vanishing H0=0. The normalized cotangent representative is a bounded-below homological complex of flat B0-modules, so its ordinary tensor computes derived tensor here. Naturality of the extension-class comparison1.2.3 and the universal quotient extension identifies the upper and lower composites. Personally reinspected1.2.8.1 and its Hom-to-hyper-Ext formula on175.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p185_*.png')):f.write(f'| evidence/{p.name} | Page185 audit: personally inspected at800dpi. |\n')
print('Page185 repairs, one verdict and three proof checks recorded.')
