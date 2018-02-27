#!/usr/bin/python3

import sys
import math
if len(sys.argv) != 2:
    print("Fatal Error, no file as input")

fileName = sys.argv[1]

with open(fileName,'r') as infile:
    n = int(infile.readline())
    infile.readline()
    matrizFlujo = [infile.readline().split() for i in range(n)]
    infile.readline()
    matrizDistancias = [infile.readline().split() for i in range(n)]

matrizFlujo = [[int(matrizFlujo[i][j]) for j in range(n)] for i in range(n)]
matrizDistancias = [[int(matrizDistancias[i][j]) for j in range(n)] for i in range(n)]

# Lectura del problema hecho.













# Escritura de fichero.
'''
with open(fileName+".out",'w') as outfile:
    outfile.write(str(len(slices))+'\n')
    for sl in slices:
        outfile.write(sl+'\n')
'''
