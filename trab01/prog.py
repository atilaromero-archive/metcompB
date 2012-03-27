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
            ys=geraexp(xs,y0,lamb,deltat)#calcula os valores do eixo y
            #faz as linhas no grafico
            pylab.plot(xs,ys,'o-',label='$\lambda$=%s; delta t=%s'%(lamb,str(deltat)))
            ysreal=geraexpreal(xs,y0,lamb)
            erroabs=numpy.abs(ysreal[-1]-ys[-1])
            errorel=numpy.abs(erroabs/ys[-1])
            print 'y0=%s'%str(y0)
            print 'x0=%s'%str(x0)
            print 'xfim=%s'%str(xfim)
            print 'lamb=%s'%str(lamb)
            print 'deltat=%s'%str(deltat)
            print 'ultimo (x,ycalculado,yreal)=(%f,%f,%f)'%(xs[-1],ys[-1],ysreal[-1])
            print 'erro absoluto=%s'%str(erroabs)
            print 'erro relativo=%s'%str(errorel)
            print
        xs=gerat(x0,xfim,deltat/10)#calcula exp(lambda*t) em intervalos de deltat/10
        ysreal=geraexpreal(xs,y0,lamb)#idem
        pylab.plot(xs,ysreal,'-',label='$e^{\lambda t}$')#plota valor teorico
        pylab.xlabel('tempo')
        pylab.ylabel('$e^{\lambda t}$',fontsize='large')
        pylab.legend(loc=9)#inclui a legenda, loc=9 poe a legenda em cima no centro
        #fig=path+'.eps'
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
