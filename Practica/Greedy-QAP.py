#!/usr/bin/python3

import sys
import math
from solucion import Permutacion
from solucion import coste
if len(sys.argv) < 2:
    print("Fatal Error, no file as input")

fileName = sys.argv[1]
if len(sys.argv) >= 2:
    solveName = sys.argv[2]

else:
    exit()

with open(fileName,'r') as infile:
    n = int(infile.readline())
    infile.readline()
    matrizFlujos = [infile.readline().split() for i in range(n)]
    infile.readline()
    matrizDistancias = [infile.readline().split() for i in range(n)]


def ordenSuma(matrizFlujos):
    orden = [(i,sum(matrizFlujos[i])) for i in range(len(matrizFlujos))]
    return sorted(orden,key=lambda val: val[1])


matrizFlujos = [[int(matrizFlujos[i][j]) for j in range(n)] for i in range(n)]
matrizDistancias = [[int(matrizDistancias[i][j]) for j in range(n)] for i in range(n)]

# Lectura del problema hecho.

greedySolution = [-1 for i in range(n)]

ordenFlujos = ordenSuma(matrizFlujos)[::-1]
ordenDistancias = ordenSuma(matrizDistancias)

for i in range(n):
    greedySolution[ordenDistancias[i][0]] = ordenFlujos[i][0]
# print(greedySolution)
greedySol = Permutacion(permutation=greedySolution,matrizFlujos=matrizFlujos,matrizDistancias=matrizDistancias)
print(greedySol)
print( coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = greedySol.permutation))

# Ahora comienza la búsqueda local.

bitsArray = [0 for i in range(n)]


mejora = True

while mejora:
    mejora = False
    for i in range(n):
        mejoraInterna = False
        if bitsArray[i] == 0:
            for j in range(n):
                if j != i:
                    difCoste = greedySol.difCoste(i,j)
                    if difCoste < 0:
                        mejora = mejoraInterna = True
                        bitsArray[i] = bitsArray[j] = 0
                        greedySol = greedySol.vecino(i,j)
            if mejoraInterna == False:
                bitsArray[i] = 1


print(greedySol)
print( coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = greedySol.permutation))

# Búsqueda local realizada.



with open(solveName,'r') as infile:
    primeraLinea = infile.readline().split()
    newN = int(primeraLinea[0])
    newCost = int(primeraLinea[1])
    mejorPerm = []
    for line in infile:
        lista = line.split()
        for i in lista:
            mejorPerm.append(int(i)-1)


mejorSol = Permutacion(permutation=mejorPerm,matrizFlujos=matrizFlujos,matrizDistancias = matrizDistancias)
print(mejorSol)
print( coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = mejorSol.permutation))









# Escritura de fichero.
'''
with open(fileName,'w') as outfile:
    outfile.write(str(len(slices))+'\n')
    for sl in slices:
        outfile.write(sl+'\n')
'''
