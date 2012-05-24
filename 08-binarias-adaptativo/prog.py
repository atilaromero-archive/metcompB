#!/usr/bin/python

#GM=4pi^2, T=1yr

pi=3.1416
def a(x,y):
    return -(4.0*pi**2.0)/(x**2+y**2)**1.5
class grav():
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
    def next(self,dt):
        x,y,vx,vy=self.x,self.y,self.vx,self.vy
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
        return x,y,vx,vy

t=0
tf=4
dt=0.001
x=1.0
y=0.0
vx=0.0
vy=2*pi
err=0.001
terra=grav(x,y,vx,vy)
count=0
while (t<=tf and count<100000):
    terra2=grav(x,y,vx,vy)
    terra2.next(dt/2)
    xf,yf,vxf,vyf=terra2.next(dt/2)
    rf2=(xf-x)**2+(yf-y)**2
    x,y,vx,vy=terra.next(dt)
    t+=dt
    dr2=(x-xf)**2+(y-yf)**2
    err_t=(dr2/rf2)**0.5
    dt_n=((err/err_t)**0.5)*dt
    print t,x,y,vx,vy,dt,err_t
    if (dt_n > dt):
        dt = min(dt_n,dt*2.5)
    else:
        dt = max(dt_n,dt/2.5)
    count+=1
