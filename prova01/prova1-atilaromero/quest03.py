#!/usr/bin/python
#import numpy
#import pylab
import sys

def main(ti,tr,beta,s,i,r,t0,tf,dt):
    vs=vi=vr=0
    tot=[s+i+r]
    t=t0
    rzero=beta*ti
    while t<=tf:
        t+=dt
        bsi=beta*s*i
        rtr=r/tr
        iti=i/ti
        #S
        s=s+vs*dt
        vs=(-bsi+rtr)*dt
        #I
        i=i+vi*dt
        vi=(bsi-iti)*dt
        #R
        r=r+vr*dt
        vr=(iti-rtr)*dt
        #print t, s, i, r, s+i+r
    print rzero, 1-s

if __name__=='__main__':
    i=10.0**(-6)
    r=0
    s=1.0-i
    t0=0.0
    tf=3000
    sys.stderr.write('ti tr beta dt: ')
    ti,tr,beta,dt=[float(x) for x in sys.stdin.readline().split()]
    #ti,tr,beta,dt=[float(x) for x in sys.argv[1:]]
    main(ti,tr,beta,s,i,r,t0,tf,dt)
    



