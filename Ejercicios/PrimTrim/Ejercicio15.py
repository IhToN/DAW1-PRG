"""
    Escribir una función en la que introduciendo una cadena devuelve dicha cadena sin blancos.
    La función se llamará sin_blancos().
"""


def sin_blancos(string):
    ret = ''
    for c in string:
        if c != ' ':
            ret += c
    return ret


strToTest = input('Introduce a phrase:\n')
print(sin_blancos(strToTest))
