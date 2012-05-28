#!/usr/bin/python
from metodos import *

x=12.0
v=0.0
t=0.0
tf=8.0
dt=0.01
x1=x2=x
v1=v2=v
def a(x):
    #f=4*x**3-2*x
    return -x
xnew=rungekutta4(a,x1,v1,dt)[0]
def e(x,v):
    #u=x**4-x**2+10
    u=x**2.0
    return u+v**2.0
while (t<=tf):
    x1,v1=rungekutta4(a,x1,v1,dt)
    x2,v2,xnew=verlet(a,x2,xnew,v2,dt)
    #print e(x1,v1)-e(x2,v2),e(x1,v1)-e(x2,v2),t
    print e(x1,v1),e(x2,v2)+0.001,t
    t+=dt
