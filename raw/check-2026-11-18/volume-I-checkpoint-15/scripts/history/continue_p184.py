"""Primary reviewer's page184 audit; run once."""
import sys,csv,re
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='184';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p184}'
ev='LNM239 scan PDF p202 / printed p184: both complete400-dpi halves, ten800-dpi crops and two1600-dpi details personally inspected, including reinspection after three lower-edge expansions; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
for old,new in [('anneau','Anneau'),('-modules','-Modules'),('pour image','pour Image'),('A-algèbre','A-Algèbre'),('B-module','B-Module')]:
 s=region('corrected');ch('corrected',s,s.replace(old,new),'capitalized nouns','III.p184.withdraw-capitalization','Withdraw optional normalization in ten printed capitalized noun instances. evidence/I_p184_subsection-setup.png; evidence/I_p184_pi-f.png; evidence/I_p184_criterion.png; evidence/I_p184_footnote.png.','reading')
for term in ['bon','variation']:
 ch('corrected','« '+term+' »',r'\textquotedbl '+term+r'\textquotedbl{}','introductory quotation','III.p184.withdraw-quotation-normalization','Restore the printed straight double quotes. evidence/I_p184_introduction.png.','reading')
for layer in ['as-printed','corrected']:
 ch(layer,"d'un topos))", "d'un topos)",'Bourbaki reference','III.p184.extra-parenthesis','Only one closing parenthesis follows topos in the print. The supplied French sources added another; the printed two opening and two closing parentheses balance. evidence/I_p184_criterion.png; evidence/I_p184_parenthesis1600.png.','reading')
for layer in ['corrected','English']:
 for old,new in [(r'$T$.',r'$T$\hspace{3.0bp}.'),(r'$(B_o,I)$,',r'$(B_o,I)$\hspace{3.0bp},'),(r'$f$.',r'$f$\hspace{3.0bp}.'),(r'$M\longrightarrow N$.',r'$M\longrightarrow N$\hspace{3.0bp}.')]:
  ch(layer,old,new,'formula punctuation','III.p184.punctuation-spacing','Restore printed formula punctuation spacing. evidence/I_p184_subsection-setup.png; evidence/I_p184_object-action.png; evidence/I_p184_pi-f.png; evidence/I_p184_footnote.png.','reading' if layer=='corrected' else 'typesetting')
 old='topos):';ch(layer,old,'topos)'+r'\hspace{3.0bp}:','criterion colon','III.p184.colon-spacing','Restore the space before the concluding colon. evidence/I_p184_criterion.png.','reading' if layer=='corrected' else 'typesetting')
