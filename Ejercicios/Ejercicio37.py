"""
    Crear utilidades matemáticas:
    a. Escribir una función a la que se le pasa un número y devuelve una tupla con sus divisores.
    b. Se define un número primo como aquel que no tiene más divisores que él mismo y la unidad.
        Escribir una función que nos devuelva un True en caso de que ser un número primo.
    c. Crear una función a la que se le pasa un límite y nos devuelve una lista con todos los
        números primos por debajo de ese límite.
    d. Seguir el método de la Criba de Eratóstenes.
"""
from math import ceil, sqrt


def divisores(numero):
    """ Devuelve una tupla con los divisores de numero
    """
    ret = ()
    for i in range(1, ceil((numero + 1) / 2)):
        if numero % i == 0:
            ret += i,
    ret += numero,
    return ret


def es_primo(numero):
    """ Comprueba si el numero es primo o no, devuelve un boolean
    """
    loop = 2
    if numero < 2:
        return False
    while loop < ceil(sqrt(numero + 1)):
        if numero % loop == 0:
            return False
        loop += 1
    return True


def primos_hasta(numero):
    """ Devuelve una lista con todos los primos menores o iguales que numero
    """
    ret = []
    for i in range(2, numero + 1):
        if es_primo(i):
            ret.append(i)
    return ret


def criba_eratostenes(numero):
    """ Devuelve una lista con todos los primos menores o iguales que numero
    Usando el método de la Criba de Eratóstenes
    """
    ret = []
    mults = []
    for elem in range(2, numero + 1):
        if elem not in mults:
            ret.append(elem)
            mults += [x for x in range(elem ** 2, numero + 1, elem)]
    return ret


print(divisores(22))
print(es_primo(13))
print(primos_hasta(3000))
print(criba_eratostenes(3000))
