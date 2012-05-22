#!/usr/bin/python
import numpy
import pylab
import sys

def main(ti,tr,beta,s,i,r,t0,tf,dt):
    t_=numpy.arange(t0,tf+dt/2,dt)
    s_=[s]
    i_=[i]
    r_=[r]
    vs=vi=vr=0
    tot=[s+i+r]
    for t in t_[1:]:
        bsi=beta*s*i
        rtr=r/tr
        iti=i/ti
        #S
        s=s+vs*dt
        vs=vs+(-bsi+rtr)*dt
        s_.append(s)
        #I
        i=i+vi*dt
        vi=vi+(bsi-iti)*dt
        i_.append(i)
        #R
        r=r+vr*dt
        vr=vr+(iti-rtr)*dt
        r_.append(r)
        #total
        tot.append(s+i+r)
    pylab.plot(t_,s_,'-',label='suscetiveis(t)')
    pylab.plot(t_,i_,'-',label='infectadas(t)')
    pylab.plot(t_,r_,'-',label='removidas(t)')
    pylab.plot(t_,tot,'-',label='total(t)')
    pylab.xlabel('t')
    pylab.ylabel('pessoas')
    pylab.legend(loc=2)
    pylab.show()
#    for x,y1,e1,y2,e2,ys3,es3 in zip(xs,ys1,es1,ys2,es2,ys3,es3):
#        print x, y1, e1, y2, e2, ys3, es3

if __name__=='__main__':
    i=10**(-6)
    r=0
    s=1-i
    t0=0
    tf=30
    ti,tr,beta,dt=[float(x) for x in sys.argv[1:]]
    main(ti,tr,beta,s,i,r,t0,tf,dt)
    



