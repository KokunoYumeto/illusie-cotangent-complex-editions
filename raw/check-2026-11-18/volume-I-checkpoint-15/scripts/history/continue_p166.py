"""Primary reviewer's page166 audit; run once."""
import sys,csv
from pathlib import Path
from datetime import datetime,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from edit_support import ROOT,LAYERS,edit_page,verdict
page='166';anchor=r'\begin{illusiebodypage}{ILL-CCD:LNM239:CH3:p166}'
ev='LNM239 scan PDF p184 / printed p166: both complete400-dpi halves and eleven800-dpi crops personally inspected; all three complete source regions read in order. '
def region(layer):
 s=(ROOT/'sources'/LAYERS[layer]).read_text();a=s.index(anchor);b=s.index(r'\end{illusiebodypage}',a);return s[a:b]
def ch(layer,old,new,line,sid,why,kind='typesetting'):edit_page(layer,anchor,old,new,page,line,sid,ev+why,kind)
old=region('corrected');new=old.replace('$(*).$','$(*)$ .').replace('$M$.','$M$ .')
ch('corrected',old,new,'inverse identities prose','III.p166.withdraw-punctuation-normalizations','Withdraw three optional punctuation-space normalizations, including the two moves of the sentence period into the mathematical reference. Retain the necessary missing-star correction.','reading')
bar=r'\mathrel{\overset{\sim}{\rule[.45ex]{14bp}{.35bp}}}';ext=r'\mathop{\mathbb E\mathrm{xt}}\nolimits'
for layer in LAYERS:
 ch(layer,r'\ReflowBodyFont ',r'\ReflowBodyFont\IllusieUprightLatinMath','page mathematics','III.p166.upright-Latin','Restore upright printed Latin mathematics.')
 old=region(layer);counts={c:old.count('\\mathcal '+c) for c in 'XYZ'}
 new=old
 for c in 'XYZ':new=new.replace('\\mathcal '+c,c)
 ch(layer,old,new,'extension names','III.p166.plain-extension-names','Restore plain printed extension names: '+str(counts)+'.')
 old=region(layer);assert old.count('*P')==5
 ch(layer,old,old.replace('*P','*p'),'five pullbacks in the inverse calculations','III.p166.augmentation-p','All five pullbacks print lowercase p, the augmentation P->B; supplied uppercase P is a shared transcription error. Restore p in all layers.','reading')
 old=region(layer);assert old.count(r'\operatorname{Ext}')==3
 ch(layer,old,old.replace(r'\operatorname{Ext}',ext),'three hyper-Ext classes','III.p166.hyperExt-letterforms','Each of the three printed Ext initials is double-stroked.')
 old=region(layer);assert old.count(r'\xrightarrow{\sim}')==3
 ch(layer,old,old.replace(r'\xrightarrow{\sim}',bar),'three comparison signs','III.p166.unheaded-isomorphisms','All three comparison signs are unheaded bars with tildes; the beta-map arrow remains headed.')
 old=region(layer);new=old.replace(' . On\\par\n\n\n\\phantomsection',' . On\n\\phantomsection').replace(r'\noindent a par définition',r'a par définition')
 if layer=='English':
  new=new.replace('$(*).$\\par\n\n\n\\phantomsection','$(*)$.\n\\phantomsection').replace(r'\noindent By definition,',r'By definition,')
  new=new.replace('$(*).$','$(*)$.')
 new+=r'\clearpage'+'\n'
 ch(layer,old,new,'last prose clause and boundary','III.p166.prose-flow','Rejoin the artificial paragraph break in the last sentence across its preserved anchor; keep English sentence periods outside the mathematical reference. Preserve all seven carriers and twelve displayed rows and the printed page boundary.','structure')
