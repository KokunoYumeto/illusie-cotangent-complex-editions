"""Primary reviewer's p129 differential comparison and localization audit."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='129';anchor=r'\begin{illusiebodypage}{illusie:I:ch1:p129}'
ev='LNM239 scan PDF p147 / printed p129: both complete 400-dpi halves and eight retained 800-dpi crops personally inspected; augmentation recropped to include both complete superscripts. All three complete source regions and four prior records read. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace("d'anneaux","d'Anneaux").replace('$A$-algèbres','$A$-Algèbres').replace('$B$-modules','$B$-Modules').replace('$T$. Notons,','$T$ . Notons,').replace('$B$, et','$B$ , et')
ch('corrected',old,new,'Scholium opening and category definitions','II.p129.withdraw-normalizations','The three capitalizations and two punctuation spaces are printed conventions and do not cause a mathematical or grammatical defect; evidence/I_p129_scholium.png and evidence/I_p129_categories.png.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','all Latin notation','II.p129.upright-Latin','The original uses upright Latin symbols in both comparison maps, the square and all three functor displays; the Delta and 1 superscripts and variable slots are preserved.')
 phrase='is a quasi-isomorphism' if layer=='English' else 'est un quasi-isomorphisme'
 ch(layer,'\\uline{'+phrase+'.}','\\uline{'+phrase+'}.','Corollary 1.2.6.5 conclusion','II.p129.underline-stop','The final period is outside the underline; evidence/I_p129_opening-map.png.')
 old=region(layer);new=old.replace('\\par\n\\noindent ','\n').replace('\n\\par\n','\n')
 ch(layer,old,new,'proof and Scholium prose','II.p129.prose-continuity','The source inserted paragraph breaks at ordinary typewritten wraps, including the standalone par commands within the Scholium opening. The scan has continuous prose at those places; actual headings and displays remain separated.','structure')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','II.p129.boundary','The page ends after the natural augmentation display (***).','structure')
ch('English',r'\text{respectively, }',r'\text{resp. }','opening comparison display','II.p129.resp','The terminology standard retains the printed abbreviation resp.','terminology')
ch('English','We have a commutative square','There is a commutative square','proof opening','II.p129.impersonal-on','The French On a is impersonal; use the prescribed impersonal register.','terminology')
verdict(page,'ILL-SC-20260804-0126','Two punctuation spaces','Both withdrawn','Printed spaces before the period after T and comma after B are harmless; no original error found.',ev)
verdict(page,'ILL-NORM-20260804-0157','Three capitalizations','All withdrawn','Anneaux, Algebres and Modules are printed mathematical conventions, not misprints.',ev)
verdict(page,'ILL-TX-20260804-0153','Eight semantic anchors and native square','All preserved; upright symbols, underline stop, prose continuity and boundary restored','Every node, arrow, superscript, category, variable slot and display label matches the enlarged scan.',ev)
verdict(page,'ILL-TR-20260804-0155','Corollary proof and Scholium','Meaning confirmed; resp. and impersonal on applied','The localized functor (**) and ordinary natural transformation (***) are distinguished correctly; no assertion that differentials themselves preserve every quasi-isomorphism is added.',ev)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('II.1.2.6.5','In the displayed square both vertical augmentations are quasi-isomorphisms by 1.2.5.3 because B and B prime are free degreewise over their respective bases. The top arrow is a quasi-isomorphism by 1.2.6.2 b), so two-out-of-three gives the bottom arrow. For the resp. arrow, Omega(B/A) is free degreewise over B; hence base change along the quasi-isomorphism B->B prime gives a quasi-isomorphism Omega(B/A)->Omega(B/A) tensor_B B prime by Kunneth. Its composite with the resp. arrow is the bottom arrow, and two-out-of-three applies again.'),('II.1.2.6.6.localization','For a quasi-isomorphism C->C prime over B, 1.2.6.2 b) with A fixed gives a quasi-isomorphism L^Delta(C/A) tensor_C C prime -> L^Delta(C prime/A). Both sides are free degreewise as C prime-modules, so their tensor with B computes derived tensor and preserves this quasi-isomorphism. Tensor associativity identifies the result with the map assigned by (*). Thus (*) sends every inverted map to an isomorphism in D.(B), and the universal property of localization gives (**).'),('II.1.2.6.6.augmentation','The augmentation L^Delta(C/A)->Omega(C/A) of 1.2.5.2 is functorial in the A-algebra C. Tensoring it with B through C->B gives (***) naturally on A-Alg/B. The target functor is not asserted here to preserve all quasi-isomorphisms; the localization claim on this page belongs to the source functor in (**).')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p129_*.png')):f.write(f'| evidence/{p.name} | Printed p129, 800-dpi crop inspected during the first reading. |\n')
print('Page 129 edits and three targeted proof checks recorded.')
