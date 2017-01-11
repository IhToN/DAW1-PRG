"""
    Queremos construir un diccionario que contenga los divisores de un número.
    La clave del diccionario será el número y el valor una tupla de los divisores de dicho número.
    Para testear la función cargaremos los números del 1 al 1000.
    a. Solución Principal
    b. A partir del diccionario anterior queremos construir un segundo diccionario que tenga el
        significado inverso. Es decir, la clave será un número y el valor una lista con todos los múltiplos
        de dicho número.
"""
from math import ceil


def divisores(numero):
    """ Devuelve una tupla con los divisores de numero
    """
    ret = ()
    for i in range(1, ceil((numero + 1) / 2)):
        if numero % i == 0:
            ret += i,
    ret += numero,
    return ret


def dic_divisores(start, stop):
    """ Devuelve un diccionario cuya clave es un número
    y el valor es una tupla con los divisores de dicho número
    sin incluir el 1 ni él mismo en el rango especificado
    """
    ret = dict()
    if start < 2:
        start = 2
    for num in range(start, stop + 1):
        temp_div = divisores(num)
        ret[num] = temp_div[1:len(temp_div) - 1]
    return ret


def dic_multiplos(start, stop):
    """ Devuelve un diccionario cuy clave es un número
    y el valor es una lista con los múltiplos de dicho número
    sin incluir el 1 ni él mismo en el rango especificado
    """
    ret = dict()
    dicdiv = dic_divisores(start, stop)
    for key in dicdiv.keys():
        mults = multiplos(dicdiv, key)
        if mults:
            ret[key] = multiplos(dicdiv, key)
    return ret

def multiplos(diccionario, clave):
    """ Devuelve un set con todos los múltiplos de clave
    dentro del diccionario de divisores
    """
    ret = set()
    for num in diccionario.keys():
        if clave in diccionario[num]:
            ret.add(num)
    return ret


print(dic_divisores(1, 1000))
print(dic_multiplos(1, 1000))
