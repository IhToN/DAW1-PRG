"""
    Define un Anagrama como una palabra que se puede obtener con las mismas letras de una palabra.
    Escribe una función a la que se le pasen dos palabras y nos diga si la segunda es un anagrama de la primera.
"""

def es_anagrama(palabra1, palabra2):
    """ Devuelve un boolean tal que palabra2 sea un anagrama de palabra1
    """
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

print(es_anagrama("paco", "copa"))
