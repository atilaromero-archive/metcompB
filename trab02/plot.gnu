f(x)=a*exp((x+c)/b)
a=93287.4
b=60.5698
c=-1328.59
plot "population.dat" u 1:2 title "crescimento populacional"
replot f(x)
set xrange[0:]
set yrange[0:]
replot
pause -1
set term postscript enhanced color
set output "plot.eps"
replot
