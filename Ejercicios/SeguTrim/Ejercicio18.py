"""
    Escribir la función palabaras a la que se le pasan dos strings, siendo el segundo una cadena
    de separadores por los que separar el primero. La función ha de devolver una lista de palabras separadas.
"""

_SEPARADORES = '.:·;,()[]{}<>_-=\'\"#¿¡?! '


def separar_cadena(cadena, separadores):
    ret = []
    cad = ''
    for letra in cadena:
        if letra in separadores:
            ret.append(cad)
            cad = ''
        else:
            cad += letra
    ret.append(cad)
    return ret


print(separar_cadena('el,per.ro de san r<o>que', _SEPARADORES))
