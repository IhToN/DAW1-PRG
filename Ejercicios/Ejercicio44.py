"""
    Crear una función que genere un diccionario que reúna como clave un número y como valor su cuadrado.
"""


def dic_cuadrados(limite):
    return {numero: numero ** 2 for numero in range(limite + 1)}


def dic_ascii():
    return {chr(char): char for char in range(65, 122) if not 91 <= char <= 96}


print(dic_cuadrados(5))
print(sorted(dic_ascii().items()))
