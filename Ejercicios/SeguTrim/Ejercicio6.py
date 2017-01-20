"""
    Hacer un pequeño programita que permita hacer dibujos con la tortuga haciendo clicks en pantalla.
    Capturar la forma dibujada (con una tupla de puntos) y, con esa forma, cambiaremos la imagen de la tortuga.
"""
import turtle

# Inicializamos to la mierda
screen = turtle.Screen()

turtobj_cm = turtle.Turtle()
turtobj_main = turtle.Turtle()

capture_mode = False
turtobj_cm.fillcolor('red')
turtobj_cm.shape('square')
turtobj_cm.up()
turtobj_cm.setpos(-300, 250)
turtobj_main.speed(9)

shapepoly = [(0, 0)]


def move_turtle(x, y):
    """Si estamos en modo captura, movemos la tortuga y vamos guardando los puntos"""
    if capture_mode:
        turtobj_main.setheading(turtobj_main.towards(x, y))
        turtobj_main.setpos(x, y)
        shapepoly.append((x, y))


def toggle_capture(x=0, y=0):
    """Activamos o desactivamos el modo captura, según toque"""
    screen.tracer(0)
    global capture_mode
    capture_mode = not capture_mode
    if capture_mode:
        turtobj_cm.fillcolor('green')
        turtobj_main.shape('classic')
    else:
        turtobj_cm.fillcolor('red')
        capture_shape()
    screen.tracer(1)


def capture_shape():
    """Capturamos la figura, la colocamos como figura de la tortuga, limpiamos el dibujo y la colocaos en el centro"""
    if not shapepoly:
        return
    screen.tracer(0)
    print(shapepoly)
    screen.register_shape('proshape', tuple(shapepoly))
    turtobj_main.shape('proshape')
    shapepoly.clear()
    shapepoly.append((0, 0))
    turtobj_main.clear()
    turtobj_main.up()
    turtobj_main.home()
    turtobj_main.down()
    screen.tracer(1)


def easter_egg(x, y):
    """Pequeño easter egg"""
    turtobj_main.circle(15)


def toggle_pen(x, y):
    """Cambiar estado del lapiz de la tortuga"""
    if turtobj_main.isdown():
        turtobj_main.up()
    else:
        turtobj_main.down()


# Capturamos el screenclick para mover la tortuga y el espacio para activar o desactivar el modo captura
screen.onkey(toggle_capture, 'space')
turtobj_cm.onclick(toggle_capture)
turtobj_main.onclick(toggle_pen, btn=1)
turtobj_main.onclick(easter_egg, btn=3)
screen.onclick(move_turtle)
screen.listen()
turtle.done()
