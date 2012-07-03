#!/usr/bin/python
import quest11
import metodos
import sys

def findmin(x,v,dt):
    t=0.0;
    while(t<500):
        xnew,vnew=metodos.rungekutta2(quest11.a,x,v,dt)
        if xnew>x:
            return x
        x,v=xnew,vnew
        t+=dt

def main(x0,v0,vf,dv,dt):
    v=v0
    while(v>=(vf-dv)):
        print v,findmin(x0,v,dt)
        v-=dv

if len(sys.argv)<3:
    print "argumentos: x0 v0 vf dv dt"
    sys.exit(1)

x0=float(sys.argv[1])
v0=float(sys.argv[2])
vf=float(sys.argv[3])
dv=float(sys.argv[4])
dt=float(sys.argv[5])

main(x0,v0,vf,dv,dt)
