"""
    Escribir una función a la que se le pase una cadena, la cual devolverá verdadero o falso.
    La función es llamará es_palindromo.
"""


# Función de Valor
def sin_blancos(string):
    ret = ''
    for c in string:
        if c != ' ':
            ret += c
    return ret


# Función de Valor
def invierte(string):
    ret = ''
    for c in string:
        ret = c + ret
    return ret


def es_palindromo(string):
    trimString = sin_blancos(string)
    return invierte(trimString) == trimString


testString = input('Introduce the phrase that you wanna check:\n')
print('It\'s palindrome?', es_palindromo(testString))
