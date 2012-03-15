f(x)=exp((x+a)*log(2)/b)+c*(x+d)
a=-559  
b=44	#tempo para duplicar a populacao (qd x=b -> exp(log(2)) -> =2)
c=20000 #crescimento linear de 20000/ano
d=10000 #inicio da parte linear (10000 BC)
#esse fit mexe apenas com a parte exponencial
fit f(x) "population.dat" u 1:2 via a,b
plot "population.dat" u 1:2 title "crescimento populacional"
replot f(x)
#set xrange[0:]
set yrange[0:]
replot
pause -1
#set term postscript enhanced color
#set output "plot.eps"
#replot
