#!/usr/bin/python
import numpy
import pylab

def main(t0,tf,dt):
    x=-1.0
    v=1
    ts=numpy.arange(t0,tf+dt/2,dt)
    def a(x):
        return -(6*x**5-6*x)
    xl=[x]  #leaprog
    vl=v+a(x)*dt/2
    xe=[x]  #euler
    ve=v
    xdif=[0]
    for t in ts:
        #leapfrog
        vt=v
        xl.append(xl[-1]+v*dt)
        v=v+a(xl[-1])*dt
        #euler
        xe.append(xe[-1]+ve*dt)
        ve=ve+a(x)*dt
        #dif
        xdif.append(xe[-1]-xl[-1])
    pylab.plot(ts,xl[:-1],'-',label='x(t) - LeapFrog')
    pylab.plot(ts,xe[:-1],'-',label='x(t) - Euler')
    pylab.plot(ts,xdif[:-1],'-',label='x(t) - diferenca')
    pylab.xlabel('t')
    pylab.ylabel('x')
    pylab.legend(loc=2)
    #for x,y1,e1,y2,e2,ys3,es3 in zip(xs,ys1,es1,ys2,es2,ys3,es3):
    #    print x, y1, e1, y2, e2, ys3, es3
    pylab.show()

if __name__=='__main__':
    import sys
    main(*[float(x) for x in sys.argv[1:]]) #(t0,tf,dt):

