#!/bin/bash
python ./quest12.py 5 -2 0.1 > quest12-a.dat
python ./quest12.py 5 -2 0.01 > quest12-b.dat
python ./quest12.py 5 -2 0.001 > quest12-c.dat
gnuplot quest12.gnu