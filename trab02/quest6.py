#!/usr/bin/python
import numpy
import pylab
#se w2 = 1, w=1, T=2piw=2pi=6.2832
#./quest3.py 1 1 1 0 0 25.1328 0.06 0.24 0.42 0.60

def main(k,m,x,v,t0,tf,dt):
    xs=numpy.arange(t0,tf+dt/2,dt)
    w2=k/m
    ys1=[]
    es1=[]
    x1=x
    v1=v
    for i in xs:
        #euler
        vtemp=v1
        v1=v1-w2*x1*dt
        x1=x1+v1*dt
        e1=(k*x1**2+m*v1**2)/2
        ys1+=[x1]
        es1+=[e1]
    #pylab.plot(xs,ys1,'-',label='x(t) - Euler')
    e0=(k*x**2+m*v**2)/2
    incl=numpy.log(e1-e0)/(tf-t0)
    pylab.plot(xs,es1,'-',label='E(t); dt=%f'%(dt))
    pylab.xlabel('t')
    pylab.ylabel('E')
    pylab.yscale('log')
    pylab.legend(loc=8)
    for x,y1,e1 in zip(xs,ys1,es1):
        print x, y1, e1

if __name__=='__main__':
    import sys
    args=[float(x) for x in sys.argv[1:7]]
    dts=sys.argv[7:]
    for dt in dts:
        argstemp=args+[float(dt)]
        main(*argstemp) #(k,m,x,v,t0,tf,dt1,dt2,dt3...)
    pylab.show()


