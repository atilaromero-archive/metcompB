#!/bin/bash
#argumentos: x0 v0 vf dv dt
python ./quest13.py 5 1 -4 0.01 0.01 > quest13.dat
gnuplot quest13.gnu