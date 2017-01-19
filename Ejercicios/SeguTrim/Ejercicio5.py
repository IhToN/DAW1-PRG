"""
    Hacer un jueguecillo de un coche.
    a. Buscar en la documentación una forma de ver el tamaño del canvas.
    b. Comprobar una colisión entre dos coches, en caso de colisión cambiarles el color.
    c. Colocar una pelota que rebote, añadiendo un ángulo de corrección. Se colocarán dos porterías y
        cuando la pelota entra por alguno de ellos se aumenta el valor de un contador.
"""
import multiprocessing.dummy as multiprocessing
import turtle
import random

screen = turtle.Screen()

car1 = turtle.Turtle()
car1.shape('square')
car1.shapesize(1, 5, 2)
car2 = turtle.Turtle()
car2.shape('square')
car2.shapesize(1, 5, 2)
ball = turtle.Turtle()
ball.shape('circle')

score = [0, 0]

stop_ball = multiprocessing.Event()


def initialize_game():
    """Inicializa los objetos principales, orientándolos y posicionándolos"""
    car1.fillcolor('red')
    car2.fillcolor('blue')
    ball.fillcolor('green')

    car1.right(90)
    car2.left(90)
    ball.right(random.choice([-1, 1]) * random.randint(25, 155))

    car1.up()
    car2.up()
    ball.up()

    car1.setpos(-400, 0)
    car2.setpos(400, 0)

    multiprocessing.Queue()
    move_ball = multiprocessing.Process(target=move_turt_ball, args=(ball, 2, stop_ball))

    move_ball.start()


def check_canvas_ball(turtobj):
    """Comprobamos si el objeto está dentro del canvas"""
    if abs(turtobj.xcor()) >= screen.window_width() / 2 - 20:
        if turtobj.xcor() < 0:
            score[1] += 1
        if turtobj.xcor() > 0:
            score[0] += 1
        turtobj.home()
        ball.right(random.choice([-1, 1]) * random.randint(25, 155))
        print(score)
    if abs(turtobj.ycor()) >= screen.window_height() / 2 - 20:
        turtobj.right(turtobj.heading() * 2)
        turtobj.fd(5)


def check_canvas_car(turtobj, down=True):
    """Comprobamos si el objeto está dentro del canvas"""
    if down:
        return turtobj.ycor() <= -screen.window_height() / 2 + 20
    else:
        return turtobj.ycor() >= screen.window_height() / 2 - 20


def check_collision(obj1, obj2):
    """Comprobamos si los objetos han colisionado entre sí"""
    if obj1.distance(obj2) < 20:
        print("Puuuum, y explotó")
        stop_ball.set()


def move_turt_ball(turtobj, step=2, stop=multiprocessing.Event()):
    """Movemos el objeto en pasos de 2"""
    while not stop.is_set():
        turtobj.forward(step)
        check_canvas_ball(turtobj)


def erasableWrite(turtobj, name, font, align, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(turtobj.position())
    eraser.write(name, font=font, align=align)
    return eraser


def move_car1_up():
    turtle.tracer(0)
    if not check_canvas_car(car1, False):
        car1.fd(-15)
    turtle.tracer(1)


def move_car1_down():
    turtle.tracer(0)
    if not check_canvas_car(car1):
        car1.fd(15)
    turtle.tracer(1)


def move_car2_up():
    turtle.tracer(0)
    if not check_canvas_car(car2, False):
        car2.fd(15)
    turtle.tracer(1)


def move_car2_down():
    turtle.tracer(0)
    if not check_canvas_car(car2):
        car2.fd(-15)
    turtle.tracer(1)


def main():
    initialize_game()

    screen.onkey(move_car1_up, "w")
    screen.onkey(move_car1_down, "s")
    screen.onkey(move_car2_up, "Up")
    screen.onkey(move_car2_down, "Down")
    screen.listen()


main()

turtle.done()
