"""Primary reviewer's image-based edits for printed p114."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='114';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p114}'
ev='LNM239 scan PDF p132 / printed p114: both complete 400-dpi halves and thirteen retained 800-dpi enlargements personally inspected. Three full source spans and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','whole page','II.p114.upright-Latin','Latin mathematical letters, exponents and subscripts are upright in the scan.')
 title='CHAPTER II' if layer=='English' else 'CHAPITRE II'
 ch(layer,r'\uline{'+title+'}',r'\uuline{'+title+'}','chapter heading','II.p114.double-underline','evidence/I_p114_chapter.png shows two separate underlines.')
 for word in (['Unless otherwise stated','We recall'] if layer=='English' else ['Sauf mention du contraire','Nous rappelons']):
  ch(layer,r'\noindent '+word,r'\noindent\hspace*{2em}'+word,'indented opening paragraphs','II.p114.indent-'+('convention' if word in ['Unless otherwise stated','Sauf mention du contraire'] else 'preliminaries'),'The ring convention and preliminary paragraph each begin with a visible first-line indent.')
 old=r'\uline{$A$-derivation from}' if layer=='English' else r'\uline{$A$-dérivation de}'
 new=r'$A$-\uline{derivation from}' if layer=='English' else r'$A$-\uline{dérivation de}'
 ch(layer,old,new,'definition emphasis','II.1.1.1.derivation-underline','evidence/I_p114_definition.png shows the underline beginning at dérivation, after the A- prefix.')
 for num,formula in [('1.1.1.1',r'd(xy)=x\,dy+y\,dx'),('1.1.1.2',r'\operatorname{Der}_A(B,M)'+(',' if layer=='English' else '')),('1.1.1.3',r'B\oplus M=S_B(M)\big/\bigoplus_{i\geq2}S_B^i(M)')]:
  old=r'\ReflowDisplay{('+num+')}{'+formula+'}'
  note=r'\quad\text{(\textsuperscript{1})}' if num=='1.1.1.3' else ''
  new=r'\ReflowDisplay{}{\hbox to\linewidth{\text{('+num+r')}\hfill$'+formula+note+r'$\hfill\phantom{\text{('+num+')}}}}'
  ch(layer,old,new,'three labelled displays','II.'+num+'.left-label','The printed equation label is on the left. '+('The display also has a printed (raised 1) note call, omitted in all three supplied layers; restore it.' if num=='1.1.1.3' else 'Keep the formula and its visible punctuation.'))
 ch(layer,r'\noindent\rule{120bp}{0.35bp}\par',r'\vfill\noindent\rule{74bp}{0.35bp}\par','footnote rule','II.p114.footnote-rule','The note is set at the page foot with a short separator, as evidence/I_p114_footnote.png shows.')
 ch(layer,r'\textsuperscript{(1)}',r'(\textsuperscript{1})','footnote marker','II.p114.note-parentheses','The parentheses are on the baseline; only the numeral is raised.')
 ch(layer,'(I 1.5.5 b)).','(I 1.5.5. b)).','footnote reference','II.p114.reference-stop','evidence/I_p114_footnote.png shows a stop after the final 5, before b).','reading')
 # Only the final vspace is the physical-boundary target.
 old=region(layer)[-180:]
 assert old.endswith('\\vspace{5.0bp}\n')
 ch(layer,old,old[:-len('\\vspace{5.0bp}\n')]+r'\clearpage'+'\n','physical boundary','II.p114.page-boundary','The footnote ends this page; the isomorphism introduced in the main text continues next page.','structure')
for layer in ['as-printed','corrected']:
 ch(layer,'COMPLEXE COTANGENT : DÉFINITION ET PREMIÈRES PROPRIÉTÉS','COMPLEXE COTANGENT : DEFINITION ET PREMIERES PROPRIETES','chapter title','II.p114.unaccented-capitals','evidence/I_p114_title.png shows no accents on the capital letters in this heading.','reading')
old=region('corrected');new=old.replace('un anneau','un Anneau').replace('-algèbre','-Algèbre').replace('-module','-Module').replace(r'\uline{algèbre',r'\uline{Algèbre').replace("l'algèbre symétrique","l'Algèbre symétrique")
ch('corrected',old,new,'seven capitalization changes','II.p114.withdraw-normalizations','All seven capitalized object words are visible in the definition, dual-number paragraph and footnote; they are not misprints. The necessary x,y quantifier repair remains.','reading')
ch('English','Some facts about derivations and differentials','Sorites on derivations and differentials','section 1.1 heading','II.1.1.Sorites','The supplied glossary GLOSSARY_SGA_EN_UNIFIED.tsv has sorite -> sorites (decided). No conflicting higher-priority decision was found. Apply the term to the visible heading.','terminology')
ch('English','A chain of results on derivations and differentials','Sorites on derivations and differentials','section 1.1 navigation title','II.1.1.Sorites-navigation','Use the same glossary term in the existing destination title; preserve its identifier.','terminology')
ch('English','We recall some familiar definitions','We recall here some familiar definitions','preliminaries','II.p114.here','Restore ici in the preliminary sentence without otherwise rephrasing it.','translation')
verdict(page,'ILL-SC-20260804-0111 / ILL-TCI-20260813-0138','Printed quantifier has only y in B(U)','x,y retained in corrected French and English','Confirmed original omission: d(xy)=x dy+y dx uses both x and y, and the Leibniz rule must hold for every pair of local sections. The scan explicitly has no x before y.',ev+'evidence/I_p114_quantifiers.png')
verdict(page,'ILL-NORM-20260804-0142','Seven printed capitalizations Anneau, Algèbre(s), Module(s)','Seven lower-case normalizations withdrawn','No mathematical or grammatical reason to change these capitals.',ev)
verdict(page,'ILL-TX-20260804-0138','Twelve anchored units; double chapter underline; unaccented capitals; left equation labels; raised-one note call','All anchors/destinations preserved; emphasis, labels, note call, indentation and reference punctuation restored','The equations, their indices and the EGA references were enlarged; the supplied missing note call was not a print omission.',ev)
verdict(page,'ILL-TR-20260804-0140','Sorites heading and ici','English glossary term and omitted here restored','Punctual agrees with the glossary. Remaining English meaning agrees with corrected French; formula typography and note call repaired in parallel.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 w.writerow(['II.1.1.1.quantifier-and-group',now,who,'targeted proof check','The Leibniz identity contains two independently variable local sections x and y, so its universal statement requires x,y in B(U); the printed quantifier omits x. For A-linear derivations d,e, (d+e)(xy)=x(d+e)(y)+y(d+e)(x), and the same identity holds for -d and zero, sectionwise and compatibly with restriction. Thus the stated set is an abelian group. No external EGA claim is asserted from an unconsulted citation.'])
 w.writerow(['II.1.1.1.3.dual-numbers',now,who,'targeted proof check','The graded symmetric algebra has degree-zero part B and degree-one part M. Its sum of terms of degree at least two is an ideal; quotienting gives underlying B-module B direct-sum M and product (b,m)(c,n)=(bc,bn+cm). This proves that the displayed quotient is the square-zero B-algebra of dual numbers on M. The canonical isomorphism introduced but not displayed on this page is not yet claimed checked.'])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p114_*.png')):f.write(f'| evidence/{p.name} | Printed p114, 800-dpi crop inspected during the first reading. |\n')
print('Page 114 edits and proof checks recorded.')
