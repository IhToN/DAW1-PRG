"""
    Crear un diccionario que cuente cuántas veces aparece un carácter en un texto.
    La función tendrá como parámteros una cadena que contiene un texto y devolverá un diccionario
    cuya clave será el carácter y el valor el contador de dicho carácter.
     a. Solución Original
     b. Hacer el contador de palabras en lugar de letras.
"""
from string import ascii_uppercase


def cuenta_caracteres(texto):
    ret = dict()
    texto = texto.upper()
    for letra in ascii_uppercase:
        if texto.count(letra):
            ret[letra] = texto.count(letra)
    return ret


def cuenta_palabras(texto):
    ret = dict()
    texto = texto.lower()
    for palabra in texto.split():
        ret[palabra] = texto.count(palabra)
    return ret


def cuenta_palabras_sep(texto, separadores):
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
