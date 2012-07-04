#/bin/bash
#argumentos de prog.py: x0 v0 const_visc const_arrast_quad fpeso dt

dt=0.01
x=0
for v in 2 10 100
do
    for visc in 0.1 0.5
    do
	for quad in 0.1 0.5
	do
	    ./prog.py $x $v 0.0   0.0   10 $dt > 0_0.dat
	    ./prog.py $x $v $visc 0.0   10 $dt > x_0.dat
	    ./prog.py $x $v 0.0   $quad 10 $dt > 0_x.dat
	    ./prog.py $x $v $visc $quad 10 $dt > x_x.dat
	    gnuplot plot.gnu 
	    mv graf.eps v$v-visc$visc-quad$quad.eps
	done
    done
done
