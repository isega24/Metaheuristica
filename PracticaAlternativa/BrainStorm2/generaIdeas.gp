#!/bin/usr/gnuplot
set xlabel "Generaciones"
set ylabel "Coste"
set term png
set output "output.png"

set title "Progresión del coste en ".objetivo." de los distintos algoritmos."


plot "./datosGrafico/Geneticos-QAP".objetivo.".dat" w l lw 2 title "Geneticos-QAP", "./datosGrafico/Geneticos-QAPOPX".objetivo.".dat" w l lw 2 title "Geneticos-QAPPMX","./datosGrafico/Geneticos-QAP2OPXMejora1".objetivo.".dat" w l lw 2 title "Geneticos-QAP2PMX:Mejora1","./datosGrafico/Geneticos-QAP2OPXMejora2".objetivo.".dat" w l lw 2 title "Geneticos-QAP2PMX:Mejora2","./datosGrafico/Geneticos-QAP2OPXMejora3".objetivo.".dat" w l lw 2 title "Geneticos-QAP2PMX:Mejora3"
