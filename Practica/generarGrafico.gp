#!/bin/usr/gnuplot
set xlabel "Generaciones"
set ylabel "Coste"
set term png
set output "output.png"
set title "Prograsión del coste de ".objetivo." con el algoritmo ".algoritmo
plot filename with lines lw 2 title "Progrsión del coste"
