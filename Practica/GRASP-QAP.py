#!/usr/bin/python3

import sys
import math
from solucion import Permutacion
from solucion import coste
from solucion import readData,readSolution
from time import time
from random import seed,shuffle,random,randrange
import numpy


def ordenSuma(matriz):
    orden = []
    for i in range(len(matriz)):
        potencial = 0
        for j in range(len(matriz)):
            potencial+=matriz[i][j] + matriz[j][i]
        orden.append((i,potencial))
    return sorted(orden,key=lambda val: val[1])

def costeAsignacion(D,F,S,r,s):
    coste = 0
    for i in range(len(S)):
        if S[i] != -1:
            coste+= F[r][i]*D[s][S[i]]+F[i][r]*D[S[i]][r]
    return coste

def candidatos(D,F,S):
    candidatos = []
    # i representa una localizacion
    for i in range(len(D)):
        if S[i] == -1:
            # j representa un establecimiento
            for j in range(len(F)):
                if j not in S:
                    candidatos.append(((j,i),costeAsignacion(D,F,S,i,j)))
    return sorted(candidatos,key=lambda val: val[1])


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
for m in range(25):
    # El mayor flujo es el más prometedor, orden inverso
    ordenFlujos = ordenSuma(matrizFlujos)[::-1]
    # La menor distancia es el más prometedor, orden normal.
    ordenDistancias = ordenSuma(matrizDistancias)
    umbralFlujos = ordenFlujos[0][1] -0.3*(ordenFlujos[0][1]-ordenFlujos[-1][1])
    umbralDistancias = ordenDistancias[0][1] + 0.3*(ordenDistancias[-1][1]-ordenDistancias[0][1])

    umbralSuperado = False
    i=0
    while not umbralSuperado and i < len(ordenFlujos):
        if ordenFlujos[i][1] < umbralFlujos:
            umbralSuperado = True
            ordenFlujos = ordenFlujos[0:min(i+1,len(ordenFlujos))]
        i+=1
    umbralSuperado = False
    i=0
    while not umbralSuperado and i < len(ordenDistancias):
        if ordenDistancias[i][1] > umbralDistancias:
            umbralSuperado = True
            ordenDistancias =ordenDistancias[0:min(i+1,len(ordenDistancias))]
        i+=1
    # Ya tenemos los primeros candidatos.
    solucion = [-1 for i in matrizFlujos]

    shuffle(ordenFlujos)
    shuffle(ordenDistancias)
    solucion[ordenFlujos[0][0]] = ordenDistancias[0][0]
    solucion[ordenFlujos[1][0]] = ordenDistancias[1][0]


    # Primera etapa conseguida.
    mejorCoste = -1
    mejorSol = None

    for i in range(n-2):
        candidats = candidatos(D=matrizDistancias,F=matrizFlujos,S=solucion)

        umbral = candidats[0][1]+0.3*(candidats[-1][1]-candidats[0][1])
        umbralSuperado = False
        i=0
        while not umbralSuperado and i < len(candidats):
            if candidats[i][1] > umbral:
                umbralSuperado = True
                candidats = candidats[0:i]
            i+=1
        shuffle(candidats)
        solucion[candidats[0][0][1]] = candidats[0][0][0]


    if mejorSol == None:
        mejorSol,l = Permutacion(solucion,matrizDistancias,matrizFlujos).busquedaLocal(50000//25)
        mejorCoste = mejorSol.coste()
    else:
        unaSol,l = Permutacion(solucion,matrizDistancias,matrizFlujos).busquedaLocal(50000//25)
        if unaSol.coste() < mejorCoste:
            mejorSol = unaSol
            mejorCoste = mejorSol.coste()

tiempo_final = time()

first_sol = mejorSol
# Se guarda es MejorES a la mejor solución por enfriamiento simulado.

with open(printFile,'w') as f:
    f.write(str(first_sol)+ "\n")
    f.write("TiempoGRASP:\t" + str(tiempo_final-tiempo_inicial)+ "\n")
    f.write("CosteGRASP:\t"+ str(coste( matDist = matrizDistancias, matFlujo = matrizFlujos,perm = first_sol.P)) + "\n")

    # Mejor Solucion

    mejorPerm, newCost = readSolution(solveName)


    mejorSol = Permutacion(P=mejorPerm,F=matrizFlujos,D = matrizDistancias)

    f.write(str(mejorSol)+"\n")
    f.write("Mejor:\t"+str(newCost)+"\n")
