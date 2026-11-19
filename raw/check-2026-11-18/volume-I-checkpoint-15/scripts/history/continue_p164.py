"""Primary reviewer's page164 audit and targeted77 reference repair; run once."""
import sys,csv,re
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='164';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p164}'
ev='LNM239 scan PDF p182 / printed p164: both complete400-dpi halves, eleven800-dpi crops and one1600-dpi Ext detail personally inspected; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('$A$-algèbre','$A$-Algèbre').replace('$P$-modules','$P$-Modules').replace('$P$,','$P$ ,').replace('$M$.','$M$ .').replace(r'$\alpha$.',r'$\alpha$ .')
ch('corrected',old,new,'opening and proof','III.p164.withdraw-normalizations','Withdraw two optional capitalizations and three punctuation-space changes.','reading')
ext=r'\mathop{\mathbb E\mathrm{xt}}\nolimits'
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p164.upright-Latin','Restore upright printed Latin mathematics.')
 old=region(layer);assert old.count(r'\mathcal X')==7
 ch(layer,old,old.replace(r'\mathcal X','X'),'extension names','III.p164.plain-X','Restore all seven plain printed X names.')
 old=region(layer);assert old.count('X*P')==3
 ch(layer,old,old.replace('X*P','X*p'),'three pullback expressions','III.p164.augmentation-p','The two prose occurrences and formula1.2.2.1 clearly print lowercase p, the augmentation P->B; the supplied uppercase P is a shared transcription error.','reading')
 old=region(layer);assert old.count(r'\operatorname{Ext}')==5
 ch(layer,old,old.replace(r'\operatorname{Ext}',ext),'five Ext operators','III.p164.Ext-letterforms','Each operator has a double-stroked E; the theorem occurrence was independently enlarged again to1600dpi.')
 if layer=='English':ch(layer,r'\uline{is an isomorphism.}',r'\uline{is an isomorphism}.','theorem ending','III.p164.underline-stop','The printed underline stops before the terminal period.')
 else:ch(layer,r'\uline{est un isomorphisme.}',r'\uline{est un isomorphisme}.','theorem ending','III.p164.underline-stop','The printed underline stops before the terminal period.')
 old=region(layer);new=old.replace('baseline=(current bounding box.center)','baseline=(TL.base)')
 new=new.replace(r'\smash{\raisebox{39.5bp}{(1.2.2.3)}}','(1.2.2.3)')
 new=new.replace(r'\node (TL) at (45,82)',r'\node[anchor=west] (TL) at (20,82)').replace(r'\node (BL) at (45,3)',r'\node[anchor=west] (BL) at (20,3)')
 new=new.replace(r'\node (TR) at (226,82)',r'\node[anchor=west] (TR) at (159,82)').replace(r'\node (BR) at (226,3)',r'\node[anchor=west] (BR) at (159,3)')
 new=new.replace(r'\draw[->] (TL) -- (BL);',r'\coordinate (leftArrow) at ([xshift=21bp]TL.south west);'+'\n'+r'    \draw[->] (leftArrow) -- (leftArrow |- BL.north);')
 new=new.replace(r'\draw[->] (TR) -- (BR);',r'\coordinate (rightArrow) at ([xshift=23bp]TR.south west);'+'\n'+r'    \draw[->] (rightArrow) -- (rightArrow |- BR.north);')
 new=new.replace(r'\node at (284,0) {$,$};',r'\node[anchor=base] at ([xshift=17bp]BR.base east) {$,$};')
 ch(layer,old,new,'naturality diagram','III.p164.diagram-geometry','Restore the common left starts of each formula column, the printed vertical arrows below the operator/subscript area, the upper-row equation-number baseline and lower-row comma baseline. Preserve all four arrows, both alpha labels, nodes, anchors and native macro; verify final geometry in the required build.')
 old=region(layer)
 def unwrap(m):
  t=m.group(1)
  return t+(r'\par' if t.startswith(r'\uline{compos') else '')+'\n'
 new,n=re.subn(r'(?m)^\\noindent\\makebox\[0pt\]\[l\]\{(.+)\}\n\\par\n',unwrap,old);assert n==8
 new=new.replace('$X\\longmapsto\\alpha(X)$\\par\n\n','$X\\longmapsto\\alpha(X)$\n')
 new=new.replace(r'\noindent définit',r'définit').replace(r'\noindent defines',r'defines')
 new=new.replace(r'\noindent carré commutatif',r'carré commutatif').replace(r'\noindent commutative square',r'commutative square')
 new=new.replace('flèche canonique\\par\n\n','flèche canonique\n').replace('canonical arrow\\par\n\n','canonical arrow\n')+r'\clearpage'+'\n'
 ch(layer,old,new,'prose paragraphs and boundary','III.p164.prose-flow','Unwrap eight artificial prose boxes and rejoin their broken clauses, preserve the separate theorem assertion and proof, all anchors, displays, and printed page boundary.','structure')
