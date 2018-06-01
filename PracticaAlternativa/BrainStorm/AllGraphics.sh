#/bin/bash

rm -r ./graficos/
mkdir ./graficos

for i in `seq 0 1999`; do
    ./grafico.sh $i

done

# Este script genera todos los gráficos individuales
