#!/usr/bin/python

def a(x):
    return -w2*x
def e(x,v):
    return (k*x**2+m*v**2)/2
class LeapFrog():
    def __init__(self,v0,dt,gamma=0):
        self.g1=1/(1+gamma*dt/2)
        self.g2=1-gamma*dt/2
        self.v=g1*(g2*v0+a(x)*dt/2)
        pass
    def next():
        vt=v
        xleapfrog+=[xleapfrog[-1]+v*dt]
        v=g1*(g2*v+a(xleapfrog[-1])*dt)
        vleapfrog+=[(vt+v)/2]
        eleapfrog+=[e(xleapfrog[-1],vleapfrog[-1])]



def main(k,m,x,v,gamma,t0,tf,dt):
    for t in ts:

    pylab.plot(ts,xleapfrog[:-1],'-',label='x(t) - LeapFrog')
    pylab.plot(ts,eleapfrog[:-1],'-',label='E(t) - LeapFrog')
    pylab.xlabel('t')
    pylab.ylabel('x')
    pylab.legend(loc=2)
    #for x,y1,e1,y2,e2,ys3,es3 in zip(xs,ys1,es1,ys2,es2,ys3,es3):
    #    print x, y1, e1, y2, e2, ys3, es3
    pylab.show()

if __name__=='__main__':
    import sys
    main(*[float(x) for x in sys.argv[1:]]) #(k,m,x,v,gamma,t0,tf,dt)

