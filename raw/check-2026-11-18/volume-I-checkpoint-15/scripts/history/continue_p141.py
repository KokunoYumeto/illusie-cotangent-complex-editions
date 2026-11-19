"""Primary reviewer's page 141 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='141';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p141}'
ev='LNM239 scan PDF p159 / printed p141: both complete 400-dpi halves, eleven 800-dpi crops and the expanded map crop personally inspected. Full source regions read in the prescribed layer order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('$q>0$,','$q>0$ ,').replace("A'=0$.","A'=0$ .").replace("A'=B_1$.","A'=B_1$ .").replace('$Y$,','$Y$ ,').replace('$V$,','$V$ ,').replace("l'anneau induit","l'Anneau induit")
ch('corrected',old,new,'hypotheses, proof and localization statement','II.p141.withdraw-normalizations','Restore five printed punctuation spaces and Anneau; none is an original error.','reading')
ch('as-printed','Par Kunneth','Par Künneth','proof reference','II.p141.Kunneth-accent','The scan visibly has the umlaut. The corrected French and English already read the print correctly; evidence/I_p141_kunneth.png.','reading')
for layer in LAYERS:
 ch(layer,r"L_{B'/B}\otimes_A A'=0",r"L_{B'/B\otimes_A A'}=0",'vanishing hypothesis','II.2.2.3.base-ring-subscript','The whole B tensor_A A-prime is the base ring inside the subscript of L, not a tensor factor outside L. This repairs a shared transcription error; evidence/I_p141_hypothesis.png and evidence/I_p141_proof-start.png.','reading')
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p141.upright-Latin','Printed Latin letters are upright, including diagram labels and subscripts.')
 old=region(layer);new=old.replace(r'\uline{$\mathcal O_X$}',r'$\underline{\mathrm{O}}_X$').replace(r'\uline{$\mathcal O_Y$}',r'$\underline{\mathrm{O}}_Y$')
 ch(layer,old,new,'localized structure rings','II.p141.structure-ring-font','The structure-ring sign is an underlined upright O, with its subscript outside the underline; evidence/I_p141_localized-sheaves.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace('(resp.\\par\n\\phantomsection','(resp.\n\\phantomsection').replace('\\noindent $Y_{/V}$)','$Y_{/V}$)')
 ch(layer,old,new,'hypothesis, proof and localization prose','II.p141.prose-continuity','Join ordinary printed line wraps, including the anchor within the parenthesis, while preserving all twelve anchors and displayed formulas.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p141.boundary','Retain the printed boundary within Proposition2.3.0.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p141','Kunneth, five punctuation spaces, Anneau','Künneth, normalized spacing and lowercase anneau','Local source-comparison verdict, not a supplied decision-record ID. Künneth is the correct printed reading and is propagated to the diplomatic layer. Withdraw the five optional spacing changes and the capitalization change. No correction of the printed mathematics is required.',ev+'evidence/I_p141_kunneth.png, evidence/I_p141_hypothesis.png and evidence/I_p141_localized-sheaves.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.2.3.hypothesis-grouping','The printed hypothesis is L(B-prime/(B tensor_A A-prime))=0. With B1=B tensor_A A-prime this is precisely the last term needed in each transitivity triangle of the proof. The supplied alternative is mathematically different: take A=B=k and A-prime=B-prime=k[t]. Higher Tor vanishes and the printed cotangent complex is L(k[t]/k[t])=0, whereas L(k[t]/k) tensor_k k[t] is nonzero already in degree0. Thus the grouping repair restores both the scan and the stated scope.'),('II.2.2.3.proof','Tor vanishing makes B1 the derived pushout by2.2.2(a). Proposition2.2.1 gives the two displayed comparisons to L(B1/A-prime) and L(B1/A). The normalized cotangent models and their base extensions are bounded above complexes of flat modules, so their quasi-isomorphisms remain quasi-isomorphisms under extension from B1 to B-prime (I3.3.2). Transitivity for A-prime->B1->B-prime and A->B1->B-prime has vanishing last term by the printed hypothesis, giving the first pair of comparisons. Composing gives exactly(i) and(ii), after the inverse-image coefficient identifications of1.1.4. This completes the proof on pp140-141.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p141_*.png')):f.write(f'| evidence/{p.name} | Page141 audit:800-dpi crop personally inspected; expanded map crop includes the complete second target. |\n')
print('Page141 edits, verdict and two proof checks recorded.')
