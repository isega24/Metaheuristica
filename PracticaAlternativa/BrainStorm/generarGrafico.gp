#!/bin/usr/gnuplot
set xlabel "X"
set ylabel "Y"
set term png
set title "Clusters y representantes en la generación ".generacion
set output "./graficos/".generacion."out.png"
set xrange [-100:100]
set yrange [-100:100]
plot filename1 with points lw 3, filename2 with points lw 3, filename3 with points lw 3, filename4 with points lw 3, filename5 with points lw 3, filename6 with points lw 7,
