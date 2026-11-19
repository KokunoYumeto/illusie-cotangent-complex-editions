"""Primary reviewer's page181 audit; run once."""
import sys,csv,re
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='181';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p181}'
ev='LNM239 scan PDF p199 / printed p181: both complete400-dpi halves and twelve800-dpi crops personally inspected; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
ch('corrected',"l'idéal de", "l'Idéal de",'proof line3','III.p181.withdraw-capitalization','Withdraw optional capitalization normalization. evidence/I_p181_factorization.png.','reading')
for layer in ['corrected','English']:
 pairs=[(r'$A$,',r'$A$\hspace{3.0bp},'),(r'$P\otimes_A Q$,',r'$P\otimes_A Q$\hspace{3.0bp},'),(r'$P$.',r'$P$\hspace{3.0bp}.')]
 # Each occurrence is separately recorded, with unique surrounding replay context.
 for old,new in pairs:ch(layer,old,new,'prose punctuation','III.p181.punctuation-spacing','Restore the printed formula punctuation spacing; no mathematical normalization. evidence/I_p181_hypotheses.png; evidence/I_p181_factorization.png.','reading' if layer=='corrected' else 'typesetting')
 text=region(layer);old=r'$P$,';new=r'$P$\hspace{3.0bp},'
 ch(layer,text,text.replace(old,new),'proof punctuation','III.p181.P-punctuation-spacing','Restore the printed spacing after P in the factorization and differential-sequence prose, and the diplomatic flatness sentence before its necessary base correction. evidence/I_p181_factorization.png; evidence/I_p181_differentials-intro.png; evidence/I_p181_flatness.png.','reading' if layer=='corrected' else 'typesetting')
 old=r'$\otimes_Q B$,' if layer=='corrected' else r'$-\otimes_Q B$,'
 ch(layer,old,r'$\otimes_Q B$\hspace{3.0bp},','flatness sentence','III.p181.tensor-functor','Restore the printed spacing and, in English, remove the added argument placeholder so the formula matches corrected French. evidence/I_p181_flatness.png.','reading' if layer=='corrected' else 'typesetting')
 if layer=='English':ch(layer,r'is flat over $Q$,',r'is flat over $Q$\hspace{3.0bp},','flatness sentence','III.p181.Q-punctuation-spacing','Align formula punctuation spacing with the corrected French; retain the necessary Q base. evidence/I_p181_flatness.png.')
 for macro,mark in [('StarSequence','.'),('DifferentialsSequence',';'),('DoubleStarSequence','.'),('ExactSequencesDiagram','.'),('ComplexSequence',',')]:
  ch(layer,r'\IllusieProposition'+macro+'POneEightyOne{'+mark+'}',r'\IllusieProposition'+macro+r'POneEightyOne{\hspace{3.0bp}'+mark+'}','display punctuation','III.p181.display-punctuation','Restore printed terminal punctuation spacing without changing its mark. evidence/I_p181_star.png; evidence/I_p181_differentials-sequence.png; evidence/I_p181_double-star.png; evidence/I_p181_diagram.png; evidence/I_p181_complex-sequence.png.','reading' if layer=='corrected' else 'typesetting')
