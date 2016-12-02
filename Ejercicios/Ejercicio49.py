"""
    Escribe una función a la que se le pasa un texto y produce un diccionario cuya claves son
    todas las letras diferentes del texto y como valor el conjunto de las palabras en las que aparece esa letra.
"""


def letras_texto(texto):
    """ Devuelve un diccionario tal que cada par es letra - set(palabras que contiene letra)
    """
    ret = dict()
    texto = texto.replace(".", "").replace(",", "").replace("-", "").lower()
    palabras = texto.split()
    for letra in texto:
        if letra not in ret:
            ret[letra] = contiene_letra(letra, palabras)
    return ret


def contiene_letra(letra, palabras):
    """ Devuelve un set con las palabras que contienen la letra
    """
    ret = set()
    for palabra in palabras:
        if letra in palabra and palabra not in ret:
            ret.add(palabra)
    return ret


print(letras_texto(
    "Habia una vez, un circo que alegraba siempre el corazón. Lleno de color, un mundo de ilusión pleno de alegría y emoción"))
