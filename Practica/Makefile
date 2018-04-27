
GREEDY=./Greedy-QAP.py
GENETICO1=./Geneticos-QAP.py
GENETICO1OPX=./Geneticos-QAPOPX.py
GENETICO2=./Geneticos-QAP2.py
GENETICO2OPX=./Geneticos-QAP2OPX.py
GENETICO2OPXM1=./Geneticos-QAP2OPXMejora1.py
GENETICO2OPXM2=./Geneticos-QAP2OPXMejora2.py
GENETICO2OPXM3=./Geneticos-QAP2OPXMejora3.py
SOLDIRECTORY=./qapsoln/
DATADIRECTORY=./qapdata/
DATAGREEDY=./solutionGreedy/
DATAGENETICO1=./solutionGenetico1/
DATAGENETICO2=./solutionGenetico2/
DATAGENETICO1OPX=./solutionGenetico1OPX/
DATAGENETICO2OPX=./solutionGenetico2OPX/
DATAGENETICO2OPXM1=./solutionGenetico2OPXMejora1/
DATAGENETICO2OPXM2=./solutionGenetico2OPXMejora2/
DATAGENETICO2OPXM3=./solutionGenetico2OPXMejora3/
TABLAS=./tablas/
SHELL=/bin/bash



all:todoGreedy todoGenetico1 todoGenetico2 todoGenetico1opx todoGenetico2opx todoGenetico2opxm1 todoGenetico2opxm2 todoGenetico2opxm3 graficos
	@ echo Todo hecho
estadisticos:estadisticosGreedy estadisticosGenetico1 estadisticosGenetico2 estadisticosGenetico1opx estadisticosGenetico2opx estadisticosGenetico2opxm1 estadisticosGenetico2opxm2 estadisticosGenetico2opxm3
	@ echo Hecho



datos:datosGreedy datosGenetico1 datosGenetico2 datosGenetico1opx datosGenetico2opx datosGenetico2opxm1 datosGenetico2opxm2 datosGenetico2opxm3
	@ echo Hecho

todoGreedy:greedy datosGreedy
	echo Todo Greedy y BL

datosGreedy:tablasGreedy tablaLatexGreedy
	echo Datos recabados

todoGenetico1:genetico1 datosGenetico1
	echo hecho

datosGenetico1:tablasgenetico1 tablaLatexgenetico1
	echo Datos recabados

todoGenetico2:genetico2 datosGenetico2
	echo hecho

datosGenetico2:tablasgenetico2 tablaLatexgenetico2
	echo Datos recabados

todoGenetico1opx:genetico1opx datosGenetico1opx
	echo hecho

datosGenetico1opx:tablasgenetico1opx tablaLatexgenetico1opx
	echo Datos recabados

todoGenetico2opx:genetico2opx datosGenetico2opx
	echo hecho

datosGenetico2opx:tablasgenetico2opx tablaLatexgenetico2opx
	echo Datos recabados

todoGenetico2opxm1:genetico2opxM1 datosGenetico2opxm1
	echo hecho

datosGenetico2opxm1:tablasgenetico2opxm1 tablaLatexgenetico2opxm1
	echo Datos recabados

todoGenetico2opxm2:genetico2opxM2 datosGenetico2opxm2
	echo hecho
datosGenetico2opxm2:tablasgenetico2opxm2 tablaLatexgenetico2opxm2
	echo Datos recabados

todoGenetico2opxm3:genetico2opxM3 datosGenetico2opxm3
	echo hecho
datosGenetico2opxm3:tablasgenetico2opxm3 tablaLatexgenetico2opxm3
	echo Datos recabados





greedy:
	./obtenerDatos.sh $(DATADIRECTORY) $(GREEDY) $(DATAGREEDY)
tablasGreedy:
	./obtenerTabla.sh $(DATAGREEDY) $(TABLAS) Greedy
	./obtenerTabla.sh $(DATAGREEDY) $(TABLAS) BL

estadisticosGreedy:
	./estadisticos.py Greedy
	./estadisticos.py BL

