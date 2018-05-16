#/bin/bash

datos=(chr22a sko81 tai100a tai150b tai256c)

for dato in ${datos[*]}; do
    gnuplot -e "objetivo='$dato'" generaComparativaGeneracionales.gp
    mv output.png ./graficos/comparativaGeneracional$dato.png
done
