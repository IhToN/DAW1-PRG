"""
    Hacer el juego de las Torres de Hanoi basándonos en los métodos del Ejercicio 22.
        mueve(x, y)        Mover el último elemento de la pila x a la pila y.
        La función mueve detecta si existe un disco de más peso sobre uno de menos y no permite el movimiento. Produce un mensaje de error.
        cima(x)        Devuelve el último elemento de la pila sin borrarlo
        El estado inicial de la pila a es [3, 2, 1]
        El estado final ha de ser mover la pila a íntegra a la pila c
"""


def introduce(lifo, elem):
    """
    Añadimos elem al final de lifo
    :param lifo:
    :param elem:
    :return:
    """
    lifo.append(elem)


def saca(lifo):
    """
    Devuelve el último elemento de lifo. Si está vacía devuelve NoneType
    :param lifo:
    :return:
    """
    if vacia(lifo):  # Comprobamos si lifo está vacía
        return None
    else:
        return lifo.pop()


def vacia(lifo):
    """
    Devuelve True si lifo está vacía. En caso contrario devuelve False
    :param lifo:
    :return:
    """
    return len(lifo) == 0  # True si la longitud es 0, False en cualquier otro caso


# Inicializamos las pilas
a = [3, 2, 1]
b = []
c = []


def cima(lifo):
    """
    Devuelve el último elemento de lifo sin borrarlo
    :param lifo:
    :return:
    """
    return lifo[-1]


def mueve(x, y):
    """
    La función mueve el último elemento de la pila x a la pila y
    :param x:
    :param y:
    :return:
    """
    if cima(x) > cima(y):
        print('You can\'t move from', x, 'to', y)
    else:
        introduce(y, saca(x))


def solucion():
    """
    Soluciona la Torre de Hanoi
    :return:
    """
    mueve(a, c)
    mostrar()
    mueve(a, b)
    mostrar()
    mueve(c, b)
    mostrar()
    mueve(a, c)
    mostrar()
    mueve(b, a)
    mostrar()
    mueve(b, c)
    mostrar()
    mueve(a, c)
    mostrar()


def mostrar():
    """
    Muestra el estado de las Torres
    :return:
    """
    print('Next movement.')
    print(a)
    print(b)
    print(c)
