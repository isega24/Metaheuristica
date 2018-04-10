
GREEDY=./Greedy-QAP.py
GENETICO1=./Geneticos-QAP.py
SOLDIRECTORY=./qapsoln/
DATADIRECTORY=./qapdata/
DATAGREEDY=./solutionGreedy/
DATAGENETICO1=./solutionGenetico1/
TABLAS=./tablas/
SHELL=/bin/bash
DATAFILES=`ls -c $(DATADIRECTORY)`


all:greedy tablasGreedy estadisticosGreedy tablaLatexGreedy
	echo Todo hecho
%:
	$(GREEDY) $@

todoGreedy:greedy tablasGreedy tablaLatexGreedy estadisticosGreedy
	echo hecho
todoGenetico1:genetico1 tablasgenetico1 tablaLatexgenetico1 estadisticosGenetico1

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
