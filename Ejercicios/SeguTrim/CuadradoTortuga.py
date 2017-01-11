''' Define una función que pinta un cuadrado. Le pasamos como parámetro el lado
de un cuadrado y la tortuga pinta un cuadrado con ese lado'''

import turtle

s = turtle.Screen()
t = turtle.Turtle()


def cuadrado(lado):
    '''Dibuja cuadrado para longitud de lado pasada como parámetro'''

    for i in range(4):
        t.forward(lado)
        t.right(90)


'''for i in range (0, 200, 2):
    cuadrado(i)'''

''' Escribir una función que llamando a la función cuadrado pinte un cuadrado,
lo gire, etc'''


def cuadradoanida(lado):
    '''Dibuja cuadrados anidados para longitud de lado pasado como parámetro'''

    t.right(90)
    cuadrado(lado)
    t.left(90)
    cuadrado(lado)
    t.right(90)


'''Función giracuadros. Va a tener 3 parametros: lado, número de cuadrados y
águlo de giro'''


def giracuadros(lado, numCuadrados, angulo):
    '''Dibuja un cuadrado de lado dado, gira el ángulo indicado y dibuja el
siguiente hasta el número deseado'''

    for i in range(numCuadrados):
        cuadrado(lado)
        t.right(angulo)


giracuadros(100, 15, 30)

# Pausar turtle para cancelar el autocierre. Se cerrará al hacer click.
turtle.exitonclick()
