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
screen.tracer(1, 0)

car1 = turtle.Turtle()
car1.shape('square')
car1.shapesize(1, 3, 3)
car2 = turtle.Turtle()
car2.shape('square')
car2.shapesize(1, 3, 3)
ball = turtle.Turtle()
ball.shape('circle')

car1_size, car2_size, ball_size = [0, 0], [0, 0], [0, 0]
score = [0, 0]

stop_car = multiprocessing.Event()


def initialize_game():
    """Inicializa los objetos principales, orientándolos y posicionándolos"""
    car1.fillcolor('red')
    car2.fillcolor('blue')
    ball.fillcolor('green')

    car1.right(90)
    car2.left(90)
    ball.right(randint(0, 360))

    car1.up()
    car2.up()
    ball.up()

    car1.setpos(-400, 0)
    car2.setpos(400, 0)

    car1_size[0], car1_size[1] = 20, 20
    car2_size[0], car2_size[1] = 20, 20
    ball_size[0], ball_size[1] = 20, 20

    multiprocessing.Queue()
    move_car1 = multiprocessing.Process(target=move_turt_car, args=(car1, 2, stop_car,))
    move_car2 = multiprocessing.Process(target=move_turt_car, args=(car2, 2, stop_car,))
    move_ball = multiprocessing.Process(target=move_turt_ball, args=(ball, 2,))

    move_car1.start()
    move_car2.start()
    move_ball.start()


def check_canvas_ball(turtobj):
    """Comprobamos si el objeto está dentro del canvas"""
    if abs(turtobj.xcor()) >= screen.window_width() / 2 - 20:
        if turtobj.xcor() < 0:
            score[1] += 1
        if turtobj.xcor() > 0:
            score[0] += 1
        turtobj.home()
        ball.right(randint(0, 360))
        print(score)
    if abs(turtobj.ycor()) >= screen.window_height() / 2 - 20:
        turtobj.right(turtobj.heading() * 2)
        turtobj.fd(5)


def check_canvas_car(turtobj):
    """Comprobamos si el objeto está dentro del canvas"""
    if abs(turtobj.ycor()) >= screen.window_height() / 2 - 20:
        turtobj.setheading(-turtobj.heading())
        turtobj.fd(5)


def check_collision(obj1, obj2):
    """Comprobamos si los objetos han colisionado entre sí"""
    if obj1.distance(obj2) < car1_size[0]:
        print("Puuuum, y explotó")
        stop_car.set()


def move_turt_car(turtobj, step=2, stop=multiprocessing.Event()):
    """Movemos el objeto en pasos de 2"""
    while not stop.is_set():
        turtobj.forward(step)
        if abs(turtobj.ycor()) >= screen.window_height() / 2 - 20:
            step = -step
        print(turtobj.get_shapepoly())
        #check_canvas_car(turtobj)


def move_turt_ball(turtobj, step=2, stop=multiprocessing.Event()):
    """Movemos el objeto en pasos de 2"""
    while not stop.is_set():
        turtobj.forward(step)
        check_canvas_ball(turtobj)


initialize_game()

screen.exitonclick()
