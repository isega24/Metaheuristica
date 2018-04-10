#/bin/bash
datos=(chr22a chr22b chr25a esc128 had20 lipa60b lipa80b nug28 sko81 sko90 sko100a sko100f tai100a tai100b tai150b tai256c tho40 tho150 wil50 wil100)

mkdir -p $3
for f in ${datos[*]}; do
    echo $f
    $2 $1$f.dat 0 $3$f.sol
done
