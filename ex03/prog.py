#!/usr/bin/python
#./prog.py 2 0 10 0.3
import numpy
import pylab

def main(ninicial,inicio,fim,lamb,delta=None):
    if delta==None:
        delta=[0.1]
    else:
        delta=[delta]
    vetores=[]
    for deltat in delta:
        xs=gerat(inicio,fim,deltat)
        if len(vetores)==0:
            vetores+=[xs]
        ys=geraexp(xs,ninicial,lamb,deltat)
        vetores+=[ys]
        #faz as linhas no grafico
        pylab.plot(xs,ys,'o-',label='lambda=%s; delta t=%s'%(lamb,str(deltat)))
    ys=geraexpreal(xs,ninicial,lamb)
    vetores+=[ys]
    pylab.plot(xs,ys,'o-',label='exp(lambda*t)')
    pylab.legend()
    pylab.savefig('plot.eps',format='eps')
    pylab.show()
    for a in zip(*vetores):
        for b in a:
            print b,
        print

def gerat(inicio,fim,deltat):
    return [x for x in numpy.arange(inicio,fim,deltat)]

#funcao que calcula os valores
#f(t+dt) = f(t)(1+kdt)
def geraexp(xs,ninicial,lamb,deltat):
    k=1+float(lamb)*float(deltat)
    y=[]
    for i in xs:
        y+=[ninicial] #acumula f(t) em uma lista
        ninicial*=k   #calcula f(t+dt)
    return y

def geraexpreal(xs,ninicial,lamb):
    y=[]
    for i in xs:
        y+=[ninicial*numpy.exp(i*lamb)]
    return y
    

if __name__=="__main__":
    import sys
    main(*[float(x) for x in sys.argv[1:]])  #./prog.py ninicial inicio fim lamb 
