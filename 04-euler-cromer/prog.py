#!/usr/bin/python
import numpy
import pylab
#./prog.py 1 1 1 0 0 300 0.01

def main(k,m,x,v,t0,tf,dt):
    xs=numpy.arange(t0,tf+dt/2,dt)
    w2=k/m
    ys1=[]
    ys2=[]
    es1=[]
    es2=[]
    x1=x
    x2=x
    v1=v
    v2=v
    for i in xs:
        #euler
        vtemp=v1
        v1=v1-w2*x1*dt
        x1=x1+vtemp*dt
        e1=(k*x1**2+m*v1**2)/2
        ys1+=[x1]
        es1+=[e1]
        #euler-cromer
        v2=v2-w2*x2*dt
        x2=x2+v2*dt
        e2=(k*x2**2+m*v2**2)/2
        ys2+=[x2]
        es2+=[e2]
    pylab.plot(xs,ys1,'-',label='x(t) - Euler')
    pylab.plot(xs,es1,'-',label='E(t) - Euler')
    pylab.plot(xs,ys2,'-',label='x(t) - Euler-Cromer')
    pylab.plot(xs,es2,'-',label='E(t) - Euler-Cromer')
    pylab.xlabel('t')
    pylab.ylabel('x')
    pylab.legend(loc=2)
    pylab.show()
    for x,y1,e1,y2,e2 in zip(xs,ys1,es1,ys2,es2):
        print x, y1, e1, y2, e2

if __name__=='__main__':
    import sys
    main(*[float(x) for x in sys.argv[1:]]) #(k,m,x,v,t0,tf,dt)


