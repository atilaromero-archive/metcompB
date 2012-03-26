#!/usr/bin/python
import numpy

inicio=0.01
fim=0.2
passo=inicio
for x in numpy.arange(inicio, fim+passo/2,passo):
    print '102400 0 3 -0.69314718055994526 %f'%x
