"""Primary reviewer's p124 audit of the free-component description."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='124';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p124}'
ev='LNM239 scan PDF p142 / printed p124: both complete 400-dpi halves and eleven retained 800-dpi crops personally inspected; all three complete source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all notation','II.p124.upright-Latin','Bare Latin letters, the free-module indexing sets and the associated-sheaf functor are upright.')
 ch(layer,r'\hspace*{8bp}\hbox{\text{#1}\hfill',r'\hbox to\linewidth{\text{#1}\hfill','five numbered displays','II.p124.left-labels','Each formula number stands at the left margin with the formula centered; restore a full-width label box.')
 old=region(layer);new=old.replace(r'\xrightarrow{\ \sim\ }',r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}',3)
 ch(layer,old,new,'(1.2.3.3), (1.2.3.4), (1.2.3.5)','II.p124.unheaded-isomorphisms','The degreewise, inductive-limit and inverse-image isomorphisms have unheaded bars. The final associated-sheaf map has an arrowhead and remains unchanged; see evidence/I_p124_degree-formula.png, evidence/I_p124_limit-formula.png, evidence/I_p124_inverse-image.png and evidence/I_p124_sheafification.png.')
 old=region(layer);new=old.replace(r'\varinjlim_\lambda',r'\varinjlim')
 ch(layer,old,new,'(1.2.3.4)','II.p124.limit-indices','evidence/I_p124_limit-formula.png has no separate lambda beneath any limit sign; all indices on A and B remain.','reading')
 ch(layer,r"\ReflowDisplay{}{A^{(P_A(B)_{n-1})}\longrightarrow A'^{(P_{A'}(B')_{n-1})}}"+'\n'+r'\noindent ',r"$A^{(P_A(B)_{n-1})}\longrightarrow A'^{(P_{A'}(B')_{n-1})}$"+'\n','line after the functoriality explanation','II.p124.inline-free-map','evidence/I_p124_inline-free-map.png shows this free-module arrow inline, followed on the same line by the prose deduite de.','structure')
 old=r'$\mathbb Z^{(P_A(B)_{n-1})}\longrightarrow'+'\n'+r"\mathbb Z^{(P_{A'}(B')_{n-1})}$."
 new=r"$\mathbb Z^{(P_A(B)_{n-1}\longrightarrow P_{A'}(B')_{n-1})}$."
 ch(layer,old,new,'line below (1.2.3.3.1)','II.p124.free-functor-on-arrow','evidence/I_p124_tensor-prose.png applies the free-abelian-group notation once to the entire arrow in its exponent. The supplied expansion into two free modules is equivalent mathematics but is not the printed notation.','reading')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n')
 for prefix in (("D'après",'Soit','Enfin') if layer!='English' else ('By','Let','Finally')):new=new.replace('\\noindent '+prefix,'\\noindent\\hspace*{38bp}'+prefix)
 ch(layer,old,new,'continuous prose and four first-line indents','II.p124.paragraphs','Join ordinary printed line wraps and restore the approximately 38bp indents on the opening, inductive-system, inverse-image and associated-sheaf paragraphs.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p124.boundary','The unpunctuated final isomorphism ends this printed page.','structure')
old=region('corrected');new=region('as-printed')
ch('corrected',old,new,'two normalization differences','II.p124.withdraw-normalizations','Restore capital Anneaux and the printed space before the period after T; neither is an original error.','reading')
ch('as-printed',r"$P_A(B)_{n-1}\longrightarrow P_{A'}(B')_{n-1}$",r"$P_A(B)_{-1}\longrightarrow P_{A'}(B')_{n-1}$",'inline map deduite de','II.p124.restore-original-missing-n','evidence/I_p124_inline-free-map.png clearly prints -1 on the left, without n. Restore that original slip only in the diplomatic layer. The map inducing the free-module arrow must start at the generator set P_A(B)_(n-1), as shown by (1.2.3.3) and (1.2.3.3.1); the supplied corrected and English readings n-1 are necessary and retained.','reading')
ch('corrected','(voir un $T$-système','(voire un $T$-système','inductive-system paragraph','II.p124.voir-voire','evidence/I_p124_local-system.png prints voir. The parenthesis broadens the hypothesis to a local inductive T-system; the French adverb is voire (even), whereas the infinitive voir has no grammatical role here. The diplomatic reading is retained.','misprint of the original')
ch('English','for $n>0$ we have','for $n>0$ there is','opening sentence','II.p124.impersonal-on','French on a is impersonal; use there is under the supplied register standard.','terminology')
ch('English','if we set','with the convention that','degree-zero convention','II.p124.impersonal-convention','French en convenant que is an impersonal convention, not authorial nous; retain the convention without introducing we.','terminology')
verdict(page,'ILL-SC-20260804-0121','Zero typed original corrections recorded','One silent index correction confirmed; voir corrected to voire','The print has P_A(B)_(-1) in the map inducing a degree-n free-module map. The left generator set must be P_A(B)_(n-1), which corrected French and English already supply. Diplomatic restores the slip. The local-system parenthesis requires the adverb voire.',ev)
verdict(page,'ILL-NORM-20260804-0152','Two capitalization/spacing changes','Both withdrawn','Neither Anneaux nor the space before the period is an original error.',ev)
verdict(page,'ILL-TX-20260804-0148','Eleven ordered anchors','All preserved; notation and inline placement repaired','Enlarged all degrees, prime marks and free-module exponents. Restored three unheaded isomorphisms, suppressed limit indices and the single free-abelian functor applied to the arrow. Named display macro retained.',ev)
verdict(page,'ILL-TR-20260804-0150','Free components and compatibility statements','Meaning confirmed; two register changes','Inductive limits and associated-sheaf terminology agree with the standard; the existing or a local inductive T-system conveys the intended alternative. No stylistic rewriting.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.p124.free-components-and-functoriality','With S=P_A(B)_(n-1), P_n=A[S] and Omega(P_n/A)=P_n tensor_A A^(S), with basis dX_s. Tensoring by the augmentation gives (L_(B/A))_n=B tensor_A A^(S). The convention S=B at n=0 gives the same formula. For a square (A,B)->(A-prime,B-prime), the recursive map sends each generator X_s to X_(phi_(n-1)(s)), so the cotangent map sends b tensor e_s to beta(b) tensor e_(phi_(n-1)(s)). This proves both descriptions, including the equivalent free-Z-module version.'),('II.p124.missing-n-refutation','The printed domain P_A(B)_(-1)=B cannot induce the stated degree-n free-module map for general n: its generators must be indexed by P_A(B)_(n-1). At n=1 and A=B=Z, P_0 is the polynomial ring on the underlying set of Z; the basis element indexed by X_0+X_1 in P_0 requires the map P_0->P-prime_0, and is not indexed by an element of B. Thus restore n-1 in the corrected statement; refined statement II.p124.free-components-and-functoriality.'),('II.p124.three-compatibilities','The filtered/local inductive-limit comparison follows degreewise by commuting the standard resolution, the module of differentials and the augmentation tensor product with the indicated limits. For the local version the construction and its equalities are local and sheafify, as on p122. A geometric inverse image, and likewise associated sheaf, preserves finite products and colimits; therefore it preserves the free resolution, the generators-and-relations construction of differentials and the balanced tensor product. Applying these facts to Omega(P/A) tensor_P B gives the two further comparisons, naturally in the ring map. The reference (1.1.4.1) here is the inverse-image formula on p118; the separate duplicated label on p119 remains tracked in Q014.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'refuted, with the refined statement\'s id' if 'refutation' in sid else 'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p124_*.png')):f.write(f'| evidence/{p.name} | Printed p124, 800-dpi crop inspected during the first reading. |\n')
print('Page 124 edits and three checks recorded.')
