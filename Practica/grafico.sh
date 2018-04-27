#/bin/bash

# El primer argumento debe ser el programa que queremos ejecutar. El segundo, el archivo de datos.
# Este script genera un archivo en datosGrafico/ con el nombre del archivo y el nombre
./$1.py ./qapdata/$2.dat 200000 datos.txt > temporal.txt
rm datos.txt

mkdir -p ./datosGrafico/ ./temp/ ./graficos/

grep generacion temporal.txt| cut -d ' ' -f 6 >>./temp/generacion.txt
grep Mejor temporal.txt| cut -d ' ' -f 5 >> ./temp/Mejor.txt

paste -d ' ' ./temp/generacion.txt ./temp/Mejor.txt > ./datosGrafico/$1$2.dat

rm temporal.txt
rm -r ./temp/


gnuplot -e "filename='./datosGrafico/$1$2.dat';algoritmo='$1';objetivo='$2'" generarGrafico.gp

mv output.png ./graficos/$1$2.png
