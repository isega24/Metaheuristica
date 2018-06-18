#!/usr/bin/env python3

import sys
import numpy as np
from benchmark import Benchmark
from cec2014 import cec14
import math
import random

from solution import *


if len(sys.argv) < 5:
    print("Use: ./main.py <problem id> <dimension> <n_ideas> <seed>")
    sys.exit()
idProblem = int(sys.argv[1])
dimension = int(sys.argv[2])
nIdeas = int(sys.argv[3])
seed = int(sys.argv[4])
nClusters = 5
maxExplProb = 0.0
maxCenterSelected = 0.5
maxClusterSelection = 0.5
random.seed(None)
bench = Benchmark()
def coste(array):
    return cec14(array,idProblem+1)
np.random.seed(seed)
outFile = "./solucionesDimension"+str(dimension)+"/funcion"+str(idProblem)+".sol"
print(outFile)


inf = bench.getLimInf()
sup = bench.getLimSup()
costes = 0
nEjec = 10
for ejecucion in range(nEjec):
    ideas = [Idea.randIdea(coste,i,dimension,inf,sup) for i in range(nIdeas)]
    # Primeras ideas creadas. Ahora el algoritmo...
    maxEvalCostFunc = 10000*dimension
    nEvalCostFunc = 0
    i = -1
    while nEvalCostFunc < maxEvalCostFunc:
        i+=1
        # Copiamos las ideas en el orden en el que estan
        newIdeas = [idea.copia() for idea in ideas]

        # Generamos los clusters a partir de las ideas de esta fase.
        modify = 0
        if i %1 == 0:
            clusters = clustering(newIdeas)
        while modify < nIdeas and nEvalCostFunc < maxEvalCostFunc:
            nEvalCostFunc+=1
            #if i %5 == 0:
            # Vemos si tenemos que mutar algun representande de cluster.
            muteProb = random.random()
            if muteProb < 0.2:
                clusterSelection = random.randrange(len(newIdeas))
                ideal = 0
                clusterS = 0
                while ideal < clusterSelection:
                    ideal += len(clusters[clusterS].ideas)
                    clusterS+=1

                clusterS-=1
                clusterS = max(0,clusterS)
                clusterToModif = clusterS
                represent = clusters[clusterToModif].clusterRepresent()
                represent.cambia(Idea.randIdea(represent.costFunc,represent.getId(),dimension,inf,sup))
                if clusters[clusterToModif].clusterRepresent().coste() < ideas[clusters[clusterToModif].clusterRepresent().id].coste():
                    ideas[clusters[clusterToModif].clusterRepresent().id].cambia(clusters[clusterToModif].clusterRepresent())
                    modify+=1

            # Vemos si tenemos que explotar un cluster o combinar dos ideas
            # de clusters distintos.
            explotationProb = random.random()
            if explotationProb < maxExplProb:
                # Hay que escoger un cluster con una probabilidad
                # variable, dependiendo del numero de ideas de cada cluster.
                ###########################################################
                # Ahora no lo estamos haciendo.

                clusterSelection = random.randrange(len(newIdeas))
                ideal = 0
                clusterS = 0
                while ideal < clusterSelection:
                    ideal += len(clusters[clusterS].ideas)
                    clusterS+=1

                clusterS-=1
                clusterS = max(0,clusterS)
                selectedCluster = clusters[clusterS]

                clusterSelection = random.random()
                if clusterSelection < maxClusterSelection:
                    represent = selectedCluster.clusterRepresent()
                    represent.cambia(selectedCluster.clusterRepresent().muta(nEvalCostFunc,maxEvalCostFunc))
                    if selectedCluster.clusterRepresent().coste() < ideas[selectedCluster.clusterRepresent().id].coste():
                        ideas[selectedCluster.clusterRepresent().id].cambia(selectedCluster.clusterRepresent())
                        modify+=1

                else:
                    ideaSelected = random.choice(selectedCluster.ideas)
                    ideaSelected.cambia(ideaSelected.muta(nEvalCostFunc,maxEvalCostFunc))
                    if ideaSelected.coste() < ideas[ideaSelected.id].coste():
                        ideas[ideaSelected.id].cambia(ideaSelected)
                        modify+=1

            else:
                # Escogemos aleatoriamente un par de clusters.
                R = random.randrange(len(clusters)*(len(clusters)-1))
                j = R%len(clusters)
                k = R//len(clusters)


                if k >= j:
                    k+=1
                l = k
                while l==k or l==j:
                    k = random.randrange(len(clusters))
                firstClust = clusters[j]
                secondClust = clusters[k]
                thirdClust = clusters[l]

                centersSelected = random.random()
                if centersSelected < maxCenterSelected:
                    nueveIdee = combinationDiffEvo(firstClust.clusterRepresent(),secondClust.clusterRepresent(),thirdClust.clusterRepresent())
                    nueveIdee.id = torneo([firstClust.clusterRepresent(),secondClust.clusterRepresent(),thirdClust.clusterRepresent()],nueveIdee)
                    if nueveIdee.getId() != -1 and nueveIdee.coste() < ideas[nueveIdee.getId()].coste():
                        ideas[nueveIdee.getId()].cambia(nueveIdee)
                        modify+=1

                else:
                    idea1Selected = random.choice(firstClust.ideas)
                    idea2Selected = random.choice(secondClust.ideas)
                    idea3Selected = random.choice(thirdClust.ideas)
                    nueveIdee = combinationDiffEvo(idea1Selected,idea2Selected,idea3Selected)
                    nueveIdee.id  = torneo([idea1Selected,idea2Selected,idea3Selected],nueveIdee)
                    if nueveIdee.getId() != -1 and nueveIdee.coste() < ideas[nueveIdee.getId()].coste():
                        ideas[nueveIdee.getId()].cambia(nueveIdee)
                        modify+=1

        if i % 1 == 0:
            print(i)
            print("Mejor coste hasta ahora: "+str(min([idea.coste() for idea in ideas])-100*(idProblem+1) ))
            print(str(nEvalCostFunc/maxEvalCostFunc*100.0)+"%  realizado")
    costes+=min([idea.coste() for idea in ideas])-100*(idProblem+1)
    print("Problema:" + str(idProblem+1)+ "\titeracion:"+str(ejecucion))


costes = costes/nEjec
print(costes)
with open(outFile,'w') as f:
    f.write(str(idProblem+1) + "\t" + str(costes) + "\n")









##
