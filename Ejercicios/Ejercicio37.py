"""
    Crear utilidades matemáticas:
    a. Escribir una función a la que se le pasa un número y devuelve una tupla con sus divisores.
    b. Se define un número primo como aquel que no tiene más divisores que él mismo y la unidad.
        Escribir una función que nos devuelva un True en caso de que ser un número primo.
    c. Crear una función a la que se le pasa un límite y nos devuelve una lista con todos los
        números primos por debajo de ese límite.
"""
from math import sqrt


def divisores(numero):
    """ Devuelve una tupla con los divisores de numero
    """
    ret = ()
    for i in range(numero + 1):
        if i % numero == 0:
            ret += i,
    return ret


def es_primo(numero):
    """ Comprueba si el numero es primo o no, devuelve un boolean
    """
    return len(divisores(sqrt(numero))) == 2


def primos_hasta(numero):
    """ Devuelve una lista con todos los primos menores o iguales que numero
    """
    ret = []
    for i in range(numero + 1):
        if es_primo(i):
            ret.append(i)
    return ret
