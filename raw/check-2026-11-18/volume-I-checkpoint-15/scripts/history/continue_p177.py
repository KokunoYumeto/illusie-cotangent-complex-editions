"""Primary reviewer's page177 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='177';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p177}'
ev='LNM239 scan PDF p195 / printed p177: both complete400-dpi halves and eleven800-dpi crops personally inspected; hypotheses crop expanded rightward and reinspected. All three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
ch('corrected','un A-module plat','un A-Module plat','hypothesis','III.p177.withdraw-capitalization','Withdraw optional Module capitalization normalization. evidence/I_p177_hypotheses.png.','reading')
for layer in ['corrected','English']:
 pairs=[(r'$P=S_A(M)$,',r'$P=S_A(M)$\hspace{3.0bp},'),('(II 1.2.4.4)).',r'(II 1.2.4.4))\hspace{3.0bp}.')]
 for macro,mark in [('Chain',','),('TransitivityTriangle','.'),('TruncatedTriangle',','),('DegreeOneMap','.'),('ConeMap',',')]:pairs.append((r'\IllusieCorollary'+macro+'POneSeventySeven{'+mark+'}',r'\IllusieCorollary'+macro+r'POneSeventySeven{\hspace{3.0bp}'+mark+'}'))
 for old,new in pairs:ch(layer,old,new,'formula punctuation','III.p177.punctuation-spacing','Withdraw optional corrected-French spacing normalizations and align English formula punctuation. evidence/I_p177_hypotheses.png; evidence/I_p177_chain.png; evidence/I_p177_triangle-one.png; evidence/I_p177_triangle-two.png; evidence/I_p177_final-proof.png.','reading' if layer=='corrected' else 'typesetting')
for layer in LAYERS:
 old=region(layer);ch(layer,old,old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath'),'body and note mathematics','III.p177.upright-Latin','Restore upright printed Latin mathematics in both font scopes.')
 old=r'\uline{a flat $A$-module}' if layer=='English' else r'\uline{un A-Module plat}'
 new=r'\uline{a flat} $A$-\uline{module}' if layer=='English' else r'\uline{un} $A$-\uline{Module plat}'
 ch(layer,old,new,'hypothesis emphasis','III.p177.A-prefix-outside-underline','The A- prefix is outside the printed underline. evidence/I_p177_hypotheses.png.')
 ch(layer,r'(I 1.4.7)\textsuperscript{(1)}',r'(I 1.4.7)\hspace{3bp}(\textsuperscript{1})','note call','III.p177.note-call','Restore baseline parentheses around the raised1. evidence/I_p177_truncation.png.')
 ch(layer,r'\textsuperscript{(1)} $L_{B/A}$',r'(\textsuperscript{1}) $L_{B/A}$','note label','III.p177.note-label','Restore baseline parentheses around the raised1 in the note. evidence/I_p177_footnote.png.')
 for xy,gap in [('263,4','28'),('279,4','20')]:ch(layer,r'\node[anchor=west] at ('+xy+r') {#1};',r'\node[anchor=base] at ([xshift='+gap+r'bp]lowerright.base east) {#1};','triangle punctuation','III.p177.triangle-punctuation-baseline','Align the punctuation with the lower row, preserving all six single-headed arrows exactly as printed. evidence/I_p177_triangle-one.png; evidence/I_p177_triangle-two.png.')
 ch(layer,r'$A\longrightarrow P\longrightarrow B$\par'+'\n\n'+r'\noindent (II 2.1.2.1)',r'$A\longrightarrow P\longrightarrow B$ (II 2.1.2.1)','proof prose','III.p177.false-proof-paragraph','Join the continuous proof sentence broken at a printed line wrap. evidence/I_p177_proof-lead.png.','structure')
 ch(layer,r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:2:9:1:truncation:n1}',r'\vfill'+'\n'+r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:2:9:1:truncation:n1}','footnote placement','III.p177.footnote-bottom','Restore the bottom footnote position with its anchor retained. evidence/I_p177_footnote.png.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p177.page-boundary','Preserve the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p177','Capital Module and seven punctuation spaces','Lowercase module and omitted spaces','Withdraw these optional normalizations. No original mathematical error identified. The two triangle degree-one edges have single ordinary heads in this print; retain them, without importing the tailed convention of other pages. Preserve the printed truncation notation and all signs.',ev+'evidence/I_p177_hypotheses.png; evidence/I_p177_triangle-one.png; evidence/I_p177_triangle-two.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.9.1.truncation-and-sign','targeted proof check','Under the hypotheses L_P/A is represented by the flat P-module Omega1_P/A in degree0, so derived scalar extension is N=Omega1_P/A tensor_P B in degree0. In the transitivity triangle N->L_B/A->L_B/P, surjectivity gives H0(L_B/P)=0 and H1(L_B/P)=I/I squared. Truncation in cohomological degrees at least-1 therefore gives N->t_[-1 L_B/A->(I/I squared)[1], with boundary -d by1.2.9. Its cone description has modules I/I squared in homological degree1 and N in degree0. The chain isomorphism from differential -d to differential d is -id in degree1 and id in degree0. This proves the stated two-term model and reconciles the signs without changing the print.'),('III.1.2.9.1.flat-symmetric-example-and-references','used and rechecked in this run','For P=S_A(M) with M flat, II1.2.4.4 on125, personally reinspected, identifies L_P/A with Omega1_P/A; the universal property gives Omega1_P/A=P tensor_A M, flat over P. Personally reinspected I1.4.7 truncations on16 and I1.4.6(a,b) on15: the former retains cohomological degrees at least-1, and the latter embeds the simplicial derived category into the ordinary derived category with nonpositive cohomology, as the note requires.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p177_*.png')):f.write(f'| evidence/{p.name} | Page177 audit: final800-dpi crop personally inspected. |\n')
 f.write('| evidence/I_p015_prop_a.png; evidence/I_p015_prop_b.png; evidence/I_p016_truncations.png; evidence/I_p125_symmetric-proposition.png | Personally reinspected for177: derived-category realization, truncation convention and flat symmetric-algebra example. |\n')
print('Page177 repairs, verdict and two checks recorded.')
