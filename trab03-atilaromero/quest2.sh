#!/bin/bash
gcc hist2.c -lm -o hist2
M=100
B=50

N=100
./hist2 0 $N $M $B > $N-$M.txt #2>$N-$M.data

N=1000
./hist2 0 $N $M $B > $N-$M.txt #2>$N-$M.data

N=5000
./hist2 0 $N $M $B > $N-$M.txt #2>$N-$M.data

gnuplot quest2.gnu #salva o grafico em quest2.eps
#evince quest2.eps
