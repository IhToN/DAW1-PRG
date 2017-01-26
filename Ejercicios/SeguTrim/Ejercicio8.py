"""
    Hacer un fractal de segmentos subdivididos en triángulos
"""
import turtle

screen = turtle.Screen()
turtobj = turtle.Turtle()
turtobj.speed(2)
turtobj.hideturtle()


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
    for i in range(1, 5):
        ret.append(tortuga.pos())
        tortuga.fd(distancia)
        if i % 2:
            tortuga.left(60)
        elif i == 2:
            tortuga.right(120)
    ret.append(tortuga.pos())
    tortuga.up()
    return ret


def main_function(repeticiones):
    """ Pinta el fractal hasta el subnivel 'repeticiones' """
    lista_puntos = [(-300, 0), (300, 0)]
    for i in range(repeticiones):
        turtobj.clear()
        segmentos = lista_puntos[:]
        lista_puntos = []
        print("Lista de segmentos en la repeticion", i, end=":\n")
        print(segmentos, end="\n")
        for l in range(0, len(segmentos) - 1):
            segmentitos = pinta_segmento(turtobj, segmentos[l], segmentos[l + 1])
            if lista_puntos:
                segmentitos.pop(0)
            for segmentito in segmentitos:
                lista_puntos.append(segmentito)


# repeticiones = int(input("Cuantos triangulitos quieres en el fractal?\n"))
repeticiones = 10
main_function(repeticiones)

turtle.done()
