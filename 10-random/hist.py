#!/usr/bin/python
import random
import sys

def pseudoaleatorio(x,n):
    a=1029.0
    b=221591.0
    c=1048576.0
    for i in range(n):
        xold=x
        x=(a*x+b)%c
        #print i,x/c
        print xold/c,x/c
    
if len(sys.argv)!=6:
    print 'argumentos: arq col minimo maximo numbarras'
    sys.exit(1)

arq=sys.argv[1]
col=int(sys.argv[2])
minimo=float(sys.argv[3])
maximo=float(sys.argv[4])
numbarras=int(sys.argv[5])
fator=(maximo-minimo)/numbarras
with open(arq) as f:
    result=[0]*numbarras
    for line in f.readlines():
        nums=line.split()  
        h=float(nums[col])  #nums[col] -> numero na coluna 'col' da linha
        assert (h>=minimo)
        assert (h<maximo)
        h=(h-minimo)/fator
        h=int(h)
        assert (h>=0)&(h<numbarras)
        result[h]+=1
    for x in range(len(result)):
        print x*fator+minimo,result[x]
        print x*fator+minimo+fator,result[x]
