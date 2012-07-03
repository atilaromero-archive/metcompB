plot "quest13.dat" u 1:2 title "x_min" w l
set xlabel "v"
set ylabel "x_min"
#set xrange[0:10]
#set yrange[0:1]
replot
pause -1
set term postscript enhanced color
set output "fig2.eps"
replot
