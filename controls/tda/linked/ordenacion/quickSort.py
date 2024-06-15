class QuickSort:
    
    def sort_primitive_ascendent(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            menores = []
            mayores = []
            iguales = []
            for i in array:
                if i < pivot:
                    menores.append(i)
                elif i > pivot:
                    mayores.append(i)
                else:
                    iguales.append(i)

            menores = self.sort_primitive_ascendent(menores)
            mayores = self.sort_primitive_ascendent(mayores)
            array = menores + iguales + mayores
            
        return array    
    
    
    
    def sort_primitive_descendent(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            menores = []
            mayores = []
            iguales = []
            for i in array:
                if i < pivot:
                    menores.append(i)
                elif i > pivot:
                    mayores.append(i)
                else:
                    iguales.append(i)

            menores = self.sort_primitive_descendent(menores)
            mayores = self.sort_primitive_descendent(mayores)
            array = mayores + iguales + menores
        return array
    

    
    def sort_models_ascendent(self, array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = getattr(array[0], attribute)
            menores = []
            mayores = []
            iguales = []
            for i in array:
                if getattr(i, attribute) < pivot:
                    menores.append(i)
                elif getattr(i, attribute) > pivot:
                    mayores.append(i)
                else:
                    iguales.append(i)

            menores = self.sort_models_ascendent(menores, attribute)
            mayores = self.sort_models_ascendent(mayores, attribute)
            array = menores + iguales + mayores
        return array
    

    
    def sort_models_descendent(self, array, attribute):
        if len(array) <= 1:
            return array
        else:
            pivot = getattr(array[0], attribute)
            menores = []
            mayores = []
            iguales = []
            for i in array:
                if getattr(i, attribute) < pivot:
                    menores.append(i)
                elif getattr(i, attribute) > pivot:
                    mayores.append(i)
                else:
                    iguales.append(i)

            menores = self.sort_models_descendent(menores, attribute)
            mayores = self.sort_models_descendent(mayores, attribute)
            array = mayores + iguales + menores
        return array
    

