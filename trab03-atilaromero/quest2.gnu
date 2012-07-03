plot "100-100.txt" u 1:2 w l
replot "1000-100.txt" u 1:2 w l
normal(x,m,s) = 0.05/(sqrt(2*pi)*s) * exp( -(x-m)**2 / (2*s*s) )
f(x) = normal(x,0,10.336808/100)
replot f(x)
set term postscript enhanced color
set output "quest2.eps"
replot "5000-100.txt" u 1:2 w l
