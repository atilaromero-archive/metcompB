plot "0_0.dat" u 1:2 title "sem atrito" w l
replot "x_0.dat" u 1:2 title "viscoso" w l
replot "0_x.dat" u 1:2 title "arrasto quadratico" w l
replot "x_x.dat" u 1:2 title "com tudo" w l
set xlabel "t"
set ylabel "x"
replot
#set xrange[0:10]
#set yrange[0:1]
#pause -1
set term postscript enhanced color
set output "graf.eps"
replot
