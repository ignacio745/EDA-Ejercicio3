from Pila import Pila

if __name__ == "__main__":
    unaPila = Pila(int)
    numero = int(input("Ingrese el numero: "))
    resultado = 1
    aux = numero
    while aux != 0:
        unaPila.apilar(aux)
        aux -= 1
    while not unaPila.vacia():
        resultado *= unaPila.desapilar()
    
    print("El factorial de {0} es {1}".format(numero, resultado))