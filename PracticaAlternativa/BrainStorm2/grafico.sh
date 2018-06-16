#/bin/bash

# El primer argumento debe ser el programa que queremos ejecutar. El segundo, el archivo de datos.
# Este script genera un archivo en datosGrafico/ con el nombre del archivo y el nombre

mkdir -p ./graficos/
gnuplot -e "generacion=$1;filename1='./generacionesPruebas/cluster1Gen$1.cl';filename2='./generacionesPruebas/cluster2Gen$1.cl';filename3='./generacionesPruebas/cluster3Gen$1.cl';filename4='./generacionesPruebas/cluster4Gen$1.cl';filename5='./generacionesPruebas/cluster5Gen$1.cl';filename6='./generacionesPruebas/representantesGen$1.cl';" generarGrafico.gp
