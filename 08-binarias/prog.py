#!/usr/bin/python

#GM=4pi^2, T=1yr

pi=3.1416
def a(x,y):
    return -(4.0*pi**2.0)/(x**2+y**2)**1.5
class grav():
    def __init__(self,x,y,vx,vy,dt):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.dt=dt
    def next(self):
        x,y,vx,vy,dt=self.x,self.y,self.vx,self.vy,self.dt
        a1=a(x,y)
        x2=x+vx*dt/2
        y2=y+vy*dt/2
        vx2=vx+a1*x*dt/2
        vy2=vy+a1*y*dt/2
        a2=a(x2,y2)
        x=x+vx2*dt
        y=y+vy2*dt
        vx=vx+a2*x2*dt
        vy=vy+a2*y2*dt
        self.x,self.y,self.vx,self.vy=x,y,vx,vy
        print x,y

t=0
tf=4
dt=0.001
terra=grav(1.0,0.0,0.0,2*pi,dt)
while (t<=tf):
    terra.next()
    t+=dt
