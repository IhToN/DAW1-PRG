"""
    Construir una lista por comprensión que contenga todos los múltiplos de tres hasta una cifra estipulada.
    b. Solución original
    a. Extender a incluir los números múltiplos de 5 y 7
"""

sol = 'b'


def multiplos_tres(numero):
    """
    Devuelve una lista que contiene todos los múltiplos de tres hasta numero incluído
    :param numero:
    :return:
    """
    if sol == 'a':
        # devolver [x para x en el rango de x+1, incluirlo si x%3 = 0
        return [x for x in range(numero + 1) if x % 3 == 0]
    elif sol == 'b':
        # devolver [x para x en el rango de x+1, incluirlo si x%3, x%5 o x%7 es 0
        return [x for x in range(numero + 1) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0]


print(multiplos_tres(1000))
