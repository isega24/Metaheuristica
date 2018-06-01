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
random.seed(None)
bench = Benchmark()
def coste(array):
    return cec14(array,idProblem+1)
np.random.seed(seed)


inf = bench.getLimInf()
sup = bench.getLimSup()

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
    modify = False
    if i %1 == 0:
        clusters = clustering(newIdeas)
    while not modify and nEvalCostFunc < maxEvalCostFunc:
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
                modify = True

        # Vemos si tenemos que explotar un cluster o combinar dos ideas
        # de clusters distintos.
        explotationProb = random.random()
        if explotationProb < 0.8:
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
            if clusterSelection < 0.4:
                represent = selectedCluster.clusterRepresent()
                represent.cambia(selectedCluster.clusterRepresent().muta(nEvalCostFunc,maxEvalCostFunc))
                if selectedCluster.clusterRepresent().coste() < ideas[selectedCluster.clusterRepresent().id].coste():
                    ideas[selectedCluster.clusterRepresent().id].cambia(selectedCluster.clusterRepresent())
                    modify = True

            else:
                ideaSelected = random.choice(selectedCluster.ideas)
                ideaSelected.cambia(ideaSelected.muta(nEvalCostFunc,maxEvalCostFunc))
                if ideaSelected.coste() < ideas[ideaSelected.id].coste():
                    ideas[ideaSelected.id].cambia(ideaSelected)
                    modify = True

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
            if centersSelected < 0.5:
                represent = firstClust.clusterRepresent()
                represent.cambia(combinationDiffEvo(firstClust.clusterRepresent(),secondClust.clusterRepresent(),thirdClust.clusterRepresent()))

                if firstClust.clusterRepresent().coste() < ideas[firstClust.clusterRepresent().id].coste():
                    ideas[firstClust.clusterRepresent().id].cambia(firstClust.clusterRepresent())
                    modify = True

            else:
                idea1Selected = random.choice(firstClust.ideas)
                idea2Selected = random.choice(secondClust.ideas)
                idea3Selected = random.choice(thirdClust.ideas)
                idea1Selected = combinationDiffEvo(idea1Selected,idea2Selected,idea3Selected)
                if idea1Selected.coste() < ideas[idea1Selected.getId()].coste():
                    ideas[idea1Selected.id].cambia(idea1Selected)
                    modify = True

    if i % 10==0:
        print(i)
        print("Mejor coste hasta ahora: "+str(min([idea.coste() for idea in ideas])-100*idProblem ))
        print(str(nEvalCostFunc/maxEvalCostFunc*100.0)+"%  realizado")



with open("./solucionesDimension"+str(dimension)+"/funcion"+str(idProblem+1)+".sol",'w') as f:
    mejorIdea = ideas[0]
    for idea in ideas:
        if idea.coste()< mejorIdea.coste():
            mejorIdea = idea
    string = ""
    for i in mejorIdea.array:
        string+=str(i)+"\t"
    string+="\n"
    f.write("MejorCoste:\t"+str(mejorIdea.coste())+"\n")
    f.write(string)









##
