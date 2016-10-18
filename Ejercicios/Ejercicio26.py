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
        if c in 'aeiou' or c in 'AEIOU':
            res += 1
    return res


print(cont_vocales('uiuaabangbangramalamadingdong'))
