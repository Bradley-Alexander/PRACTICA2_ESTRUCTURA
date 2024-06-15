from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty
class Binaria:
    def busqueda_binaria(self, data):
        list = Linked_List()
        if list.isEmpty:
            raise LinkedEmpty("List empty")
        
        else:
            array = list.toArray
            inicio = 0
            fin = len(array) - 1
            while inicio <= fin:
                medio = (inicio + fin) // 2
                if array[medio] == data:
                    list.add(array[medio], list._length)
                    return list
                elif array[medio] > data:
                    fin = medio - 1
                else:
                    inicio = medio + 1
