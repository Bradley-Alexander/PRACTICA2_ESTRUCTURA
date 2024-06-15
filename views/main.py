import sys
sys.path.append('../')
from controls.tda.linked.linkedList import Linked_List
from controls.atencionDaoControl import AtencionDaoControl
import time

import random
# pc = PersonaControl()
# cd = CensoDao()
# pcd = PersonaDaoControl()
at = AtencionDaoControl()

try:
    

    listaS = Linked_List()
    listaS.add("Cuanchaca", listaS._length)
    listaS.add("Cale", listaS._length)
    listaS.add("Criollo", listaS._length)
    listaS.add("Cale", listaS._length)
    listaS.add("Crmijos", listaS._length)
    listaS.add("Cera", listaS._length)
    listaS.add("Curimilma", listaS._length)
    listaS.print
    listaS.sort(1)
    listaS.print
    
    print("---------------------------")
    print("BUSQUEDA SECUENCIAL")
    print("---------------------------")
    listita = listaS.search_number_equals("C")
    
    listita.print

    print("---------------------------")
    print("BUSQUEDA SECUENCIAL MODELOS")
    print("---------------------------")
    listita = pdc._list().search_number_equals_models("Morocho", "_apellidos")
    
    listita.print

    print("---------------------------")
    print("BUSQUEDA BINARIA")
    print("---------------------------")
    listaS.print
    listaS.sort(1)
    listita = listaS.busqueda_binaria("Cale")
    print(listita)

    print("---------------------------")
    print("BUSQUEDA BINARIA MODELS")
    print("---------------------------")
    pdc._list().print
    listitaAux = pdc._list().sort_models("_apellidos", 1)
    listitaAux.print
    listaAux =  listitaAux.busqueda_binaria_models("Ver","_apellidos")
    print(listaAux)

    print("---------------------------")
    print("BUSQUEDA BINARIA SECUENCIAL ---")
    print("---------------------------")
    listaS.print
    listaS.sort(1)
    listita = listaS.busqueda_binaria_secuencial("Cale")
    print(listita)


    print("---------------------------")
    print("BUSQUEDA BINARIA SECUENCIAL MODELS")
    print("---------------------------")
    pdc._list().print
    listitaAux = pdc._list().sort_models("_apellidos", 1)
    listitaAux.print
    listaAux =  listitaAux.busqueda_binaria_secuencial_models("Ver","_apellidos")
    print(listaAux)

    print("---------------------------")
    lista =pdc._list()
    print(lista)
    lista.sort_models("_apellidos", 1)
    print(lista)
    arreglo = lista.toArray
    print(arreglo)
    """     listaAux.print
    print("----------models----------------")
    pdc._list().print
    listota = pdc._list()
    print(listota)
    print("---------------------------")
    listita = listota.search_number_equals_models("Morocho", "_apellidos") """
    
    

    """   lista = Linked_List()
    for i in range(10):
        lista.add(round(random.random()*100,2))

    lista.add(32.5)

    lista.print
    inicio = time.time()
    lista.sort(1)
    lista.print
    """
    """ print("---------------------------")
    listaS = Linked_List()
    listaS.add("Morocho", listaS._length)
    listaS.add("Cale", listaS._length)
    listaS.add("Criollo", listaS._length)
    listaS.add("Calva", listaS._length)
    listaS.add("Armijos", listaS._length)
    listaS.add("Huanchaca", listaS._length)
    listaS.add("Curimilma", listaS._length)
    listaS.print
    listaS.sort(1)
    listaS.print

    pdc._list().print
    listaAux = pdc._list().sort_models("_nombre", 1)
    listaAux.print

    fin = time.time()
    print("Tiempo de ejecucion: ", fin-inicio)


    print("BUSCANDOOOO")
    listita = listaS.search_number_equals("H")
    
    listita.print """


except Exception as e:
    print(e)  