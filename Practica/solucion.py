def coste(matDist, matFlujo,perm):
    cost = 0
    for i in range(len(matDist)):
        for j in range(len(matDist[0])):
            cost+=matFlujo[i][j]*matDist[perm.permuta(i)][perm.permuta(j)]

    return cost

class Permutacion:
    def __init__(self,n,permutation,matrizDistancias,matrizFlujos):
        self.n = n
        self.permutation = permutation
        self.matrizDistancias = matrizDistancias
        self.matrizFlujos = matrizFlujos
        self.cost = coste(matDist = self.matrizDistancias, matFlujo = self.matrizFlujos,perm=self)

    def permuta(self,i):
        if i >= 0 and i < self.n:
            return self.permutation[i]
        else:
            return -1

    def coste(self):
        return self.cost
    def __str__(self):
        cadena = ""
        for i in self.permutation:
            cadena += str(i)+ " "

        return cadena
