from cluster import *
from timeit import default_timer as timer


def readInput(inputName):
    curvas = []
    file = open(inputName, "r")
    line = file.readline()

    for line in file:   
        curvaString = line.split(",")
        id= int(curvaString[0])
        t= float(curvaString[4])

        stringA = curvaString[1].split(";")
        stringB = curvaString[2].split(";")
        stringC = curvaString[3].split(";")
        A = Point(stringA)
        B = Point(stringB)
        C = Point(stringC)

        curva = Curva(id, A, B ,C ,t)
        curvas.append(curva)
    
    file.close()
    return curvas

def writeOutputs(outName, similares , diferentes):
    file = open(outName , "w")

    file.write("Similares: \n")
    if len(similares) == 0:
        file.write(str(similares))
    else:
        i = 0
        for cluster in similares:
            file.write(str(i) + ": " + str(cluster)[6: -1])
            i+=1

    file.write("\nDiferentes: \n")
    file.write(str(diferentes))
    file.close()

def main():
    print("Ingrese el nombre del archivo con las curvas: ")
    fileName = input()
    print("Abirendo: " + fileName)
    curvas = readInput(fileName)


    print("Prosesando curvas: " + fileName)

    start = timer()
    respuesta = solucion(curvas)
    end = timer()
    print("Tiempo de ejecución: "  + str(end - start) + "s")

    similares = respuesta[0]
    diferentes = respuesta[1]

    print("Los resultados son: ")
    print("- Grupos de curvas similares:  ")
    if len(similares) == 0:
        print(str(similares))
    else:
        i = 0
        for cluster in similares:
            print(str(i) + ": " + str(cluster)[6: -1])
            i+=1
    print("- Curvas diferentes:  ")
    print(diferentes)

    print("Escribiendo resultados en ./outputFiles/out.txt")
    writeOutputs("./outputFiles/out.txt", similares , diferentes)


main()