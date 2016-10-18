"""
   Definir una función a la cual se le pase una cadena y ésta devuelva el número de
   ocurrencias de cada una de las vocales.
"""


def cont_vocales(cadena):
    """
    Devuelve la cantidad de vocales desglosadas (mayúsculas o minúsculas, no tildadas) de la cadena
    :param cadena:
    :return:
    """
    res = [0, 0, 0, 0, 0]
    for c in cadena:
        if c == 'a' or c == 'A':
            res[0] += 1
        elif c == 'e' or c == 'E':
            res[1] += 1
        elif c == 'i' or c == 'I':
            res[2] += 1
        elif c == 'o' or c == 'O':
            res[3] += 1
        elif c == 'u' or c == 'U':
            res[4] += 1
    return res


print(cont_vocales('uiuaabangbangramalamadingdong'))
