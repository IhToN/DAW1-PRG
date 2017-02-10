"""
    Queremos escribir un programa al que le vamos dando palabras de forma interactiva.
    Este programa nos dará dichas palabras y calculará y almacenará todas las palabras posibles que se puedan
    formar con las combinaciones posibles de las letras de cada palabra introducida.
"""
import itertools

def lista_anagramas(palabra):
    """ Devuelve un set con todos los anagramas de una palabra
    """
    ret = set()
    for elem in itertools.permutations(palabra):
        ret.add(''.join(elem))
    return ret


def lista_shifts(palabra, posicion):
    """ Devuelve con todas las posibles "palabras" generadas por el movimiento de una letra
    de la palabra, especificada por la posicion (de 0 hasta len(palabra)-1)
    """
    ret = []
    letra = palabra.pop(posicion)
    for i in range(len(palabra) + 1):
        combination = ''.join(palabra[:i] + list(letra) + palabra[i:])
        combination2 = ''.join(palabra[i:] + list(letra) + palabra[:i])
        ret.append(combination)
        ret.append(combination2)
    return tuple(ret)


def add_anagrama(diccionario, palabra):
    """ Agrega la palabra y sus anagramas a un diccionario.
    """
    diccionario[palabra] = lista_anagramas(palabra)


def main():
    dicc = dict()

    palabra = input("Introduce una palabra a agregar al diccionario de Anagramas:\n")
    while palabra:
        add_anagrama(dicc, palabra)
        palabra = input("Introduce una palabra a agregar al diccionario de Anagramas:\n")

    for par in dicc.items():
        print(len(par[1]), par)