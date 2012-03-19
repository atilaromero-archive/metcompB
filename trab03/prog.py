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
    pylab.show()

#funcao que calcula os valores
def geraexp(ninicial,inicio,fim,lamb,deltat):
    k=1+float(lamb)*float(deltat)
    x=[]
    y=[]
    ninicial=float(ninicial)
    for i in numpy.arange(float(inicio),float(fim),float(deltat)):
        x+=[i] #acumula os valores de t em uma lista
        y+=[ninicial] #acumula f(t) em uma lista
        ninicial*=k   #calcula f(t+dt)
    return [x,y]

if __name__=="__main__":
    import sys
    main(*sys.argv[1:])  #./prog.py ninicial inicio fim lamb 
