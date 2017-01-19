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

shapepoly = []


def move_turtle(x, y):
    """Si estamos en modo captura, movemos la tortuga y vamos guardando los puntos"""
    if capture_mode:
        turtobj_main.setpos(x, y)
        shapepoly.append((x, y))


def toggle_capture():
    """Activamos o desactivamos el modo captura, según toque"""
    global capture_mode
    capture_mode = not capture_mode
    if capture_mode:
        turtobj_cm.fillcolor('green')
    else:
        turtobj_cm.fillcolor('red')
        capture_shape()


def capture_shape():
    """Capturamos la figura, la colocamos como figura de la tortuga, limpiamos el dibujo y la colocaos en el centro"""
    shapepoly.append(shapepoly[0])
    print(shapepoly)
    screen.register_shape('proshape', tuple(shapepoly))
    turtobj_main.shape('proshape')
    shapepoly.clear()
    turtobj_main.clear()
    turtobj_main.up()
    turtobj_main.home()
    turtobj_main.down()


# Capturamos el screenclick para mover la tortuga y el espacio para activar o desactivar el modo captura
screen.onclick(move_turtle)
screen.onkey(toggle_capture, 'space')
screen.listen()

turtle.done()
