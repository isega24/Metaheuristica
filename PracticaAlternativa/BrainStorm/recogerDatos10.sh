#/bin/bash

for j in `seq 0 19`; do

    echo "Funcion $j dimension 10"
    echo "" > ./solucionesDimension10/funcion$j.sol
    ./main.py $j 10 100 2000

done
