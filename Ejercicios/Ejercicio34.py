"""
    Escribir una función a la que se le da como parámetro una tupla de números enteros y devuelve la suma de todos los elementos.
    a. Solución Original
    b.
"""


def suma_numeros(lista_numeros):
    """ Devuelve la suma de todos los elementos de 'lista_numeros'
    """
    ret = 0
    for elem in lista_numeros:
        ret += elem
    return ret
