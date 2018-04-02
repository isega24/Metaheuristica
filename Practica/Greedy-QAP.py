#!/usr/bin/python3

import sys
import math
from solucion import Permutacion
from solucion import coste
from solucion import readData,readSolution
from time import time
from random import seed,shuffle
import numpy
if len(sys.argv) < 2:
    print("Fatal Error, no file as input")
if len(sys.argv) >=3:
    randseed = int(sys.argv[2])
    seed(randseed)
fileName = sys.argv[1]
solveName = "./qapsoln/"+fileName[10:-3]+"sln"

n,matrizFlujos,matrizDistancias = readData(filename=fileName)
matrizFlujos = numpy.array(matrizFlujos)
matrizDistancias = numpy.array(matrizDistancias)
n = int(n)


def ordenSuma(matriz):
    orden = [(i,sum(matriz[i])) for i in range(len(matriz))]
    return sorted(orden,key=lambda val: val[1])


matrizFlujos = [[int(matrizFlujos[i][j]) for j in range(len(matrizFlujos[i]))] for i in range(len(matrizFlujos))]
matrizDistancias = [[int(matrizDistancias[i][j]) for j in range(len(matrizDistancias[i]))] for i in range(len(matrizFlujos))]

# Lectura del problema hecho.

greedySolution = [-1 for i in range(n)]

# Iniciamos el conteo de tiempo.
tiempo_inicial = time()
ordenFlujos = ordenSuma(matrizFlujos)[::-1]
ordenDistancias = ordenSuma(matrizDistancias)

for i in range(n):
    greedySolution[ordenDistancias[i][0]] = ordenFlujos[i][0]

tiempo_greedy = time()
# print(greedySolution)
greedySol = Permutacion(P=greedySolution,F=matrizFlujos,D=matrizDistancias)
print(greedySol)
print("TiempoGreedy:\t" + str(tiempo_greedy-tiempo_inicial))
print("CosteGreedy:\t"+ str(coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = greedySol.P)))

# Ahora comienza la búsqueda local.
tiempo_inicio_BL = time()
BLSol = greedySol.busquedaLocal(MaxIter=50000)
tiempo_final_BL = time()


print(BLSol)
print("TiempoBL:\t" + str(tiempo_greedy-tiempo_inicial + tiempo_final_BL - tiempo_inicio_BL))
print("CosteBL:\t" +str(coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = BLSol.P)))

# Búsqueda local realizada.



mejorPerm, newCost = readSolution(solveName)


mejorSol = Permutacion(P=mejorPerm,F=matrizFlujos,D = matrizDistancias)

print(mejorSol)
print("Mejor:\t"+str(newCost))
