from controls.tda.linked.node import Node
from controls.exception.linkedEmpty import LinkedEmpty
from controls.exception.arrayPositionException import ArrayPositionException
from numbers import Number
from controls.tda.linked.ordenacion.quickSort import QuickSort
from controls.tda.linked.ordenacion.mergeSort import MergeSort
from controls.tda.linked.ordenacion.shellSort import ShellSort

class Linked_List(object):  
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value

    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0

    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node            
        else:
            headOld = self.__head
            node = Node(data, headOld)
            self.__head = node
        
        self.__length += 1

    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)            
        else:            
            node = Node(data)
            self.__last._next = node
            self.__last = node        
            self.__length += 1

    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:            
            self.__addLast__(data)
        else:            
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next#self.getNode(pos) 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1
    
    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:            
            self.__last._data = data
        else:                        
            node = self.getNode(pos)            
            node._data = data
            
    

    @property
    def toArray(self):
        array = []
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self.__length:
                array.append(node._data)
                cont += 1
                node = node._next
        return array
    
    def deleteFirst(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self.__length == 1:
                self.__last = None
            self._length = self._length - 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            element = self.__last._data
            aux = self.getNode(self._length - 2)

            #self.__head = aux
            if aux == None:
                self.__last = None
                if self.__length == 2:
                    self.__last = self.__head
                else:
                    self.__head = None
            else:
                self.__last = None
                self.__last = aux
                self.__last._next = None
            self._length = self._length - 1
            return element


    def delete(self, pos):
        pos = pos 
        if self.isEmpty:
            raise LinkedEmpty("List is Empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Position is out of range")
        elif pos == 0:
            self._head = self.__head._next
            self.__length -= 1
            
        elif pos == self._length -1:
            self.__last = self.getNode(pos-1)
            #restarId
            self.__length -= 1
        else:
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next._next
            node_preview._next = node_last
            self.__length -= 1
            
        for i in range(pos, self._length):
            self.getNode(i)._data._id = i+1
        



    """Obtiene el objeto nodo"""
    def getNode(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length - 1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    """Obtiene el objeto nodo"""
    def get(self, pos):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        elif pos < 0 or pos >= self._length:
            raise ArrayPositionException("Index out range")
        elif pos == 0:
            return self.__head._data
        elif pos == (self.__length - 1):
            return self.__last._data
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node._data
        

    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node != None:
                out += str(node._data)+ "\t"
                node = node._next
        return out
    
    
    @property
    def print(self):
        node = self.__head
        data = ""    
        while node != None:
            data += str(node._data)+"    "            
            node = node._next
        print("Lista de datos")
        print(data)

    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])


    #PARA ORDENAR VALORES NUMÉRICOS O CADENAS
    def sort(self, type, metodo):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], Number) or isinstance(array[0], str):
                                
                if metodo == "Quick":
                    order = QuickSort()
                elif metodo == "Merge":
                    order = MergeSort()
                elif metodo == "Shell":
                    order = ShellSort()

                if type == 1:
                    array = order.sort_primitive_ascendent(array)
                else:
                    array = order.sort_primitive_descendent(array)
            
            self.toList(array)

    #PARA ORDENAR MODELOS PARA LA PRÁCTICA
    def sort_models(self, attribute, type, metodo):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            if isinstance(array[0], object):

                if metodo == "Quick":
                    order = QuickSort()
                elif metodo == "Merge":
                    order = MergeSort()
                elif metodo == "Shell":
                    order = ShellSort()

                if type == 1:
                    array = order.sort_models_ascendent(array, attribute)
                else:
                    array = order.sort_models_descendent(array, attribute)
            self.toList(array)
        return self
    


    #BUSQUEDA BINARIA PARA VALORES NUMÉRICOS
    def busqueda_binaria(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            min = 0
            max = len(array) -1
            while min <= max:             
                mid = int((min + max) // 2)
                if array[mid] == data:                    
                    list.add(array[mid], list._length)
                    return list
                elif array[mid] > data:
                    max = mid - 1
                else:
                    min = mid + 1
            return "No se encontro el dato"

    #BUSQUEDA BINARIA PARA MODELOS PARA LA PRÁCTICA
    def busqueda_binaria_models(self, data, attribute):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            min = 0
            max = len(array) -1
            while min <= max:        
                mid = int((min + max) // 2)
                if array[mid].__getattribute__(attribute) == data:                    
                    list.add(array[mid], list._length)
                    return list
                elif array[mid].__getattribute__(attribute) > data:
                    max = mid - 1
                else:
                    min = mid + 1
            return None

    #BUSQUEDA SECUENCIAL BINARIA PARA VALORES NUMÉRICOS
    def busqueda_binaria_secuencial(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            min = 0
            max = len(array) -1
            encontrado = 0
            while min <= max:             
                mid = int((min + max) // 2)
                if array[mid] == data:                    
                    encontrado = 1
                    break
                elif array[mid] > data:
                    max = mid - 1
                else:
                    min = mid + 1

            if encontrado == 1:
                for i in range(0, len(array)):
                    if array[i] == data:
                    #if array[i].lower().startswith(data.lower()):
                        list.add(array[i], list._length)
                return list
            else:  
                return "No se encontro el dato"



    #BUSQUEDA SECUENCIAL BINARIA PARA MODELOS PARA LA PRÁCTICA
    def busqueda_binaria_secuencial_models(self, data, attribute):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray
            min = 0
            max = len(array) -1
            encontrado = 0
            while min <= max:        
                mid = int((min + max) // 2)
                if array[mid].__getattribute__(attribute) == data:                    
                    encontrado = 1
                    break
                elif array[mid].__getattribute__(attribute) > data:
                    max = mid - 1
                else:
                    min = mid + 1

            if encontrado == 1:
                for i in range(0, len(array)):
                    if array[i].__getattribute__(attribute) == data:
                        list.add(array[i], list._length)            
                return list
            else:   
                return None


    #FUNCION USADA EN EL ROUTER PARA ELEGIR ENTRE BUSQUEDA BINARIA O SECUENCIAL BINARIA    
    def busqueda_binaria_o_secuencial_binaria_models(self, data, attribute, metodo):
        if metodo == "1":
            return self.busqueda_binaria_models(data, attribute)
        else:
            return self.busqueda_binaria_secuencial_models(data, attribute)