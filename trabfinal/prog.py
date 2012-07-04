#!/usr/bin/python
import metodos
import sys

def mkfunc_a(cvisc,cquad,fpeso):
    def a(x,v):
        return -(cvisc*v +cquad*v*v+fpeso) 
    return a

def main(x,v,cvisc,cquad,fpeso,dt):
    a=mkfunc_a(cvisc,cquad,fpeso)
    t=0.0;
    while(x>=0):
        print t,x,v
        x,v=metodos.rungekutta4(a,x,v,dt)
        t+=dt

if len(sys.argv)<3:
    print "argumentos: x0 v0 const_visc const_arrast_quad fpeso dt"
    sys.exit(1)

x0=float(sys.argv[1])
v0=float(sys.argv[2])
cv=float(sys.argv[3])
cq=float(sys.argv[4])
fp=float(sys.argv[5])
dt=float(sys.argv[6])

main(x0,v0,cv,cq,fp,dt)
