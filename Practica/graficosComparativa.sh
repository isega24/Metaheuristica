#/bin/bash

programas=(Geneticos-QAP Geneticos-QAP2 Geneticos-QAPOPX Geneticos-QAP2OPX Geneticos-QAP2OPXMejora1 Geneticos-QAP2OPXMejora2 Geneticos-QAP2OPXMejora3)
datos=(chr22a sko81 tai100a tai150b tai256c)

for dato in ${datos[*]}; do
    gnuplot -e "objetivo='$dato'" generaComparativa.gp
    mv output.png ./graficos/comparativa$dato.png
done
