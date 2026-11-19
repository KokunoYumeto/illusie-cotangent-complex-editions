"""Reviewer-directed first-reading changes for printed page 108; not an OCR decision engine."""
import sys, csv
from pathlib import Path
from datetime import datetime, timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT, LAYERS, edit_page, verdict
page='108';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p108}'
evidence='LNM239 scan PDF p126 / printed p108: both full 400-dpi halves personally compared with all three complete source regions; eleven 800-dpi crops inspected, including the prior degree definition on p107. '
def change(layer,old,new,line,statement,why,kind='typesetting'):
    edit_page(layer,anchor,old,new,page,line,statement,evidence+why,kind)
for layer in LAYERS:
    change(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','throughout','I.p108.upright-Latin','The Latin variables and differentials are upright, including the square labels.')
    p=ROOT/'sources'/LAYERS[layer];s=p.read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);reg=s[a:b]
    change(layer,reg,reg.replace(r'\Lambda',r'\wedge'),'4.3.1.2–3','I.p108.exterior-sign','All exterior-algebra signs are plain wedges without a capital-Lambda foot. The entire explicitly bounded page span is the unique replay context.','reading')
    change(layer,r'\Gamma_A^kE',r'\Gamma^kE','gamma_k definition','I.4.3.1.2b.gamma-target','evidence/I_p108_gamma-arrow.png shows no subscript A under Gamma; retain only the superscript k.','reading')
    # Restore the two inline conditions; both are part of the proposition paragraphs.
    if layer=='English':
        old=r'\ReflowDisplay{}{d(x\otimes1)=1\otimes ux,\qquad d(1\otimes y)=0}'+'\n\n'+r'\noindent \uline{for}'
        new=r'$d(x\otimes1)=1\otimes ux,\ d(1\otimes y)=0$ \uline{for}'
    else:
        old=r'\ReflowDisplay{}{d(x\otimes1)=1\otimes ux,\qquad d(1\otimes y)=0}'+'\n\n'+r'\noindent \uline{pour}'
        new=r'$d(x\otimes1)=1\otimes ux,\ d(1\otimes y)=0$ \uline{pour}'
    change(layer,old,new,'4.3.1.2(a), condition','I.4.3.1.2a.inline','evidence/I_p108_a-formula.png: the two conditions are inline, immediately followed by pour/for.','structure')
    old=r'\ReflowDisplay{}{d\bigl(\gamma_k(x)\otimes1\bigr)=\gamma_{k-1}(x)\otimes ux,'+'\n'+r'\qquad d(1\otimes y)=0}'+'\n\n'+r'\noindent \uline{'+('for' if layer=='English' else 'pour')+'}'
    new=r'$d(\gamma_k(x)\otimes1)=\gamma_{k-1}(x)\otimes ux,\ d(1\otimes y)=0$ \uline{'+('for' if layer=='English' else 'pour')+'}'
    change(layer,old,new,'4.3.1.2(b), condition','I.4.3.1.2b.inline','evidence/I_p108_b-formula.png: normal-sized parentheses, k and k-1, comma, and inline condition; the paragraph continues into pour/for.','structure')
    # Both clauses belong to their preceding paragraphs, not independent displays.
    p=ROOT/'sources'/LAYERS[layer];s=p.read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);reg=s[a:b]
    old=reg;reg=reg.replace('telle que}\n\n$d(', 'telle que}\n$d(').replace('such that}\n\n$d(', 'such that}\n$d(')
    change(layer,old,reg,'4.3.1.2(a,b)','I.p108.paragraphs','The statements and their inline formulas form continuous paragraphs in the print.','structure')
    if layer!='English':
        for degree in ['premier','second']:
            old=r'\uline{(anti-commutative pour le '+degree+r' degré) une unique'+'\n'+r'$A$-dérivation}'
            new=r'(\uline{anti-commutative pour le '+degree+r' degré}) \uline{une unique}'+'\n'+r'$A$-\uline{dérivation}'
            change(layer,old,new,'4.3.1.2(a,b)','I.p108.underline-'+degree,'The parenthesis delimiters and coefficient A are outside the underline; une unique and dérivation are distinct underlined spans.')
        change(layer,r'(resp. $y$) \uline{section de} $E$ (resp. $F$).',r'(resp. $y$) \uline{section de $E$} (resp. $F$).','4.3.1.2(a)','I.p108.underline-Ea','evidence/I_p108_a-formula.png: section de E is underlined through E.')
        change(layer,r'(resp. $y$) \uline{section de} $E$ (resp. $F$),',r'(resp. $y$) \uline{section de $E$} (resp. $F$),','4.3.1.2(b)','I.p108.underline-Eb','The same section de E underline appears in (b).')
    else:
        change(layer,r'\uline{(anticommutative in the first degree), there exists a'+'\n'+r'unique $A$-derivation}',r'(\uline{anticommutative in the first degree}), \uline{there exists a'+'\n'+r'unique} $A$-\uline{derivation}','4.3.1.2(a)','I.p108.underline-a','Preserve printed emphasis: parentheses and coefficient A are not underlined.')
        change(layer,r'\uline{(anticommutative in the second degree), there exists'+'\n'+r'a unique $A$-derivation}',r'(\uline{anticommutative in the second degree}), \uline{there exists'+'\n'+r'a unique} $A$-\uline{derivation}','4.3.1.2(b)','I.p108.underline-b','Preserve printed emphasis: parentheses and coefficient A are not underlined.')
        change(layer,r'(resp. $y$) \uline{a section of} $E$ (resp. $F$).',r'(resp. $y$) \uline{a section of $E$} (resp. $F$).','4.3.1.2(a)','I.p108.underline-Ea','The original section de E is underlined through E.')
        change(layer,r'(resp. $y$) \uline{a section of} $E$ (resp. $F$), where',r'(resp. $y$) \uline{a section of $E$} (resp. $F$), where','4.3.1.2(b)','I.p108.underline-Eb','The original section de E is underlined through E.')
        change(layer,r'\hspace{44bp}(a)\quad',r'\hspace{44bp}a)\quad','part label','I.p108.part-a','The printed part label is a), with no opening parenthesis.')
        change(layer,r'\hspace{44bp}(b)\quad',r'\hspace{44bp}b)\quad','part label','I.p108.part-b','The printed part label is b), with no opening parenthesis.')
    p=ROOT/'sources'/LAYERS[layer];s=p.read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);reg=s[a:b]
    change(layer,reg,reg.replace(r'\({}^{(1)}\)',r'(\textsuperscript{1})'),'4.3.1.3 and bottom note','I.p108.note-markers','Both note markers have baseline parentheses and a raised numeral 1, as the two retained note crops show.')
    change(layer,r'$\operatorname{Kos}_{\bullet}(u)\longrightarrow\operatorname{Kos}_{\bullet}(u\')$.'.replace("u\\'","u'"),r'$\operatorname{Kos}_{\bullet}(u)\longrightarrow\operatorname{Kos}_{\bullet}(u\')$'.replace("u\\'","u'"),'last body line','I.p108.final-punctuation','evidence/I_p108_final-arrow.png shows no full stop after the final Koszul arrow.','reading')
    change(layer,r'\noindent\rule{120bp}{0.35bp}\par',r'\par\vfill\noindent\rule{68bp}{0.35bp}\par\vspace{4bp}','bottom note rule','I.p108.footnote-rule','The note sits at the bottom under a short rule, approximately 68bp in the authority.')
    p=ROOT/'sources'/LAYERS[layer];s=p.read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);reg=s[a:b];old=reg[-len('\\vspace{5.0bp}\n'):]
    if old!='\\vspace{5.0bp}\n': raise ValueError('unexpected final span')
    # Anchored unique trailing context avoids the earlier vspace instances.
    tail=reg[-350:]
    change(layer,tail,tail[:-len(old)]+r'\clearpage'+'\n','physical boundary','I.p108.page-boundary','Keep the end of the physical page after the complete bottom note.','structure')
