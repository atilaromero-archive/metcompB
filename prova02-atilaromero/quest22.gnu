plot "quest22.dat" u 1:2 title "desvio padrao" w l
set xlabel "passo"
set ylabel "desvio"
#set xrange[0:10]
#set yrange[0:1]
replot
pause -1
set term postscript enhanced color
set output "fig4.eps"
replot
