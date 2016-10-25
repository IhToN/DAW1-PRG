"""
    Escribe una función a la que se suman dos puntos y se hace la suma vectorial de dichos puntos.
"""


def suma_vectorial(p1, p2):
    """
    Devuelve la suma vectorial de dos puntos
    :param p1:
    :param p2:
    :return:
    """
    return p1[0] + p2[0], p1[1] + p2[1]  # Sumamos ambas X y sumamos ambas Y, devolviendo una tupla


# Preguntamos e inicializamos los puntos, el primer punto preguntamos valor a valor
x1 = int(input('Introduce el primer punto (x):\n'))
y1 = int(input('Introduce el primer punto (y):\n'))
punto1 = x1, y1
# El segundo punto, como somos prós, pedimos que el usuario ponga x,y
punto2 = tuple(int(x) for x in input('Introduce el segundo punto (y):\n').split(","))

print('Suma vectorial de', punto1, 'y', punto2, '=', suma_vectorial(punto1, punto2))
