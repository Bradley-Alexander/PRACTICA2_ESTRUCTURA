from controls.tda.linked.linkedList import Linked_List
from controls.exception.linkedEmpty import LinkedEmpty



class Secuencial:

    def busqueda_secuencial(self, data):
        list = Linked_List()
        if list.isEmpty:
            raise LinkedEmpty("List empty")
        
        else:
            array = list.toArray
            for i in range(0, len(array) -1):
                if array[i] == data:
                    list.add(array[i], list._length)
                    return list
            return None