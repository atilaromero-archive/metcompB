plot "quest21.dat" u 1:2 title "caminhante 1" w l
replot "quest21.dat" u 1:3 title "caminhante 2" w l
replot "quest21.dat" u 1:4 title "caminhante 3" w l
replot "quest21.dat" u 1:5 title "caminhante 4" w l
replot "quest21.dat" u 1:6 title "caminhante 5" w l
replot "quest21.dat" u 1:7 title "caminhante 6" w l
set xlabel "t"
set ylabel "posicao"
replot
#set xrange[0:10]
#set yrange[0:1]
pause -1
set term postscript enhanced color
set output "fig3.eps"
replot
