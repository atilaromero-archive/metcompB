#!/usr/bin/python
import numpy
def an(a,n):
    sinal=(-1.0)**n
    pot=a**(1.0+n)
    return sinal/pot
    
def f(a,n,x):
    r=0
    for i in range(n+1):
        r+=an(a,i)*((x-a)**i)
    return r
for x in numpy.arange(0.1,2.01,0.01):
    a=1
    print x,
    for n in [0,1,2,4,10,100,200]:
        print f(a,n,x),
    print

