# Para instalar en otros SOs ver:
# - stackoverflow.com/a/21530768/3414720
# - cython.readthedocs.io

OUT=./resultados
.PHONY: build


debian-install:
	apt install python3-dev cython3

build:
	python3 setup.py build_ext --inplace




%:
	mkdir -p $(OUT)
	./main.py $@ 10 100 0 $(OUT)/problema$@Dimension10.txt

all:
	./recogerDatos.sh 
