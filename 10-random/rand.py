#!/usr/bin/python
import random
import sys

def pseudoaleatorio(x,n):
    a=1029.0
    b=221591.0
    c=1048576.0
    for i in range(n):
        xold=x
        x=(a*x+b)%c
        #print i,x/c
        print xold/c,x/c
    
x=float(sys.argv[1])
n=int(sys.argv[2])
pseudoaleatorio(x,n)
