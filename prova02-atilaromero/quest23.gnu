f(x)=a*x + b
a=1
b=0
plot "quest22.dat" u 3:4 title "desvio padrao" w l
fit f(x) "quest22.dat" u 3:4 via a, b
replot f(x) title sprintf("f(passo)=%f*passo+%f",a,b)
set xlabel "passo (log)"
set ylabel "desvio (log)"
replot
pause -1
set term postscript enhanced color
set output "fig5.eps"
replot
