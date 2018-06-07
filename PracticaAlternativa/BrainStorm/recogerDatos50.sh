#/bin/bash

for j in `seq 0 19`; do

    echo "Funcion $j dimension 50"
    echo "" > ./solucionesDimension50/funcion$j.sol
    ./main.py $j 50 100 2000

donerecogerDatos
