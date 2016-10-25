"""
    Escribe una función a la que se suman dos puntos y se hace la suma vectorial de dichos puntos.
    a. Solución Original
    b. Definir la resta vectorial
    c. Definir el módulo del vector de un punto (distancia al origen)
"""
from math import sqrt, hypot


def suma_vectorial(p1, p2):
    """ Devuelve la suma vectorial de dos puntos
    """
    return p1[0] + p2[0], p1[1] + p2[1]  # Sumamos ambas X y sumamos ambas Y, devolviendo una tupla


def resta_vectorial(p1, p2):
    """ Devuelve la resta vectorial de dos puntos
    """
    return p1[0] - p2[0], p1[1] - p2[1]  # restamos ambas X y restamos ambas Y, devolviendo una tupla


def modulo(punto):
    """ Devuelve el módulo del vector punto
    """
    return sqrt(punto[0] ** 2 + punto[1] ** 2)
    # También se puede hacer con la función "hypot"
    # return hypot(punto[0], punto[1])


# Preguntamos e inicializamos los puntos, el primer punto preguntamos valor a valor
x1 = int(input('Introduce el primer punto (x):\n'))
y1 = int(input('Introduce el primer punto (y):\n'))
punto1 = x1, y1
# El segundo punto, como somos prós, pedimos que el usuario ponga x,y
''' Traduciendo la frase de abajo es:
 punto2 va a ser una tupla, la tupla va a ser igual que convertir a integer x.
 la x es cada elemento que hay en dividir la cadena introducida según sus comas
 es decir:
 1,4,5,6 la x irá pasando siendo x = 1, x = 4, x = 5, x = 6
'''
punto2 = tuple(int(x) for x in input('Introduce el segundo punto (x,y):\n').split(","))

print('Suma vectorial de', punto1, 'y', punto2, '=', suma_vectorial(punto1, punto2))
print('Resta vectorial de', punto1, 'y', punto2, '=', resta_vectorial(punto1, punto2))
print('Módulo de', punto1, '=', modulo(punto1))
