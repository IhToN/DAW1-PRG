"""
    a. Escribir una función que pinte triángulos inscritos en un círculo.
    b. Escribir una función que pinte cuadrados inscritos en un círculo.
    c. Escribir una función que pinte un polígono regular de X lados.ç
    d. Escribir una función que pinte X polígonos regulares concéntricos, cada uno más grande que el anterior.
"""

import turtle
from math import tan, sqrt

s = turtle.Screen()
t = turtle.Turtle()
t.speed(2)


def orientar_centro():
    '''Colocar la tortuga mirando al centro'''
    return 180 + tan(t.ycor() / t.xcor())


def poligono(vertices, lado):
    '''Pinta un polígono regular para un lado y número de lados dado por el usuario'''
    originhead = t.heading()
    t.setheading(90)
    t.down()
    for i in range(vertices):
        t.forward(lado)
        t.right(360 / vertices)
    t.up()
    t.setheading(originhead)


def circunferencia(lado, lados_poly):
    '''Recorremos una circunferencia y pintamos el número de triángulos dado'''
    t.up()
    angulo = 360 / lados_poly
    t.setpos(0, lado / 2)
    # t.setheading(90)
    for i in range(lados_poly):
        poligono(lados_poly, lado // lados_poly)
        t.rt(angulo)
        t.forward(lado / lados_poly * 3.15)


def concentricos(lados_poly, size, num_polys):
    for i in range(num_polys):
        t.up()
        t.setpos(0, 0)
        t.setheading(90)
        r = size // 2 + i * 15
        t.setpos(-r, -r)
        poligono(lados_poly, sqrt(2 * r ** 2))


# circunferencia(500, 5)
concentricos(12, 100, 15)

turtle.exitonclick()
