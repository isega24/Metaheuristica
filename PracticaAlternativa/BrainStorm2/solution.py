

import random
import numpy as np
import sklearn
sup = 100.0
inf = -100.0


# Parámetros:
# ListaIdeas es una lista con ideas con identificadores distintos.
# nuevaIdea es una idea que competirá por entrar en la generación actual.
# Esta función devolverá una copia de nuevaIdea pero con el identificador
# de la peor idea de listaIdeas. En caso de que la nueva idea no supere en coste
# a ninguna, su identificador será -1.
def torneo(listaIdeas,nuevaIdea):
    cambiaPor = -1
    costeAnterior = listaIdeas[0].coste()+1
    for i in range(len(listaIdeas)):
        costeactual = listaIdeas[i].coste()
        if nuevaIdea.coste() < costeactual and costeAnterior < costeactual:
            cambiaPor = listaIdeas[i].getId()
            #print(i,costeactual,costeAnterior,nuevaIdea.coste(),cambiaPor)
            #input()
            costeAnterior = costeactual
    return cambiaPor


def combinationMean(idea1,idea2):
    return Idea(np.array([ (idea1.array[i]+idea2.array[i])/2 for i in range(len(idea1.array))]),idea1.costFunc,idea1.id)
def combinationDiffEvo(idea1,idea2,idea3):
    array = np.array(idea1.array[:])
    for i in range(len(array)):
        array[i]+= (idea3.array[i]-idea2.array[i])/2
        if array[i] > sup or array[i] < inf:
            array[i] = random.random()*(sup-inf)+inf
    return Idea(array,idea1.costFunc,idea1.id)
def eucDist(idea1,idea2):
    d = 0
    p1 = idea1.array
    p2 = idea2.array
    for i in range(len(p1)):
        d+= (p1[i]-p2[i])**2
    return d

def eucDistCentroid(centroid1,centroid2):
    d = 0
    if len(centroid1) == 0 or len(centroid2) == 0:
        return 0
    for i in range(len(centroid1)):
        d+= (centroid1[i]-centroid2[i])**2
    return d

def clusDist(c1,c2):
    dist = eucDist(c1.ideas[0],c2.ideas[0])
    for i in c1.ideas:
        for j in c2.ideas:
            newDist = eucDist(i,j)
            if newDist < dist:
                dist = newDist

    return dist

def clusDistCentroid(c1,c2):
    return eucDistCentroid(c1.centroid,c2.centroid)

def sigmoid(x):
    if x >50:
        return 1
    elif x < -50:
        return 0
    else:
        return 1/(1+np.exp(-x))

def clustering(ideas,clust=5):
    centroides = random.sample([idea.array for idea in ideas],clust)

    #Primeros centroides hechos.

    clusters = [[] for  i in centroides]

    for i in range(200):
        # Primero meto los puntos.
        clusters = [[] for  i in centroides]
        for idea in ideas:
            mejorDist = eucDist(Idea(centroides[0],idea.costFunc,-1),idea)
            mejor = 0
            for j in range(len(centroides)):
                dist = eucDist(Idea(centroides[j],idea.costFunc,-1),idea)
                if dist < mejorDist:
                    mejorDist = dist
                    mejor = j
            clusters[mejor].append(idea)
        #Luego creo nuevos centroides.
        idClust = 0
        for cluster in clusters:
            nuevoCentroide = [0 for k in centroides[0]]
            for j in range(len(cluster)):
                for l in range(len(cluster[j].array)):
                    nuevoCentroide[l]+= cluster[j].array[l]
            nuevoCentroide = [valor/max(1,len(cluster)) for valor in nuevoCentroide]
            centroides[idClust] = nuevoCentroide
            idClust+=1
    return [Cluster(cluster) for cluster in clusters]


def clusteringMin(ideas,clust = 5):
    nClusters = len(ideas)
    clusters = [Cluster([idea]) for idea in ideas]

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
        clusters[X]= clusters[X].join(clusters.pop(Y))
    return clusters


def clusteringCentroid(ideas,clust = 5):
    nClusters = len(ideas)
    clusters = [centroidCluster([idea]) for idea in ideas]

    while len(clusters) > clust:
        X,Y = 0, 1
        minDist = clusDistCentroid(clusters[0],clusters[1])
        for i in range(len(clusters)):
            for j in range(i+1,len(clusters)):
                otherDist = clusDistCentroid(clusters[i],clusters[j])
                if otherDist < minDist:
                    minDist = otherDist
                    X = i
                    Y = j
        clusters[X]= clusters[X].join(clusters.pop(Y))
    return clusters