old=region('English');new=old.replace(", we have\\par",", one has\\par").replace('We thus define a map','One thus defines a map').replace('We shall show that','It will be shown that').replace('We have, in','One has, in')
ch('English',old,new,'four impersonal clauses','III.p166.impersonal-on','Preserve impersonal on in all four corresponding clauses; keep notre assertion as our assertion.','translation')
verdict(page,'SUPPLIED-SOURCE-DIFF:I:p166','Missing pushout star on the right of the final H_0 comparison; spaced prose punctuation','Star supplied through the native macro argument; three optional punctuation changes','Local source-comparison verdict, not a supplied record ID. Confirm the missing-star repair: H_0s-double-prime inverse is a kernel map acting on an extension, so the omitted pushout operator is necessary and is explicit in the preceding two comparisons. Retain omission in diplomatic. Withdraw optional punctuation changes. Newly restore all five printed lowercase pullback p occurrences in all layers, plain names, double-stroked Ext initials, unheaded comparison bars and prose flow.',ev+'evidence/I_p166_final-comparison.png; evidence/I_p166_comparison-doubleprime.png; evidence/I_p166_beta-alpha.png; evidence/I_p166_alpha-beta1.png; evidence/I_p166_alpha-beta2.png.')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC');who='GPT-6 Astra Pro; effort not exposed; ILLUSIE continuation 2026-11-19'
events=[('III.1.2.3.proof.H0-independence-conclusion','The displayed equality H_0t-prime H_0s-prime=H_0t-double-prime H_0s-double-prime follows from homotopy invariance. Taking inverses gives H_0s-prime inverse H_0t-prime inverse=H_0s-double-prime inverse H_0t-double-prime inverse. Applying the common composite to H_0alg(Z) by pushout gives the final extension isomorphism. This verifies the order of the four inverse maps and explains why the final missing star is an actual omission, not ordinary map composition.'),('III.1.2.3.proof.beta-alpha','For alpha(X)=chi diff(X*p), the representative used to define beta can be chosen with s=id_M and Y=diff(X*p). The equivalence1.1.9 identifies alg diff(X*p) with X*p. There is a natural map H_0(X*p)->X*H_0p inducing the identity on the constant kernel M and on H_0P; H_1P=0 gives short exactness, hence it is an isomorphism. Pulling back along (H_0p)^(-1) then returns X. Thus all four rows are valid, proving beta alpha=id. All three X*p factors are lowercase augmentation pullbacks.'),('III.1.2.3.proof.alpha-beta-reduction','Insert beta(y) into alpha by pulling the ordinary algebra extension back along p:P->B and applying chi diff. Kernel pushout by (H_0s)^(-1) commutes with this pullback and with diff. The connecting-class identity chi(t*Y)=(sigma t)chi(Y), I3.2.3.3 (directly rechecked on77 for164), moves this kernel map outside chi as sigma H_0s inverse. This gives exactly the second displayed row, with the two trailing lowercase p pullbacks. It verifies only the reduction on166; completion of alpha beta=id remains on167.')]
with (ROOT/'CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n')
 for sid,outcome in events:w.writerow([sid,now,who,'targeted proof check',outcome])
with (ROOT/'EVIDENCE_INDEX.md').open('a') as f:
 for p in sorted((ROOT/'evidence').glob('I_p166_*.png')):f.write(f'| evidence/{p.name} | Page166 audit:800-dpi crop personally inspected. |\n')
q=ROOT/'READING_QUESTIONS.tsv'
with q.open(newline='') as f:rows=list(csv.reader(f,delimiter='\t'))
for row in rows[1:]:
 if row[0]=='I-Q008':row[1]+=';166';row[4]+=' All three hyper-Ext initials on166 directly confirmed.';row[6]+='; evidence/I_p166_beta-map.png; evidence/I_p166_inverse-goal.png; evidence/I_p166_alpha-beta-lead.png'
with q.open('w',newline='') as f:csv.writer(f,delimiter='\t',lineterminator='\n').writerows(rows)
print('Page166 repairs, verdict and three checks recorded.')
