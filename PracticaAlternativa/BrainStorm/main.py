#!/usr/bin/env python3

import sys
import numpy as np
from benchmark import Benchmark
import math
import random

from solution import *


if len(sys.argv) < 6:
    print("Use: ./main.py <problem id> <dimension> <n_ideas> <seed> <output file>")
    sys.exit()
idProblem = int(sys.argv[1])
dimension = int(sys.argv[2])
nIdeas = int(sys.argv[3])
seed = int(sys.argv[4])
outFile = sys.argv[5]
nClusters = 5
random.seed(seed)
bench = Benchmark()
coste = bench.getFuncion(idProblem)


inf = bench.getLimInf()
sup = bench.getLimSup()

ideas = [Idea.randIdea(coste,id,dimension,inf,sup) for i in range(nIdeas)]
# Primeras ideas creadas. Ahora el algoritmo...
nEval = 2000
for i in range(nEval):
    # Copiamos las ideas en el orden en el que estan
    newIdeas = [idea.copia() for idea in ideas]

    # Generamos los clusters a partir de las ideas de esta fase.
    modify = False
    while not modify:
        clusters = clustering(newIdeas)
        # Vemos si tenemos que mutar algun representande de cluster.
        muteProb = random.random()
        if muteProb < 0.2:
            clusterToModif = random.randrange(len(clusters))
            clusters[clusterToModif].clusterRepresent() = clusters[clusterToModif].clusterRepresent().muta(i,nEval)
            if clusters[clusterToModif].clusterRepresent().coste() < ideas[clusters[clusterToModif].clusterRepresent().id].coste():
                ideas[clusters[clusterToModif].clusterRepresent().id] = clusters[clusterToModif].clusterRepresent()
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
                selectedCluster.clusterRepresent() = selectedCluster.clusterRepresent().muta(i,nEval)
                if selectedCluster.clusterRepresent().coste() < ideas[selectedCluster.clusterRepresent().id].coste():
                    ideas[selectedCluster.clusterRepresent().id] = selectedCluster.clusterRepresent()
                    modify = True

            else:
                ideaSelected = choice(selectedCluster.ideas)
                ideaSelected = ideaSelected.muta(i,nEval)
                if ideaSelected.coste() < ideas[ideaSelected.id].coste():
                    ideas[ideaSelected.id] = ideaSelected
                    modify = True

        else:
            # Escogemos aleatoriamente un par de clusters.
            R = random.randrange(len(clusters)*(len(clusters)-1))
            i = R%len(clusters)
            j = R//len(clusters)
            if i >= j:
                i+=1
            firstClust = clusters[i]
            secondClust = clusters[j]

            centersSelected = random.random()
            if centersSelected < 0.5:
                firstClust.clusterRepresent() = combinationMean(firstClust.clusterRepresent(),secondClust.clusterRepresent())

                if firstClust.clusterRepresent().coste() < ideas[firstClust.clusterRepresent().id].coste():
                    ideas[firstClust.clusterRepresent().id] = firstClust.clusterRepresent()
                    modify = True

            else:
                idea1Selected = choice(firstClust.ideas)
                idea2Selected = choice(secondClust.ideas)
                idea1Selected = combinationMean(idea1Selected,idea2Selected)
                if idea1Selected.coste() < ideas[idea1Selected.id].coste():
                    ideas[idea1Selected.id] = idea1Selected
                    modify = True

        print(i)
        











##
