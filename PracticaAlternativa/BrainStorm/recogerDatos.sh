#/bin/bash

for j in `seq 0 19`; do
    for i in `seq 10 20 50`; do
        ./main.py $j $i 20 20000 

    done
done
