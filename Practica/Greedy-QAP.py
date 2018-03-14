#!/usr/bin/python3

import sys
import math
from solucion import Permutacion
from solucion import coste
from solucion import readData,readSolution
import numpy
if len(sys.argv) < 2:
    print("Fatal Error, no file as input")

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

ordenFlujos = ordenSuma(matrizFlujos)[::-1]
ordenDistancias = ordenSuma(matrizDistancias)

for i in range(n):
    greedySolution[ordenDistancias[i][0]] = ordenFlujos[i][0]
# print(greedySolution)
greedySol = Permutacion(P=greedySolution,F=matrizFlujos,D=matrizDistancias)
print(greedySol)
print( coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = greedySol.P))

# Ahora comienza la búsqueda local.

BLSol = greedySol.busquedaLocal()


print(BLSol)
print( coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = BLSol.P))

# Búsqueda local realizada.



mejorPerm, newCost = readSolution(solveName)


mejorSol = Permutacion(P=mejorPerm,F=matrizFlujos,D = matrizDistancias)

print(mejorSol)
print(newCost)









# Escritura de fichero.
'''
with open(fileName,'w') as outfile:
    outfile.write(str(len(slices))+'\n')
    for sl in slices:
        outfile.write(sl+'\n')
'''
