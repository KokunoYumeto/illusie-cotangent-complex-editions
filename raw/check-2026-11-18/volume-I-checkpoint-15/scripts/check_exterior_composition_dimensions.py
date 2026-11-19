"""Exact finite Dold-Kan dimension check for the p99 composition example.

Take L=M=k, a field, and X=k[1] direct-sum k[-1]. For a mixed
vector space, split Dold-Kan decompositions give the double binomial
inversion below. The input dimension polynomials have total degree <=4,
so their coefficients outside p+q<=4 vanish identically. This computes
terms, not differentials or homology, and uses no external edition.
"""
from math import comb
import json

def choose2(n):
    return n*(n-1)//2

def coefficient(f,p,q):
    return sum((-1)**(p+q-i-j)*comb(p,i)*comb(q,j)*f(i,j)
               for i in range(p+1) for j in range(q+1))

def first(p,q):
    return choose2(p+q)

def direct_composite(p,q):
    return choose2(choose2(p+q))

def iterated_extension(p,q):
    return choose2(1+choose2(p)+choose2(q))

functions={'F(X)':first,'(GF)(X)':direct_composite,
           'G(F(X))':iterated_extension}
result={}
for name,f in functions.items():
    entries=[{'p':p,'q':q,'dimension':coefficient(f,p,q)}
             for p in range(5) for q in range(5)
             if coefficient(f,p,q)]
    assert all(e['dimension']>0 and e['p']+e['q']<=4 for e in entries)
    diagonal=[coefficient(f,n,n) for n in range(3)]
    result[name]={'nonzero_normalized_terms':entries,
                  'degree_zero_diagonal':diagonal,
                  'degree_zero_dimension':sum(diagonal)}
assert result['F(X)']['nonzero_normalized_terms']==[
    {'p':0,'q':2,'dimension':1},
    {'p':1,'q':1,'dimension':1},
    {'p':2,'q':0,'dimension':1}]
assert result['(GF)(X)']['degree_zero_dimension']==3
assert result['G(F(X))']['degree_zero_dimension']==1
print(json.dumps(result,indent=2))
