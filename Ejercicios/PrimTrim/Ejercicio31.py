"""
    En una empresa hay 15 trabajadores. Se quiere hacer un torneo de ajedrez. Hay que escribir una función a la que
    se le pasa una lista de todos los empleados de la empresa y la función devuelve otra lista
    con todas las partidas posibles entre empleados. Nota: Un empleado no juega contra sí mismo.
    a. Solución Original
    b. Generar el orden en el que se van a ejecutar las partidas.
        Generamos un número al azar del tamaño de la lista, sacamos la pareja elegida y la guardamos en una nueva lista, borrando la pareja de la original.
"""
from random import randint

trabajadores = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15']


def posibles_partidas(participantes):
    """
    Devuelve una lista con las posibles parejas de participantes
    :param participantes:
    :return:
    """
    return [(p1, p2) for p1 in trabajadores for p2 in trabajadores if p1 != p2]


def partidas(participantes):
    """
    Devuelve el orden en el cual las posibles_partidas se van a ejecutar
    :param participantes:
    :return:
    """
    pospartidas = posibles_partidas(participantes)
    ret = []
    while pospartidas:
        idx = randint(0, len(pospartidas) - 1)
        ret.append(pospartidas[idx])
        del (pospartidas[idx])
    return ret


print(len(posibles_partidas(trabajadores)), posibles_partidas(trabajadores))
print(len(partidas(trabajadores)), partidas(trabajadores))
