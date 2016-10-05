"""
    Escribir una función a la que se le pase una cadena, la cual devolverá verdadero o falso.
    La función es llamará es_palindromo.
        a. Hacerlo usando las funciones del ejercicio 15 y 16.
        b. Hacerlo con un algoritmo propio.
"""

solution = 'b'  # Solución a comprobar


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
    # Solución A
    if solution == 'a':
        trimString = sin_blancos(string)
        return invierte(trimString) == trimString
    elif solution == 'b':
        ret = ''
        for c in string:
            if c != ' ':
                ret += c
        invRet = ''
        for c in ret:
            invRet = c + invRet
        return ret == invRet


testString = input('Introduce the phrase that you wanna check:\n')
print('It\'s palindrome?', es_palindromo(testString))