for layer in LAYERS:
 s=region(layer);ch(layer,s,s.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath'),'body and footnote','III.p184.upright-Latin','Restore upright printed Latin mathematics in both font scopes.')
 s=region(layer);ch(layer,s,s.replace(r'\textsuperscript{(1)}',r'(\textsuperscript{1})'),'body and footnote calls','III.p184.raised-footnote-numerals','Only the numeral is raised; parentheses remain on the baseline. evidence/I_p184_functor.png; evidence/I_p184_footnote.png.')
 s=region(layer);a=s.index(r'  \begin{tikzpicture}');b=s.index(r'  \end{tikzpicture}',a);old=s[a:b];new=old
 for node in ['LC','LB','ZTL','JT','CT','ZTR','ZBL','IB','BB','ZBR']:
  new=new.replace(r'\node ('+node+')',r'\node[anchor=base] ('+node+')')
 for node in ['COT','BOB']:
  new=re.sub(r'\\node \('+node+r'\)(\s*)at \(195,',r'\\node[anchor=base west] ('+node+r')\1at (192,',new)
 for left,right in [('ZTL','JT'),('JT','CT'),('CT','COT'),('COT','ZTR'),('ZBL','IB'),('IB','BB'),('BB','BOB'),('BOB','ZBR')]:
  new=new.replace(f'({left}) -- ({right})',f'([xshift=3bp,yshift=3bp]{left}.base east) -- ([xshift=-3bp,yshift=3bp]{right}.base west)')
 new=new.replace('(LB) -- (LC)','(0,12) -- (0,64.7)').replace('(IB) -- node[left] {$u$} (JT)','(111,12) -- node[left] {$u$} (111,64.7)').replace('(BB) -- node[right] {$f$} (CT)','(151,12) -- node[right] {$f$} (151,64.7)').replace('(BOB) -- node[right] {$f_o$} (COT)','(195,12) -- node[right] {$f_o$} (195,64.7)')
 ch(layer,old,new,'morphism-of-extensions diagram','III.p184.diagram-baselines','Align each exact row on one baseline and each vertical arrow under the main letter, including the o-indexed column. Preserve all twelve directed edges, all labels, and the separate underlined extension objects. evidence/I_p184_diagram.png.')
 if layer=='English':
  pairs=[('his study,'+r'\par'+'\n\n'+r'\noindent especially','his study, especially'),('there is a'+r'\par'+'\n\n'+r'\vspace{1.68bp}','there is a'),(r'\noindent functor (1.1.1.2)','functor (1.1.1.2)'),('and to'+r'\par'+'\n\n'+r'\vspace{1.56bp}','and to'),(r'\noindent each morphism','each morphism'),(r'\hspace{3.0bp}.\par'+'\n\n'+r'\vspace{0.72bp}'+'\n'+r'\noindent Note',r'\hspace{3.0bp}. Note'),('rings'+r'\par'+'\n\n'+r'\noindent in a topos','rings in a topos')]
 else:
  old=(r'\textquotedbl\par' if layer=='as-printed' else r'\textquotedbl{}\par')+'\n\n'+r'\noindent des obstructions.'
  pairs=[(old,r'\textquotedbl{} des obstructions.'),("qu'on a"+r'\par'+'\n\n'+r'\vspace{1.68bp}',"qu'on a"),(r'\noindent un foncteur','un foncteur'),('et à'+r'\par'+'\n\n'+r'\vspace{1.56bp}','et à'),(r'\noindent chaque morphisme','chaque morphisme'),('induit'+r'\par'+'\n\n'+r'\vspace{0.72bp}'+'\n'+r'\noindent par','induit par')]
 for old,new in pairs:ch(layer,old,new,'continuous prose','III.p184.false-prose-paragraph','Join false paragraphs at printed line wraps, retaining all anchors. evidence/I_p184_introduction.png; evidence/I_p184_subsection-setup.png; evidence/I_p184_object-action.png; evidence/I_p184_pi-f.png; evidence/I_p184_criterion.png.','structure')
 ch(layer,r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S2:1:1:n1}',r'\vfill'+'\n'+r'\phantomsection\hypertarget{ILL-CCD:LNM239:CH3:S2:1:1:n1}','footnote placement','III.p184.footnote-bottom','Preserve the printed bottom footnote block and rule. evidence/I_p184_footnote.png.','structure')
 s=region(layer);ch(layer,s,s+r'\clearpage'+'\n','page boundary','III.p184.page-boundary','Preserve the printed page boundary.','structure')
for term in ['right','variation']:
 ch('English','“'+term+'”',r'\textquotedbl '+term+r'\textquotedbl{}','introductory quotations','III.p184.English-quotes','Retain printed straight quote form without changing the existing translation. evidence/I_p184_introduction.png.')
ch('English','We first fix','One first fixes','setup','III.p184.on','On se fixe is impersonal; retain the authorial we/us corresponding to nous in the introduction. evidence/I_p184_subsection-setup.png; evidence/I_p184_introduction.png.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p184','complèter; ten capitalized noun instances; five punctuation spaces; straight quotes','compléter; lowercase nouns; omitted spaces; guillemets','Retain the necessary accent correction complèter->compléter, confirmed at1600dpi. Withdraw optional noun-case, quotation and spacing normalization. Both French sources added a second closing parenthesis after topos; remove this shared transcription error.',ev+'evidence/I_p184_accent1600.png; evidence/I_p184_parenthesis1600.png; evidence/I_p184_introduction.png; evidence/I_p184_criterion.png; evidence/I_p184_footnote.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.2.1.1.functor','targeted proof check','For a morphism f:B->C of square-zero extensions, f(I) is contained in J and descends to f0:B0->C0. If b lifts b0, then u(b0 i)=f(b)f(i)=f0(b0)u(i); the final expression uses the C0-action on J, well-defined because J^2=0. Thus (f0,u) is an A-Algmod morphism. Restrictions and quotient maps preserve identities and composition, so the displayed assignment is a functor.'),('III.2.1.1.pushout-criterion','targeted proof check','The adjoint v:I tensor_B0 C0->J sends i tensor c0 to f(i)c for a local lift c of c0. This is independent of the lift because f(i) is in J and J^2=0. Its image is the ideal IC. The pushout B0 tensor_B C is C/IC, and its canonical map to C0=C/J is an isomorphism exactly when IC=J, exactly when v is surjective. The calculation is local and applies to the sheaves of rings in the stated topos.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p184_*.png')):f.write(f'| evidence/{p.name} | Page184 audit: personally inspected;800dpi except explicit1600dpi details. |\n')
print('Page184 repairs, one verdict and two proof checks recorded.')
