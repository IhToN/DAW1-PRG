"""
    Escribir una función a la que se le da como parámetro una tupla de números enteros
    y devuelva la suma de todos los elementos de dicha tupla.
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
    # Otra posible solución es con la función sum(iterable)
    # return sum(lista_numeros)
