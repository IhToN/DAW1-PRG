"""
    En una empresa hay 15 trabajadores. Se quiere hacer un torneo de ajedrez. Hay que escribir una función a la que
    se le pasa una lista de todos los empleados de la empresa y la función devuelve otra lista
    con todas las partidas posibles entre empleados. Nota: Un empleado no juega contra sí mismo.
"""

trabajadores = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15']


def partidas(participantes):
    return [p1 + ' vs ' + p2 for p1 in trabajadores for p2 in trabajadores if p1 != p2]


print(partidas(trabajadores))
