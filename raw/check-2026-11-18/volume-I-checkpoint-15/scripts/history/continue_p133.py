"""Primary reviewer's page 133 transitivity-sequence audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page
page='133';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p133}'
ev='LNM239 scan PDF p151 / printed p133: both complete 400-dpi halves and eleven retained 800-dpi crops personally inspected; flatness and name crops expanded and reinspected. All three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace("d'anneaux","d'Anneaux").replace('$T$.','$T$ .').replace('$P$,','$P$ ,').replace('$Q$,','$Q$ ,').replace("C'$,","C'$ ,")
ch('corrected',old,new,'opening and sequence prose','II.p133.withdraw-normalizations','The two Anneaux capitals and four punctuation spaces are printed conventions, not errors. Restore them in corrected French.','reading')
for layer in LAYERS:
 old=region(layer);new=old.replace(r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath')
 ch(layer,old,new,'Latin symbols throughout','II.p133.upright-Latin','All Latin variables and indices are upright; apply the convention also inside the sequence font group.')
 old=region(layer);new=old.replace('baseline=(current bounding box.center)','baseline=(At.base)',1).replace('baseline=(current bounding box.center)','baseline=(A.base)',1)
 ch(layer,old,new,'diagrams (2.1.1.2) and (2.1.1.5)','II.p133.diagram-tag-baselines','Both printed numbers align with the top row, not the middle of the diagram; evidence/I_p133_resolution.png and evidence/I_p133_functoriality.png. All seven arrows in each diagram are retained, with the identity label and bottom comma only where printed.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace('\\par\n\\vspace{2.3bp}\n\\noindent ','\n')
 ch(layer,old,new,'continuous prose around five displays','II.p133.prose-continuity','Ordinary typewritten wraps, including the continuation after the colon, are not new paragraphs; remove only those false breaks. All ten semantic anchors and both contents destinations are retained.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p133.boundary','Preserve the printed page boundary after the continuing functoriality sentence.','structure')
ch('English','We denote','One denotes','definition (2.1.1.4)','II.p133.impersonal-denote','On note is impersonal under the supplied register standard. The existing degreewise and true triangle terminology agrees with the earlier definitions.','terminology')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.2.1.1.3-and-2.1.1.4','In degree n, Q_n is a free polynomial algebra over P_n. Its differentials over A_n decompose into Omega(P_n/A_n) tensor Q_n and the free Q_n-module on the polynomial generators. Thus the first summand embeds and the quotient is Omega(Q_n/P_n), giving the displayed short exact sequence. This quotient is flat, so Tor_1 over Q_n with C_n vanishes and scalar extension preserves the injection as well as right exactness. These natural maps commute with simplicial operators, yielding the short exact sequence of simplicial C-modules in (2.1.1.4). The last denominator P on p133 also agrees with the necessary correction of the repeated A in the cited p117 formula (1.1.2.13).'),('II.2.1.1.functoriality','A commutative map of triples A->B->C and A-prime->B-prime->C-prime induces the map P_A^Delta(B)->P_A-prime^Delta(B-prime) by functoriality of the standard free resolution. Together with C->C-prime it induces Q=P_P^Delta(C)->Q-prime. Applying universal differentials sends d(p) to d(image(p)); hence both maps in the exact sequence commute with the induced semilinear maps. Tensoring along Q->C and Q-prime->C-prime gives the required map of exact sequences. Identity and composition follow on every free generator. The category of true triangles cited at I 3.2.4 is indeed the localization of short exact sequences, as reread on pp81-82; no change of reference or terminology is necessary.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p133_*.png')):f.write(f'| evidence/{p.name} | Printed p133, 800-dpi crop inspected during the first reading. |\n')
print('Page 133 edits and two targeted proof checks recorded.')
