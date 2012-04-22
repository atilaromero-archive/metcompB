#!/usr/bin/python
import numpy
import pylab
#./prog.py 1 1 1 0 0 300 0.01

def main(k,m,x,v,t0,tf,dt):
    xs=numpy.arange(t0,tf+dt/2,dt)
    w2=k/m
    a=w2
    ys1=[]
    ys2=[]
    ys3=[]
    es1=[]
    es2=[]
    es3=[]
    x1=x
    x2=x
    x3=x
    v1=v
    v2=v
    v3=v
    xold=x-v*dt
    for i in xs:
        #euler
        e1=(k*x1**2+m*v1**2)/2
        ys1+=[x1]
        es1+=[e1]
        vtemp=v1
        v1=v1-w2*x1*dt
        x1=x1+vtemp*dt
        #euler-cromer
        e2=(k*x2**2+m*v2**2)/2
        ys2+=[x2]
        es2+=[e2]
        v2=v2-w2*x2*dt
        x2=x2+v2*dt
        #verlet
        xnew=2*x3-xold-w2*x3*dt*dt
        v3=(xnew-xold)/(2*dt)
        e3=(k*x3**2+m*v3**2)/2
        ys3+=[x3]
        es3+=[e3]
        xold=x3
        x3=xnew
    pylab.plot(xs,ys1,'-',label='x(t) - Euler')
    pylab.plot(xs,es1,'-',label='E(t) - Euler')
    pylab.plot(xs,ys2,'-',label='x(t) - Euler-Cromer')
    pylab.plot(xs,es2,'-',label='E(t) - Euler-Cromer')
    pylab.plot(xs,ys3,'-',label='x(t) - Verlet')
    pylab.plot(xs,es3,'-',label='E(t) - Verlet')
    pylab.xlabel('t')
    pylab.ylabel('x')
    pylab.legend(loc=2)
    pylab.show()
    for x,y1,e1,y2,e2,ys3,es3 in zip(xs,ys1,es1,ys2,es2,ys3,es3):
        print x, y1, e1, y2, e2, ys3, es3

if __name__=='__main__':
    import sys
    main(*[float(x) for x in sys.argv[1:]]) #(k,m,x,v,t0,tf,dt)


