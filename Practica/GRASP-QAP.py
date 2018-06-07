#!/usr/bin/python3

import sys
import math
from solucion import Permutacion
from solucion import coste
from solucion import readData,readSolution
from time import time
from random import seed,shuffle,random,randrange,sample
import numpy


def ordenSuma(matriz):
    orden = []
    for i in range(len(matriz)):
        potencial = 0
        for j in range(len(matriz)):
            potencial+=matriz[i][j] + matriz[j][i]
        orden.append((i,potencial))
    return orden

def costeAsignacion(D,F,S,r,s):
    # r es la instalacion
    # s es la ubicacion
    coste = 0
    # i es la instalación
    for i in range(len(S)):
        if S[i] != -1:
            coste+= F[r][i]*D[s][S[i]]+F[i][r]*D[S[i]][s]
    return coste

def candidatos(D,F,S):
    candidatos = []
    S_c = range(len(S))
    S_c = list(set(S_c)-set(S))

    # i representa una instalación
    for i in range(len(F)):
        if S[i] == -1:
            # j representa una ubicación
            for j in S_c:
                candidatos.append(((i,j),costeAsignacion(D,F,S,i,j)))
    return candidatos


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
mejorSol = None
mejorCoste = -1
for m in range(25):
    # El mayor flujo es el más prometedor, orden inverso
    ordenFlujos = ordenSuma(matrizFlujos)[::-1]
    maximoF = max([ordenFlujos[i][1] for i in range(len(ordenFlujos))])
    minimoF = min([ordenFlujos[i][1] for i in range(len(ordenFlujos))])
    # La menor distancia es el más prometedor, orden normal.
    ordenDistancias = ordenSuma(matrizDistancias)
    maximoD = max([ordenDistancias[i][1] for i in range(len(ordenDistancias))])
    minimoD = min([ordenDistancias[i][1] for i in range(len(ordenDistancias))])

    umbralFlujos = maximoF -0.3*(maximoF-minimoF)
    umbralDistancias = minimoD + 0.3*(maximoD-minimoD)

    i=0
    mejores = []
    while  i < len(ordenFlujos):
        if ordenFlujos[i][1] <= umbralFlujos:
            mejores.append(ordenFlujos[i])
        i+=1
    ordenFlujos = mejores
    i=0
    mejores = []
    while i < len(ordenDistancias):
        if ordenDistancias[i][1] >= umbralDistancias:
            mejores.append(ordenDistancias[i])
        i+=1
    ordenDistancias = mejores
    # Ya tenemos los primeros candidatos.
    solucion = [-1 for i in matrizFlujos]

    ordenFlujos = sample(ordenFlujos,2)
    ordenDistancias = sample(ordenDistancias,2)
    solucion[ordenFlujos[0][0]] = ordenDistancias[0][0]
    solucion[ordenFlujos[1][0]] = ordenDistancias[1][0]


    # Primera etapa conseguida.


    for i in range(n-2):
        candidats = candidatos(D=matrizDistancias,F=matrizFlujos,S=solucion)
        maximo = max([candidats[i][1] for i in range(len(candidats))])
        minimo = min([candidats[i][1] for i in range(len(candidats))])
        umbral = minimo+0.3*(maximo-minimo)
        i=0
        mejores = []
        while i < len(candidats):
            if candidats[i][1] >= umbral:
                mejores.append(candidats[i])
            i+=1
        candidats = mejores
        candidats = sample(candidats,1)
        solucion[candidats[0][0][0]] = candidats[0][0][1]


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
