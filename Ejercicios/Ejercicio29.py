"""
    Construir una lista por comprensión que contenga todos los múltiplos de tres hasta una cifra estipulada.
"""


def multiplos_tres(numero):
    """
    Devuelve una lista que contiene todos los múltiplos de tres hasta numero incluído
    :param numero:
    :return:
    """
    #devolver [x para x en el rango de x+1, incluirlo si x%3 = 0
    return [x for x in range(numero + 1) if x % 3 == 0]


print(multiplos_tres(1000))
