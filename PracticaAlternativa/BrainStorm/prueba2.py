#!/usr/bin/env python3

import sys
import numpy as np
#from benchmark import Benchmark
import math
import random

from solution import *


dimension = 2
nIdeas = 100

nClusters = 5
random.seed(None)
np.random.seed(None)
#bench = Benchmark()
def coste(array):

    #return array[1]**2+array[0]**4-array[0]**2-array[0]
    cost = 10*len(array)
    for i in array:
        cost+=i**2-10*math.cos(2*math.pi*i)
    return cost


inf = -100.0 #bench.getLimInf()
sup = 100.0 #bench.getLimSup()

ideas = [Idea.randIdea(coste,i,dimension,inf,sup) for i in range(nIdeas)]
# Primeras ideas creadas. Ahora el algoritmo...
nEval = 2000
maxEvalCostFunc = 10000*dimension
nEvalCostFunc = 100
i = -1
clusters = clusteringCentroid(ideas,clust=nClusters)
while nEvalCostFunc < maxEvalCostFunc:
    i+=1
    nuevasIdeas = []
    for cluster in clusters:
        nuevasIdeas+= cluster.ideas
    clusters = clusteringCentroid(ideas,clust=nClusters)
    # Copiamos las ideas en el orden en el que estan

    if i%1==0:
        j=0
        t = 0
        for m in clusters:
            t+=1
            printFile = "cluster"+str(t)+"Gen"+str(i)+".cl"
            with open("./generacionesPruebas/"+printFile,'w') as f:
                j+=1

                for k in m.ideas:
                    string = ""
                    for v in k.array:
                        string += str(v)+"\t"

                    f.write(string+"\n")

        printFile = "representantesGen"+str(i)+".cl"
        with open("./generacionesPruebas/"+printFile,'w') as f:
            for m in clusters:
                string = ""
                represent = m.clusterRepresent()
                for j in represent.array:
                    string += str(j) + "\t"
                f.write(string+"\n")

    # Generamos los clusters a partir de las ideas de esta fase.
    modify = False
    while not modify:
        nEvalCostFunc+=1
        #if i %5 == 0:

        # Vemos si tenemos que mutar algun representande de cluster.
        muteProb = random.random()
        if muteProb < 0.2:
            clusterSelection = random.randrange(len(ideas))
            ideal = 0
            clusterS = 0
            while ideal < clusterSelection:
                ideal += len(clusters[clusterS].ideas)
                clusterS+=1

            clusterS-=1
            clusterS = max(0,clusterS)

            clusterToModif = clusterS
            clusterToModify = clusters[clusterToModif]
            represent = clusterToModify.clusterRepresent()
            ideaCambiada = Idea.randIdea(represent.costFunc,represent.getId(),dimension,inf,sup)
            if represent.coste() > ideaCambiada.coste():
                clusters[clusterToModif].quitaPunto(represent)
                clusters[clusterToModif].aniadePunto(ideaCambiada)
                modify = True

        # Vemos si tenemos que explotar un cluster o combinar dos ideas
        # de clusters distintos.
        explotationProb = random.random()
        if explotationProb < 0.8:
            # Hay que escoger un cluster con una probabilidad
            # variable, dependiendo del numero de ideas de cada cluster.
            ###########################################################
            # Ahora no lo estamos haciendo.

            clusterSelection = random.randrange(len(ideas))
            ideal = 0
            clusterS = 0
            while ideal < clusterSelection:
                ideal += len(clusters[clusterS].ideas)
                clusterS+=1

            clusterS-=1
            clusterS = max(0,clusterS)

            selectedCluster = clusters[clusterS]
            clusterSelection = random.random()
            if clusterSelection < 0.3:
                represent = selectedCluster.clusterRepresent()
                ideaCambiada = selectedCluster.clusterRepresent().muta(i,nEval)

                if represent.coste() > ideaCambiada.coste():
                    selectedCluster.quitaPunto(represent)

                    masCercano = 0
                    distanciaCercana = eucDistCentroid(clusters[masCercano].centroid,ideaCambiada.array)
                    for j in range(len(clusters)):
                        nuevaDistancia = eucDistCentroid(clusters[j].centroid,ideaCambiada.array)
                        if nuevaDistancia < distanciaCercana:
                            distanciaCercana = nuevaDistancia
                            masCercano = j
                    selectedCluster = clusters[masCercano]
                    selectedCluster.aniadePunto(ideaCambiada)
                    modify = True

            else:
                ideaSelected = random.choice(selectedCluster.ideas)
                ideaCambiada = ideaSelected.muta(i,nEval)

                if ideaSelected.coste() > ideaCambiada.coste():
                    selectedCluster.quitaPunto(ideaSelected)
                    masCercano = 0
                    distanciaCercana = eucDistCentroid(clusters[masCercano].centroid,ideaCambiada.array)
                    for j in range(len(clusters)):
                        nuevaDistancia = eucDistCentroid(clusters[j].centroid,ideaCambiada.array)
                        if nuevaDistancia < distanciaCercana:
                            distanciaCercana = nuevaDistancia
                            masCercano = j
                    selectedCluster = clusters[masCercano]
                    selectedCluster.aniadePunto(ideaCambiada)
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
                ideaCambiada = combinationDiffEvo(firstClust.clusterRepresent(),secondClust.clusterRepresent(),thirdClust.clusterRepresent())

                if represent.coste() > ideaCambiada.coste():
                    firstClust.quitaPunto(represent)

                    masCercano = 0
                    distanciaCercana = eucDistCentroid(clusters[masCercano].centroid,ideaCambiada.array)
                    for j in range(len(clusters)):
                        nuevaDistancia = eucDistCentroid(clusters[j].centroid,ideaCambiada.array)
                        if nuevaDistancia < distanciaCercana:
                            distanciaCercana = nuevaDistancia
                            masCercano = j
                    selectedCluster = clusters[masCercano]

                    selectedCluster.aniadePunto(ideaCambiada)
                    modify = True

            else:
                idea1Selected = random.choice(firstClust.ideas)
                idea2Selected = random.choice(secondClust.ideas)
                idea3Selected = random.choice(thirdClust.ideas)
                ideaCambiada = combinationDiffEvo(idea1Selected,idea2Selected,idea3Selected)

                if idea1Selected.coste() > ideaCambiada.coste():
                    firstClust.quitaPunto(idea1Selected)

                    masCercano = 0
                    distanciaCercana = eucDistCentroid(clusters[masCercano].centroid,ideaCambiada.array)
                    for j in range(len(clusters)):
                        nuevaDistancia = eucDistCentroid(clusters[j].centroid,ideaCambiada.array)
                        if nuevaDistancia < distanciaCercana:
                            distanciaCercana = nuevaDistancia
                            masCercano = j
                    selectedCluster = clusters[masCercano]

                    selectedCluster.aniadePunto(ideaCambiada)
                    modify = True
    if i % 10==0:
        print(i)
        ideasInClusters = []
        for cluster in clusters:
            ideasInClusters+=cluster.ideas
        print("Mejor coste hasta ahora: "+str(min([idea.coste() for idea in ideasInClusters])))
        print(str(nEvalCostFunc/maxEvalCostFunc*100.0)+"%  realizado")














##
