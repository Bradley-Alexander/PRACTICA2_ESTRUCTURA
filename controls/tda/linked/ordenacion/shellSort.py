class ShellSort:
    def sort_shell_number_ascendent(self, array):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array
    
    def sort_shell_number_descendent(self, array):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] < temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array
    
    def sort_models_ascendent(self, array, attribute):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                temp = array[i]
                j = i
                while j >= gap and getattr(array[j - gap], attribute) > getattr(temp, attribute):
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array
    
    def sort_models_descendent(self, array, attribute):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                temp = array[i]
                j = i
                while j >= gap and getattr(array[j - gap], attribute) < getattr(temp, attribute):
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array