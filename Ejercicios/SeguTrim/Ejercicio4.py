"""
    Colorear una serie de cuadrados de distintos colores, cada uno dentro del otro.
"""

import turtle
from random import randint
from math import hypot

s = turtle.Screen()
t = turtle.Turtle()
t.speed(10)


def color_generator():
    """Genera un color hexadecimal aleatorio"""
    return '#%02X%02X%02X' % (randint(0, 255), randint(0, 255), randint(0, 255))


def poligono(vertices, lado):
    """Pinta un polígono regular para un lado y número de lados dado por el usuario"""
    originhead = t.heading()
    t.setheading(90)
    t.down()
    for i in range(vertices * 2):
        t.forward(lado // 2)
        if i % 2 == 0:
            t.right(360 / vertices)
    t.up()
    t.setheading(originhead)


def cuadrados_coloreados(min_size, num_cuadrados):
    """Pinta una serie de cuadrados concéntricos de distinto color, cada uno más pequeño que el anterior"""
    for i in range(num_cuadrados, 1, -1):
        t.up()
        t.setpos(0, 0)
        apotema = min_size * (i * 0.5)
        lado = apotema // 2
        print("Apotema " + str(apotema) + " - Lado " + str(lado))
        t.setpos(-lado // 2, 0)
        t.begin_fill()
        t.fillcolor(color_generator())
        poligono(4, lado)
        t.end_fill()


cuadrados_coloreados(150, 40)

turtle.exitonclick()
