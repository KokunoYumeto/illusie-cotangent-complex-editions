"""Primary reviewer's page158 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='158';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p158}'
ev='LNM239 scan PDF p176 / printed p158: both complete400-dpi halves and nine800-dpi page crops personally inspected; all three full source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('A-algèbre','A-Algèbre').replace('A-module plat','A-Module plat').replace('$C=S_A(M)$,','$C=S_A(M)$ ,').replace(r'$C\simeq A[t_1,\ldots,t_r]$.',r'$C\simeq A[t_1,\ldots,t_r]$ .')
ch('corrected',old,new,'condition and lemma prose','III.p158.withdraw-normalizations','Withdraw two optional capitalizations and two punctuation-space changes.','reading')
for layer in LAYERS:
 old=region(layer);assert old.count(r'\ReflowBodyFont ')==2
 ch(layer,old,old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath'),'body and note mathematics','III.p158.upright-Latin','Restore upright printed Latin mathematical letters; retain all five source-width sequence-arrow macros.')
 ch(layer,r'\mathcal X','X','1.1.7.2 extension','III.p158.extension-X','The extension name is plain upright X, not calligraphic, in evidence/I_p158_diff-sequence.png.')
 old=region(layer);assert old.count(r'\textsuperscript{(1)}')==2
 new=old.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})').replace(r'immédiat(\textsuperscript{1})',r'immédiat (\textsuperscript{1})').replace(r'shows(\textsuperscript{1})',r'shows (\textsuperscript{1})')
 ch(layer,old,new,'footnote call and label','III.p158.footnote-parentheses','Restore baseline parentheses around the raised1 and the space before the body call.')
 old=region(layer);new=old
 new=new.replace('\\par\n\n\\vspace{4.22bp}\n',' ').replace('\\par\n\n\\vspace{0.48bp}\n',' ')
 new=new.replace('supposer \n\n$M$','supposer $M$').replace('suppose that \n\n$M$','suppose that $M$')
 assert new.count('\\par\n\n\\vspace{0.12bp}\n')==2
 new=new.replace('\\par\n\n\\vspace{0.12bp}\n',' ')
 if layer=='English':new=new.replace(r'\noindent\hspace*{0.7bp}{is exact.}', 'is exact.')
 else:
  new=new.replace(r'\noindent\hspace*{1.42bp}\makebox[48.84bp][s]{est exacte.}', 'est exacte.')
  new=new.replace('aurons\\par\n\n\\noindent\\hspace*{-0.72bp}\\makebox[49.68bp][s]{pas besoin.}\\par','aurons pas besoin.\\par')
 note=r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S1:1:6:split-exactness-conclusion:n1}'
 new=new.replace(note,r'\vfill'+'\n'+note)
 ch(layer,old,new,'paragraphs and footnote','III.p158.prose-flow','Remove artificial line-end paragraphs and fixed prose boxes inside continuous sentences, retain every anchor, and keep the footnote at the page foot.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p158.boundary','Retain the printed page boundary.','structure')
old=region('English');new=old.replace('we may suppose','one may suppose').replace('we are reduced','one is reduced')
ch('English',old,new,'local inductive-limit argument','III.p158.on-register','Translate both on clauses impersonally; retain We shall say/write for Nous and Let us prove for Prouvons.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p158','Two capitalized terms and two punctuation spaces; reference I4.2.1.3','Optional normalizations; reference unchanged','Local source-comparison verdict, not a supplied decision-record ID. Withdraw the optional normalizations. Retain I4.2.1.3: its bounded contractible-complex case gives the local filtered finite-free approximation of a flat module required here. No original mathematical error found; all twenty sequence arrows, relative bases, sequence ends and the polynomial isomorphism agree.',ev+'evidence/I_p158_limit-proof.png; evidence/I_p100_proposition.png; evidence/I_p158_diff-sequence.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.1.6.split-and-converse','For B1=C direct-sum J with J square-zero, the section induces Omega_C/A ->Omega_B1/A tensor_B1 C; together with d:J ->the middle term this gives the decomposition J direct-sum Omega_C/A. Conversely a splitting retraction r of the injective conormal arrow gives an A-derivation D:B1->J with D|J=id. The map b ->b-D(b) is an A-algebra homomorphism, since J^2=0 and D is a derivation; it kills J and therefore descends to a section C->B1. This directly proves the footnote converse as well as the main continuation; the external EGA citation itself was not consulted.'),('III.1.1.7.1.flat-symmetric-algebra','Reinspected the printed proposition I4.2.1.3 on100. Apply it to the bounded contractible two-term complex M --id->M: a component presents flat M as a local filtered inductive limit of finite free modules F_lambda. Sym commutes with these limits, so C is the corresponding local limit of C_lambda=Sym(F_lambda). Pull an A-extension B->C back to each C_lambda; its kernel remains I with restricted action and the filtered local inductive limit of these pullbacks is B, because filtered colimits commute with finite limits in sheaves. Locally each C_lambda is a finite polynomial algebra and finitely many generators lift after a common cover, giving a section and hence a split conormal sequence by1.1.6. Differentials and tensor products commute with the filtered local colimit, and filtered colimits preserve exactness, proving condition(L) for C. This proves exactness only for the final extension; it does not assume M locally free or the final extension globally split.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p158_*.png')):f.write(f'| evidence/{p.name} | Page158 audit:800-dpi crop personally inspected. |\n')
 f.write('| evidence/I_p100_proposition.png | Earlier proposition crop personally reinspected for the precise local inductive-limit reference on158. |\n')
print('Page158 edits, verdict and two proof checks recorded.')
