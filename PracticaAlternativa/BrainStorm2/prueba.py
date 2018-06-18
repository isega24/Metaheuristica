#!/usr/bin/env python3

import sys
import numpy as np
#from benchmark import Benchmark
import math
import random

from solution import *


dimension = 2
nIdeas = 100
maxExplProb = 0.0
maxCenterSelected = 0.5
maxClusterSelection = 0.5
nClusters = 5
random.seed(None)
np.random.seed(None)
#bench = Benchmark()
def coste(array):
    cost = 10*len(array)
    for i in array:
        cost+=i**2-10*math.cos(2*math.pi*i)
    return cost


inf = -100.0 #bench.getLimInf()
sup = 100.0 #bench.getLimSup()


# Primeras ideas creadas. Ahora el algoritmo...
nEval = 2000
maxEvalCostFunc = 100000*dimension

costes = 0
nEjec = 25
for ejec in range(nEjec):
    ideas = [Idea.randIdea(coste,i,dimension,inf,sup) for i in range(nIdeas)]
    nEvalCostFunc = 0
    i = -1
    while nEvalCostFunc < maxEvalCostFunc:
        i+=1
        # Copiamos las ideas en el orden en el que estan
        newIdeas = [idea.copia() for idea in ideas]
        if i % 1==0:
            clusters = clustering(newIdeas,clust=nClusters)
        ## Imprimir para los gráficos.
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
        modify = 0
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
            if explotationProb < maxExplProb:#nEvalCostFunc/maxEvalCostFunc:
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
                    represent.cambia(selectedCluster.clusterRepresent().muta(i,nEval))
                    if selectedCluster.clusterRepresent().coste() < ideas[selectedCluster.clusterRepresent().id].coste():
                        ideas[selectedCluster.clusterRepresent().id].cambia(selectedCluster.clusterRepresent())
                        mejora = True
                        while mejora:
                            represent = selectedCluster.clusterRepresent()
                            represent.cambia(selectedCluster.clusterRepresent().muta(i,nEval))
                            nEvalCostFunc+=1
                            if selectedCluster.clusterRepresent().coste() < ideas[selectedCluster.clusterRepresent().id].coste():
                                ideas[selectedCluster.clusterRepresent().id].cambia(selectedCluster.clusterRepresent())
                            else:
                                mejora = False

                        modify+=1

                else:
                    ideaSelected = random.choice(selectedCluster.ideas)
                    ideaSelected.cambia(ideaSelected.muta(i,nEval))
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
        if i % 1==0:
            ##print(i)
            print("Mejor coste hasta ahora: "+str(min([idea.coste() for idea in ideas])))
            print(str(nEvalCostFunc/maxEvalCostFunc*100.0)+"%  realizado")
            pass

    costes += min([idea.coste() for idea in ideas])
    print("Ejecucion " + str(ejec) +"\tCoste medio actual:"+str(int(100.0*costes/(ejec+1))/100.0 ))
costes /=nEjec

print("Coste de media: " + str(costes))











##
