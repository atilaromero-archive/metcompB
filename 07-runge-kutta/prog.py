#!/usr/bin/python
def a(x):
    return -x
class RungeKutta():
    def __init__(self,x0,v0,dt):
        self.x=x0
        self.v=v0
        self.dt=dt
    def next(self):
        x0=self.x
        v0=self.v
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
        self.x=x0+(1.0/6)*(v0+2*v1+2*v2+v3)*dt
        self.v=v0+(1.0/6)*(a0+2*a1+2*a2+a3)*dt
        return self.x,self.v
        
if __name__=="__main__":
    x=1.0
    v=1.0
    dt=0.1
    t=0.0
    tf=100.0
    func=RungeKutta(x,v,dt)
    while (t<=tf):
        x,v=func.next()
        print t,x,v,0.5*(v*v+x*x)
        t+=dt
