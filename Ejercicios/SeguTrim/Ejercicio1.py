"""
    Hacer un triángulo equilátero con un lado dado.
        a. Queremos una función a la que pasamos el tamaño del lado y cuántos triángulos queremos y nos dibuje
        una figura simétrica formada por triángulos que no se superpongan
        b. Hacer estrella con un número de puntas dado
"""

# Importamos métodos necesarios de turtle y creamos la pantalla.
import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.speed(10)


def equilatero(lado):
    '''Genera un triángulo equilatero para un lado dado por usuario'''

    for i in range(3):
        t.forward(lado)
        t.right(120)


def giratriangulo(triangulos, lado):
    '''Genera figura simétrica con número de triángulos y longitud de lado
    definidos por usuario '''

    for i in range(triangulos):
        # Para que la suma total de ángulos sea la circunferencia completa
        angulo = 360 / triangulos
        t.right(angulo)
        equilatero(lado)


def estrella(puntas, longitud):
    '''Genera figura simétrica con número de puntas y longitud de lado definido
     por usuario'''

    for i in range(puntas):
        if puntas % 2 == 0:
            # Al ser impar para completar 360 grados y que la figura sea cerrada
            # hay que contar una punta menos, para vertices pares no se puede
            # sin levantar el trazo.
            angulo = 180.0 + 180 / (puntas - 1)


        else:
            # Para que se invierta el sentido de la línea creando el vértice
            # Y la suma de todos los ángulos sea 360 grados.
            angulo = 180.0 + 180 / puntas

        t.right(angulo)
        t.forward(longitud)


estrella(12, 300)

# Pausar turtle para cancelar el autocierre. Se cerrará al hacer click.
turtle.exitonclick()
