from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Nodo import Nodo

class Nodo:
    __elemento = None
    __siguiente:Nodo = None

    def __init__(self, elemento) -> None:
        self.__elemento = elemento
    
    def setSiguiente(self, sig:(Nodo | None)) -> None:
        assert isinstance(sig, Nodo) or sig==None, "El parametro sig debe ser del tipo Nodo"
        self.__siguiente = sig
    
    def getSiguiente(self) -> Nodo:
        return self.__siguiente
    
    def getDato(self):
        return self.__elemento