"""
    Tablas de multiplicar bien formateadas.
"""


def tabla_del(numero, cuantos):
    for i in range(cuantos + 1):
        # print('{0:3d}  x {1:3d} = {2:3d}'.format(numero, i, numero * i))
        print(str(numero).ljust(4), 'x'.center(3), str(i).rjust(4), '='.center(3), str(numero * i).rjust(4))


tabla_del(15, 25)
