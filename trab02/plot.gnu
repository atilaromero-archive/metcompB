f(x)=exp((x+a)*b)+c*x+d
a=1500
b=0.0063
c=20000
d=200000000
fit f(x) "population.dat" u 1:2 via a,b,c,d
plot "population.dat" u 1:2 title "crescimento populacional"
replot f(x)
#set xrange[0:]
set yrange[0:]
replot
#pause -1
#set term postscript enhanced color
#set output "plot.eps"
#replot
