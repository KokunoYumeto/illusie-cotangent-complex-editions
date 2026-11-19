"""Primary reviewer's page149 audit; run once."""
import sys,csv,shutil
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='149';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p149}'
ev='LNM239 scan PDF p167 / printed p149: both complete400-dpi halves and eleven800-dpi crops personally inspected. All three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');assert old.count('$i>0$.')==2
ch('corrected',old,old.replace('$i>0$.','$i>0$ .'),'two Tor hypotheses','II.p149.withdraw-spacing','Withdraw the two optional punctuation-space normalizations.','reading')
ch('corrected',r'$z\in Z$,',r'$z\in Z$ ,','remark','II.p149.withdraw-spacing','Withdraw the optional comma-space normalization.','reading')
for layer in ['corrected','English']:
 ch(layer,'h=fp=qg','h=fp=gq','composition in2.3.9','II.2.3.9.composition','The print has qg, but p:Z->X,f:X->S,q:Z->Y,g:Y->S in the personally checked p148 diamond force fp=gq. qg is not composable. Preserve qg in diplomatic French. evidence/I_p149_composition.png; evidence/I_p148_diamond.png.','misprint of the original')
for layer in LAYERS:
 ch(layer,r"L_{B'/B}\otimes_A A'=0",r"L_{B'/B\otimes_A A'}=0",'proof vanishing hypothesis','II.2.3.10.base-ring-subscript','The complete base ring B tensor_A A-prime is printed inside the subscript of L; the supplied source placed the tensor outside. This shared transcription error recurs from p141 and is repaired in all three layers. evidence/I_p149_proof.png.','reading')
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','Latin notation','II.p149.upright-Latin','Printed Latin mathematical letters are upright.')
 old=region(layer);assert old.count(r'\mathcal O')==12
 ch(layer,old,old.replace(r'\mathcal O',r'\underline{\mathrm{O}}'),'structure-sheaf symbols','II.p149.structure-sheaves','All twelve structure-sheaf symbols are upright underlined O, with subscripts outside the underline.')
 ch(layer,r'\mathcal T\!or_i^S',r'\underline{\operatorname{Tor}}_i^S','remark sheaf Tor','II.p149.sheaf-Tor','The sheaf Tor symbol is printed upright and underlined; indices i and S remain outside the underline.')
 if layer=='English':old=r'\uline{In the situation of} (2.3.8),';new=r'\uline{In the situation of (2.3.8),}'
 else:old=r'\uline{Dans la situation de} (2.3.8),';new=r'\uline{Dans la situation de (2.3.8),}'
 ch(layer,old,new,'2.3.10 opening','II.p149.underline-scope','The reference2.3.8 and comma belong to the printed underline; the separate2.3.11 reference remains outside its underline.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace('\\par\n\\vspace{4.0bp}\n','\n')
 new=new.replace('\\noindent $\\operatorname{Tor}', '$\\operatorname{Tor}')
 ch(layer,old,new,'corollary hypotheses, proof and remark','II.p149.prose-continuity','Join printed prose line wraps and artificial gaps at the two Tor hypotheses, preserving every anchor and the real display/statement divisions.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p149.boundary','Retain the printed page boundary.','structure')
old=region('English');new=old.replace('Apply (2.2.3); the hypothesis','Apply (2.2.3), since the hypothesis').replace('of (loc. cit.) being','of (loc. cit.) is')
ch('English',old,new,'proof syntax','II.p149.proof-syntax','Repair the dangling participial clause after a semicolon while preserving the causal assertion of French étant satisfaite.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p149','Three punctuation spaces; h=fp=qg; tensor placed outside L in supplied transcription','Three normalized punctuation spaces; same two formula defects','Local source-comparison verdict, not a supplied decision-record ID. Withdraw the three optional space normalizations. Correct the original qg->gq only in corrected French/English; repair the shared cotangent-subscript transcription in all layers.',ev+'evidence/I_p149_composition.png; evidence/I_p149_proof.png; evidence/I_p149_tor-10.png; evidence/I_p149_tor-11.png; evidence/I_p149_remark-final-expanded.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.3.9','Apply2.3.8 with X-prime=Z,S-prime=Y,u=p,f-prime=q,v=g and f:X->S. Its canonical ring map becomes exactly p^{-1}O_X tensor_{h^{-1}O_S}q^{-1}O_Y -> O_Z, and is a localization. The common composite is necessarily h=fp=gq: qg in the printed parenthesis is ill-typed, since the displayed q has source Z and g has source Y. This proves the corollary and independently fixes the correction direction.'),('II.2.3.10-11','On the topos X-prime put A=(fu)^{-1}O_S, B=u^{-1}O_X, A-prime=f-prime^{-1}O_S-prime and B-prime=O_X-prime. The displayed Tor condition is exactly the Tor-vanishing hypothesis of2.2.3. By2.3.8 the map B tensor_A A-prime -> B-prime is a localization, and2.3.1 gives L(B-prime/(B tensor_A A-prime))=0. Thus2.2.3 gives both base-change maps and their direct-sum map as quasi-isomorphisms after the inverse-image coefficient identifications. The tensor must lie inside the base subscript; placing it outside does not express the localization vanishing. Replacing X-prime,S-prime,u,f-prime,v by Z,Y,p,q,g gives2.3.11 with exactly the displayed targets L(Z/Y) and L(Z/S). The sheaf-Tor comparison of2.3.12 continues on150 and is not claimed here.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p149_*.png')):f.write(f'| evidence/{p.name} | Page149 audit:800-dpi crop personally inspected; expanded final lines resolve initial edge clips. |\n')
print('Page149 edits, verdict and two proof/use checks recorded.')
