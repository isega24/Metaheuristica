#!/bin/usr/gnuplot
set xlabel "X"
set ylabel "Y"
set term png
set title "Clusters y representantes en la generación ".generacion
set output "./graficos/".generacion."out.png"
set xrange [-100:100]
set yrange [-100:100]
plot filename1 with points lw 1 title "cluster1", filename2 with points lw 1 title "cluster2", filename3 with points lw 1 title "cluster3", filename4 with points lw 1 title "cluster4", filename5 with points lw 1 title "cluster5", filename6 with points lw 2 title"Representantes",