tablaLatexGreedy:
	mkdir -p tablasLatex
	./tablasLatex.py Greedy > ./tablasLatex/Greedy.txt
	./tablasLatex.py BL > ./tablasLatex/BL.txt


genetico1:
	./obtenerDatos.sh $(DATADIRECTORY) $(GENETICO1) $(DATAGENETICO1)

tablasgenetico1:
	./obtenerTabla.sh $(DATAGENETICO1) $(TABLAS) Genetico1

tablaLatexgenetico1:
	mkdir -p tablasLatex
	./tablasLatex.py Genetico1 > ./tablasLatex/Genetico1.txt

estadisticosGenetico1:
	./estadisticos.py Genetico1

genetico2:
	./obtenerDatos.sh $(DATADIRECTORY) $(GENETICO2) $(DATAGENETICO2)

tablasgenetico2:
	./obtenerTabla.sh $(DATAGENETICO2) $(TABLAS) Genetico2

tablaLatexgenetico2:
	mkdir -p tablasLatex
	./tablasLatex.py Genetico2 > ./tablasLatex/Genetico2.txt

estadisticosGenetico2:
	./estadisticos.py Genetico2

genetico1opx:
	./obtenerDatos.sh $(DATADIRECTORY) $(GENETICO1OPX) $(DATAGENETICO1OPX)

tablasgenetico1opx:
	./obtenerTabla.sh $(DATAGENETICO1OPX) $(TABLAS) Genetico1OPX

tablaLatexgenetico1opx:
	mkdir -p tablasLatex
	./tablasLatex.py Genetico1OPX > ./tablasLatex/Genetico1OPX.txt

estadisticosGenetico1opx:
	./estadisticos.py Genetico1OPX


genetico2opx:
	./obtenerDatos.sh $(DATADIRECTORY) $(GENETICO2OPX) $(DATAGENETICO2OPX)

tablasgenetico2opx:
	./obtenerTabla.sh $(DATAGENETICO2OPX) $(TABLAS) Genetico2OPX

tablaLatexgenetico2opx:
	mkdir -p tablasLatex
	./tablasLatex.py Genetico2OPX > ./tablasLatex/Genetico2OPX.txt

estadisticosGenetico2opx:
	./estadisticos.py Genetico2OPX






genetico2opxM1:
	./obtenerDatos.sh $(DATADIRECTORY) $(GENETICO2OPXM1) $(DATAGENETICO2OPXM1)

tablasgenetico2opxm1:
	./obtenerTabla.sh $(DATAGENETICO2OPXM1) $(TABLAS) Genetico2OPXM1

tablaLatexgenetico2opxm1:
	mkdir -p tablasLatex
	./tablasLatex.py Genetico2OPXM1 > ./tablasLatex/Genetico2OPXM1.txt

estadisticosGenetico2opxm1:
	./estadisticos.py Genetico2OPXM1



genetico2opxM2:
	./obtenerDatos.sh $(DATADIRECTORY) $(GENETICO2OPXM2) $(DATAGENETICO2OPXM2)

tablasgenetico2opxm2:
	./obtenerTabla.sh $(DATAGENETICO2OPXM2) $(TABLAS) Genetico2OPXM2

tablaLatexgenetico2opxm2:
	mkdir -p tablasLatex
	./tablasLatex.py Genetico2OPXM2 > ./tablasLatex/Genetico2OPXM2.txt

estadisticosGenetico2opxm2:
	./estadisticos.py Genetico2OPXM2

genetico2opxM3:
	./obtenerDatos.sh $(DATADIRECTORY) $(GENETICO2OPXM3) $(DATAGENETICO2OPXM3)

tablasgenetico2opxm3:
	./obtenerTabla.sh $(DATAGENETICO2OPXM3) $(TABLAS) Genetico2OPXM3

tablaLatexgenetico2opxm3:
	mkdir -p tablasLatex
	./tablasLatex.py Genetico2OPXM3 > ./tablasLatex/Genetico2OPXM3.txt

estadisticosGenetico2opxm3:
	./estadisticos.py Genetico2OPXM3


graficos:
	@ echo Comenzando la recolecta de datos gráficos
	./AllGraphics.sh
	./graficosComparativa.sh
