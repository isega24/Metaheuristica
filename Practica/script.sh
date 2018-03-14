#/bin/bash
for f in `ls $1`; do
  $2 $1$f
done
