#!/usr/bin/python
import numpy
import pylab

def main(A,B,x0,xf,la,lb,dt):
    xs=numpy.arange(x0,xf+dt/2,dt)
    As=[]
    Bs=[]
    for i in xs:
        As+=[A]
        Bs+=[B]
        B+= (A*la-B*lb)*dt
        A+= ((-A)*la)*dt
    pylab.plot(xs,As,'+-',label='A')
    pylab.plot(xs,Bs,'+-',label='B')
    pylab.legend()
    pylab.show()

if __name__=='__main__':
    import sys
    main(*[float(x) for x in sys.argv[1:]]) #main(A,B,x0,xf,la,lb,dt)

