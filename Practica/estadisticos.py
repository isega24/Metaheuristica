#!/usr/bin/python3

import sys
import math

if len(sys.argv) < 2:
    print("Este script necesita el nombre del algoritmo sobre el que queremos hallar los estadisticos.")

algoritmo = sys.argv[1]

desviacion = 0
tiempoMedio = 0
i = 0
with open("./tablas/Tabla"+algoritmo+".txt",'r') as infile:
    for line in infile:
        i+=1
        datos = line.split()
        coste = int(datos[0])
        tiempo = float(datos[1])
        mejorCoste = int(datos[2])
        desviacion+=100*(coste-mejorCoste)/(1.0*mejorCoste)
        tiempoMedio+=tiempo
desviacion=desviacion/i
tiempoMedio=tiempoMedio/i
print("Desviacion: "+str(desviacion))
print("Tiempo Medio: "+str(tiempoMedio))
