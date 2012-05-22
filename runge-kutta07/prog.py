#!/usr/bin/python
import numpy
x=1.0
v=1.0
t0=0
tf=100
dt=0.1
def a(x):
    return -x
for t in numpy.arange(t0,tf+dt/2,dt):
    x0=x
    v0=v
    a0=a(x0)
    x1=x0+v0*dt/2
    v1=v0+a0*dt/2
    a1=a(x1)
    x2=x0+v1*dt/2
    v2=v0+a1*dt/2
    a2=a(x2)
    x3=x0+v2*dt
    v3=v0+a2*dt
    a3=a(x3)
    x=x0+(1.0/6)*(v0+2*v1+2*v2+v3)*dt
    v=v0+(1.0/6)*(a0+2*a1+2*a2+a3)*dt
    print t,x,v,0.5*(v*v+x*x)
