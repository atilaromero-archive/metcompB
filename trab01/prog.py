#!/usr/bin/python
#./prog.py dados.dat
import numpy
import pylab
import os

def main(path):
    with open(path)as f:
        vetores=[]
        for line in f:
            y0,x0,xfim,lamb,deltat = [float(x) for x in line.split()]
            xs=gerat(x0,xfim,deltat)
            if len(vetores)==0:
                vetores+=[xs]
            ys=geraexp(xs,y0,lamb,deltat)
            vetores+=[ys]
            #faz as linhas no grafico
            pylab.plot(xs,ys,'o-',label='lambda=%s; delta t=%s'%(lamb,str(deltat)))
            ysreal=geraexpreal(xs,y0,lamb)
            erroabs=numpy.abs(ysreal[-1]-ys[-1])
            errorel=numpy.abs(erroabs/ys[-1])
            print 'y0=%s'%str(y0)
            print 'x0=%s'%str(x0)
            print 'xfim=%s'%str(xfim)
            print 'lamb=%s'%str(lamb)
            print 'deltat=%s'%str(deltat)
            print 'erro absoluto=%s'%str(erroabs)
            print 'erro relativo=%s'%str(errorel)
            print
        vetores+=[ysreal]
        pylab.plot(xs,ysreal,'-',label='exp(lambda*t)')
        pylab.legend()
        pylab.savefig('plot.eps',format='eps')
        print 'grafico salvo em plot.eps'
        pylab.show()
        printvetores(vetores)

def printvetores(vetores):
    for a in zip(*vetores):
        for b in a:
            print b,
        print

def gerat(inicio,fim,deltat):
    return [x for x in numpy.arange(inicio,fim,deltat)]

#funcao que calcula os valores
#f(t+dt) = f(t)(1+kdt)
def geraexp(xs,y0,lamb,deltat):
    k=1+float(lamb)*float(deltat)
    y=[]
    for i in xs:
        y+=[y0] #acumula f(t) em uma lista
        y0*=k   #calcula f(t+dt)
    return y

def geraexpreal(xs,y0,lamb):
    y=[]
    for i in xs:
        y+=[y0*numpy.exp(i*lamb)]
    return y
    
if __name__=="__main__":
    import sys
    main(*sys.argv[1:])  #./prog.py dados.dat (y0,x0,xfim,lamb,deltat)
