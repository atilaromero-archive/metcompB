#!/usr/bin/python
# usar: python trab.py dados.txt
# ou    ./trab.py dados.txt

def ordena(lista1):
    lista=lista1[:]
    troca=True
    passos=0
    while(troca):
        troca=False
        for i in range(len(lista)-1):
            passos+=1
            if lista[i]>lista[i+1]:
                lista.insert(i,lista.pop(i+1))
                troca=True
    return (lista,passos)

def ordena2(lista1):
    lista=lista1[:]
    troca=True
    passos=0
    lasttroca=(len(lista)-1)
    while(troca):
        troca=False
        for i in range(lasttroca):
            passos+=1
            if lista[i]>lista[i+1]:
                lista.insert(i,lista.pop(i+1))
                troca=True
                lasttroca=i
    return (lista,passos)
        
def main(arquivo):
    with open(arquivo) as f:
        lines=f.readlines()
    numeros=[float(x) for x in lines]
    ord1=ordena(numeros)
    print 'ordena1',ord1[1]
    for x in ord1[0]:
        print x
    ord2=ordena2(numeros)
    print 'ordena2',ord2[1]
    for x in ord2[0]:
        print x
    
if __name__=="__main__":
    import sys
    main(*sys.argv[1:])
