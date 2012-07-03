#!/bin/bash
gcc hist1.c -lm -o hist1
N=1000

M=1
B=2
./hist1 0 $N $M $B > $N-$M.txt 2>$N-$M.data

M=10
B=10
./hist1 0 $N $M $B > $N-$M.txt 2>$N-$M.data

M=100
B=50
./hist1 0 $N $M $B > $N-$M.txt 2>$N-$M.data

gnuplot quest1.gnu #salva o grafico em quest1.eps
#evince quest1.eps
