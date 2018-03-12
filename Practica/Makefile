
PROGRAM=./Greedy-QAP.py
SOLDIRECTORY=./qapsoln/
DATADIRECTORY=./qapdata/
ls=/bin/ls $(DATADIRECTORY)

%:
	$(PROGRAM) $(DATADIRECTORY)$@.dat $(SOLDIRECTORY)$@.sln
all:
	for OUT in $(DATADIRECTORY)*.dat;do echo $(OUT) ; done
