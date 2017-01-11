"""
    Vamos a construir una pila LIFO last in first out. Vamos a crear unas funciones para manejar dicha pila.
    Estas funciones serán:
        introduce(pila, x)    Añadimos un elemento al final de la pila
        saca(pila)        Devolvemos el último elemento de la pila (si la pila está vacía, devuelve None
        vacia(pila)        Devuelve un boolean, true = pila vacía
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
