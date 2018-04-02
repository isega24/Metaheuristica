#/bin/bash

datos=(chr22a chr22b chr25a esc128 had20 lipa60b lipa80b nug28 sko81 sko90 sko100a sko100f tai100a tai100b tai150b tai256c tho40 tho150 wil50 wil100)

mkdir -p ./temp/
touch ./temp/Tiempo$3.txt
touch ./temp/Coste$3.txt
touch ./temp/Mejor$3.txt

for f in ${datos[*]}; do
    grep Tiempo$3 $1$f.sol| cut -f 2 >>./temp/Tiempo$3.txt
    grep Coste$3 $1$f.sol| cut -f 2 >>./temp/Coste$3.txt
    grep Mejor $1$f.sol| cut -f 2 >> ./temp/Mejor.txt

done

paste -d ' ' ./temp/Coste$3.txt ./temp/Tiempo$3.txt ./temp/Mejor.txt > $2Tabla$3.txt

rm -r ./temp/
