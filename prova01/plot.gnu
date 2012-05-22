f(x)=1-1/x
plot "data.txt" u 1:2 title "SIR"
set xlabel "R0"
set ylabel "1-s"
set xrange[0:10]
set yrange[0:1]
replot f(x)
pause -1
set term postscript enhanced color
set output "quest03.eps"
replot
