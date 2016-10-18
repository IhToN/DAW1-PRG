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
        if c in 'Aa':
            res[0] += 1
        elif c in 'Ee':
            res[1] += 1
        elif c in 'Ii':
            res[2] += 1
        elif c in 'Oo':
            res[3] += 1
        elif c in 'Uu':
            res[4] += 1
    return res


def mostrar(cadena):
    """
    Muestra el desglose de vocales de la cadena
    :param cadena:
    :return:
    """
    shw = cont_vocales(cadena)
    print("Desglose de Vocales:")
    print("     A =", shw[0])
    print("     E =", shw[1])
    print("     I =", shw[2])
    print("     O =", shw[3])
    print("     U =", shw[4])


mostrar('uiuaadingdangramalamadingdong')
