"""
    Crear una lista por comprensión que contenga todas las sílabas posibles en castellano
    cuya primera letra sea una consonante y cuya segunda sea una vocal.
    a. Solucion original
    b.
"""


def silabas_convoc():
    return [con + voc for con in 'bcdfghjklmnñpqrstvwxyz' for voc in 'aeiou']


def palabras_ds():
    return [sil1 + sil2 for sil1 in silabas_convoc() for sil2 in silabas_convoc()]


print(len(silabas_convoc()), silabas_convoc())
print(len(palabras_ds()), palabras_ds())
