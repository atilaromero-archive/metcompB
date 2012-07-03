#!/usr/bin/python
import randi
import sys
import math

if len(sys.argv)==2:
    randi.randi(int(sys.argv[1])) #inicia semente com argumento
else:
    randi.randi(0) #inicia semente com zero

#zera a tabela de posicoes
N=100
tabpos=[0]*N
for passo in range(1000):
    for caminhante in range(N):
        #randi.moeda retorna 1 ou -1
        tabpos[caminhante]+=randi.moeda()
    med=sum(tabpos)/float(N)
    quad=sum([x*x for x in tabpos])/float(N)
    desv=(quad-med**2)**0.5
    if passo!=0:#por causa do log(passo)
        print passo,desv,math.log(passo),math.log(desv)
