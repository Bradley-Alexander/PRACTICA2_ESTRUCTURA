import sys
sys.path.append('../')
from controls.tda.linked.linkedList import Linked_List
from controls.atencionDaoControl import AtencionDaoControl
import time

import random
at = AtencionDaoControl()

try:


    lista = Linked_List()

    for i in range(20000):
        numero_aleatorio = random.randint(1, 10000)
        lista.add(numero_aleatorio)
    

    lista.sort(1, "Quick")

    listaBinaria = lista
    listaSecuencialBinaria = lista


    print("-------------------------------------------------")
    print("BUSQUEDA BINARIA")
    inicio = time.time()
    listota = listaBinaria.busqueda_binaria(1000.5)
    if listota == "No se encontro el dato":
        print("No se encontro el dato")
    else:
        listota.print
    fin = time.time()
    print("Tiempo de ejecucion: ", fin-inicio)

    print("-------------------------------------------------")
    print("BUSQUEDA BINARIA SECUENCIAL")
    inicio = time.time()
    listita = listaSecuencialBinaria.busqueda_binaria_secuencial(1000.5)
    if listita == "No se encontro el dato":
        print("No se encontro el dato")
    else:
        print("Encontrado")
    fin = time.time()
    print("Tiempo de ejecucion: ", fin-inicio)


    print("-------------------------------------------------")







    lista = Linked_List()
    for i in range(10000):
        lista.add(round(random.random()*100,2))

    listaQuickSort = lista
    listaMergeSort = lista
    listaShellSort = lista

    print("-------------------------------------------------")
    print("QUICK SORT")

    inicio = time.time()    
    listaQuickSort.sort(1, "Quick")
    print("Ordenado")
    #listaQuickSort.print

    fin = time.time()

    print("Tiempo de ejecucion: ", fin-inicio)
    print("-------------------------------------------------")
    print("MERGE SORT")

    inicio = time.time()
    listaMergeSort.sort(1, "Merge")
    print("Ordenado")
    #listaMergeSort.print

    fin = time.time()

    print("Tiempo de ejecucion: ", fin-inicio)
    print("-------------------------------------------------")
    print("SHELL SORT")

    inicio = time.time()
    listaShellSort.sort(1, "Shell")
    print("Ordenado")
    #listaShellSort.print

    fin = time.time()

    print("Tiempo de ejecucion: ", fin-inicio)
    print("-------------------------------------------------")




except Exception as e:
    print(e)  