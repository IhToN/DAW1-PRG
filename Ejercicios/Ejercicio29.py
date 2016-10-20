"""
    Construir una lista por comprensión que contenga todos los múltiplos de tres hasta una cifra estipulada.
    a. Solución original
    b. Extender a incluir los números múltiplos de 5 y 7
    c. Incluir sólo los múltiplos de 3 y 7
"""

sol = 'c'


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
    elif sol == 'c':
        # devolver [x para x en el rango de x+1, incluirlo si x%3 y x%7 es 0
        return [x for x in range(numero + 1) if x % 3 == 0 and x % 7 == 0]


print(multiplos_tres(1000))
