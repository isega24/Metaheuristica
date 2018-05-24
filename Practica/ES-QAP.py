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
solVecina = mejorSol.copia()
mejorCoste = mejorSol.coste()
maxExitos = len(matrizFlujos)
maxVecinosGenerados = 10*maxExitos
M = 50000/maxVecinosGenerados
T0 = 0.3*mejorCoste/(-math.log(0.3))
TF = min(T0,1.0/1000)
beta = (T0-TF)/(M*T0*TF)

T = T0
while T > TF:
    exitos = 0
    vecinosgenerados = 0
    while exitos < maxExitos and maxVecinosGenerados > vecinosgenerados:
        randNum = randrange(len(matrizFlujos)**2-len(matrizFlujos))

        j = randNum//len(matrizFlujos)
        i = randNum%len(matrizFlujos)
        vecinosgenerados+=1
        if j >= i:
            j+=1
        difCost = solVecina.difCoste(i,j)
        if difCost < 0 or random()<= math.exp(-difCost/T):
            solVecina = solVecina.vecino(i,j)
            if solVecina.coste() < mejorCoste:
                mejorCoste = solVecina.coste()
                mejorSol = solVecina.copia()
    T = T/(1+beta*T)

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
