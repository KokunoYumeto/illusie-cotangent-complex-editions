"""Page176 exact continuation after an escaped-apostrophe target mismatch; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='176';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p176}'
ev='LNM239 scan PDF p194 / printed p176: both complete400-dpi halves, nine800-dpi crops and a1600-dpi missing-component crop personally inspected; inline-map crop expanded and reinspected. All three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
# The first script applied eight spacing rows and as-printed edits through the missing-p repair, then stopped before the line-end join.
layer='as-printed'
if layer!='English':ch(layer,r"\uline{est l'opérateur bord de la suite exacte d'homologie du triangle de transiti-} "+'\n'+r"\uline{vité défini par}",r"\uline{est l'opérateur bord de la suite exacte d'homologie du triangle de transitivité défini par}",'statement line ending','III.p176.line-end-hyphen','Join the line-end word and its underline. evidence/I_p176_statement.png.','structure')
old=region(layer);new=old
new=new.replace(r'$M\in\operatorname{ob} B\text{-Mod}$,\par'+'\n\n',r'$M\in\operatorname{ob} B\text{-Mod}$,'+'\n')
new=new.replace(r'\noindent le carré ci-dessous','le carré ci-dessous').replace(r'\noindent the square below','the square below')
new=new.replace(r'\quad induit un\par'+'\n\n',r'\quad induit un'+'\n').replace(r'\quad induces a\par'+'\n\n',r'\quad induces a'+'\n').replace(r'\noindent morphisme de P-extensions','morphisme de P-extensions').replace(r'\noindent morphism of P-extensions','morphism of P-extensions')
ch(layer,old,new,'proof prose','III.p176.false-prose-paragraphs','Join the two continuous proof sentences while retaining every anchor and displayed diagram. evidence/I_p176_proof-lead.png; evidence/I_p176_inline-map.png.','structure')
old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p176.page-boundary','Preserve the printed page boundary.','structure')
for layer in ['corrected','English']:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p176.upright-Latin','Restore upright printed Latin mathematics.')
 for xy in ['45,49','181,49','111,42','269,42']:
  ch(layer,'at ('+xy+r') {$\sim$};','at ('+xy+r') {$\simeq$};','vertical isomorphisms','III.p176.isomorphism-underbars','Restore the lower bar of each of the four printed isomorphism labels. evidence/I_p176_boundary-square.png; evidence/I_p176_hom-square.png.','reading')
 ch(layer,r'\node[anchor=west] at (244,8) {$#1$};',r'\node[anchor=base] at ([xshift=40bp]BR.base east) {$#1$};','first square punctuation','III.p176.boundary-comma-baseline','Place the terminal comma on the lower-row baseline. evidence/I_p176_boundary-square.png.')
 old=region(layer);a=old.index(r'\providecommand{\IllusieTransitivityHomSquarePOneSeventySix}');b=old.index(r'\providecommand{\IllusieTransitivityExtensionMorphismPOneSeventySix}',a);block=old[a:b];new=block
 for name,xy in [('TL','50,80'),('TR','230,80'),('BL','50,8'),('BR','230,8')]:
  import re
  new=re.sub(r'\\node \('+name+r'\) at \([^)]*\)',r'\\node[anchor=west] ('+name+') at ('+xy+')',new)
 new=new.replace(r'\draw[->] (TL.south) -- (BL.north);',r'\draw[->] (70,70) -- (70,18);').replace(r'\draw[->] (TR.south) -- (BR.north);',r'\draw[->] (250,70) -- (250,18);')
 for oldxy,newxy in [('80,42','57,42'),('111,42','76,42'),('269,42','256,42'),('292,42','279,42')]:new=new.replace('at ('+oldxy+')','at ('+newxy+')')
 new=new.replace(r'\node[anchor=west] at (333,8) {$#1$};',r'\node[anchor=base] at ([xshift=25bp]BR.base east) {$#1$};')
 ch(layer,block,new,'Hom square layout','III.p176.hom-square-columns','Restore the printed left alignment within each column, vertical arrows near the start of each expression, adjacent labels and baseline comma. evidence/I_p176_hom-square.png.')
 ch(layer,r'\binom{p}{-d_{P/A}}:',r'\left(\begin{array}{c}p\\[10bp]-d_{P/A}\end{array}\right):','inline homomorphism','III.p176.inline-column-height','Restore the tall two-component column, preserving both components. evidence/I_p176_inline-map.png.')
 old=region(layer);a=old.index(r'\providecommand{\IllusieTransitivityExtensionDiagramPOneSeventySix}');b=old.index('% FIN DU FICHIER' if layer=='as-printed' else '% END SOURCE',a);block=old[a:b];new=block
 new=new.replace('(291,88)','(306,88)').replace(r'\node (TP)  at (150,79)',r'\node[anchor=west] (TP)  at (135,79)').replace(r'\node (BO)  at (65,8)',r'\node[anchor=west] (BO)  at (63,8)').replace(r'\node (BS)  at (150,8)',r'\node[anchor=west] (BS)  at (135,8)')
 for oldxy,newxy in [('226,79','247,79'),('276,79','287,79'),('226,8','247,8'),('276,8','287,8'),('158,43','143,43'),('234,43','255,43')]:new=new.replace('at ('+oldxy+')','at ('+newxy+')')
 new=new.replace(r'\draw[->] (TI.south) -- (BO.north);',r'\draw[->] (TI.south) -- (TI.south|-BO.north);').replace(r'\draw[->] (TP.south) -- (BS.north);',r'\draw[->] (135,68) -- (135,18);')
 new=new.replace(r'\binom{p}{-d_{P/A}}',r'\left(\begin{array}{c}p\\[10bp]-d_{P/A}\end{array}\right)').replace(r'\node[anchor=west] at (286,8) {$#1$};',r'\node[anchor=base] at ([xshift=20bp]BZR.base east) {$#1$};')
 ch(layer,block,new,'extension diagram layout','III.p176.extension-columns','Restore the printed off-center vertical columns, tall central label and lower-row period; preserve all eleven arrows. evidence/I_p176_extension-top.png; evidence/I_p176_extension-labels.png; evidence/I_p176_extension-bottom.png.')
 if layer=='as-printed':
  ch(layer,r'\node[anchor=west] at (143,43) {$\displaystyle\left(\begin{array}{c}p\\[10bp]-d_{P/A}\end{array}\right)$};',r'\node[anchor=west] at (143,43) {$\displaystyle\left(\begin{array}{c}\phantom{p}\\[10bp]-d_{P/A}\end{array}\right)$};','final diagram central label','III.1.2.9.printed-missing-p','Restore the blank upper component visible at1600dpi. The corrected and English layers retain p, required by the preceding explicit map and compatibility with the quotient B. evidence/I_p176_missing-p1600.png.','reading')
 if layer!='English':ch(layer,r"\uline{est l'opérateur bord de la suite exacte d'homologie du triangle de transiti-} "+'\n'+r"\uline{vité défini par}",r"\uline{est l'opérateur bord de la suite exacte d'homologie du triangle de transitivité défini par}",'statement line ending','III.p176.line-end-hyphen','Join the line-end word and its underline. evidence/I_p176_statement.png.','structure')
 old=region(layer);new=old
 new=new.replace(r'$M\in\operatorname{ob} B\text{-Mod}$,\par'+'\n\n',r'$M\in\operatorname{ob} B\text{-Mod}$,'+'\n')
 new=new.replace(r'\noindent le carré ci-dessous','le carré ci-dessous').replace(r'\noindent the square below','the square below')
 new=new.replace(r'\quad induit un\par'+'\n\n',r'\quad induit un'+'\n').replace(r'\quad induces a\par'+'\n\n',r'\quad induces a'+'\n').replace(r'\noindent morphisme de P-extensions','morphisme de P-extensions').replace(r'\noindent morphism of P-extensions','morphism of P-extensions')
 ch(layer,old,new,'proof prose','III.p176.false-prose-paragraphs','Join the two continuous proof sentences while retaining every anchor and displayed diagram. evidence/I_p176_proof-lead.png; evidence/I_p176_inline-map.png.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p176.page-boundary','Preserve the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p176','Four printed punctuation spaces','Four removed spaces','Withdraw optional normalization; harmless commented line-layout differences do not change the text. Four simeq underbars and diagram alignment restored in every layer.',ev+'evidence/I_p176_boundary-square.png; evidence/I_p176_hom-square.png.')
verdict(page,'III.1.2.9.existing-silent-p-repair','Blank upper component in final diagram','Upper component p','Confirm the necessary repair in corrected French and English; restore the actual omission in diplomatic French. The preceding formula explicitly gives (p,-d_P/A), and the right square forces the first component to be the quotient p.',ev+'evidence/I_p176_missing-p1600.png; evidence/I_p176_inline-map.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
outcome='For N=Omega1_P/A tensor_P B, the derivation d:P->N gives the P-extension B plus N with structural map(p,-d) by1.2.5.4. Since d(I squared)=0 after tensoring with B, this map factors through P/I squared; on I/I squared it is -d and on B it is the identity. Pushing out the universal P-extension by -d therefore gives precisely that boundary extension. For general M, composing N->M proves commutativity of the Hom square by functoriality. Via1.2.3,1.2.8 and Yoneda this identifies the homology boundary with the negative conormal differential. Reinspected III1.1.6 on157 and II1.1.2.6 on116; the latter uses scalar-extension adjunction for the B-module M. The missing upper p in the final printed label is necessary to obtain this map and commute with the quotient.'
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['III.1.2.9.negative-conormal-boundary',now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p176_*.png')):f.write(f'| evidence/{p.name} | Page176 audit: final800-dpi or1600-dpi crop personally inspected. |\n')
 f.write('| evidence/I_p157_conormal-map.png; evidence/I_p116_universal-property.png; evidence/I_p115_dual-isomorphism.png | Personally reinspected for176: conormal map, derivation universal property and adjacent derivation/algebra-map convention. |\n')
print('Page176 repairs, two verdicts and sign proof recorded.')
