"""
    Buscar todos los números impares NO primos menores que mil y contarlos. Y cuántos números pares y primos hay.
"""
from math import ceil, sqrt


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


ninp = {x for x in range(1, 1000, 2) if not es_primo(x)}
npp = {x for x in range(0, 1000, 2) if es_primo(x)}  # El único número Par Primo es 2.

print("Números impares NO primos menores que mil:", len(ninp), "\nNúmeros pares primos menores que mil:", len(npp))
