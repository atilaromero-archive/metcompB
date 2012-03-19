#!/usr/bin/python
from numpy import *
import pylab

def readarq(path):
    with open(path)as f:
        lines=f.readlines()
        m=[l.split() for l in lines]
        m=[[float(c) for c in l] for l in m]
    return m
dados=readarq('population.dat')
xs=[x[0] for x in dados]
ys=[x[1] for x in dados]
pylab.plot(xs,ys)
def fitfunc(p,x):
    return numpy.exp((x+p[0])*log(2)/p[1])+p[2]*(x+p[3])
def errfunc(p,x,y):
    return fitfunc(p,x)-y
p=[-559,44,20000,10000]
p1,sucess = 
pylab.show()
