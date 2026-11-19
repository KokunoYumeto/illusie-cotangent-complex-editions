"""Reviewer-directed first-reading repairs for printed page 110."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='110';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p110}'
ev='LNM239 scan PDF p128 / printed p110: both full 400-dpi halves and twelve 800-dpi decision crops personally inspected against all three complete source regions. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def change(layer,old,new,line,sid,why,kind='typesetting'):
 edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
bar=r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}'
for layer in LAYERS:
 change(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','throughout','I.p110.upright-Latin','The Latin variables, arrow labels, degree labels and differentials are upright.')
 old=region(layer);change(layer,old,old.replace(r'\Lambda',r'\wedge'),'4.3.1.7','I.p110.exterior-sign','Both exact sequences have plain exterior wedges.','reading')
 old=region(layer);new=old.replace(r'\xrightarrow{\ \sim\ }',bar).replace(r'\simeq',bar)
 change(layer,old,new,'four isomorphisms','I.p110.isomorphism-bars','The top two isomorphisms, splitting display and inline reduction all have unheaded bars with tildes.')
 old=r'\ReflowDisplay{}{\operatorname{Kos}_{\bullet}(u\oplus u\')'.replace("u\\'","u'")
 new=r'\ReflowDisplay{}{\begin{gathered}\operatorname{Kos}_{\bullet}(u\oplus u\')'.replace("u\\'","u'")
 change(layer,old,new,'top two formulas','I.p110.stacked-isomorphisms-start','evidence/I_p110_tensor-isomorphisms.png shows the two Koszul identities stacked, not side by side.','structure')
 change(layer,'\n\\qquad\n\\operatorname{Kos}^{\\bullet}(u\\oplus u\')','\\\\[12bp]\n\\operatorname{Kos}^{\\bullet}(u\\oplus u\')','top two formulas','I.p110.stacked-isomorphisms-break','Restore the printed line break between the two displayed identities.','structure')
 old=r'\operatorname{Kos}^{\bullet}(u)\otimes\operatorname{Kos}^{\bullet}(u\').}'.replace("u\\'","u'")
 new=r'\operatorname{Kos}^{\bullet}(u)\otimes\operatorname{Kos}^{\bullet}(u\').\end{gathered}}'.replace("u\\'","u'")
 change(layer,old,new,'top two formulas','I.p110.stacked-isomorphisms-end','Close the two-line display after the printed final full stop.','structure')
 old=r'\ReflowDisplay{}{(*)\qquad 0\longrightarrow E\xrightarrow{u}F\xrightarrow{v}G\longrightarrow0}'
 new=r'\par\vspace{6bp}\noindent\makebox[0pt][l]{(*)}\hspace*{74bp}\(0\longrightarrow E\xrightarrow{\hspace{4bp}u\hspace{4bp}}F\xrightarrow{\hspace{4bp}v\hspace{4bp}}G\longrightarrow0\)\par\vspace{6bp}'
 change(layer,old,new,'sequence (*)','I.p110.sequence-label','evidence/I_p110_proposition.png: (*) is at the left margin, well separated from the centered exact sequence; retain both labels and all five terms.')
 old=r'\ReflowDisplay{}{\operatorname{Kos}_{\bullet}(\operatorname{Id}_M)'+bar+'\n'+r'\operatorname{Kos}_{\bullet}(\operatorname{Id}_{M\'})\otimes'.replace("M\\'","M'")+'\n'+r'\operatorname{Kos}_{\bullet}(\operatorname{Id}_{M\'\'})}'.replace("M\\'\\'","M''")
 new='$'+old[len(r'\ReflowDisplay{}{'):-1]+'$'
 change(layer,old,new,'proof after Utilisant / Using','I.p110.inline-sum','evidence/I_p110_inline-sum.png: the factorization using M-prime and M-double-prime is inline in one continuous paragraph.','structure')
 old=region(layer);new=old.replace(r'\cdots',r'\ldots')
 change(layer,old,new,'two exact sequences','I.p110.ellipsis','evidence/I_p110_exact-first.png and exact-second.png show baseline ellipsis dots in both sequences.')
 change(layer,r'\longrightarrow S^nG\longrightarrow0,\\',r'\longrightarrow S^nG\longrightarrow0\\[10bp]','first exact sequence end','I.p110.sequence-punctuation','The first sequence ends with 0 and no comma; the second ends with parenthesis and comma. Restore also their printed vertical separation.','reading')
 old=region(layer)[-250:]
 if not old.endswith('\\vspace{5.0bp}\n'):raise ValueError('unexpected ending')
 change(layer,old,old[:-len('\\vspace{5.0bp}\n')]+r'\clearpage'+'\n','physical boundary','I.p110.page-boundary','End the physical page after the Koszul exact-sequence definition.','structure')
# Restore the quotation begun on p109, with its inner pair and outer closing mark.
change('as-printed','"produit tensoriel")"',r'\textquotedbl{}produit tensoriel\textquotedbl{})\textquotedbl{}','opening line','I.p110.straight-quotes','The print has straight inner quotation marks followed by a parenthesis and the outer closing quote begun on p109.')
change('corrected','« produit tensoriel »)',r'\textquotedbl{}produit tensoriel\textquotedbl{})\textquotedbl{}','opening line','I.p110.restore-outer-quote','The former normalization replaced the inner quotes and deleted the necessary outer closing quote; restore the printed sequence.','reading')
change('English',"``tensor-product'' differential);",r'\textquotedbl{}tensor-product\textquotedbl{} differential)\textquotedbl{};','opening line','I.p110.English-outer-quote','Restore the outer closing quote corresponding to the opening quote on p109, and use the printed straight form for the nested quotation.','reading')
old=region('corrected');new=old.replace("d'algèbres","d'Algèbres").replace(r'\uline{modules plats}',r'\uline{Modules plats}').replace('$A$-module','$A$-Module').replace('Le scindage','Le splittage')
change('corrected',old,new,'throughout','I.p110.withdraw-normalizations','The print has Algèbres, Modules, Module and splittage. These are intelligible printed forms, not errors; withdraw all four remaining optional normalizations.','reading')
change('English','Passing to a local filtered colimit and localizing','Passing to a local inductive limit and localizing','proof opening','I.p110.terminology-inductive-limit','evidence/I_p110_inductive-limit.png reads limite inductive locale. DECISIONS_20261119.tsv, English limite inductive row (medium confidence), requires inductive limit for translations from French. Remove the unprinted filtered qualification while preserving the local limit and localization.','terminology')
verdict(page,'ILL-SC-20260804-0107','No new mathematical original error established on this page','No mathematical alteration in corrected French','The finite free split case is explicitly checked; the Lazard–Deligne local reduction is a cited dependency, not a new proof in this audit.',ev)
verdict(page,'ILL-NORM-20260804-0138','Straight nested quotes with an outer closing quote; Algèbres/Modules/Module; splittage','All five optional normalization entries withdrawn','The quote edit had also removed a structural closing mark belonging to the opening mark on p109.',ev)
verdict(page,'ILL-TX-20260804-0134','Ten anchored units; two stacked isomorphisms and a later inline identity','All anchors preserved; displays, bars, wedges, ellipses, punctuation and label placement restored','All degrees, primes, Id subscripts, sequence terms, arrows and underlines were inspected at enlarged scale.',ev)
verdict(page,'ILL-TR-20260804-0136','limite inductive locale; split case and exact Koszul sequences','local inductive limit; shared structural and notation repairs','Terminology changed under the supplied standard. Other English meaning and terminology retained, with no stylistic rewriting.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[
('I.4.3.1.5.differential-compatibility','The exterior/symmetric exponential map sends E and E-prime into their respective tensor factors, and similarly F and F-prime. On these generators d agrees with d tensor 1 plus the signed 1 tensor d; the derivation rule therefore proves compatibility for Kos-subscript. For Kos-superscript, use the divided-power generators and the addition formula gamma_n(e+e-prime)=sum gamma_i(e) gamma_j(e-prime); applying d to either side and shifting i or j gives the same two sums. With the tensor differential signed by the relevant exterior degree, the second map is compatible as well. This completes the assertion begun on p109.'),
('I.4.3.1.6.finite-free-split-case','For M=A generated by e, the total-weight n>0 part of Kos-subscript(Id_M) is 0->A(e tensor t^(n-1))->A t^n->0 with differential coefficient 1, hence split exact; weight zero is A. The cochain analogue is 0->A gamma_n(e)->A gamma_(n-1)(e) tensor f->0, also coefficient 1. Tensoring rank-one factors proves the finite free identity case in each weight without a torsion assumption. For a split finite free sequence F=E direct-sum G, Kos-subscript(u)=Kos-subscript(Id_E) tensor S(G), and Kos-superscript(v)=Gamma(E) tensor Kos-superscript(Id_G). Their augmentations/inclusions are therefore quasi-isomorphisms, yielding the two displayed weight-n exact sequences. This checks the split finite free calculation directly, including the n=0 interpretation as A->A. It does not re-prove Lazard–Deligne or the local filtered-limit reduction for arbitrary flat sheaves.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,body in events:w.writerow([sid,now,who,'targeted proof check',body])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p110_*.png')):f.write(f'| evidence/{p.name} | Printed p110, 800-dpi decision crop inspected during the first reading. |\n')
print('Page 110 edits, verdicts, terminology repair and targeted checks recorded.')
