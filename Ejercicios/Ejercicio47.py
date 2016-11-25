"""
    Queremos escribir un programa al que le vamos dando palabras de forma interactiva.
    Este programa nos dará dichas palabras y calculará y almacenará todas las palabras posibles que se puedan
    formar con las combinaciones posibles de las letras de cada palabra introducida.
"""


def lista_anagramas(palabra):
    ret = []
    for i in range(len(palabra)):
        for elem in lista_shifts(list(palabra), i):
            if elem not in ret:
                ret.append(elem)
    return ret


def lista_shifts(palabra, posicion):
    ret = []
    letra = palabra.pop(posicion)
    for i in range(len(palabra) + 1):
        combination = ''.join(palabra[:i] + list(letra) + palabra[i:])
        combination2 = ''.join(palabra[i:] + list(letra) + palabra[:i])
        ret.append(combination)
        ret.append(combination2)
    return tuple(ret)


def add_anagrama(diccionario, palabra):
    diccionario[palabra] = lista_anagramas(palabra)
    return diccionario


dicc = dict()
add_anagrama(dicc, "hola")
print(dicc)
