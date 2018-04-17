
from solucion import *
from primerGenetico import primeraGeneracion, cruce, seleccionTorneo
import random

class Poblacion:
    def __init__(self,matDist,matFlujo,Nind,p_muta=0.001):
        self.D = matDist
        self.F = matFlujo
        self.n = Nind
        self.popu = primeraGeneracion(matDist=self.D,matFlujo=self.F,Nindividuos=self.n)
        self.mejor = self.mejorPoblActual(self.popu)
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
    def peorActual(self):
        costeMax = self.popu[0].coste()
        peorSol = 0
        for i in range(len(self.popu)):
            nuevoCoste = self.popu[i].coste()
            if nuevoCoste > costeMax:
                peorSol = i
                costeMax = nuevoCoste

        return self.popu.pop(peorSol)

    def generaPadres(self):
        return seleccionTorneo(self.popu,2)

    def proximaGeneracion(self):
        listaPadres = self.generaPadres()

        hijos = [cruce(listaPadres[0],listaPadres[1]),cruce(listaPadres[0],listaPadres[1])]

        mutaciones = max(int(len(listaPadres)*((len(self.D)**2-len(self.D))/2) *self.p_muta),1)

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


        # Vemos si los dos hijos generados pueden entrar en la población. Buscamos
        # los dos peores:

        hijos.append(self.peorActual())
        hijos.append(self.peorActual())

        hijos = sorted([(hijo,hijo.coste()) for hijo in hijos],key=lambda val:val[1])

        self.popu += [hijos[0][0],hijos[1][0]]

        if hijos[0][0].coste() < self.mejor.coste():
            self.mejor = hijos[0][0]

        return 2

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