# Corrected French must not retain optional normalization.
s=(ROOT/'sources'/LAYERS['corrected']).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);reg=s[a:b]
new=reg.replace('algèbre','Algèbre').replace(r'\uline{modules}',r'\uline{Modules}').replace('de celle-ci.)','de celle-ci).').replace('(4.3.1.2), s\'appelle','(4.3.1.2) s\'appelle')
change('corrected',reg,new,'throughout','I.p108.withdraw-normalizations','The print has capital Algèbre/Modules, terminal )., and no comma before s\'appelle. None creates a mathematical or grammatical defect requiring correction; all nine optional changes are withdrawn.','reading')
for layer in ['corrected','English']:
    change(layer,r'(-1)^{qn\'}'.replace("n\\'","n'"),r'(-1)^{qn}','opening formula','I.4.3.1.1.Leibniz-sign','evidence/I_p108_leibniz.png confirms printed qn-prime. The p107 definition assigns n to x and n-prime to x-prime. Passing d across the first factor requires qn. With x=1, x-prime=e of odd degree and a derivation d(e)=1 over Z, the printed rule forces 1=-1. CHECK_EVENTS records the counterexample and the corrected sign. Diplomatic French preserves qn-prime.','misprint of the original')
verdict(page,'ILL-SC-20260804-0105','Printed Leibniz sign qn-prime; zero source errors previously recorded','Repair to qn only in corrected French and English','Reject the zero-error verdict: the sign uses the second factor instead of the first and contradicts the unit test. No other mathematical alteration is introduced.',evidence+'See I.4.3.1.1.Leibniz-sign in CHECK_EVENTS.')
verdict(page,'ILL-NORM-20260804-0136','Capital Algèbre/Modules; ).; no comma before s\'appelle','All nine normalization differences withdrawn','These are optional normalization, not corrections of an original error.',evidence)
verdict(page,'ILL-TX-20260804-0132','Ten source anchors; added Gamma subscript A; two inline equations turned into displays','All anchors retained; notation, flow, underlines, note marks and boundary restored','The scan confirms k alone above Gamma; both proposition equations are inline and all square arrows and primes are present.',evidence)
verdict(page,'ILL-TR-20260804-0134','English follows the printed incorrect Leibniz exponent','Follow the corrected qn exponent and original formula/underline structure','The remaining prose conveys the French, including the deliberately literal donkey idiom; no style edit or terminology change is needed.',evidence)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[
('I.4.3.1.1.Leibniz-sign','The prior definition gives x degree (m,n), x-prime degree (m-prime,n-prime), and d degree (p,q). A left derivation requires d(xx-prime)=d(x)x-prime+(-1)^(qn)x d(x-prime). For B=exterior_Z(e) with e degree (0,1), the ordinary contraction d(e)=1 has degree (0,-1). Taking x=1 and x-prime=e makes the printed formula d(e)=-d(e), hence 1=-1. The repaired exponent qn yields 1=1 and the usual graded Leibniz rule. This is an original sign error; diplomatic qn-prime is retained.'),
('I.4.3.1.2.Koszul-differentials','Part (a): define d on the tensor algebra by d(e)=u(e) in the symmetric factor and d(f)=0, using the first-degree sign. The relations e*e=0 and e*e-prime+e-prime*e=0 are preserved because the symmetric factors commute. This descends uniquely to wedge(E) tensor S(F). Its square vanishes on generators and cross terms cancel, so d squared is zero without dividing by 2. Part (b): prescribe d(gamma_k(e))=gamma_(k-1)(e) tensor u(e), d(f)=0. The divided-power addition and scaling relations are preserved. The product relation is preserved by Pascal\'s identity binom(i+j-1,i-1)+binom(i+j-1,i)=binom(i+j,i). These generators determine the derivation uniquely. Its square on gamma_k(e) is gamma_(k-2)(e) tensor (u(e) wedge u(e))=0; cross terms cancel under the odd second-degree rule. All verifications are local and compatible with restriction, so they apply to module sheaves. This supplies the omitted proof for k>=1; the degree-zero divided power is a constant annihilated by d.'),
('I.4.3.1.3.Koszul-functoriality','For a commuting square with maps a:E->E-prime, b:F->F-prime and b u=u-prime a, wedge(a) tensor S(b), respectively Gamma(a) tensor wedge(b), commutes with d on every displayed generator. The unique extension therefore commutes with d everywhere. Exterior degree decreases for Kos-subscript and increases for Kos-superscript, giving the chain/cochain conventions of the footnote.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,body in events:w.writerow([sid,now,who,'targeted proof check',body])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for path in sorted((ROOT/'evidence').glob('I_p108_*.png')):f.write(f'| evidence/{path.name} | Printed p108 (or explicitly named prior p107 degree definition), 800-dpi crop inspected during the first reading. |\n')
print('Page 108 edits and explicit check events recorded; page completion not inferred.')
