"""Primary reviewer's page165 audit and targeted79 repairs; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='165';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p165}'
ev='LNM239 scan PDF p183 / printed p165: both complete400-dpi halves, eleven800-dpi crops and one1600-dpi comma detail personally inspected; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');assert old.count('$P$-modules')==2
ch('corrected',old,old.replace('$P$-modules','$P$-Modules'),'two prose occurrences','III.p165.withdraw-capitalizations','Withdraw two optional capitalizations; retain the necessary removal of the printed stray comma in on ,a.','reading')
for layer in ['corrected','English']:
 old=region(layer);assert old.count('(I 3.2.3.7)')==2
 ch(layer,old,old.replace('(I 3.2.3.7)','(I 3.2.3.8)'),'choice and independence references','III.1.2.3.proof.references','Both references print3.2.3.7. Direct reinspection of page79 shows that this lemma characterizes the zero class, whereas Proposition3.2.3.8(a) supplies a representative after a quasi-isomorphism of the kernel and3.2.3.8(b) supplies the common comparison and homotopy used here. Correct both last digits, retaining the printed references in the as-printed layer. evidence/I_p079_conditions.png; evidence/I_p079_prop3238a-full.png; evidence/I_p079_prop3238b-full.png.','misprint of the original')
ext=r'\mathop{\mathbb E\mathrm{xt}}\nolimits';bar=r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}'
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p165.upright-Latin','Restore upright printed Latin mathematics.')
 old=region(layer);assert old.count(r'\mathcal Y')==18 and old.count(r'\mathcal Z')==3
 ch(layer,old,old.replace(r'\mathcal Y','Y').replace(r'\mathcal Z','Z'),'extension names','III.p165.plain-extension-names','Restore eighteen plain Y and three plain Z names.')
 ch(layer,r'\operatorname{Ext}',ext,'opening class','III.p165.hyperExt-letterform','The printed E has a distinct double stroke; restore the hyper-Ext operator.')
 old=region(layer);assert old.count(r'_*')==8
 new=old.replace("(H_0t')_*","H_0t'*").replace("(H_0t'')_*","H_0t''*").replace("{t'}_*","t'*").replace("{t''}_*","t''*")
 ch(layer,old,new,'pushout operations','III.p165.baseline-stars','All eight stars follow the map name on the baseline. The last display has H_0t prime and double prime with no added parentheses. Preserve primes, H_0 subscripts and the true inverse parentheses in the transport display.')
 old=region(layer);assert old.count(r'\xrightarrow{\sim}')==3 and old.count(r'\xleftarrow{\sim}')==2
 ch(layer,old,old.replace(r'\xrightarrow{\sim}',bar).replace(r'\xleftarrow{\sim}',bar),'five isomorphism signs','III.p165.unheaded-isomorphisms','The inline F--H_0E sign and both signs in each comparison display are plain unheaded bars with a tilde. All thirteen ordinary headed maps elsewhere remain unchanged.')
 old=region(layer);new=old
 if layer=='English':new=new.replace('\\noindent\\mbox{}\\par\n','')
 else:new=new.replace('extension de\\par\n\n\\noindent $B$ par $M$','extension de $B$ par $M$')
 new=new.replace("\\longrightarrow L$ \n\n\\phantomsection","\\longrightarrow L$ \n\\phantomsection")
 new=new.replace('une extension \n\n\\phantomsection','une extension \n\\phantomsection').replace('an extension \n\n\\phantomsection','an extension \n\\phantomsection')
 new=new.replace('(1.1.8.2),\\par\n\n\n\\phantomsection','(1.1.8.2),\n\\phantomsection')
 new=new.replace(r'\noindent on ,a',r'on ,a').replace(r'\noindent on a',r'on a').replace(r'\noindent we have',r'one has')
 new+=r'\clearpage'+'\n'
 ch(layer,old,new,'prose and page boundary','III.p165.prose-flow','Rejoin the broken H_0 extension clause and the comparison paragraph across its anchors, remove the artificial blank English prose line, and retain all seven display carriers, anchors and the printed page boundary.','structure')
old=region('English');new=old.replace('We thus have','One thus has').replace('respectively ','resp. ')
ch('English',old,new,'extension construction and comparisons','III.p165.impersonal-abbreviations','Preserve impersonal on in the construction and preserve all three printed resp. abbreviations. The earlier structural join renders the other on a as one has.','translation')
# Targeted reinspection of the cited proposition, not a renewed full-page audit.
for layer in LAYERS:
 edit_page(layer,r'\begin{illusiebodypage}{illusie:I:ch1:p079}',r'u\in\operatorname{Ext}^{1}(E,F)',r'u\in'+ext+r'^{1}(E,F)','79','3.2.3.8(a) class','I.3.2.3.8a.hyperExt-letterform','corrects the earlier run: evidence/I_p079_prop3238a-full.png personally inspected at800dpi while resolving page165 references; all three corresponding assertion regions read. The E in the hyper-Ext class is double-stroked. The ordinary Ext in(b) is plain and is not changed. Targeted repair only; the final whole-work search and second reading remain pending.','typesetting')
s=(ROOT/'sources'/LAYERS['English']).read_text();a=s.index(r'\hypertarget{illusie:I:ch1:p079:proposition:3238}');b=s.index(r'\hypertarget{illusie:I:ch1:p079:display:prop-a}',a);old=s[a:b]
assert old.count('respectively')==3
edit_page('English',r'\begin{illusiebodypage}{illusie:I:ch1:p079}',old,old.replace('respectively','resp.'),'79','3.2.3.8(a)','I.3.2.3.8a.resp','corrects the earlier run: evidence/I_p079_prop3238a-full.png; all three assertion regions compared. Retain the three printed resp. abbreviations, as required by the supplied translation conventions. No other page79 prose is recertified.','translation')
verdict('79','I.3.2.3.8a:reference-reinspection','Plain Ext in the supplied class u; printed double-stroked E','Same','Targeted superseding verdict: restore the double-stroked E in the assertion(a) class in all layers and retain three resp. abbreviations in its English. Ordinary Ext in(b) remains plain. No other earlier decision is changed.','corrects the earlier run: evidence/I_p079_prop3238a-full.png; evidence/I_p079_prop3238b-full.png.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p165','P-Modules twice; on ,a; both references I3.2.3.7','P-modules twice; on a; same references','Local source-comparison verdict, not a supplied record ID. Withdraw both optional capitalization changes. Confirm removal of the tiny stray comma, directly visible at1600dpi, as a grammatical misprint. Newly correct both reference digits to3.2.3.8 in corrected French and English only. Restore plain extension names, hyper-Ext, baseline stars, unheaded bars and prose flow; retain all inverse maps and primes.',ev+'evidence/I_p165_choice.png; evidence/I_p165_comparison-data.png; evidence/I_p165_comma1600.png; evidence/I_p079_prop3238a-full.png; evidence/I_p079_prop3238b-full.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.3.proof.representatives','Directly compared the cited lemma and proposition on79. The zero-class criterion3.2.3.7 does not assert existence of representatives for arbitrary y. Proposition3.2.3.8(a), applied to E=Omega_P/A and F=M in simplicial P-modules, gives s:M->N and Y with y=(sigma s)^(-1)chi(Y). Its part(b), with the two s maps as its t maps and the current t maps as its r maps, gives the common L and homotopy. Both page165 references therefore require3.2.3.8. This is a use-and-type check of the proposition, not a new proof of it.'),('III.1.2.3.proof.H0-extension','Apply normalized homology to0->N->E->P->0. H_1(P)=0 makes H_0(N)->H_0(E) injective; right exactness supplies H_0(E)->H_0(P)->0. The kernel remains square-zero because products already vanish degreewise. The quasi-isomorphisms s and p give isomorphisms H_0(M)=M->H_0(N) and H_0(P)->B, so pushout by (H_0s)^(-1) and pullback by (H_0p)^(-1) produce precisely an A-extension of B by M with middle algebra isomorphic to H_0(E). Both inverse directions in the print are necessary.'),('III.1.2.3.proof.independence-H0','The functor alg commutes with kernel pushouts by1.1.8.2, giving the printed isomorphisms after passage to a common extension Z. H_0 of the pushout extension is the pushout of H_0 of the extension: the pushout is the quotient of the direct sum of its middle additive group and the new kernel by (i(n),-t(n)); H_0 preserves that cokernel and direct sum. Acyclicity of P ensures the resulting sequence is again short exact. Homotopic t-prime s-prime and t-double-prime s-double-prime induce equal H_0 maps. Transport along their common inverse therefore identifies the two extensions of B by M. This checks the independence argument through the displayed H_0 comparison; the two inverse identities for the theorem are still to be read on166.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'used and rechecked in this run' if sid.endswith('representatives') else 'targeted proof check',outcome])
q=ROOT/'READING_QUESTIONS.tsv'
with q.open(newline='') as f:rows=list(csv.reader(f,delimiter='\t'))
for row in rows[1:]:
 if row[0]=='I-Q008':
  row[1]='68;77;79;91;125;138;162;163;164;165';row[4]+=' The opening class on165 and the assertion3.2.3.8(a) on79 both print double-stroked E; the ordinary extension group in79(b) is plain and remains so.';row[6]+='; evidence/I_p165_class.png; evidence/I_p079_prop3238a-full.png; evidence/I_p079_prop3238b-full.png'
with q.open('w',newline='') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows)
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p165_*.png')):f.write(f'| evidence/{p.name} | Page165 audit: personally inspected at'+('1600' if '1600' in p.name else '800')+'dpi. |\n')
 for name in ['conditions','prop-b-inline','prop3238-reinspection','prop3238a-full','prop3238b-full']:f.write(f'| evidence/I_p079_{name}.png | Targeted reference reinspection for165; the two full expanded assertion crops complete the initially clipped reference crop. |\n')
print('Page165 and targeted79 repairs, verdicts and three checks recorded.')
