#!/usr/bin/python

def a(x):
    return -x

class Metodos():
    def __init__(self,x,v):
        self.x=x
        self.v=v
    def next_euler(self,dt):
        self.xold=self.x
        v=self.v
        self.v=self.v+a(x)*dt
        self.x=self.x+v*dt
        return self.x,self.v
    def next_euler_cromer(self,dt):
        self.xold=self.x
        self.v=self.v+a(x)*dt
        self.x=self.x+self.v*dt 
        return self.x,self.v
    def next_verlet(self,dt):
        xnew=2*self.x-self.xold+a(self.x)*dt*dt
        self.v=(xnew-self.xold)/(2*dt)
        xold=self.x
        self.x=xnew
        return self.xold,self.v
