def coste(matDist, matFlujo,perm):
    cost = 0
    for i in range(len(matDist)):
        for j in range(len(matDist[0])):
            cost+=matFlujo[i][j]*matDist[perm[i]][perm[j]]

    return cost

class Permutacion:
    def __init__(self,permutation,matrizDistancias,matrizFlujos, cost=None):
        self.permutation = permutation
        self.matrizDistancias = matrizDistancias
        self.matrizFlujos = matrizFlujos
        self.cost = cost

    def permuta(self,i):
        if i >= 0 and i < len(self.permutation):
            return self.permutation[i]
        else:
            return -1

    def coste(self):
        if self.cost == None:
            self.cost = coste(matDist=self.matrizDistancias,matFlujo=self.matrizFlujos,perm=self.permutation)
        return self.cost
    def __str__(self):
        cadena = ""
        for i in self.permutation:
            cadena += str(i+1)+ " "
        return cadena
    # Devuelve la diferencia de coste entre esta Permutacion
    # y la que resulta al aplicar la permutacion (i j) a la misma.
    def difCoste(self,r,s):
        difCost = 0
        for k in range(len(self.permutation)):
            if k != r and k != s:
                difCost += self.matrizFlujos[r][k]*(self.matrizDistancias[self.permuta(s)][self.permuta(k)] - self.matrizDistancias[self.permuta(r)][self.permuta(k)])
                difCost += self.matrizFlujos[k][r]*(self.matrizDistancias[self.permuta(k)][self.permuta(s)] - self.matrizDistancias[self.permuta(k)][self.permuta(r)])
                difCost += self.matrizFlujos[s][k]*(self.matrizDistancias[self.permuta(r)][self.permuta(k)] - self.matrizDistancias[self.permuta(s)][self.permuta(k)])
                difCost += self.matrizFlujos[k][s]*(self.matrizDistancias[self.permuta(k)][self.permuta(r)] - self.matrizDistancias[self.permuta(k)][self.permuta(s)])
        return difCost

    # Devuelve el objeto Permutacion que surje al aplicar (i j) a la actual.
    def vecino(self,r,s):
        # Cambiar los términos de la la permutacion.
        nuevaPemutacion = [i for i in self.permutation]
        nuevaPemutacion[r],nuevaPemutacion[s]=nuevaPemutacion[s],nuevaPemutacion[r]
        # Diferencia de coste
        nuevoCoste = self.coste() + self.difCoste(r,s)

        # Creacion de el nuevo objeto Permutacion:

        return Permutacion(permutation= nuevaPemutacion, matrizDistancias = self.matrizDistancias, matrizFlujos = self.matrizFlujos,cost = nuevoCoste)
