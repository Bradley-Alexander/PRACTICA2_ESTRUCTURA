class HeapSort:

    def sort_primitive_ascendent(self, array):
        len_array = len(array)
        for i in range(len_array // 2 - 1, -1, -1):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < len_array and array[largest] > array[l]:
                largest = l
            if r < len_array and array[largest] > array[r]:
                largest = r
            if largest != i:
                array[i], array[largest] = array[largest], array[i]
                self.heapify(array, len_array, largest)
        for i in range(len_array - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        return array



    def sort_primitive_descendent(self, array):
        len_array = len(array)
        for i in range(len_array // 2 - 1, -1, -1):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < len_array and array[largest] < array[l]:
                largest = l
            if r < len_array and array[largest] < array[r]:
                largest = r
            if largest != i:
                array[i], array[largest] = array[largest], array[i]
                self.heapify(array, len_array, largest)
        for i in range(len_array - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        return array
    
    def sort_models_ascendent(self, array, attribute):
        len_array = len(array)
        for i in range(len_array // 2 - 1, -1, -1):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < len_array and getattr(array[largest], attribute) > getattr(array[l], attribute):
                largest = l
            if r < len_array and getattr(array[largest], attribute) > getattr(array[r], attribute):
                largest = r
            if largest != i:
                array[i], array[largest] = array[largest], array[i]
                self.heapify(array, len_array, largest)
        for i in range(len_array - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        return array
    
    def sort_models_descendent(self, array, attribute):
        len_array = len(array)
        for i in range(len_array // 2 - 1, -1, -1):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < len_array and getattr(array[largest], attribute) < getattr(array[l], attribute):
                largest = l
            if r < len_array and getattr(array[largest], attribute) < getattr(array[r], attribute):
                largest = r
            if largest != i:
                array[i], array[largest] = array[largest], array[i]
                self.heapify(array, len_array, largest)
        for i in range(len_array - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        return array
    


