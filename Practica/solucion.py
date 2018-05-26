from random import shuffle, randrange, random
import math
def coste(matDist, matFlujo,perm):
    cost = 0
    for i in range(len(perm)):
        for j in range(len(perm)):
            cost+=matFlujo[i][j]*matDist[perm[i]][perm[j]]

    return cost

def readData(filename):
    with open(filename,'r') as infile:
        n = int(infile.readline())
        #matrizFlujos = [infile.readline().split() for i in range(n)]
        archivo = infile.read().split()
        #print(archivo)
        F = []
        for i in range(n):
            lista = []
            for j in range(n):
                lista.append(int(archivo.pop(0)))

            F.append(lista)
        #matrizDistancias = [infile.readline().split() for i in range(n)]

        D = []
        for i in range(n):
            lista = []
            for j in range(n):
                lista.append(int(archivo.pop(0)))

            D.append(lista)
        return n,F,D
def readSolution(filename):
    with open(filename,'r') as infile:
        primeraLinea = infile.readline().split()
        newN = int(primeraLinea[0])
        newCost = int(primeraLinea[1])
        mejorPerm = []
        for line in infile:
            lista = line.split()
            for i in lista:
                mejorPerm.append(int(i)-1)
        return mejorPerm,newCost


class Permutacion:
    def __init__(self,P,D,F, cost=None):
        self.P = P
        self.D = D
        self.F = F
        self.cost = cost

    def randPerm(D,F):
        perm = [i for i in range(len(D))]
        shuffle(perm)
        return Permutacion(P=perm,D=D,F=F)
    def permuta(self,i):
        if i >= 0 and i < len(self.P):
            return self.P[i]
        else:
            print("La estas liando en permuta")
            return -1



    def coste(self):
        if self.cost == None:
            self.cost = coste(matDist=self.D,matFlujo=self.F,perm=self.P)
        return self.cost
    def __str__(self):
        cadena = ""
        for i in self.P:
            cadena += str(i+1)+ " "
        return cadena
    # Devuelve la diferencia de coste entre esta Permutacion
    # y la que resulta al aplicar la permutacion (i j) a la misma.
    def difCoste(self,i,j):

        difCost = 0
        difCost += self.F[i][i]*( self.D[self.permuta(j)][self.permuta(j)] - self.D[self.permuta(i)][self.permuta(i)] )
        difCost += self.F[i][j]*( self.D[self.permuta(j)][self.permuta(i)] - self.D[self.permuta(i)][self.permuta(j)] )
        difCost += self.F[j][i]*( self.D[self.permuta(i)][self.permuta(j)] - self.D[self.permuta(j)][self.permuta(i)] )
        difCost += self.F[j][j]*( self.D[self.permuta(i)][self.permuta(i)] - self.D[self.permuta(j)][self.permuta(j)] )
        for k in range(len(self.P)):
            if k != i and k != j:
                difCost += self.F[k][i]*( self.D[self.permuta(k)][self.permuta(j)] - self.D[self.permuta(k)][self.permuta(i)] )
                difCost += self.F[k][j]*( self.D[self.permuta(k)][self.permuta(i)] - self.D[self.permuta(k)][self.permuta(j)] )
                difCost += self.F[i][k]*( self.D[self.permuta(j)][self.permuta(k)] - self.D[self.permuta(i)][self.permuta(k)] )
                difCost += self.F[j][k]*( self.D[self.permuta(i)][self.permuta(k)] - self.D[self.permuta(j)][self.permuta(k)] )
        return difCost


    # Devuelve el objeto Permutacion que surje al aplicar (i j) a la actual.
    def copia(self):
        return Permutacion(D=self.D,F=self.F,cost=self.cost,P=[i for i in self.P])

    def vecino(self,r,s):
        # Cambiar los términos de la la permutacion.
        nuevaPemutacion = [i for i in self.P]
        nuevaPemutacion[r],nuevaPemutacion[s] = nuevaPemutacion[s],nuevaPemutacion[r]

        # Diferencia de coste

        difCost = self.difCoste(r,s)
        nuevoCoste = self.coste() + difCost
        #print(coste( matDist = self.D, matFlujo = self.F,perm = nuevaPemutacion),nuevoCoste,difCost,nuevoCoste-coste( matDist = self.D, matFlujo = self.F,perm = nuevaPemutacion))
        # Creacion de el nuevo objeto Permutacion:

        return Permutacion(P= nuevaPemutacion, D = self.D, F = self.F,cost = nuevoCoste)

    def vecinoSinEva(self,r,s):
        # Cambiar los términos de la la permutacion.
        nuevaPemutacion = [i for i in self.P]
        nuevaPemutacion[r],nuevaPemutacion[s] = nuevaPemutacion[s],nuevaPemutacion[r]
        perm = Permutacion(P= nuevaPemutacion, D = self.D, F = self.F)
        return perm

    def busquedaLocal(self,MaxIter=-1):
        it = 0
        bitsArray = [0 for i in range(len(self.P))]
        mejora = True
        mejorSol = self.copia()
        while (it < MaxIter or MaxIter == -1) and mejora:
            mejora = False
            for i in range(len(self.P)):
                mejoraInterna = False
                if bitsArray[i] == 0:
                    for j in range(len(self.P)):
                        if j != i:
                            difCoste = mejorSol.difCoste(i,j)
                            if MaxIter!=-1:
                                it = it+1
                            if difCoste < 0:
                                mejora = mejoraInterna = True
                                bitsArray[i] = bitsArray[j] = 0
                                mejorSol = mejorSol.vecino(i,j)
                            if MaxIter<=it and MaxIter!=-1:
                                return mejorSol,it
                    if mejoraInterna == False:
                        bitsArray[i] = 1

        return mejorSol,it

    def ES(self,nBusquedas=50000):
        mejorSol = self.copia()
        solVecina = mejorSol.copia()
        mejorCoste = mejorSol.coste()
        maxExitos = len(self.P)
        maxVecinosGenerados = 10*maxExitos
        M = nBusquedas/maxVecinosGenerados
        T0 = 0.3*mejorCoste/(-math.log(0.3))
        TF = min(T0,1.0/1000)
        beta = (T0-TF)/(M*T0*TF)

        T = T0
        while T > TF:
            exitos = 0
            vecinosgenerados = 0
            while exitos < maxExitos and maxVecinosGenerados > vecinosgenerados:
                randNum = randrange(len(self.P)**2-len(self.P))

                j = randNum//len(self.P)
                i = randNum%len(self.P)
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
        return mejorSol




    def bigMute(self):
        t = len(self.P)//4
        newP = self.P[:]
        indicesCambio = [i for i in range(len(self.P))]
        shuffle(indicesCambio)
        indicesCambio = indicesCambio[:t+1]
        cambiados = []
        for i in indicesCambio:
            cambiados.append(newP[i])
            newP[i] = -1

        i = 0
        while len(cambiados) > 0:
            while newP[i] != -1:
                i+=1
            newP[i] = cambiados.pop(0)

        return Permutacion(P=newP, D= self.D, F=self.F)
