"""
    Vamos a construir una pila LIFO last in first out. Vamos a crear unas funciones para manejar dicha pila.
    Estas funciones serán:
        introduce(pila, x)    Añadimos un elemento al final de la pila
        saca(pila)        Devolvemos el último elemento de la pila (si la pila está vacía, devuelve None
        vacia(pila)        Devuelve un boolean, true = pila vacía
"""


def introduce(lifo, elem):
    lifo.append(elem)  # Añade el elemento al final de la pila


def saca(lifo):
    if vacia(lifo):
        return None  # Devolvemos el NoneType si la pila está vacía
    else:
        return lifo.pop()  # Devolvemos el último elemento si NO está vacía


def vacia(lifo):
    return len(lifo) == 0  # True si la longitud es 0, False en cualquier otro caso
