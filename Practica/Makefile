
PROGRAM=./Greedy-QAP.py
SOLDIRECTORY=./qapsoln/
DATADIRECTORY=./qapdata/
DATAGREEDY=./solutionGreedy/
TABLASGREEDY=./tablas/
SHELL=/bin/bash
DATAFILES=`ls -c $(DATADIRECTORY)`


all:greedy tablasGreedy estadisticosGreedy
	echo Todo hecho
%:
	$(PROGRAM) $@
greedy:
	./obtenerDatos.sh $(DATADIRECTORY) $(PROGRAM) ./solutionGreedy/
tablasGreedy:
	./obtenerTabla.sh $(DATAGREEDY) $(TABLASGREEDY) Greedy
	./obtenerTabla.sh $(DATAGREEDY) $(TABLASGREEDY) BL

estadisticosGreedy:
	./estadisticos.py Greedy
	./estadisticos.py BL
