"""
    Hacer un jueguecillo de un coche.
    a. Buscar en la documentación una forma de ver el tamaño del canvas.
    b. Comprobar una colisión entre dos coches, en caso de colisión cambiarles el color.
    c. Colocar una pelota que rebote, añadiendo un ángulo de corrección. Se colocarán dos porterías y
        cuando la pelota entra por alguno de ellos se aumenta el valor de un contador.
"""
import multiprocessing.dummy as multiprocessing
import turtle
from random import randint

screen = turtle.Screen()
car1 = turtle.Turtle()
car1.shape('square')
car2 = turtle.Turtle()
car2.shape('square')
ball = turtle.Turtle()
ball.shape('circle')

car1_size, car2_size, ball_size = [0, 0], [0, 0], [0, 0]

stop_car = multiprocessing.Event()


def initialize_game():
    """Inicializa los objetos principales, orientándolos y posicionándolos"""
    car1.fillcolor('red')
    car2.fillcolor('blue')
    ball.fillcolor('green')

    # car1.setheading(0)
    car2.left(180)
    ball.left(170)

    car1.up()
    car2.up()
    ball.up()

    car1.setpos(-400, 0)
    car2.setpos(400, 0)

    car1_size[0], car1_size[1] = 20, 20
    car2_size[0], car2_size[1] = 20, 20
    ball_size[0], ball_size[1] = 20, 20

    multiprocessing.Queue()
    move_car1 = multiprocessing.Process(target=move_object, args=(car1, 90, stop_car,))
    move_car2 = multiprocessing.Process(target=move_object, args=(car2, 90, stop_car,))
    move_ball = multiprocessing.Process(target=move_object, args=(ball, -10,))

    move_car1.start()
    move_car2.start()
    move_ball.start()


def check_canvas(turtobj):
    """Comprobamos si el objeto está dentro del canvas"""
    if turtobj == car1:
        turtobj_size = car1_size
    elif turtobj == car2:
        turtobj_size = car2_size
    elif turtobj == ball:
        turtobj_size = ball_size

    width = screen.window_width() // 2 - turtobj_size[0]
    height = screen.window_height() // 2 - turtobj_size[1]
    xcor = turtobj.xcor()
    ycor = turtobj.ycor()
    return not (width < xcor or -width > xcor or height < ycor or -height > ycor)


def check_collision(obj1, obj2):
    """Comprobamos si los objetos han colisionado entre sí"""
    if obj1.distance(obj2) < car1_size[0]:
        print("Puuuum, y explotó")
        stop_car.set()


def bounce(turtobj, horizontal=True):
    if turtobj.xcor() > 0 and turtobj.ycor() > 0:
        if horizontal:
            ret = turtobj.towards(0, screen.window_height() // 2)
    elif turtobj.xcor() > 0 and turtobj.ycor() < 0:
        if horizontal:
            ret = turtobj.towards(0, -screen.window_height() // 2)
    elif turtobj.xcor() < 0 and turtobj.ycor() > 0:
        if horizontal:
            ret = turtobj.towards(0, -screen.window_height() // 2)
    elif turtobj.xcor() > 0 and turtobj.ycor() > 0:
        if horizontal:
            ret = turtobj.towards(0, screen.window_height() // 2)
    else:
        ret = 90
    return ret


def move_object(turtobj, variance=0, stop=multiprocessing.Event()):
    """Movemos el objeto en pasos de 5"""
    while not stop.is_set():
        turtobj.forward(5)
        if not check_canvas(turtobj):
            randvariance = randint(0, abs(variance))
            if variance < 0:
                randvariance = -randvariance
            angle = turtobj.towards(0, turtobj.ycor())
            if angle == 0:
                angle = 180
            turtobj.setheading(bounce(turtobj))
            print(bounce(turtobj))
        if turtobj == car1 or turtobj == car2:
            check_collision(car1, car2)


initialize_game()

screen.exitonclick()
