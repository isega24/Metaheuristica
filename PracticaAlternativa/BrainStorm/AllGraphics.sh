#/bin/bash

rm -r ./graficos/
mkdir ./graficos

for i in `seq 0 19`; do
    ./grafico.sh $i

done

# Este script genera todos los gráficos individuales
