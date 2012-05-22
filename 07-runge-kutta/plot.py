#!/usr/bin/python
import pylab
import numpy
import sys
path=sys.argv[1]
data=numpy.genfromtxt(path)
def col(n):
    return [c[n] for c in data]
pylab.plot(col(0),col(1),'-',label='x(t)')
pylab.plot(col(0),col(2),'-',label='v(t)')
pylab.plot(col(0),col(3),'-',label='e(t)')
pylab.xlabel('t')
pylab.ylabel('u')
pylab.legend(loc=2)
pylab.show()
