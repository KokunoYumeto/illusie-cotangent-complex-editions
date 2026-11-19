"""Primary reviewer's page178 audit; run once after checkpoint14 freeze."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='178';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p178}'
ev='LNM239 scan PDF p196 / printed p178: both complete400-dpi halves and ten800-dpi crops personally inspected. All three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old,new in [('A-algèbre','A-Algèbre'),("l'algèbre","l'Algèbre"),('A-module','A-Module'),('un anneau','un Anneau'),('B-algèbre','B-Algèbre'),('C-algèbre','C-Algèbre'),("d'anneaux","d'Anneaux"),('B-modules','B-Modules')]:
 text=region('corrected');assert old in text
 ch('corrected',text,text.replace(old,new),'prose capitalization','III.p178.withdraw-capitalization','Withdraw optional capitalization normalization. evidence/I_p178_scholium-prose.png; evidence/I_p178_introduction.png; evidence/I_p178_topos-and-definition.png; evidence/I_p178_stability.png; evidence/I_p178_factorization.png.','reading')
for layer in ['corrected','English']:
 for old,new in [(r'$T$,',r'$T$\hspace{3.0bp},'),(r"$B'\otimes_A B''$;",r"$B'\otimes_A B''$\hspace{3.0bp};"),(r'$C$,',r'$C$\hspace{3.0bp},'),(r'$I$.',r'$I$\hspace{3.0bp}.')]:
  ch(layer,old,new,'formula punctuation','III.p178.punctuation-spacing','Withdraw optional corrected-French spacing normalization and align English formula punctuation. evidence/I_p178_topos-and-definition.png; evidence/I_p178_stability.png; evidence/I_p178_factorization.png.','reading' if layer=='corrected' else 'typesetting')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','body mathematics','III.p178.upright-Latin','Restore upright printed Latin mathematics throughout the page.')
 text=region(layer);assert text.count(r'\operatorname{Ext}')==2
 ch(layer,text,text.replace(r'\operatorname{Ext}',r'\mathop{\mathbb E\mathrm{xt}}\nolimits'),'scholium display','III.p178.hyperExt-initial','Restore both double-stroked E initials. evidence/I_p178_ext-left.png; evidence/I_p178_ext-right.png.')
 ch(layer,r'$B\simeq S_A(M)$',r'$B\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}S_A(M)$','definition of almost free','III.p178.unheaded-isomorphism-bar','The definition has a tilde over a single unheaded bar, not a two-bar simeq. evidence/I_p178_topos-and-definition.png.')
 ch(layer,'Grothendieck'+r'\par'+'\n\n'+r'\noindent (\hspace{3.0bp}[17] 7.4.2.2).','Grothendieck '+r'(\hspace{3.0bp}[17] 7.4.2.2).','scholium conclusion','III.p178.false-reference-paragraph','Join the continuous sentence across a printed line wrap. evidence/I_p178_scholium-prose.png.','structure')
 if layer=='English':
  ch(layer,'on a first'+r'\par'+'\n\n'+r'\noindent reading.','on a first reading.','introduction','III.p178.false-reading-paragraph','Restore continuous prose at the English-only artificial break. evidence/I_p178_reading-note.png.','structure')
  ch(layer,'an almost free'+r'\par'+'\n\n'+r'\noindent $C$-algebra.','an almost free $C$-algebra.','stability','III.p178.false-C-algebra-paragraph','Restore continuous prose at the English-only artificial break. evidence/I_p178_stability.png.','structure')
  ch(layer,'We continue to work','One continues to work','topos','III.p178.impersonal-register','French On takes impersonal English under the supplied standard; retain the distinct nous/we statements. evidence/I_p178_topos-and-definition.png.','translation')
  ch(layer,'We denote by','One denotes by','complex introduction','III.p178.impersonal-register','French On notera takes impersonal English. evidence/I_p178_factorization.png.','translation')
  ch(layer,'then locally an inductive limit','then a local inductive limit','Lazard-Deligne consequence','III.p178.local-inductive-limit','Use the established local inductive limit term, matching glossary589 and the local-system formulation of I4.2.1.3; do not replace it by an assertion about a fixed local cover. evidence/I_p178_stability.png; evidence/I_p100_proposition.png.','terminology')
 text=region(layer);ch(layer,text,text+r'\clearpage'+'\n','page boundary','III.p178.page-boundary','Preserve the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p178','Thirteen capitalized technical nouns and four punctuation spaces','Lowercase nouns and omitted spaces','Withdraw these optional normalizations; no original mathematical error identified. The two Ext operators are double-stroked; the definition uses a single unheaded isomorphism bar. Preserve the exact reference numbers, primes, truncation notation and two unlabelled factorization arrows.',ev+'evidence/I_p178_scholium-prose.png; evidence/I_p178_topos-and-definition.png; evidence/I_p178_stability.png; evidence/I_p178_factorization.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.9.2.low-degree-hyperExt','targeted proof check','Let K=t_{-2]}L_B/A. The truncation triangle K->L_B/A->t_[-1 L_B/A has K in cohomological degrees at most-2. For a module M in degree0 and i=0,1, both Hom_D(K,M[i]) and Hom_D(K[1],M[i]) vanish by the standard degree separation. Applying Hom(-,M[i]) therefore proves the displayed isomorphism with its contravariant direction. Personally reinspected the truncation definition on16 and the Ext0/Der comparison II1.2.4.3 on125. Combined with1.2.3 and1.2.9.1 this gives the stated low-degree interpretation; the external theorem [17]7.4.2.2 has not been inspected.'),('III.1.3.1.almost-free-stability','targeted proof check','For Bprime=Sym_A(Mprime), Bdoubleprime=Sym_A(Mdoubleprime), the coproduct universal property gives Bprime tensor_A Bdoubleprime=Sym_A(Mprime direct-sum Mdoubleprime), whose generator module is flat. For any B-algebra C, scalar extension gives B tensor_A C=Sym_C(M tensor_A C), with M tensor_A C flat over C. For the local inductive-limit assertion, apply the personally reinspected I4.2.1.3 on100 to the contractible two-term complex M--id-->M; its degree0 expresses M as a local inductive limit of finite free modules. Symmetric algebra preserves this local inductive limit, giving the claimed finite-type free algebras.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 f.write('| evidence/I_p016_truncations.png; evidence/I_p125_ext-der.png; evidence/I_p100_proposition.png; evidence/I_p100_local-colimit.png | Personally reinspected for178: truncation convention, Ext0/Der and the local finite-free approximation reference. |\n')
print('Page178 repairs, verdict and two checks recorded.')
