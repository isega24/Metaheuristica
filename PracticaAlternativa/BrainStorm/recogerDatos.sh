#/bin/bash

for j in `seq 0 19`; do
    for i in `seq 10 20 50`; do
        rm ./solucionesDimension$i/funcion$j.sol
        echo "" > ./solucionesDimension$i/funcion$j.sol
        ./main.py $j $i 40 0

    done
done
