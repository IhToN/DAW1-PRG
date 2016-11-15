"""
    Crear un diccionario que contenga una tupla binomial como clave, y como valor tendrá la distancia
    al origen del punto especificado por la tupla. Escribir una función  a la que se le pasa un punto
    y devuelve la distancia al origen del punto.
"""
from math import hypot
from random import randint




def addPunto(diccionario, x, y):
    diccionario[(x, y)] = hypot(x, y)


def generadorPuntos(cantidad, limite_inferior, limite_superior):
    for elemento in range(cantidad):
        addPunto(diccionario, randint(limite_inferior, limite_superior), randint(limite_inferior, limite_superior))

diccionario = {}
generadorPuntos(50, -100, 100)
print(diccionario)
