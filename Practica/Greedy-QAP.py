#!/usr/bin/python3

import sys
import math
from solucion import Permutacion
from solucion import coste
if len(sys.argv) != 2:
    print("Fatal Error, no file as input")

fileName = sys.argv[1]

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
greedySol = Permutacion(n=n,permutation=greedySolution,matrizFlujos=matrizFlujos,matrizDistancias=matrizDistancias)
print(greedySol.coste())









# Escritura de fichero.
'''
with open(fileName,'w') as outfile:
    outfile.write(str(len(slices))+'\n')
    for sl in slices:
        outfile.write(sl+'\n')
'''
