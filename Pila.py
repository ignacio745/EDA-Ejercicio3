from Nodo import Nodo

class Pila:
    __cabeza:Nodo = None
    __tipo:type = None

    def __init__(self, tipo:type=int) -> None:
        self.__cabeza = None
        self.__tipo = tipo
    
    def vacia(self):
        return self.__cabeza == None

    def apilar(self, elemento):
        assert isinstance(elemento, self.__tipo), "El elemento a agregar debe ser del tipo {0}, no {1}".format(self.__tipo, type(elemento))
        unNodo = Nodo(elemento)
        unNodo.setSiguiente(self.__cabeza)
        self.__cabeza = unNodo
    
    
    def desapilar(self):
        assert not self.vacia(), "La pila esta vacia"
        elemento = self.__cabeza.getDato()
        self.__cabeza = self.__cabeza.getSiguiente()
        return elemento