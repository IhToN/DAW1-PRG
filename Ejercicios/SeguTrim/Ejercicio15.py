"""
    Realizar un análisis de un texto, el cual consistirá en separar un texto por palabras y realizar
    un conteos de cuantas veces aparece la palabra en dicho texto.
        Considerando el separador blanco.
        Considerando un conjunto de separadores.
        Hacer una versión de este programa que permita realizar un análisis de un .py,
            de tal forma que reconozca los operadores.
"""

separadores = set('.:;,()_-\'\"¿¡?!')


def cuenta_palabras(texto):
    """ Devuelve un diccionario cuyas claves son palabras y su valor la cantidad de veces
    que aparecen en el texto
    """
    ret = dict()
    texto = texto.lower().split()
    for palabra in texto:
        ret[palabra] = texto.count(palabra)
    return ret


def cuenta_palabras_sep(texto, separadores):
    """ Devuelve un diccionario cuyas claves son palabras y su valor la cantidad de veces
    que aparecen en el texto dividido no sólo por espacios, sino por cualquier set de separadores
    """
    for separador in separadores:
        texto = texto.replace(separador, ' ')
    return cuenta_palabras(texto)


def abrir():
    res = dict()
    strf = input("¿Qué fichero quieres abrir?\n")
    try:
        fichero = open(strf)
        for linea in fichero:
            newdic = cuenta_palabras_sep(linea, separadores)
            for key, value in newdic.items():
                if key in res:
                    res[key] = res[key] + value
                else:
                    res[key] = value
        fichero.close()
        print(res)
        return res
    except FileNotFoundError as Error:
        print("El fichero no existe, te va a tocar hacer otra cosita.\n")


abrir()
