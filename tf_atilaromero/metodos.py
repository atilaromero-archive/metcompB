#!/usr/bin/python

def nextv(a,v,x,dt,gamma=0):
    g1=1/(1+gamma*dt/2)
    g2=1-gamma*dt/2
    v=g1*(g2*v+a(x,v)*dt/2)
    return v

def euler(a,x,v,dt):
    vtemp=v
    v=v+a(x,v)*dt
    x=x+vtemp*dt
    return x,v
def euler_cromer(a,x,v,dt):
    v=v+a(x,v)*dt
    x=x+v*dt 
    return x,v
def verlet(a,xold,x,v,dt):
    xnew=2*x-xold+a(x,v)*dt*dt
    v=(xnew-xold)/(2*dt)
    return x,v,xnew
def leapfrog(a,x,v,dt):
    vt=v
    x=x+v*dt 
    v=v+a(x,v)*dt
    v=(vt+v)/2
    return x,v
def rungekutta4(a,x,v,dt):
    a0=a(x,v)
    x1=x+v*dt/2
    v1=v+a0*dt/2
    a1=a(x1,v1)
    x2=x+v1*dt/2
    v2=v+a1*dt/2
    a2=a(x2,v2)
    x3=x+v2*dt
    v3=v+a2*dt
    a3=a(x3,v3)
    x=x+(1.0/6)*(v+2*v1+2*v2+v3)*dt
    v=v+(1.0/6)*(a0+2*a1+2*a2+a3)*dt
    return x,v
def rungekutta2(a,x,v,dt):
    a0=a(x,v)
    x1=x+v*dt/2
    v1=v+a0*x*dt/2
    a1=a(x1)
    x=x+v1*dt
    v=v+a1*x1*dt
    return x,v
