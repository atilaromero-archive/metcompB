#!/usr/bin/python
import randi

randi.randi(0)
for i in range(1000):
    print sum([randi.moeda() for x in range(50)])
