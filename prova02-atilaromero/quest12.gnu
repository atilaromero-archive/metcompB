plot "quest12-a.dat" u 1:2 title "dt=0.1" w l
replot "quest12-b.dat" u 1:2 title "dt=0.01" w l
replot "quest12-c.dat" u 1:2 title "dt=0.001" w l
set xlabel "t"
set ylabel "x"
replot
#set xrange[0:10]
#set yrange[0:1]
pause -1
set term postscript enhanced color
set output "fig1.eps"
replot
