# Historical first-stage page-1 edits. Run only against the corresponding pre-edit source state.
# CORRECTIONS.tsv and replay_corrections.py are the canonical complete replay.
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from edit_support import edit, edit_page, verdict, ROOT, LAYERS
A=r'\begin{illusiebodypage}{illusie:I:ch1:p001}'
def change(layer, old, new, line, evidence, kind='reading'):
 edit_page(layer,A,old,new,'1',line,'I.1.1',f'LNM239 PDF p. 19, printed p. 1: {evidence}',kind)
for layer in LAYERS:
 # Page-local heading implementations retain the existing macro names and anchors.
 title='CHAPTER I' if layer=='English' else 'CHAPITRE I'
 heading='RELATIVE HOMOTOPICAL ALGEBRA' if layer=='English' else 'ALGÈBRE HOMOTOPIQUE RELATIVE'
 newheading=heading if layer=='English' else 'ALGEBRE HOMOTOPIQUE RELATIVE'
 old=rf'\IllusieChapterHeading{{{title}}}{{{heading}}}'
 new=r'\begingroup'+ '\n'+r'\renewcommand{\IllusieChapterHeading}[2]{%'+ '\n'+r'  \begin{center}\fontsize{11}{14}\selectfont\uuline{#1}\par\smallskip\uline{#2}\end{center}\vspace{5bp}}'+ '\n'+rf'\IllusieChapterHeading{{{title}}}{{{newheading}}}'+ '\n'+r'\endgroup'
 change(layer,old,new,'chapter heading','evidence/I_p001_header.png shows two rules beneath CHAPITRE I, one beneath the unaccented ALGEBRE heading.')
 section='Review.' if layer=='English' else 'Rappels.'
 change(layer,rf'\IllusieBodySection{{1.}}{{{section}}}',r'\begingroup'+ '\n'+r'\renewcommand{\IllusieBodySection}[2]{\par\Needspace{40bp}\noindent #1\quad #2\par\vspace{3bp}}'+ '\n'+rf'\IllusieBodySection{{1.}}{{\uline{{{section[:-1]}}}.}}'+ '\n'+r'\endgroup','section heading','Only Rappels is underlined; the final period lies beyond the rule.')
 term='Simplicial objects' if layer=='English' else 'Objets simpliciaux'
 hom='homotopies'
 old=rf'\IllusieBodySubsection{{1.1.}}{{{term}, {hom} ([10], [11], [23]).}}'
 new=r'\begingroup'+ '\n'+r'\renewcommand{\IllusieBodySubsection}[2]{\par\Needspace{32bp}\noindent #1\quad #2\par\vspace{2bp}}'+ '\n'+rf'\IllusieBodySubsection{{1.1.}}{{\uline{{{term}}}, \uline{{{hom}}} ([10], [11], [23]).}}'+ '\n'+r'\endgroup'
 change(layer,old,new,'subsection heading','Separate rules under Objets simpliciaux and homotopies; comma, references and final period are not underlined.')
 word='or' if layer=='English' else 'ou'
 change(layer,rf'\delta_i^n\; (\text{{{word} }}\delta_i)',rf'd_n^i\; (\text{{{word} }}d^i)','first display','evidence/I_p001_coface.png and I_p001_face.png show Latin d with upper i, lower n, and abbreviated d with upper i.')
 change(layer,rf'\sigma_i^n\; (\text{{{word} }}\sigma_i)',rf's_n^i\; (\text{{{word} }}s^i)','second display','evidence/I_p001_codegeneracy.png shows Latin s with upper i, lower n, and abbreviated s with upper i.')
 change(layer,r'X(\delta_i^n)',r'X(d_n^i)','simplicial-object paragraph, face formula','evidence/I_p001_face.png clearly prints X(d_n^i), while the induced map is d_i^n.')
 change(layer,r'X(\sigma_i^n)',r'X(s_n^i)','simplicial-object paragraph, degeneracy formula','The inline formula after the underlined dégéné-rescence is X(s_n^i), distinct from s_i^n.')
 change(layer,r'\Delta^{\circ}',r'\Delta^{\mathrm{o}}','simplicial-object paragraph','The opposite-category mark is a raised lowercase o, not a circle operator.')
 change(layer,r'(\Delta^p)^{\circ}',r'(\Delta^p)^{\mathrm{o}}','paragraph after (1.1.1)','The same raised lowercase o follows the parenthesized product category.')
 # Footnote is not a sentence and has no printed terminal point.
 factor='factors' if layer=='English' else 'facteurs'
 times='times' if layer=='English' else 'fois'
 change(layer,rf'\Delta^p=\underbrace{{\Delta\times\cdots\times\Delta}}_{{p\ \text{{{factor}}}}}$.}}',rf'\Delta^p=\underbrace{{\Delta\times\ldots\times\Delta}}_{{p\ \text{{{times}}}}}$}}','footnote (*)','evidence/I_p001_note.png shows p fois, low dots and no terminal period; the product signs are retained.')
 if layer!='English':
  if layer=='corrected':
   change(layer,'On note $\\Delta$ la catégorie dont les objets sont les ensembles finis\ntotalement ordonnés non vides, les flèches les applications croissantes au sens\nlarge. Pour $n\\in\\mathbb{N}$ et $i\\in[0,n]$, on désigne par','On note $\\Delta$ la catégorie dont les objets sont les ensembles finis totale-\\linebreak\nment ordonnés non vides, les flèches les applications croissantes au sens large.\nPour $n\\in\\mathbb{N}$ et $i\\in[0,n]$, on désigne par','first paragraph','The printed line ends totale- and the next starts ment; this is not an original misprint.')
  else:
   change(layer,'totale-\nment','totale-\\linebreak\nment','first paragraph','The existing literal carrier hyphen requires a line break so that TeX does not print totale- ment within one line.','typesetting')
  change(layer,'Un objet simplicial de','Un \\uline{objet simplicial} de','simplicial-object paragraph','The first defining occurrence objet simplicial is underlined.')
  change(layer,'la i-ième flèche de face','la i-ième \\uline{flèche de face}','simplicial-object paragraph','flèche de face is underlined; i-ième is not.')
  old='la i-ième flèche de dégénérescence\n' if layer=='corrected' else 'la i-ième flèche de dégéné-\nrescence '
  new='la i-ième \\uline{flèche de dégéné-}\\linebreak\n\\uline{rescence} '
  change(layer,old,new,'simplicial-object paragraph','The print underlines flèche de dégéné- and rescence across the carrier break.')
  change(layer,'des objets $p$-simpliciaux','des objets \\uline{$p$-simpliciaux}','paragraph after (1.1.1)','The whole p-simpliciaux term is underlined.')
  change(layer,'des objets cosimpliciaux','des objets \\uline{cosimpliciaux}','paragraph after (1.1.1)','cosimpliciaux is underlined.')
  change(layer,'des objets $p$-cosimpliciaux','des \\uline{objets} $p$-\\uline{cosimpliciaux}','paragraph after (1.1.1)','evidence/I_p001_emphasis.png shows separate rules beneath objets and cosimpliciaux, leaving p- without a rule.')
  change(layer,'des objets simpliciaux mixtes de','des \\uline{objets simpliciaux mixtes de}','last body line','evidence/I_p001_emphasis.png shows the rule beginning at objets and continuing through de.')
 else:
  change(layer,'A simplicial object of','A \\uline{simplicial object} of','simplicial-object paragraph','Restores the emphasis of the French defining term without changing English wording.')
  change(layer,'face map $X(d_n^i)$','\\uline{face map} $X(d_n^i)$','simplicial-object paragraph','Restores emphasis corresponding to flèche de face.')
  change(layer,'degeneracy map $X(s_n^i)$','\\uline{degeneracy map} $X(s_n^i)$','simplicial-object paragraph','Restores emphasis corresponding to flèche de dégénérescence.')
  change(layer,'$p$-simplicial objects of','\\uline{$p$-simplicial} objects of','paragraph after (1.1.1)','Restores emphasis corresponding to p-simpliciaux.')
  change(layer,'cosimplicial objects of $C$, that is, functors from $\\Delta$','\\uline{cosimplicial} objects of $C$, that is, functors from $\\Delta$','paragraph after (1.1.1)','Restores emphasis corresponding to cosimpliciaux.')
  change(layer,'$p$-cosimplicial objects of','$p$-\\uline{cosimplicial} \\uline{objects} of','paragraph after (1.1.1)','Restores the two separately underlined French words in their English order.')
  change(layer,'of mixed simplicial objects in','of \\uline{mixed simplicial objects in}','last body line','Restores emphasis corresponding to objets simpliciaux mixtes de.')
verdict('1','I.1.1 / SC0016','Two printed carrier breaks: totale-/ment and dégéné-/rescence','Both words joined','reverted','PDF p. 19 shows the carrier breaks; no mathematical or linguistic defect justifies removing them under the present diplomatic contract. SC0016 reports no original misprint; the newly detected d/s notation errors affect all three supplied layers and are transcription errors.')
from shutil import copy2
for f in ['header','coface','codegeneracy','face','note','emphasis']:
 copy2('tmp/pdfs/I/scan019/'+f+'.png',ROOT/'evidence'/('I_p001_'+f+'.png'))
