#!/usr/bin/python3

import sys
import math
from solucion import Permutacion
from solucion import coste
from solucion import readData,readSolution
from time import time
from random import seed,shuffle
import numpy
from primerGenetico import *


if len(sys.argv) < 2:
    print("Fatal Error, no file as input")
if len(sys.argv) >=3:
    randseed = int(sys.argv[2])
    seed(randseed)

printFile = ""
if len(sys.argv) >= 4:
    printFile = sys.argv[3]
fileName = sys.argv[1]
solveName = "./qapsoln/"+fileName[10:-3]+"sln"

n,matrizFlujos,matrizDistancias = readData(filename=fileName)
matrizFlujos = numpy.array(matrizFlujos)
matrizDistancias = numpy.array(matrizDistancias)
n = int(n)


matrizFlujos = [[int(matrizFlujos[i][j]) for j in range(len(matrizFlujos[i]))] for i in range(len(matrizFlujos))]
matrizDistancias = [[int(matrizDistancias[i][j]) for j in range(len(matrizDistancias[i]))] for i in range(len(matrizFlujos))]

# Lectura del problema hecho.

tiempo_inicial = time()
# Primer algoritmo.
Pobl = Poblacion(matDist=matrizDistancias,matFlujo=matrizFlujos,Nind=50)
i = 0
n = 0
while i < 50000:
    #if n %25== 0:
        #print("Costes de la poblacion:")
        #print([i.coste() for i in Pobl.popu])
    print(str(int(i/500.0))+"%  en la generacion "+str(n))
    print("Mejor coste hasta ahora: "+str(Pobl.mejor.coste()))
    #print(i)
    n+=1
    i += Pobl.proximaGeneracion()


tiempo_final = time()

first_sol = Pobl.mejor

with open(printFile,'w') as f:
    f.write(str(first_sol)+ "\n")
    f.write("TiempoGenetico1:\t" + str(tiempo_final-tiempo_inicial)+ "\n")
    f.write("CosteGenetico1:\t"+ str(coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = first_sol.P)) + "\n")

    # Mejor Solucion

    mejorPerm, newCost = readSolution(solveName)


    mejorSol = Permutacion(P=mejorPerm,F=matrizFlujos,D = matrizDistancias)

    f.write(str(mejorSol)+"\n")
    f.write("Mejor:\t"+str(newCost)+"\n")
