# script para construir curva de infeccao - prova1 2012 - 1
for b in `seq .1 .005 1.`
do
# entradas a.out:  tau_i tau_r beta  dt
         echo       10    30    $b   .1 | ./quest03.py
# saida: R0=beta*tau_i, 1 - s(infinito)	 
done
