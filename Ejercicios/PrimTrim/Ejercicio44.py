"""
    Crear una función que genere un diccionario que reúna como clave un número y como valor su cuadrado.
        a. Solución Original
        b. Hacer un diccionario por comprensión con la letra y su valor ASCII (65 a 90 y 97 a 122).
"""


def dic_cuadrados(limite):
    return {numero: numero ** 2 for numero in range(limite + 1)}


def dic_ascii():
    return {chr(char): char for char in range(65, 122) if not 91 <= char <= 96}


print(dic_cuadrados(5))
print(sorted(dic_ascii().items())) # Mérito de Alfon, por aprender a usar Stackoverflow