ch('English','free term by term','free degreewise','condition(L)','III.p164.degreewise','Use degreewise for terme a terme, consistently with glossary entries1283/1392/1401.','terminology')
old=region('English');new=old.replace('We deduce an','One deduces an').replace('We shall construct an inverse isomorphism to $\\alpha$.','An inverse isomorphism to $\\alpha$ will be constructed.')
ch('English',old,new,'construction and proof lead','III.p164.impersonal-on','Preserve impersonal on in both clauses.','translation')
# Reference77 explicitly distinguishes ordinary Ext from hyper-Ext.
for layer in LAYERS:
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(r'\IllusiePninetyfiveDisplay{(3.2.3.4)}');b=s.index('\n\n',a);old=s[a:b]
 new=old.replace(r'\longrightarrow\operatorname{Ext}',r'\longrightarrow'+ext)
 edit_page(layer,r'\begin{illusiebodypage}{illusie:I:ch1:p077}',old,new,'77','(3.2.3.4) target','I.3.2.3.4.hyperExt-letterform','corrects the earlier run: evidence/I_p077_ext-map.png personally reinspected at800dpi for164. The source ordinary Ext has plain E and is retained; the target hyper-Ext has a double-stroked E and is restored. All three corresponding formula regions read. Targeted reference repair only, not a new full-page or second-reading certification.','typesetting')
verdict('77','I.3.2.3.4.hyperExt-letterform:reference-reinspection','Both operators plain in supplied formula','Same','Targeted superseding verdict: retain the printed plain source Ext and restore only the double-stroked target hyper-Ext, directly visible in the800-dpi reference crop. Other77 decisions and reading status unchanged.','corrects the earlier run: evidence/I_p077_ext-map.png; all three formula regions read.')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p164','Two capitalized terms, three punctuation spaces; three printed lowercase pullback p occurrences transcribed P','Optional normalizations; same uppercase pullback error','Local source-comparison verdict, not a supplied decision-record ID. Withdraw optional normalizations; restore lowercase augmentation p in all three pullbacks and all three layers. No original mathematical error identified. Restore plain X, five double-stroked Ext initials, diagram alignment, underline stop and prose; English uses degreewise and impersonal on.',ev+'evidence/I_p164_pullback-differentials.png; evidence/I_p164_alpha-class.png; evidence/I_p164_naturality-square.png; evidence/I_p164_theorem-Ext1600.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.2.condition-L','Evaluation in each simplicial degree preserves ring extensions, their kernels and differentials, and exactness of simplicial modules is detected degreewise. Every P_n is a free A-algebra, hence a symmetric algebra on a free and therefore flat A-module, so1.1.7.1 gives condition(L) in that degree. Thus P satisfies(L) as an algebra of Simpl(T); no assertion that P is free on one simplicial module is needed. Pulling X back along p:P->B gives E times_B P with constant kernel M and conormal extension0->M->Omega_(E times_B P)/A tensor_(E times_B P) P->Omega_P/A->0.'),('III.1.2.2.alpha-additivity','Inverse image of algebra extensions along p preserves Baer sum by1.1.5.3; diff preserves it by1.1.7.3. The map chi sends a short exact sequence to its connecting morphism Omega_P/A->M[1]; the pushout/pullback identities I3.2.3.3 imply compatibility with the fiber-product-and-addition construction of Baer sum. Thus their composite alpha is a group homomorphism and commutes with kernel maps M->N. The reference I3.2.3.4 on77 was directly reinspected and indeed maps ordinary extension classes to hyper-Ext classes.'),('III.1.2.2.3.naturality-exercise','For A-prime->A and B-prime->B, let E be X and let v:P-prime->P be the induced resolution map. The extension pulled back after forgetting A is (E times_B B-prime) times_B-prime P-prime, canonically E times_B P-prime, which maps to E times_B P by (e,z)->(e,v(z)). Functorial differentials give a map between the two conormal short exact sequences, with id_M on kernels and the canonical Omega_P-prime/A-prime ->Omega_P/A on quotients, viewing the lower sequence as P-prime-modules. The upper sequence maps isomorphically to the pullback of the lower one since the maps on both ends are identities. Naturality of the connecting morphism chi then identifies its class with the right-hand restriction/precomposition map. The left-hand map is exactly forgetting the base A to A-prime, followed by pullback along B-prime->B, in the printed order1.1.5.4 then1.1.5.3. This proves the exercise square commutes. The theorem proof merely starts at the page end and is not yet credited.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
q=ROOT/'READING_QUESTIONS.tsv'
with q.open(newline='') as f:rows=list(csv.reader(f,delimiter='\t'))
for row in rows[1:]:
 if row[0]=='I-Q008':
  row[1]='68;77;91;125;138;162;163;164';row[4]+=' All four operators on163 and five on164 are directly confirmed. Reference77(3.2.3.4) has plain ordinary Ext on the left but double-stroked hyper-Ext on the right; only the latter is repaired on targeted reinspection.';row[6]+='; evidence/I_p163_ext-square.png; evidence/I_p164_alpha-class.png; evidence/I_p164_alpha-hom.png; evidence/I_p164_naturality-square.png; evidence/I_p164_theorem-Ext1600.png; evidence/I_p077_ext-map.png'
with q.open('w',newline='') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows)
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p164_*.png')):
  dpi='1600' if '1600' in p.name else '800';f.write(f'| evidence/{p.name} | Page164 audit:{dpi}-dpi crop personally inspected; expanded vertical-map crop completes the left Omega and theorem detail resolves its Ext letterform. |\n')
 f.write('| evidence/I_p077_ext-map.png; evidence/I_p077_functoriality.png | Reinspected for164: chi sends ordinary extension classes to hyper-Ext and respects pullback/pushout. |\n')
print('Page164 and targeted77 repairs, verdicts and three checks recorded.')
