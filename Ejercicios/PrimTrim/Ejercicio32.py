"""
    Crear una lista con 1000 números generados al azar entre 1 y 100.
"""
from random import randint


def random_1_100():
    """
    Devuelve una lista de 1000 elementos con numeros aleatorios entre 1 y 100
    :return:
    """
    return [randint(1, 100) for x in range(1000)]


print(len(random_1_100()), random_1_100())
