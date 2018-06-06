#!/usr/bin/python3

import sys

casos=["had20","chr22a","chr22b","chr25a","nug28","tho40","wil50","lipa60b","lipa80b","sko81","sko90","sko100a","sko100f","tai100a","tai100b","wil100","esc128","tai150b","tho150","tai256c"]

if len(sys.argv) < 2:
    print("Este script necesita el nombre del algoritmo sobre el que queremos usar la tabla de latex.")

algoritmo = sys.argv[1]
print("\\textbf{Algoritmo "+algoritmo+"}")
print("\\begin{table}[htbp]")
print("\t\\begin{center}")
print("\t\t\\begin{tabular}{|l|l|l|l|l|}")
print("\t\t\t\\hline")

with open("./tablas/Tabla"+algoritmo+".txt",'r') as infile:
    print("\t\t\tCaso & MejorCoste & Coste obtenido & Desviación & tiempo \\\\")
    print("\t\t\t\\hline \\hline")
    i=0
    for line in infile:
        datos = line.split()
        coste = int(datos[0])
        tiempo = float(datos[1])
        mejorCoste = int(datos[2])
        cadena = "\t\t\t"+ casos[i]+" & "+ str(mejorCoste)+ " & " + str(coste) + " & " + str(int((coste-mejorCoste)*10000.0/mejorCoste)/100.0) + " & " + str(int(100*tiempo)/100.0) + "\\\\ \\hline"
        i+=1
        print(cadena)



print("\t\t\t\\end{tabular}")
print("\t\t\\caption{Datos obtenidos para el algoritmo "+ algoritmo +"}")
print("\t\t\\label{tabla:Datos"+algoritmo+"}")
print("\t\\end{center}")
print("\\end{table}")
print("\\newpage")
