#!/usr/bin/python
#./prog.py 2 0 10 0.3
import numpy
import pylab

def main(ninicial,inicio,fim,lamb):
    for deltat in [1,0.1,0.5]: #tres deltas t escolhidos
        x,y=geraexp(ninicial,inicio,fim,lamb,deltat)
        #faz as tres linhas no grafico
        pylab.plot(x,y,'o-',label='lambda=%s; delta t=%s'%(lamb,str(deltat)))
    pylab.legend()
    pylab.savefig('plot2.eps',format='eps')
    pylab.show()

#funcao que calcula os valores
#f(t+dt)=f(t)+kt**2dt
def geraexp(ninicial,inicio,fim,lamb,deltat):
    x=[]
    y=[]
    ninicial=float(ninicial)
    for i in numpy.arange(float(inicio),float(fim),float(deltat)):
        k=float(lamb)*float(deltat)*i**2
        x+=[i] #acumula os valores de t em uma lista
        y+=[ninicial] #acumula f(t) em uma lista
        ninicial+=k   #calcula f(t+dt)
    return [x,y]

if __name__=="__main__":
    import sys
    main(*sys.argv[1:])  #./prog.py ninicial inicio fim lamb 
