f(x)=1/x
plot f(x) title "1/x"
replot "data.txt" u 1:2 with lines title "n=0"
replot "data.txt" u 1:3 with lines title "n=1"
replot "data.txt" u 1:4 with lines title "n=2"
replot "data.txt" u 1:5 with lines title "n=4"
replot "data.txt" u 1:6 with lines title "n=10"
replot "data.txt" u 1:7 with lines title "n=100"
replot "data.txt" u 1:8 with lines title "n=200"
set grid
replot
pause -1
set term postscript enhanced color
set output "trab1.eps"
replot