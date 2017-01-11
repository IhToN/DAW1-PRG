"""
    Vamos a imprimir una tabla ASCII desde el 32 hasta el 255 (se puede probar desde 0, a ver qué hace).
"""


def printASCII(idStart, idFin):
    copystart = idStart
    while copystart <= idFin:
        if copystart % 8 == 0:
            print('')
        print(copystart, ' = ', chr(copystart))
        copystart += 1


printASCII(0, 255)
