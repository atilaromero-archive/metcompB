#!/usr/bin/python

def a(x):
    return -x

def nextv(v,x,gamma=0,dt):
    g1=1/(1+gamma*dt/2)
    g2=1-gamma*dt/2
    v=g1*(g2*v+a(x)*dt/2)
    return v

def euler(x,v,dt):
    vtemp=v
    v=v+a(x)*dt
    x=x+vtemp*dt
    return x,v
def euler_cromer(x,v,dt):
    v=v+a(x)*dt
    x=x+v*dt 
    return x,v
def verlet(xold,x,v,dt):
    xnew=2*x-xold+a(x)*dt*dt
    v=(xnew-xold)/(2*dt)
    return x,v,xnew
def leapfrog(x,v,dt):
    vt=v
    x=x+v*dt 
    v=v+a(x)*dt
    v=(vt+v)/2
    return x,v
def rungekutta4(x,v,dt):
    a0=a(x)
    x1=x+v*dt/2
    v1=v+a0*dt/2
    a1=a(x1)
    x2=x+v1*dt/2
    v2=v+a1*dt/2
    a2=a(x2)
    x3=x+v2*dt
    v3=v+a2*dt
    a3=a(x3)
    x=x+(1.0/6)*(v+2*v1+2*v2+v3)*dt
    v=v+(1.0/6)*(a0+2*a1+2*a2+a3)*dt
    return x,v
def rungekutta2(x,v,dt):
    a0=a(x)
    x1=x+v*dt/2
    v1=v+a0*x*dt/2
    a1=a(x1)
    x=x+v1*dt
    v=v+a1*x1*dt
    return x,y
