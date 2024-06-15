from typing import Type
from controls.dao.daoAdapter import DaoAdapter
from models.atencion import Atencion

class AtencionDaoControl(DaoAdapter):
    def __init__(self):
        super().__init__(Atencion)
        self.__atencion = None

    @property
    def _atencion(self):
        if self.__atencion == None:
            self.__atencion = Atencion()
        return self.__atencion

    @_atencion.setter
    def _atencion(self, value):
        self.__atencion = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__atencion._id = self._lista._length + 1
        self._save(self.__atencion)

    def merge(self, pos):
        self._merge(self.__atencion, pos) 

    def delete(self, pos):
        self._delete(pos)
