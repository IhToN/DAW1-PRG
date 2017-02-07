"""
    Tablas de multiplicar bien formateadas.
"""


def tabla_del(numero, cuantos):
    for i in range(cuantos + 1):
        print('{0:3d}  x {1:3d} = {2:3d}'.format(numero, i, numero * i))


tabla_del(15, 25)
