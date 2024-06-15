import enum
class CategoriaCalificacion(enum.Enum):
    MALO = 0
    REGULAR = 1
    BUENO = 2
    MUY_BUENO = 3
    EXCELENTE = 4

    def getInstance(self):
        if self.instance == None:
            self.instance = CategoriaCalificacion()
        return self.instance
