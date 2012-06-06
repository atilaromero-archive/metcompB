#!/usr/bin/python
import sys

def randi(semente=None):
    a=1029.0
    b=221591.0
    c=1048576.0
    if semente!=None:
        randi.semente=semente
    randi.semente=(a*randi.semente+b)%c
    return randi.semente/c

def randirange(ini,fim,semente=None):
    x=randi(semente)
    return int(x*(fim-ini)+ini)

def moeda(semente=None):
    return randirange(0,2,semente)*2-1

def dado(semente=None):
    return randirange(1,7,semente)

def roleta(semente=None):
    return randirange(0,37,semente)
