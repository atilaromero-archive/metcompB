#!/usr/bin/python
import numpy
import pylab
#./prog.py 1 1 1 0 0 300 0.01

def main(k,m,x,v,t0,tf,dt):
    ts=numpy.arange(t0,tf+dt/2,dt)
    w2=k/m
    def a(x):
        return -w2*x
    def e(x,v):
        return (k*x**2+m*v**2)/2
    xverlet=[x-v*dt,x]
    vverlet=[v]
    everlet=[e(x,v)]
    xleapfrog=[x]
    vleapfrog=[v] 
    eleapfrog=[e(x,v)]
    gamma=0
    g1=1/(1+gamma*dt/2)
    g2=1-gamma*dt/2
    v=g1*(g2*v+a(x)*dt/2)
    for t in ts:
        #verlet
        xverlet+=[2*xverlet[-1]-xverlet[-2]+a(xverlet[-1])*dt*dt]
        vverlet+=[(xverlet[-1]-xverlet[-3])/(2*dt)]
        everlet+=[e(xverlet[-2],vverlet[-1])]
        #leapfrog
        vt=v
        xleapfrog+=[xleapfrog[-1]+v*dt]
        v=g1*(g2*v+a(xleapfrog[-1])*dt)
        vleapfrog+=[(vt+v)/2]
        eleapfrog+=[e(xleapfrog[-1],vleapfrog[-1])]
    xverlet=xverlet[1:]
    pylab.plot(ts,xverlet[:-1],'-',label='x(t) - Verlet')
    pylab.plot(ts,everlet[:-1],'-',label='E(t) - Verlet')
    pylab.plot(ts,xleapfrog[:-1],'-',label='x(t) - LeapFrog')
    pylab.plot(ts,eleapfrog[:-1],'-',label='E(t) - LeapFrog')
    pylab.xlabel('t')
    pylab.ylabel('x')
    pylab.legend(loc=2)
    #for x,y1,e1,y2,e2,ys3,es3 in zip(xs,ys1,es1,ys2,es2,ys3,es3):
    #    print x, y1, e1, y2, e2, ys3, es3
    pylab.show()

if __name__=='__main__':
    import sys
    main(*[float(x) for x in sys.argv[1:]]) #(k,m,x,v,t0,tf,dt)


