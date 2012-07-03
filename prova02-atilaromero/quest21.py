#!/usr/bin/python
import randi
import sys

if len(sys.argv)==2:
    randi.randi(int(sys.argv[1])) #inicia semente com argumento
else:
    randi.randi(0) #inicia semente com zero

#zera a tabela de posicoes
tabpos=[0,0,0,0,0,0]
for passo in range(1000):
    for caminhante in range(6):
        #randi.moeda retorna 1 ou -1
        tabpos[caminhante]+=randi.moeda()
    #imprime o passo e a tab de posicoes
    print passo,' '.join([str(x) for x in tabpos])