class Idea:
    """docstring for Idea."""
    def __init__(self, array,costFunc,iden):
        self.array = np.array(array)
        self.costFunc = costFunc
        self.cost = costFunc(self.array)
        self.id = iden


    def copia(self):
        return Idea(self.array[:],self.costFunc,self.id)
    def coste(self):
        return self.cost

    def getId(self):
        return self.id

    def randIdea(costFunc,iden,dim,inf,sup):
        array = np.array([random.random()*(sup-inf)-sup for i in range(dim)])
        return Idea(array,costFunc,iden)


    def muta(self,currentiter,maxiter):
        newIdea = self.copia()
        for i in range(len(newIdea.array)):
            newIdea.array[i] += random.random()*sigmoid((maxiter/2.0-currentiter)/20)*np.random.normal(0,1)
            if newIdea.array[i] > sup:
                newIdea.array[i] = sup
            if newIdea.array[i] < inf:
                newIdea.array[i] = inf
        return newIdea

    def cambia(self,idea):
        self.array = idea.array[:]
        self.costFunc = idea.costFunc
        self.cost = idea.coste()
        self.id = idea.getId()

    def realCost(self):
        return self.costFunc(self.array)


class centroidCluster(object):

    def __init__(self,ideas = None):
        self.ideas = ideas
        self.centroid = None
        self.representor = None
        if self.ideas != None:
            self.centroid = self.calcCentroid()
            self.representor = self.clusterRepresent()

        else:
            self.centroid = None
            self.representor = None

    def calcCentroid(self):
        if self.centroid == None and self.ideas != None:
            centroid = np.array([0 for i in range(len(self.ideas[0].array))])
            for i in range(len(self.ideas[0].array)):
                for j in range(len(self.ideas)):
                    centroid[i]+= self.ideas[j].array[i]
                centroid[i]/=len(self.ideas)

        return centroid

    def quitaPunto(self,antiguaIdea):
        n = len(self.ideas)
        suma = np.array([n*i for i in self.centroid])
        if n != 1:
            self.centroid = np.array([(self.centroid[i]-antiguaIdea.array[i])/(n-1) for i in range(len(self.centroid))])
            encontrado = False
            i = 0
            while antiguaIdea.id != self.ideas[i].id:
                i+=1
            self.ideas.pop(i)

            self.representor = self.clusterRepresent()
        else:
            self.centroid = None
            self.ideas = None
            self.represent = None

        #Toda eliminar a la idea del cluster



    def clusterRepresent(self):
        mejor = 0
        if self.ideas == None:
            return None
        mejorCoste = self.ideas[0].realCost()

        for i in range(len(self.ideas)):
            newCost = self.ideas[i].realCost()
            if newCost < mejorCoste:
                newCost = mejorCoste
                mejor = i
        self.representor = self.ideas[mejor]
        return self.representor
    def aniadePunto(self,nuevaIdea):
        n = len(self.ideas)
        suma = np.array([n*i for i in self.centroid])
        self.centroid = np.array([(self.centroid[i]+nuevaIdea.array[i])/(n+1) for i in range(len(self.centroid))])
        self.ideas.append(nuevaIdea)
        self.representor = self.clusterRepresent()

    def join(self,otherCluster):
        return centroidCluster(self.ideas + otherCluster.ideas)
    def len(self):
        return len(self.ideas)

    def randIdea(self):
        return random.choice(self.ideas)



class Cluster(object):
    """docstring for Cluster."""
    def __init__(self,ideas=None):
        self.ideas = ideas
        self.representor = None

    def append(self,idea):
        if self.ideas == None:
            self.ideas = []
        self.ideas.append(idea)

    def clusterRepresent(self):
        if self.representor == None:
            mejor = 0
            mejorCoste = self.ideas[0].realCost()

            for i in range(len(self.ideas)):
                newCost = self.ideas[i].realCost()
                if newCost < mejorCoste:
                    newCost = mejorCoste
                    mejor = i
            self.representor = self.ideas[mejor]
        return self.representor

    def join(self,otherCluster):
        return Cluster(self.ideas + otherCluster.ideas)
    def len(self):
        return len(self.ideas)

    def randIdea(self):
        return random.choice(self.ideas)