ch('corrected',r'comme $\Omega^1_{Q/P}$ est plat sur $P$',r'comme $\Omega^1_{Q/P}$ est plat sur $Q$','flatness sentence','III.1.3.4.flatness-base','The print unmistakably says P. Tensoring the Q-module sequence over Q requires Q-flatness, supplied by Q being almost free over P. P-flatness is true but does not justify this inference. Preserve P diplomatically; make the necessary proof-base correction here and confirm the supplied English Q. evidence/I_p181_flatness.png.','misprint of the original')
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','body mathematics','III.p181.upright-Latin','Restore upright printed Latin mathematics.')
 if layer=='English':old=r'\uline{Then the}\par'+'\n\n'+r'\noindent \uline{canonical map}';new=r'\uline{Then the canonical map}'
 else:old=r'\uline{Alors la flèche}\par'+'\n\n'+r'\noindent \uline{canonique}';new=r'\uline{Alors la flèche canonique}'
 ch(layer,old,new,'proposition hypothesis','III.p181.false-hypothesis-paragraph','Restore a continuous underlined phrase at the printed line wrap. evidence/I_p181_hypotheses.png.','structure')
 if layer=='English':pairs=[('almost free \n\nover','almost free\nover'),('for the \n\nideal','for the\nideal')]
 else:pairs=[('qui est \n\npresque','qui est\npresque'),('Notant $I$ \n\n(resp.','Notant $I$\n(resp.')]
 for old,new in pairs:ch(layer,old,new,'proof opening','III.p181.false-proof-paragraph','Remove a false paragraph at a printed line wrap without changing the wording. evidence/I_p181_factorization.png.','structure')
 ch(layer,r'\par'+'\n\n'+r'\vspace{2.4bp}'+'\n'+r'\noindent ','\n','flatness sentence','III.p181.false-flatness-paragraph','Restore continuous prose before the exact sequence. evidence/I_p181_flatness.png.','structure')
 text=region(layer);a=text.index(r'\providecommand{\IllusiePropositionExactSequencesDiagramPOneEightyOne}');b=text.index('\n}',a)+2;old=text[a:b];new=old
 for node in ['toplabel','topleftzero','topthree','toprightzero','bottomlabel','bottomleftzero','bottomthree','bottomrightzero']:
  new=new.replace(r'\node ('+node+')',r'\node[anchor=base] ('+node+')')
 for node,x,y in [('topone',84,100),('toptwo',174,100),('bottomone',84,0),('bottomtwo',174,0)]:
  new=re.sub(r'\\node \('+node+r'\) at \([^)]*\)',r'\\node[anchor=base west] ('+node+f') at ({x},{y})',new)
 for left,right in [('topleftzero','topone'),('topone','toptwo'),('toptwo','topthree'),('topthree','toprightzero'),('bottomleftzero','bottomone'),('bottomone','bottomtwo'),('bottomtwo','bottomthree'),('bottomthree','bottomrightzero')]:
  new=new.replace('([xshift=4bp]'+left+'.east) -- ([xshift=-4bp]'+right+'.west)', '([xshift=4bp,yshift=3bp]'+left+'.base east) -- ([xshift=-4bp,yshift=3bp]'+right+'.base west)')
 for node,x in [('one',90),('two',180),('three',290)]:
  new=new.replace('([yshift=-5bp]top'+node+'.south)',f'({x},88)').replace('([yshift=5bp]bottom'+node+'.north)',f'({x},15)')
 new=new.replace(r'\node[anchor=west] at (389,0) {#1};',r'\node[anchor=base] at ([xshift=18bp]bottomrightzero.base east) {#1};')
 assert old.count(r'\draw[->]')==new.count(r'\draw[->]')==11
 ch(layer,old,new,'two-row differential diagram','III.p181.diagram-alignment','Restore the printed baseline-aligned rows, left alignment of each conormal/differential pair, vertical differential arrows and final period baseline. Preserve all eleven edges and all three labels. evidence/I_p181_diagram.png.')
 old=region(layer);ch(layer,old,old+r'\clearpage'+'\n','page boundary','III.p181.page-boundary','Preserve the printed page boundary.','structure')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p181','Idéal and twelve punctuation spaces','Lowercase idéal and omitted spaces','Withdraw optional capitalization and punctuation normalization; preserve all four exact sequences and the identity-complex notation.',ev+'evidence/I_p181_factorization.png; evidence/I_p181_star.png; evidence/I_p181_differentials-sequence.png; evidence/I_p181_double-star.png; evidence/I_p181_diagram.png; evidence/I_p181_complex-sequence.png.')
verdict(page,'SUPPLIED-ENGLISH-REPAIR:I:p181-flatness','Omega1_Q/P flat over P','French retained P; English already had Q','Confirm supplied English Q as the necessary base for the tensor exactness argument; bring corrected French into agreement. Diplomatic P retained.',ev+'evidence/I_p181_flatness.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.3.4.factorization','targeted proof check','Let R=P tensor_A Q, augmented to B by p tensor q. Both inclusions P->R and Q->R are almost-free algebra maps, by base change of the respective almost-free A-algebras. The special case proved on this page makes both induced complex maps quasi-isomorphisms. The multiplication/evaluation map R->Q induced by P->Q and id_Q is a retraction of Q->R; its complex map is therefore a quasi-isomorphism by two-out-of-three. Composing P->R->Q proves the desired arbitrary compatible comparison. This supplies the implicit use of the second inclusion in the printed reduction.'),('III.1.3.4.exactness-and-flatness','targeted proof check','The top row is1.3.3.1 with base P and almost-free algebra Q. For a polynomial Q, the differential sequence over A is split exact on its relative generators and Omega1_Q/P is free over Q. Local filtered passage gives the same left exactness and Q-flatness for almost-free Q. Equivalently Q=Sym_P(N) with N flat gives Omega1_Q/P=Q tensor_P N, flat over Q. Thus Tor1_Q(Omega1_Q/P,B)=0, and tensoring gives(**). The printed P-flatness is weaker and insufficient for this Q-tensor argument; necessary correction P->Q, already present in English. Personally reinspected the free hypothesis and1.1.2.13 on117; its previously checked final-term correction from C/A to C/B remains required.'),('III.1.3.4.diagram-and-conclusion','targeted proof check','For x in I, both paths around the left square give d_Q/A(x) tensor1. For y in J, projection of d_Q/A(y) to relative Q/P differentials is d_Q/P(y), the upper quotient map, so the right square commutes with identity at the right. Both rows are short exact; hence the induced map of two-term complexes is termwise injective with quotient [Omega1_Q/P tensor_Q B --id--> Omega1_Q/P tensor_Q B] in degrees-1,0. The quotient is contractible by the identity homotopy, so the canonical map is a quasi-isomorphism.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,kind,outcome in events:w.writerow([sid,now,who,kind,outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p181_*.png')):f.write(f'| evidence/{p.name} | Page181 audit:800-dpi crop personally inspected. |\n')
 f.write('| evidence/I_p117_free-hypothesis.png; evidence/I_p117_free-sequence.png | Personally reinspected for181: free-algebra differential sequence and its hypotheses. |\n')
print('Page181 repairs, two verdicts and three targeted checks recorded.')
