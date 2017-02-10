"""
    Descargar y recorrer http://www.teoruiz.com/lemario/lemario-20101017.txt.gz
        Comprobar si una palabra está o no en el diccionario.
        Dada una palabra devolver una lista con todos los anagramas de esa palabra que pertenezcan al castellano.
"""
from Ejercicios.PrimTrim.Ejercicio47 import lista_anagramas

_DICCIONARIO = 'lemario-20101017.txt'


def word_in_dic(word):
    """ Comprueba que word esté en el diccionario de palabras.
    """
    try:
        fichero = open(_DICCIONARIO)
        for palabra in fichero:
            if word == palabra.strip():
                fichero.close()
                return True
        fichero.close()
        return False
    except FileNotFoundError as error:
        print("No se ha podido abrir el archivo.", error)

def anagrams_in_dic(word):
    """ Devuelve una lista de todos los anagramas de una palabra siempre que estos estén en el diccionario
    de palabras.
    """
    lanagrams = lista_anagramas(word)
    ret = []
    for anagrama in lanagrams:
        if word_in_dic(anagrama):
            ret.append(anagrama)
    return sorted(ret)

print(anagrams_in_dic("roma"))
