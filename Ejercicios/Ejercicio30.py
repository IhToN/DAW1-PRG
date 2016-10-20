"""
    Crear una lista por comprensión que contenga todas las sílabas posibles en castellano
    cuya primera letra sea una consonante y cuya segunda sea una vocal.
"""


def silabas_convoc():
    return [con + voc for con in 'bcdfghjklmnñpqrstvwxyz' for voc in 'aeiou']


print(silabas_convoc())
