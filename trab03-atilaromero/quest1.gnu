plot "1000-1.txt" u 1:2 w l
replot "1000-10.txt" u 1:2 w l
set term postscript enhanced color
set output "quest1.eps"
replot "1000-100.txt" u 1:2 w l
