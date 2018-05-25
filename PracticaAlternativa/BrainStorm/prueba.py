#!/usr/bin/env python3

import sys
import numpy as np
#from benchmark import Benchmark
import math
import random

from solution import *


dimension = 2
nIdeas = 20

nClusters = 5
random.seed(None)
#bench = Benchmark()
def coste(array):
    cost = 0
    for i in array:
        cost+=i**2
    return cost


inf = -100 #bench.getLimInf()
sup = 100.0 #bench.getLimSup()

ideas = [Idea.randIdea(coste,i,dimension,inf,sup) for i in range(nIdeas)]
# Primeras ideas creadas. Ahora el algoritmo...
nEval = 1000
for i in range(nEval):
    # Copiamos las ideas en el orden en el que estan
    newIdeas = [idea.copia() for idea in ideas]
    clusters = clustering(newIdeas)
    if i%10==0:
        j=0
        print("Generacion " + str(i))
        for m in clusters:
            print("Cluster "+str(j))
            j+=1

            for k in m.ideas:
                string = ""
                for v in k.array:
                    string += str(v)+"\t"

                print(string)

        for m in clusters:
            print("Mejor representante:")
            string = ""
            represent = m.clusterRepresent()
            for j in represent.array:
                string += str(j) + "\t"
            print(string)

    # Generamos los clusters a partir de las ideas de esta fase.
    modify = False
    Fails = 0
    while not modify and Fails < 2000:
        Fails+=1
        #if i %5 == 0:

        # Vemos si tenemos que mutar algun representande de cluster.
        muteProb = random.random()
        if muteProb < 0.2:
            clusterToModif = random.randrange(len(clusters))
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

            selectedCluster = random.choice(clusters)
            clusterSelection = random.random()
            if clusterSelection < 0.4:
                represent = selectedCluster.clusterRepresent()
                represent.cambia(selectedCluster.clusterRepresent().muta(i,nEval))
                if selectedCluster.clusterRepresent().coste() < ideas[selectedCluster.clusterRepresent().id].coste():
                    ideas[selectedCluster.clusterRepresent().id].cambia(selectedCluster.clusterRepresent())
                    modify = True

            else:
                ideaSelected = random.choice(selectedCluster.ideas)
                ideaSelected.cambia(ideaSelected.muta(i,nEval))
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














##
