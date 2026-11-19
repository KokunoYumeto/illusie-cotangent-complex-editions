"""Reviewer-directed page-109 first-reading edits; no automated scan decisions."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='109';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p109}'
ev='LNM239 scan PDF p127 / printed p109: both full 400-dpi halves personally compared with the complete three source regions; thirteen enlarged 800-dpi decision crops inspected. '
def change(layer,old,new,line,sid,why,kind='typesetting'):
 edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
for layer in LAYERS:
 change(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','throughout','I.p109.upright-Latin','The variables, differentials and arrow labels are upright Latin throughout.')
 old=region(layer);change(layer,old,old.replace(r'\Lambda',r'\wedge'),'4.3.1.4–5','I.p109.exterior-sign','The exterior algebra has the plain wedge sign in both pairing and direct-sum displays.','reading')
 change(layer,r'E\xrightarrow{u}F\xrightarrow{v}G',r'E\xrightarrow{\hspace{12bp}u\hspace{12bp}}F\xrightarrow{\hspace{16bp}v\hspace{16bp}}G','first display','I.p109.composite-arrows','evidence/I_p109_composite.png shows long rightward arrows labelled u and v.')
 old=r'\begin{array}{rcl}'+'\n'+r'(i)&\operatorname{Kos}_{\bullet}(u)&\longrightarrow SG,\\[2bp]'+'\n'+r'(ii)&\Gamma E&\longrightarrow\operatorname{Kos}^{\bullet}(v).'+'\n'+r'\end{array}'
 new=r'\begin{array}{l@{\hspace{10bp}}l}'+'\n'+r'(i)&\operatorname{Kos}_{\bullet}(u)\longrightarrow SG,\\[12bp]'+'\n'+r'(ii)&\Gamma E\longrightarrow\operatorname{Kos}^{\bullet}(v).'+'\n'+r'\end{array}'
 change(layer,old,new,'maps (i), (ii)','I.p109.labelled-map-alignment','evidence/I_p109_labelled-maps.png: the domains begin at the same left edge, and both labels are left aligned; the punctuation is already correct.')
 change(layer,r'$\vee$',r'${}^{\vee}$','4.3.1.4 opening','I.p109.duality-mark','evidence/I_p109_duality-mark.png shows the standalone duality mark raised above the baseline.')
 change(layer,r'\operatorname{Kos}^{\bullet}(u^{\vee})\longrightarrow A}',r'\operatorname{Kos}^{\bullet}(u^{\vee})\longrightarrow A,}','complex pairing','I.4.3.1.4.punctuation','evidence/I_p109_complex-pairing.png shows a terminal comma after A.','reading')
 old=r'\noindent '+('In the situation' if layer=='English' else 'Dans la situation')
 new=r'\noindent\hspace{44bp}'+('In the situation' if layer=='English' else 'Dans la situation')
 change(layer,old,new,'duality paragraph','I.p109.paragraph-indent','evidence/I_p109_indented-dual.png shows the paragraph beginning at an indented position.','structure')
 old=region(layer);new=old.replace(r'\xrightarrow{\ \sim\ }',r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}')
 change(layer,old,new,'4.3.1.5 displays','I.p109.isomorphism-bars','evidence/I_p109_sum-isomorphisms.png shows two horizontal unheaded bars with tildes, not arrows.')
 old=r'\noindent '+('are compatible' if layer=='English' else 'sont compatibles')
 new=r'\noindent\textquotedbl{}'+('are compatible' if layer=='English' else 'sont compatibles')
 change(layer,old,new,'last line','I.p109.open-quote','evidence/I_p109_quote-boundary.png shows an opening straight double quote immediately before sont.','reading')
 old=region(layer)[-250:];new=old[:-len('\\vspace{5.0bp}\n')]+r'\clearpage'+'\n'
 if not old.endswith('\\vspace{5.0bp}\n'):raise ValueError('unexpected page ending')
 change(layer,old,new,'physical boundary','I.p109.page-boundary','Keep the physical boundary after munit / the corresponding unfinished English clause.','structure')
old=region('corrected');new=old.replace("d'algèbres","d'Algèbres").replace('$A$-modules','$A$-Modules')
change('corrected',old,new,'throughout','I.p109.withdraw-normalizations','The print has two capital Algèbres and capital Modules. These three optional lower-case normalizations are not repairs of original errors.','reading')
change('as-printed',r'\Gamma(E\oplus E\')'.replace("E\\'","E'"),r'\Gamma(E\otimes E\')'.replace("E\\'","E'"),'second direct-sum display','I.4.3.1.5.printed-tensor','evidence/I_p109_sum-isomorphisms.png shows a diagonal cross inside the circle: tensor, not direct sum. Retain this original misprint here. Corrected French and English already have the necessary direct sum. A degree-one dimension test and the divided-power exponential law justify that repair in CHECK_EVENTS.','reading')
verdict(page,'ILL-SC-20260804-0106','The second display prints Gamma(E tensor E-prime)','Corrected French/English retain Gamma(E direct-sum E-prime)','Reject the earlier zero-error inventory: the diplomatic source silently repaired a real original misprint. Its printed tensor is restored; the existing direct sum in the other layers is justified.',ev+'evidence/I_p109_sum-isomorphisms.png; CHECK_EVENTS I.4.3.1.5.divided-power-sum.')
verdict(page,'ILL-NORM-20260804-0137','Algèbres twice; Modules once','Three lower-case normalizations withdrawn','None is necessary to repair the original.',ev)
verdict(page,'ILL-TX-20260804-0133','Ten anchored regions, raised duality mark, plain wedges, unheaded isomorphisms, terminal pairing comma and opening quote','All ten anchors retained; typography and punctuation restored','The whole-page image and thirteen crops resolve the displayed and inline formulas, all primes and duals.',ev)
verdict(page,'ILL-TR-20260804-0135','French canonical pairings, perfect duality, zero composite and direct-sum formulas','English meaning retained; only shared notation/punctuation/structure restored','No English terminology or meaning repair was needed; locally free of finite type follows the supplied terminology standard.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[
('I.4.3.1.3.zero-composite','targeted proof check','For v u=0, map wedge(E) tensor S(F) to S(G) by the augmentation wedge(E)->A and S(v). On e in E, the image of d(e)=u(e) is v u(e)=0; on F the differential vanishes. The derivation rule proves compatibility everywhere. The map Gamma(E)->Gamma(F) tensor wedge(G)=Kos-superscript(v) is Gamma(u) in exterior degree zero. Its differential on gamma_k(e) is gamma_(k-1)(u(e)) tensor v u(e)=0; the divided-power addition relations extend this to all sections. Thus both displayed maps are maps of differential bigraded algebras.'),
('I.4.3.1.5.divided-power-sum','targeted proof check','The printed Gamma(E tensor E-prime) cannot have the displayed exponential decomposition: over any field take E=E-prime=k and F=F-prime=0. In divided-power degree one its dimension is 1, whereas Gamma(E) tensor Gamma(E-prime) has dimension 2. The required domain is Gamma(E direct-sum E-prime). The canonical map sends gamma_n(e,e-prime) to the sum over i+j=n of gamma_i(e) tensor gamma_j(e-prime); the inverse is induced by the two inclusions and multiplication. The divided-power addition relation verifies the compositions. Combining with the exterior direct-sum isomorphism gives the corrected second display. The claim about differential compatibility continues on p110 and is not marked checked yet.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,body in events:w.writerow([sid,now,who,kind,body])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p109_*.png')):f.write(f'| evidence/{p.name} | Printed p109, 800-dpi crop inspected during the first reading. |\n')
print('Page 109 edits, verdicts and two mathematical check events recorded.')
