"""
    Crear un diccionario que cuente cuántas veces aparece un carácter en un texto.
    La función tendrá como parámteros una cadena que contiene un texto y devolverá un diccionario
    cuya clave será el carácter y el valor el contador de dicho carácter.
     a. Solución Original
     b. Hacer el contador de palabras en lugar de letras.
     c. Hacer una segunda versión del contador de palabras que sea capaz de usar más de un separador.
     d. Leer de un archivo y procesar según la función C
"""
from string import ascii_uppercase


def cuenta_caracteres(texto):
    """ Devuelve un diccionario cuyas claves son caracteres y su valor la cantidad de veces que
    aparecen en el texto
    """
    ret = dict()
    texto = texto.upper()
    for char in texto:
        if char not in ret:
            ret[char] = 1
        else:
            ret[char] += 1
    return ret


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


texto_prueba = "Un viejo y una vieja van pa' Albacete, van pa' Albacete," \
               "y a mitá de camino va y se la mete, va y se la mete."

print("Contador de Letras:")
print(cuenta_caracteres(texto_prueba))
print(sorted(cuenta_caracteres(texto_prueba).items()))

print("\nContador de Palabras")
print(cuenta_palabras(texto_prueba))
print(sorted(cuenta_palabras(texto_prueba).items()))

print("\nContador de Palabras por Separadores")
separadores = set('.:;,()_-\'')
print(cuenta_palabras_sep(texto_prueba, separadores))
print(sorted(cuenta_palabras_sep(texto_prueba, separadores).items()))
