#!/usr/bin/python3

import sys
import math
from solucion import Permutacion
from solucion import coste
from solucion import readData,readSolution
from time import time
from random import seed,shuffle,random,randrange
import numpy


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
# Algoritmo.

mejorSol = Permutacion.randPerm(D=matrizDistancias,F=matrizFlujos)
mejorSol = mejorSol.ES(nBusquedas=50000)

tiempo_final = time()

# Se guarda es MejorES a la mejor solución por enfriamiento simulado.
first_sol = mejorSol

with open(printFile,'w') as f:
    f.write(str(first_sol)+ "\n")
    f.write("TiempoES:\t" + str(tiempo_final-tiempo_inicial)+ "\n")
    f.write("CosteES:\t"+ str(coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = first_sol.P)) + "\n")

    # Mejor Solucion

    mejorPerm, newCost = readSolution(solveName)


    mejorSol = Permutacion(P=mejorPerm,F=matrizFlujos,D = matrizDistancias)

    f.write(str(mejorSol)+"\n")
    f.write("Mejor:\t"+str(newCost)+"\n")
