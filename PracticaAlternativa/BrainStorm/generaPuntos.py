import random
import math
import numpy as np

def eucDist(p1,p2):
    d = 0
    for i in range(len(p1)):
        d+= (p1[i]-p2[i])**2
    return d


def coste(punto):
    cost = 0

    for i in punto:
        cost += abs(math.cos(20*i))
    return cost


def clusDist(c1,c2):
    dist = eucDist(c1[0],c2[0])
    for i in c1:
        for j in c2:
            newDist = eucDist(i,j)
            if newDist < dist:
                dist = newDist

    return dist


def clustering(puntos,clust = 5):
    nClusters = len(puntos)
    clusters = [[punto] for punto in puntos]

    while len(clusters) > clust:
        X,Y = 0, 1
        minDist = clusDist(clusters[0],clusters[1])
        for i in range(len(clusters)):
            for j in range(i+1,len(clusters)):
                otherDist = clusDist(clusters[i],clusters[j])
                if otherDist < minDist:
                    minDist = otherDist
                    X = i
                    Y = j
        clusters[X]+=clusters.pop(Y)
    return clusters


def clusterRepresent(clust):
    mejor = 0
    mejorCoste = coste(clust[0])

    for i in range(len(clust)):
        newCost = coste(clust[i])
        if newCost < mejorCoste:
            newCost = mejorCoste
            mejor = i

    return mejor

def sigmoid(x):
    return 1/(1+np.exp(-x))

def modificaPunto(p,currentiter,maxiter):
    newP = p[:]
    for i in range(len(p)):
        newP[i] = newP[i] + random.random()*sigmoid((maxiter/2.0-currentiter)/20)*np.random.normal(0,1)
    return newP

random.seed(100)
puntos = []
for i in range(50):
    X,Y= random.random()*2-1,random.random()*2-1
    puntos.append([X,Y])
    print(X,Y)

clusters = clustering(puntos=puntos)
j=1
for i in clusters:
    print("Cluster "+str(j))
    j+=1

    for k in i:
        string = ""
        for v in k:
            string += str(v)+"\t"

        print(string)

for i in clusters:
    print("Mejor representante:")
    string = ""
    represent = clusterRepresent(i)
    for j in i[represent]:
        string += str(j) + "\t"
    print(string)

print("Cómo modifica cada vez la función de \"mutacion\"")
for i in range(200):
    represent =[0,0]
    print("Representante modificado:" + str(modificaPunto(represent,maxiter=200,currentiter=i)))
