#!/usr/bin/python
import quest11
import metodos
import sys

def main(x,v,dt):
    t=0.0;
    while(t<3):
        print t,x,v
        x,v=metodos.rungekutta2(quest11.a,x,v,dt)
        t+=dt

if len(sys.argv)<3:
    print "argumentos: x0 v0 dt"
    sys.exit(1)

x0=float(sys.argv[1])
v0=float(sys.argv[2])
dt=float(sys.argv[3])

main(x0,v0,dt)
