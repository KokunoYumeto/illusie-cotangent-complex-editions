"""Primary reviewer's page163 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='163';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p163}'
ev='LNM239 scan PDF p181 / printed p163: both complete400-dpi halves and eight800-dpi crops personally inspected; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
ch('corrected',"d'anneaux","d'Anneaux",'ring square introduction','III.p163.withdraw-capitalization','Withdraw the optional capitalization change. The separate correction of the unmatched parenthesis remains justified.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','body and diagrams','III.p163.upright-Latin','Restore upright printed Latin variables and module-category names.')
 old=region(layer);assert old.count(r'\operatorname{Ext}')==4
 ch(layer,old,old.replace(r'\operatorname{Ext}',r'\mathop{\mathbb E\mathrm{xt}}\nolimits'),'Ext square','III.p163.Ext-letterforms','All four enlarged Ext operators have the double-stroked initial E.')
 for macro,node in [('IllusieBaseChangeSquarePOneSixtyThree','Bp'),('IllusieResolutionBaseChangeDiagramPOneSixtyThree','Pp'),('IllusieExtBaseChangeSquarePOneSixtyThree','TL')]:
  s=region(layer);a=s.index('\\providecommand{\\'+macro+'}');b=s.index('\n}',a)+2;old=s[a:b]
  ch(layer,old,old.replace('baseline=(current bounding box.center)',f'baseline=({node}.base)'),'three diagram numbers','III.p163.tag-'+node,'Align the external equation number with the printed upper-row baseline, preserving its anchor and macro.')
 s=region(layer);a=s.index(r'\providecommand{\IllusieResolutionBaseChangeDiagramPOneSixtyThree}');b=s.index('\n}',a)+2;old=s[a:b];new=old
 new=new.replace(r'\node (P)  at (116,109)',r'\node (P)  at (85,109)')
 new=new.replace('    \\draw[->] (Bp) -- (B);\n','')
 new=new.replace(r'\draw[->] (P) -- (B);',r'\draw[->] (P) -- (B);'+'\n'+r'    \draw[->,preaction={draw=white,line width=10bp}] (Bp) -- (B);')
 new=new.replace(r'\node at (167,-3) {$,$};',r'\node[anchor=base] at ([xshift=51bp]A.base) {$,$};')
 ch(layer,old,new,'resolution diagram','III.p163.resolution-geometry','Restore the printed P column, left of B, and the deliberate gap in A-to-P where B-prime-to-B crosses it; the crossing is not a vertex. Keep all nine arrows and put the comma on the A baseline.')
 s=region(layer);a=s.index(r'\providecommand{\IllusieExtBaseChangeSquarePOneSixtyThree}');b=s.index('\n}',a)+2;old=s[a:b];new=old
 new=new.replace(r'\node (TL) at (38,86)',r'\node[anchor=west] (TL) at (0,86)').replace(r'\node (TR) at (190,86)',r'\node[anchor=west] (TR) at (152,86)')
 new=new.replace(r'\node (BL) at (38,3)',r'\node[anchor=west] (BL) at (0,3)').replace(r'\node (BR) at (190,3)',r'\node[anchor=west] (BR) at (146,3)')
 new=new.replace(r'\draw[->] (TL) -- (BL);',r'\coordinate (leftArrow) at ([xshift=23bp]TL.south west);'+'\n'+r'    \draw[->] (leftArrow) -- (leftArrow |- BL.north);')
 new=new.replace(r'\draw[->] (TR) -- (BR);',r'\coordinate (rightArrow) at ([xshift=23bp]TR.south west);'+'\n'+r'    \draw[->] (rightArrow) -- (rightArrow |- BR.north);')
 new=new.replace(r'\node at (232,-2) {$,$};',r'\node[anchor=base] at ([xshift=17bp]BR.base east) {$,$};')
 ch(layer,old,new,'Ext square geometry','III.p163.Ext-square-geometry','Restore the left alignment of the upper and lower left formulas and the printed vertical arrow columns, rather than centering arrows on formulas of unequal width. Restore the lower-right comma baseline. All four arrow directions and formulas remain unchanged; final geometry awaits PDF verification.')
 old=region(layer);new=old.replace('dans le\\par\n\n\\noindent sens','dans le sens').replace('in the\\par\n\n\\noindent following','in the following')
 new=new.replace('vérification est\\par\n\n','vérification est\n').replace('verification is\\par\n\n','verification is\n')
 new=new.replace(r'\noindent triviale.',r'triviale.').replace(r'\noindent trivial.',r'trivial.')+r'\clearpage'+'\n'
 ch(layer,old,new,'opening and conclusion','III.p163.prose-flow','Join two artificial prose paragraphs while preserving all anchors and the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p163','Printed unmatched parenthesis in II references; capitalized Anneaux','Unmatched parenthesis removed; optional lowercasing','Local source-comparison verdict, not a supplied decision-record ID. Retain the necessary corrected-French/English parenthesis repair, directly confirmed by the enlarged conclusion; preserve the original diplomatically. Withdraw optional capitalization. Restore four Ext letterforms, upper-row diagram-number baselines, P column, nonvertex crossing gap, vertical Ext columns, punctuation and prose. The actual reference numbers and arrow types are valid.',ev+'evidence/I_p163_conclusion-references.png; evidence/I_p163_resolution-diagram.png; evidence/I_p163_resolution-crossing.png; evidence/I_p163_ext-square.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.1.3.resolution-functoriality','With the names in the earlier construction reversed, the commutative ring square A-prime->A, B-prime->B gives the natural map P_A-prime(B-prime)->P_A(B). Its augmentation and structure maps commute by functoriality of the standard free resolution, yielding all three horizontal arrows and both triangles in1.2.1.3. The cited II1.2.1.2 diagram on121 was personally reinspected; it states precisely this construction with the dummy primed names exchanged.'),('III.1.2.1.4.Ext-naturality','Write alpha:Omega_P-prime/A-prime ->Omega_P/A for the differential map over P-prime->P, and beta:L_B-prime/A-prime ->L_B/A for its tensor-augmentation map over B-prime->B. The maps Omega->L send dx to dx tensor1, so beta composed with the primed map equals the unprimed map composed with alpha, degreewise and hence in the derived categories. Under the derived adjunction isomorphisms, a class in Ext_P^1(Omega_P/A,M) corresponds to a morphism L_B/A->M[1]. Restricting scalars and precomposing by beta has adjoint the restriction of the original class precomposed by alpha. These are exactly the right and left downward routes, proving the square commutes. Postcomposition by a B-module map M->N proves naturality in M too. References II1.1.2.8 on116 and II1.2.3.2 on123 were directly reinspected and agree with these maps; no flatness of B-prime->B is required.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p163_*.png')):f.write(f'| evidence/{p.name} | Page163 audit:800-dpi crop personally inspected, including all17 diagram arrows, four Ext symbols and references. |\n')
 f.write('| evidence/I_p116_semilinear-map.png; evidence/I_p116_base-change-map.png; evidence/I_p121_functoriality-diagram.png; evidence/I_p123_functorial-map.png | Reinspected for163: natural differential map, standard-resolution functoriality and cotangent map used in the Ext square. |\n')
print('Page163 edits, verdict and two checks recorded.')
