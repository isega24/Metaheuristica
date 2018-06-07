#/bin/bash

for i in `seq 0 19`; do
    echo Funcion$i: `cat ./solucionesDimension30/funcion$i.sol|grep Coste`
done
