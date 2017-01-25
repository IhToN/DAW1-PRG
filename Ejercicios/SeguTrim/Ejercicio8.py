"""
    Hacer un fractal de segmentos subdivididos en triángulos
"""
import turtle

screen = turtle.Screen()
turtobj = turtle.Turtle()
turtobj.speed(0)


# [(p1x, p1y, p1d), (p2x, p2y, p2d)]

def pinta_segmento(tortuga, punto1, punto2):
    """ Pintamos el segmento con su respectivo triángulo

        Tortuga = Objeto de Turtle
        Punto# = Tupla(x, y, heading)

        Devuelve una lista de tuplas con los nuevos puntos"""
    tortuga.up()
    tortuga.setpos(punto1)
    tortuga.setheading(tortuga.towards(punto2))
    distancia = tortuga.distance(punto2) / 3

    ret = []

    tortuga.down()
    ret.append((tortuga.xcor(), tortuga.ycor()))
    tortuga.fd(distancia)
    ret.append((tortuga.xcor(), tortuga.ycor()))
    tortuga.left(60)
    tortuga.fd(distancia)
    ret.append((tortuga.xcor(), tortuga.ycor()))
    tortuga.right(120)
    tortuga.fd(distancia)
    ret.append((tortuga.xcor(), tortuga.ycor()))
    tortuga.left(60)
    tortuga.fd(distancia)
    ret.append((tortuga.xcor(), tortuga.ycor()))

    return ret


def main_function(repeticiones):
    """ Pinta el fractal"""
    lista_puntos = [(-900, 0), (900, 0)]
    subsegs = []
    for i in range(repeticiones):
        turtobj.clear()
        segmentos = list()
        if subsegs:
            for subseg in subsegs:
                segmentos.append(subseg)
        else:
            segmentos.append(lista_puntos[0])
            segmentos.append(lista_puntos[1])
        subsegs = []
        for l in range(0, len(segmentos) - 1):
            segmentitos = pinta_segmento(turtobj, segmentos[l], segmentos[l + 1])
            for segmentito in segmentitos:
                subsegs.append(segmentito)


repeticiones = int(input("Cuantos triangulitos quieres en el fractal?\n"))
main_function(repeticiones)

turtle.done()
