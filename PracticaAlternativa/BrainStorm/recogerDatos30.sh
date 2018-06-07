#/bin/bash

for j in `seq 0 19`; do

    echo "Funcion $j dimension 30"
    echo "" > ./solucionesDimension30/funcion$j.sol
    ./main.py $j 30 100 2000

done
