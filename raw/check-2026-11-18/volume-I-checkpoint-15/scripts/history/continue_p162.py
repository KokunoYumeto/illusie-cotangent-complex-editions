"""Primary reviewer's page162 audit and targeted earlier reference repair; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='162';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p162}'
ev='LNM239 scan PDF p180 / printed p162: both complete400-dpi halves and nine800-dpi crops personally inspected; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('-module','-Module').replace("d'anneaux","d'Anneaux").replace('$T$,','$T$ ,')
ch('corrected',old,new,'body and footnote','III.p162.withdraw-normalizations','Withdraw five optional capitalization changes and one punctuation-space change.','reading')
bar=r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}'
ext=r'\mathop{\mathbb E\mathrm{xt}}\nolimits'
for layer in LAYERS:
 old=region(layer);assert old.count(r'\ReflowBodyFont ')==2
 ch(layer,old,old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath'),'page mathematics','III.p162.upright-Latin','Restore upright printed Latin mathematics in all formulas, diagram and footnote.')
 old=region(layer);assert old.count(r'\mathcal O')==8
 ch(layer,old,old.replace(r'\mathcal O',r'\underline{\mathrm{O}}'),'ringed-topos paragraph','III.p162.structure-sheaves','Restore eight printed underlined structure-sheaf O symbols.')
 old=region(layer);assert old.count(r'\operatorname{Ext}')==5
 ch(layer,old,old.replace(r'\operatorname{Ext}',ext),'five Ext symbols','III.p162.Ext-letterforms','The enlarged goal, comparison and footnote show five double-stroked initial E symbols followed by upright xt; each has been checked locally.')
 old=region(layer);assert old.count(r'\widetilde L')==3
 ch(layer,old,old.replace(r'\widetilde L',r'L^{\sim}'),'chain-complex notation','III.p162.chain-tilde','The three chain-complex L symbols have the tilde at the upper right, not centered above L.')
 old=region(layer);a=old.index(r'\providecommand{\IllusieDerHomPOneSixtyTwo}');b=old.index('\n}',a)+2
 frag=old[a:b];ch(layer,frag,frag.replace(r'\xrightarrow{\sim}',bar),'Der-Hom comparison','III.p162.unheaded-isomorphism','Only the Der-Hom comparison is unheaded; retain the two headed main isomorphisms and the native simeq signs.')
 old=region(layer);assert old.count(r'\textsuperscript{(1)}')==2
 ch(layer,old,old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})'),'body call and footnote label','III.p162.footnote-parentheses','Both occurrences show a raised1 inside baseline parentheses.')
 old=region(layer);new=old
 new=new.replace('$X$\\par\n\n\\noindent\\makebox[0pt][l]{par un ', '$X$ par un ')
 new=new.replace('$X$\\par\n\n\\noindent\\makebox[0pt][l]{by an ', '$X$ by an ')
 new=new.replace('$)}\\par\ns\'identifie', '$) s\'identifie').replace('$)}\\par\nis naturally', '$) is naturally')
 new=new.replace('défini-\\par\n\n\\noindent tion','définition').replace('defini-\\par\n\n\\noindent tion','definition')
 new=new.replace('isomorphisme\\par\n\n\\noindent canonique','isomorphisme canonique')
 new=new.replace('isomorphism\\par\n\n\\noindent which is canonical','canonical isomorphism')
 new=new.replace(r'\noindent\makebox[0pt][l]{\hspace*{-5.0bp}(\textsuperscript{1})',r'\noindent(\textsuperscript{1})')
 new=new.replace('désigne}\\par\nle complexe','désigne le complexe').replace('denotes}\\par\nthe corresponding','denotes the corresponding')
 new=new.replace('\\vspace{5bp}\n\\phantomsection\\hypertarget{ILL-CCD:LNM239:CH3:S1:2:0:isomorphism:n1}','\\vfill\n\\phantomsection\\hypertarget{ILL-CCD:LNM239:CH3:S1:2:0:isomorphism:n1}')+r'\clearpage'+'\n'
 ch(layer,old,new,'prose, note and boundary','III.p162.prose-flow','Join the broken top paragraph, definition word and canonical-isomorphism clause; unwrap the footnote prose, place its rule at the foot, and preserve all anchors and the printed boundary.','structure')
# The reference check exposed a concrete earlier-run letterform omission.
for layer in LAYERS:
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(r'\IllusiePeightysixDisplay{(3.2.1.15)}');b=s.index('\n\n',a);old=s[a:b]
 assert old.count(r'\operatorname{Ext}')==3
 edit_page(layer,r'\begin{illusiebodypage}{illusie:I:ch1:p068}',old,old.replace(r'\operatorname{Ext}',ext),'68','(3.2.1.15)','I.3.2.1.15.Ext-letterforms','corrects the earlier run: evidence/I_p068_ext15.png was personally reinspected at800dpi for the reference on162. Its three initial E symbols are double-stroked; all three corresponding formula regions were read and the plain supplied operators are replaced in each layer. This is a targeted reference repair, not a new full-page or second-reading certification.','typesetting')
verdict('68','I.3.2.1.15.Ext-letterforms:reference-reinspection','Three plain supplied Ext operators','Same','Targeted superseding verdict for the three operators in this formula only: restore the double-stroked E on direct800-dpi reinspection while checking the reference on162. No other68 decisions or second-reading status superseded.','corrects the earlier run: evidence/I_p068_ext15.png; all three formula regions read.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p162','Five capitalized terms and one punctuation space','Optional normalizations','Local source-comparison verdict, not a supplied decision-record ID. Withdraw optional normalizations. Restore eight underlined O symbols, five double-stroked Ext operators, three upper-right tildes, the unheaded Der-Hom sign, note parentheses and prose flow. The two main isomorphisms are headed and retained. No original mathematical error found; the fundamental theorem is only announced here.',ev+'evidence/I_p162_der-hom.png; evidence/I_p162_theorem-goal.png; evidence/I_p162_ext-comparison.png; evidence/I_p162_footnote.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.10.topos-extensions','Transporting the structure sheaf of X-prime across the underlying-topos equivalence i gives an f-inverse(O_Y)-algebra E on X with a square-zero surjection E->O_X and specified kernel I. Conversely such an algebra extension defines a ringed topos with the same underlying topos X, structure sheaf E, and the required maps to X and Y. These constructions are inverse up to the specified isomorphisms and carry extension morphisms to the usual algebra-extension morphisms. Hence they identify isomorphism classes with the printed Exal group. The already verified automorphism formula id+Dq identifies its automorphisms with Der over f-inverse(O_Y); the universal property of Omega_X/Y gives the printed O_X-linear Hom description.'),('III.1.2.1.derived-adjunction','The standard resolution reference I1.5.5.6 on20 and cotangent definition II1.2.3.1 on123 were reinspected. Each P_n is a free A-algebra, so Omega_Pn/A is a free P_n-module and the simplicial module Omega_P/A is flat in the sense used for the derived tensor. Thus B derived-tensor_P Omega_P/A is represented by B tensor_P Omega_P/A=L_B/A. Applying I3.3.4.4 with ring map P->B, E=Omega_P/A and F=M gives Ext_B^1(L_B/A,M)~=Ext_P^1(Omega_P/A,M); its inverse is exactly1.2.1.1. The footnote uses I3.2.1.15, directly reinspected on68, with constant ring B and constant module M: normalization/associated chain complex sends M to degree0, giving Ext_B^n(L,M)~=Ext_B^n(L-tilde,M)=H^n RHom_B(L-tilde,M). This checks the stated reduction, not the unproved fundamental theorem announced in1.2.0.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
q=ROOT/'READING_QUESTIONS.tsv'
with q.open(newline='') as f:rows=list(csv.reader(f,delimiter='\t'))
for row in rows[1:]:
 if row[0]=='I-Q008':
  row[1]='68;91;125;138;162';row[4]+=' Page138 and all five operators on162 are also directly confirmed. Reference reinspection on162 confirms and repairs the three operators in68(3.2.1.15); no uninspected occurrence is inferred.';row[6]+='; evidence/I_p138_kodaira-spencer-class.png; evidence/I_p162_theorem-goal.png; evidence/I_p162_ext-comparison.png; evidence/I_p162_footnote.png; evidence/I_p068_ext15.png'
with q.open('w',newline='') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows)
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p162_*.png')):f.write(f'| evidence/{p.name} | Page162 audit:800-dpi crop personally inspected, including every displayed index, exponent, reference and small sign. |\n')
 f.write('| evidence/I_p020_resunderline.png; evidence/I_p068_ext15.png; evidence/I_p091_Ext-isomorphism.png; evidence/I_p091_flat-comparison.png; evidence/I_p123_definition-formula.png | Reinspected for162: standard resolution, constant-ring Ext comparison, derived adjunction, flat comparison and cotangent definition. |\n')
print('Page162 and targeted68 repairs, verdicts and two checks recorded.')
