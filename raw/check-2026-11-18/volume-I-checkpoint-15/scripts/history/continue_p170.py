"""Primary reviewer's page170 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='170';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p170}'
ev='LNM239 scan PDF p188 / printed p170: both complete400-dpi halves and twelve800-dpi crops personally inspected; relation and final-sentence crops were expanded/replaced and reinspected after incomplete initial captures. All three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
ch('corrected','Q-module','Q-Module','square lead','III.p170.withdraw-capitalization','Withdraw the optional capitalization normalization. evidence/I_p170_base-change.png.','reading')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p170.upright-Latin','Restore upright printed Latin mathematics.')
 ch(layer,r'\operatorname{Hom}_Q(',r'\operatorname{Hom}(','square upper left','III.p170.unprinted-Hom-subscript','The printed Hom has no Q subscript. Its module category is clear from context. Ordinary Ext_Q on the right retains its plain E and printed subscript. evidence/I_p170_square-top.png.','reading')
 ch(layer,r'd^1_{P/A}',r'd_{P/A}','final relation','III.p170.unprinted-derivation-exponent','The print has d_P/A without a superscript1. Restore its actual notation in all layers. evidence/I_p170_relation.png.','reading')
 ch(layer,r'\binom{f}{-u}',r'\left(\begin{array}{r}f\\[8bp]-u\end{array}\right)','B-extension arrow label','III.p170.two-row-map-label','Restore the tall parenthesized two-row label with the minus sign to the left of u and letter alignment; retain the sign and map components. evidence/I_p170_extension-arrows.png.')
 ch(layer,r'\node at (216,-2) {$.$};',r'\node[anchor=base] at ([xshift=76bp]B.base) {$.$};','extension diagram period','III.p170.diagram-period','Put the period on the baseline of the lower B, as printed.')
 old=region(layer);new=old
 for name,x,y in [('TL',0,82),('TR',170,82),('BL',0,9),('BR',170,9)]:
  ox=48 if name in ('TL','BL') else 190
  new=new.replace(f'\\node ({name}) at ({ox},{y})',f'\\node[anchor=west] ({name}) at ({x},{y})')
 new=new.replace(r'(TL) -- (BL);',r'([xshift=30bp]TL.south west) -- ([xshift=30bp]BL.north west);')
 new=new.replace(r'(TR) -- node[right=17bp] {$\operatorname{alg}$} (BR);',r'([xshift=31bp]TR.south west) -- node[right=8bp] {$\operatorname{alg}$} ([xshift=31bp]BR.north west);')
 new=new.replace(r'\node at (259,4) {$,$};',r'\node[anchor=base] at ([xshift=35bp]BR.base east) {$,$};')
 ch(layer,old,new,'compatibility square','III.p170.square-alignment','Restore aligned left edges of upper/lower expressions, vertical arrows at the printed operator/argument junction, alg beside the right arrow, and the comma on the lower formula baseline. All four arrows and labels retained. evidence/I_p170_square-top.png; evidence/I_p170_square-arrows.png; evidence/I_p170_square-bottom.png.')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p170.page-boundary','Preserve the printed page boundary.','structure')
ch('English','We thus have','One thus has','proof opening','III.p170.impersonal-on-opening','French On a is impersonal.','translation')
ch('English','we may reduce to assuming','one may reduce to assuming','functorial reduction','III.p170.impersonal-on-reduction','French on peut is impersonal.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p170','Q-Module','Q-module','Withdraw the optional capitalization. No original mathematical error identified. Restore two unprinted additions (Hom subscriptQ and d exponent1), upright Latin mathematics, tall signed two-row label, diagram alignment/punctuation and page boundary; retain ordinary Ext and the negative derivation in the B-algebra structure.',ev+'evidence/I_p170_base-change.png; evidence/I_p170_square-top.png; evidence/I_p170_relation.png; evidence/I_p170_extension-arrows.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.5.4.B-extension','targeted proof check','For an A-derivation u:B->M with C-module structure through f, (f,-u):B->C plus M is an A-algebra morphism: -u(bb-prime)=f(b)(-u(b-prime))+f(b-prime)(-u(b)). Its composite with the projection is f. Thus the displayed split A-extension, supplied with this B-structure, is a B-extension of C by M. The negative sign is mathematically coherent and printed.'),('III.1.2.5.4.relation-star-star','targeted proof check','Write K=Omega^1_P/A tensor_P Q and i:K->Omega^1_Q/A for the injection in(*). By the definition of alg, personally reinspected on159, alg(*)={(q,eta):eta maps to d_Q/P(q)}. The map Q plus K -> alg(*) given by (q,m) |-> (q,d_Q/A(q)+i(m)) is a ring isomorphism: derivation gives multiplicativity, exactness gives its unique inverse, and it is the identity on kernel K and quotient Q. The P-structure (p,0) of alg(*) corresponds to (p,-d_P/A(p) tensor1). Therefore it is precisely the extension defining partial(d_P/A tensor1). This verifies(**) and its sign directly. Naturality under coefficient pushout reduces the general square to this identity case, giving the compatibility. The deferred author proof on later pages has not yet been read.'),('III.1.2.5.4.reference-and-base-change','used and rechecked in this run','Personally reinspected II2.1.1.3 on133: the displayed exact sequence of differentials is the one used here, with Q=P_P^Delta(C). The quotient is degreewise locally free for the standard free resolution, so extension of scalars to C preserves exactness degreewise. The associated triangle is1.2.5.2. All Omega bases and scalar-extension subscripts on170 agree with that construction.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p170_*.png')):f.write(f'| evidence/{p.name} | Page170 audit: final800-dpi crop personally inspected. |\n')
 f.write('| evidence/I_p133_exact-sequence.png; evidence/I_p159_Y-prime.png; evidence/I_p159_alg-pullback.png | Personally reinspected for170: differential exact sequence and alg definition. |\n')
print('Page170 repairs, verdict and three checks recorded.')
