"""
    Definir una función a la cual se le pase una cadena y ésta devuelva cuántas vocales tiene esa cadena.
"""


def cont_vocales(cadena):
    """
    Devuelve la cantidad de vocales (mayúsculas o minúsculas, no tildadas) de la cadena
    :param cadena:
    :return:
    """
    res = 0
    for c in cadena:
        if es_vocal(c):
            res += 1
    return res


def es_vocal(char):
    """
    Devuelve True si la cadena es un caracter vocálico
    :param char:
    :return:
    """
    ret = False
    if len(char) != 1:  # Hoyga, 'pe' NO es una es_vocal, de momento será es_vocal cuando sólo haya 1 letra en la cadena
        return ret
    else:   # Toda esta perorata se puede hacer en una línea como lo ha hecho Blas, así se ve un poco más claro
        if char in 'aeiou' \
                or char in 'áéíóú' \
                or char in 'äëïöü' \
                or char in 'àèìòù' \
                or char in 'âêîôû' \
                or char in 'AEIOU' \
                or char in 'ÁÉÍÓÚ' \
                or char in 'ÄËÏÖÜ' \
                or char in 'ÀÈÌÒÙ' \
                or char in 'ÂÊÎÔÛ':
            ret = True
    return ret


print(cont_vocales('uiuaadingdangramalamadingdong'))
