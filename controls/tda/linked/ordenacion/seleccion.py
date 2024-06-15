class Seleccion:
    def sort_primitive_ascendent(self, array):
        len_array = len(array)
        for i in range(len_array - 1):
            k = i
            for j in range(i + 1, len_array):
                if array[j] < array[k]:
                    k = j
            array[i], array[k] = array[k], array[i] 
        return array

    
    def sort_primitive_descendent(self, array):
        len_array = len(array)
        for i in range(len_array - 1):
            k = i
            for j in range(i + 1, len_array):
                if array[j] > array[k]:
                    k = j
            array[i], array[k] = array[k], array[i] 
        return array
    
    def sort_models_ascendent(self, array, attribute):
        len_array = len(array)
        for i in range(len_array - 1):
            k = i
            for j in range(i + 1, len_array):
                if getattr(array[j], attribute) < getattr(array[k], attribute):
                    k = j
            array[i], array[k] = array[k], array[i]
        return array


    
    def sort_models_descendent(self, array, attribute):
        len_array = len(array)
        for i in range(len_array - 1):
            k = i
            for j in range(i + 1, len_array):
                if getattr(array[j], attribute) > getattr(array[k], attribute):
                    k = j
            array[i], array[k] = array[k], array[i]
        return array

