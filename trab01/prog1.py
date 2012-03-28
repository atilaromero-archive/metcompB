#!/usr/bin/python
#./prog.py dados.dat
import numpy
import pylab
import os

def main(path):
    with open(path)as f:
        for line in f:
            y0,x0,xfim,lamb,deltat = [float(x) for x in line.split()]
            xs=gerat(x0,xfim,deltat)#monta os valores do eixo x
            ys=geraexp(xs,y0,lamb,deltat)#calcula os valores de exp(lambda*t)
            ysreal=geraexpreal(xs,y0,lamb)
            errorel=[numpy.abs((a-b)/b) for (a,b) in zip(ys, ysreal)]#lista de erros relativos
            #faz as linhas no grafico
            pylab.plot(xs,errorel,'+-')
        #xs=gerat(x0,xfim,deltat/10)#calcula exp(lambda*t) em intervalos de deltat/10
        #ysreal=geraexpreal(xs,y0,lamb)#idem
        #pylab.plot(xs,ysreal,'-',label='exp(lambda*t)')#plota valor teorico
        pylab.xlabel('tempo')
        pylab.ylabel('Erro relativo')
        #pylab.legend(loc=9)#inclui a legenda, loc=9 poe a legenda em cima no centro
        fig=path+'.eps'
        #pylab.savefig(fig,format='eps')
        #print 'grafico salvo em '+fig
        pylab.show()#mostra o grafico

#gera os valores de x, com intervalos de deltat
def gerat(inicio,fim,deltat):
    return [x for x in numpy.arange(inicio,fim+deltat/2,deltat)]

#funcao que calcula os valores
#f(t+dt) = f(t)(1+kdt)
def geraexp(xs,y0,lamb,deltat):
    k=1+float(lamb)*float(deltat)
    y=[]
    for i in xs:
        y+=[y0] #acumula f(t) em uma lista
        y0*=k   #calcula f(t+dt)
    return y #retorna a lista que contem todos os valores de y

def geraexpreal(xs,y0,lamb):
    y=[]
    for i in xs:
        y+=[y0*numpy.exp(i*lamb)]
    return y
    
if __name__=="__main__":
    import sys
    main(*sys.argv[1:])  #./prog.py dados.dat (y0,x0,xfim,lamb,deltat)
