#/bin/bash

for i in `seq 0 19`; do
    echo Funcion$i: `cat ./solucionesDimension10/funcion$i.sol|grep Coste`
done
