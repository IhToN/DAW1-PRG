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
import time


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
    primos = [x for x in range(2, numero + 1)]
    for index in range(0, (numero + 1) // 2):
        primos = criba(index, primos)
    return [x for x in primos if x]


def criba(index, lista_criba):
    salto = lista_criba[index]
    if salto:
        for mul in range(index + salto, len(lista_criba), salto):
            lista_criba[mul] = False
    return lista_criba


print(divisores(22))
print(es_primo(13))
t1 = time.time()
print(primos_hasta(3000))
t2 = time.time()
print(t2 - t1)
print(criba_eratostenes(3000))
print(time.time() - t2)
