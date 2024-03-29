#Juan José Aguado
#Código 8957833
#Fecha 8-02-2023

from heapq import heappush, heapify, heappop
from collections import deque

def eje():
    ent = [int(x) for x in input().split()]
    cap = ent[0] #capacidad del ferry
    tiempo = ent [1] #tiempo que se demora en cruzar
    cant = ent[2] #cantidad de carros que hay
    heapIzq = []
    heapDer = []
    res = deque() #van a haber carros por izquierda y derecha y el resultado
    for i in range(cant):
        ent = input().split()
        if ent[1] == "left":
            heappush(heapIzq, (int(ent[0]),i)) #lo agrego a la lista de la izquierda con su indice
        elif ent[1] == "right":
            heappush(heapDer, (int(ent[0]),i)) #lo agrego a la lista de la derecha con su indice
        res.append(0) #añado a la lista para asi luego poder reemplazar con indices
    viaje = 0 #tiempo que se han demorado
    ferry = "left"
    while len(heapDer) or len(heapIzq):
        viaje += tiempo
        avanza = False
        if len(heapDer) > 0 and heapDer[0][0] <= viaje:
            avanza = True
        if len(heapIzq) > 0 and heapIzq[0][0] <= viaje:
            avanza = True
        if avanza:
            if ferry == "left":
                ferry = "right"
                if len(heapIzq) > 0:
                    for i in range(min(cap, len(heapIzq))):
                        if heapIzq[0][0] <= viaje - tiempo: #si ya ha llegado a la orilla
                            car = heappop(heapIzq)
                            res[car[1]] = viaje
            elif ferry == "right" :
                ferry = "left"
                if viaje != 0 and len(heapDer) > 0:
                    for i in range(min(cap, len(heapDer))):
                        if heapDer[0][0] <= viaje - tiempo: #si ya ha llegado a la orilla
                            car = heappop(heapDer)
                            res[car[1]] = viaje
    return res


def imprimir():
    f = open("ferry.txt", "w")
    casos = int(input()) #recibe el numero de casos
    for i in range(casos): #ejecuta el prigrama para todos los casos
        res = eje() #hace la ejecucion que devuelve una lista
        for j in res:
            print ("%s" %j, file=f) #imprime cada elemento en una linea
        print("", file=f)
    f.close()
imprimir()