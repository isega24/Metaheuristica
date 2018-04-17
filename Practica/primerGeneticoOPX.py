
from solucion import *
import random

def primeraGeneracion(matDist,matFlujo,Nindividuos):
    generacion = []
    for i in range(Nindividuos):
        generacion.append(Permutacion.randPerm(D=matDist,F=matFlujo))

    return generacion

# Selecciona por torneo binario una cantidad de nInd del conjunto generacion.
def seleccionTorneo(generacion,nInd):
    newGen = []
    for i in range(nInd):
        randNum = random.randrange(len(generacion)**2)
        # randNum x N^2 = N*l + k, 0 <=l,k< N
        # seleccionamos a la pareja k,l para intentar reproducirse.
        k = randNum%len(generacion)
        l = int(randNum/len(generacion))
        primero = generacion[k]
        segundo = generacion[l]
        if primero.coste() < segundo.coste():
            newGen.append(primero)
        else:
            newGen.append(segundo)

    return newGen

def cruce(primera,segunda):
    # Hacer otro cruce
    Perm1 = primera.P
    Perm2 = segunda.P
    inicio = random.randrange(len(Perm1))
    final = random.randrange(len(Perm1))
    if inicio < final:
        copiados1 = [i for i in Perm1[inicio:final]]
        copiados2 = [i for i in Perm2[inicio:final]]
        nueva1 = [-1 for i in range(inicio)] + copiados1 + [-1 for i in range(final,len(Perm1))]
        nueva2 = [-1 for i in range(inicio)] + copiados2 + [-1 for i in range(final,len(Perm2))]

    else:
        copiados1 = [i for i in Perm1[:final]] + [i for i in Perm1[inicio:]]
        copiados2 = [i for i in Perm2[:final]] + [i for i in Perm2[inicio:]]
        nueva1 = [i for i in Perm1[:final]] + [-1 for i in range(final,inicio)]+[i for i in Perm1[inicio:]]
        nueva2 = [i for i in Perm2[:final]] + [-1 for i in range(final,inicio)]+[i for i in Perm2[inicio:]]


    i = final

    # Primer hijo.
    while i != inicio:
        # Averiguando la correspondencia.

        valor = Perm1[i]
        index = i

        while valor in copiados2 :
            index = copiados2.index(valor)
            valor = copiados1[index]


        nueva2[i] = valor

        i = (i+1)%len(Perm1)


    i = final

    # Segundo hijo.
    while i != inicio:
        # Averiguando la correspondencia.
        valor = Perm2[i]
        index = i

        while valor in copiados1:
            index = copiados1.index(valor)
            valor = copiados2[index]


        nueva1[i] = valor

        i = (i+1)%len(Perm1)



    # Aqui la modificacion que queda.

    return [Permutacion(P=nueva1,D=primera.D,F=primera.F),Permutacion(P=nueva2,D=primera.D,F=primera.F)]


class Poblacion:
    def __init__(self,matDist,matFlujo,Nind,p_cruce=0.7,p_muta=0.001):
        self.D = matDist
        self.F = matFlujo
        self.n = Nind
        self.popu = primeraGeneracion(matDist=self.D,matFlujo=self.F,Nindividuos=self.n)
        self.mejor = self.mejorPoblActual(self.popu)
        self.p_cruce = p_cruce
        self.p_muta = p_muta

    def mejorPoblActual(self,hijos):
        costeMin = hijos[0].coste()
        mejorSol = hijos[0]
        for i in hijos:
            nuevoCoste = i.coste()
            if nuevoCoste < costeMin:
                mejorSol = i
                costeMin = nuevoCoste
        return mejorSol

    def peorActual(self,hijos):
        costeMax = hijos[0].coste()
        peorSol = 0
        for i in range(len(hijos)):
            nuevoCoste = hijos[i].coste()
            if nuevoCoste > costeMax:
                peorSol = i
                costeMax = nuevoCoste

        return peorSol

    def generaPadres(self):
        return seleccionTorneo(self.popu,self.n)

    def proximaGeneracion(self):
        numEvaluaciones = 0
        ##### Estos costes estaban contemplados en la generacion anterior
        listaPadres = self.generaPadres()

        emparejamientos = int(len(listaPadres)*self.p_cruce/2)
        hijos = []
        # Se emparejan los primeros padres porque la aleatoriedad ya ha seleccionado
        # las primeras parejas como parejas prometedoras para el cruce. Lo demás se deja
        # como la copia de los padres seleccionados.

        for i in range(emparejamientos):
            hijos += cruce(listaPadres[2*i],listaPadres[2*i+1])



        ##### Los hijos no están evaluados. Se evaluan
        numEvaluaciones += emparejamientos

        hijos += [padre.copia() for padre in listaPadres[emparejamientos:] ]

        # Consideramos una mutacion la aplicacion de un ciclo de orden 2
        # sobre la permutacion de la solucion. Así, hay varias posibles mutaciones:
        # Sobre cada individuo(id):
        #   Sobre cada (i,j) posible ciclo (i!=j)

        mutaciones = max(int(len(listaPadres)*((len(self.D)**2-len(self.D))/2) *self.p_muta),1)

        ##### Las mutaciones son vecinos de la solucion. Cuentan como evaluaciones.
        numEvaluaciones+= mutaciones

        for i in range(mutaciones):
            Ind = random.randrange(len(hijos))
            confPerm = random.randrange(len(self.D)**2-len(self.D))
            i = confPerm%len(self.D)
            j = int(confPerm/len(self.D))
            if i <=j:
                j += 1
            if hijos[Ind].cost == None:
                hijos[Ind] = hijos[Ind].vecinoSinEva(i,j)
            else:
                hijos[Ind] = hijos[Ind].vecino(i,j)

        # Ahora seleccionamos al mejor de las poblaciones.


        mejoractual = self.mejorPoblActual(hijos)


        if self.mejor.coste() > mejoractual.coste():
            self.mejor = mejoractual
        else:
            hijos[self.peorActual(hijos)] = self.mejor

        self.popu = hijos

        return numEvaluaciones

    def aplicaBL(self,maxEval = 50000,prob = 0.1,mejores = False,nSteps = 400):

        if mejores:
            self.popu.sort(key=lambda individuo: individuo.coste())
        elif prob != 1.0:
            random.shuffle(self.popu)
        nIndivMejorados = int(prob*len(self.popu))
        mejoras = 0
        i = 0
        while mejoras < maxEval and i < nIndivMejorados:

            self.popu[i],mejorasI = self.popu[i].busquedaLocal(min(nSteps,maxEval-mejoras))
            mejoras += mejorasI

            i+=1
        return mejoras
