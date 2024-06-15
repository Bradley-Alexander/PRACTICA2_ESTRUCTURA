class MergeSort:
    
    def sort_merge_number_ascendent(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            
            self.sort_merge_number_ascendent(left)
            self.sort_merge_number_ascendent(right)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
                
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        return array
    
    def sort_merge_number_descendent(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            
            self.sort_merge_number_descendent(left)
            self.sort_merge_number_descendent(right)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
                
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        return array
    
    def sort_models_ascendent(self, array, attribute):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            
            self.sort_models_ascendent(left, attribute)
            self.sort_models_ascendent(right, attribute)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if getattr(left[i], attribute) < getattr(right[j], attribute):
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
                
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        return array
    
    def sort_models_descendent(self, array, attribute):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            
            self.sort_models_descendent(left, attribute)
            self.sort_models_descendent(right, attribute)
            
            i = j = k = 0
            
            while i < len(left) and j < len(right):
                if getattr(left[i], attribute) > getattr(right[j], attribute):
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
                
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
                
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        return array

        