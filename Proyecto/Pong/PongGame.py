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

enable_ia1, enable_ia2 = False, False
initial_delay = 5

screen = turtle.Screen()
turtle.bgcolor('#0f0f0f')

screen.delay(initial_delay)
car1 = turtle.Turtle()
car1.shape('square')
car1.shapesize(1, 5, 2)
car2 = turtle.Turtle()
car2.shape('square')
car2.shapesize(1, 5, 2)
ball = turtle.Turtle()
ball.shape('circle')
marker = turtle.Turtle()

score = [0, 0]

stop_ball = multiprocessing.Event()
stop_car1 = multiprocessing.Event()
stop_car2 = multiprocessing.Event()


def initialize_game():
    """Inicializa los objetos principales, orientándolos y posicionándolos"""
    draw_field()

    marker.hideturtle()

    car1.up()
    car2.up()
    ball.up()
    marker.up()

    car1.fillcolor('red')
    car2.fillcolor('blue')
    ball.fillcolor('green')
    car1.pencolor('#000000')
    car2.pencolor('#000000')
    ball.pencolor('#000000')
    marker.color('white')

    car1.left(90)
    car2.left(90)
    ball.right(random.choice([-1, 1]) * random.randint(155, 205))

    car1.setpos(-400, 0)
    car2.setpos(400, 0)
    marker.sety(screen.window_height() / 2 - 160)

    draw_marker()
    multiprocessing.Queue()
    move_ball = multiprocessing.Process(target=move_turt_ball, args=(ball, 2, stop_ball))

    move_ball.start()


def check_canvas_ball(turtobj):
    """Comprobamos si el objeto está dentro del canvas"""
    screen.tracer(0)
    if abs(turtobj.xcor()) >= screen.window_width() / 2 - 10:
        if turtobj.xcor() < 0:
            score[1] += 1
        if turtobj.xcor() > 0:
            score[0] += 1
        turtobj.home()
        screen.delay(initial_delay)
        ball.right(random.choice([-1, 1]) * random.randint(155, 205))
        draw_marker()
        print(score)
    if abs(turtobj.ycor()) >= screen.window_height() / 2 - 30:
        turtobj.right(turtobj.heading() * 2)
        turtobj.fd(15)
    screen.tracer(1)


def check_canvas_car(turtobj, down=True):
    """Comprobamos si el objeto está dentro del canvas"""
    screen.tracer(0)
    if down:
        return turtobj.ycor() <= -screen.window_height() / 2 + 90
    else:
        return turtobj.ycor() >= screen.window_height() / 2 - 90
    screen.tracer(1)


def bounce_car1():
    """Comprobamos si la pelota toca el coche 1"""
    if car1.xcor() <= ball.xcor() <= car1.xcor() + 20 and car1.ycor() - 90 <= ball.ycor() <= car1.ycor() + 10:
        car1.setx(car1.xcor() - 5)
        screen.tracer(0)
        if screen.delay() > 0:
            if enable_ia1:
                screen.delay(screen.delay() - 1)
            else:
                screen.delay(screen.delay() - .5)
        screen.tracer(1)
        angle = 45
        if ball.ycor() <= car1.ycor() - 30:
            angle = -angle
        ball.right(180 + angle)
        ball.fd(15)
        car1.setx(car1.xcor() + 5)


def bounce_car2():
    """Comprobamos si la pelota toca el coche 2"""
    if car2.xcor() - 20 <= ball.xcor() <= car2.xcor() and car2.ycor() - 90 <= ball.ycor() <= car2.ycor() + 10:
        car2.setx(car2.xcor() + 5)
        screen.tracer(0)
        if screen.delay() > 0:
            if enable_ia2:
                screen.delay(screen.delay() - 1)
            else:
                screen.delay(screen.delay() - .5)
        screen.tracer(1)
        angle = 45
        if ball.ycor() <= car1.ycor() - 30:
            angle = -angle
        ball.right(180 + angle)
        ball.fd(15)
        car2.setx(car2.xcor() - 5)


def move_turt_ball(turtobj, step=2, stop=multiprocessing.Event()):
    """Movemos el objeto en pasos de 2"""
    while not stop.is_set():
        bounce_car1()
        bounce_car2()
        turtobj.forward(step)
        check_canvas_ball(turtobj)
        if enable_ia1:
            move_car_ia(car1)
        if enable_ia2:
            move_car_ia(car2)


def draw_field():
    ball.clear()
    ball.pensize(3)
    ball.pencolor('white')
    ball.speed(0)
    ball.down()
    ball.setpos(0, -screen.window_height() // 2 + 30)
    ball.setpos(0, screen.window_height() // 2 - 30)
    ball.fd(screen.window_width() // 2 - 30)
    ball.right(90)
    ball.fd(screen.window_height() // 2 - 30)
    ball.fd(screen.window_height() // 2 - 30)
    ball.right(90)
    ball.fd(screen.window_width() // 2 - 30)
    ball.fd(screen.window_width() // 2 - 30)
    ball.right(90)
    ball.fd(screen.window_height() // 2 - 30)
    ball.fd(screen.window_height() // 2 - 30)
    ball.right(90)
    ball.fd(screen.window_width() // 2 - 30)
    ball.up()
    ball.home()
    ball.speed(3)


def draw_marker():
    marker.clear()
    marker.write(str(score[0]) + "          " + str(score[1]), align="center", font=("Helvetica", 80, "normal"))


def erasableWrite(turtobj, name, font, align, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(turtobj.position())
    eraser.write(name, font=font, align=align)
    return eraser


def move_car(car, fd, event):
    while not event.is_set() and not check_canvas_car(car, fd < 0):
        car.fd(fd)


def move_car_ia(car):
    car.setpos(car.xcor(), ball.ycor())


def move_car1_up():
    stop_car1.clear()
    proc = multiprocessing.Process(target=move_car, args=(car1, 2, stop_car1))
    proc.start()


def move_car1_down():
    stop_car1.clear()
    proc = multiprocessing.Process(target=move_car, args=(car1, -2, stop_car1))
    proc.start()


def move_car2_up():
    stop_car2.clear()
    proc = multiprocessing.Process(target=move_car, args=(car2, 2, stop_car2))
    proc.start()


def move_car2_down():
    stop_car2.clear()
    proc = multiprocessing.Process(target=move_car, args=(car2, -2, stop_car2))
    proc.start()


def stopev_car1():
    stop_car1.set()


def stopev_car2():
    stop_car2.set()


def main():
    initialize_game()

    if not enable_ia1:
        screen.onkeypress(move_car1_up, "w")
        screen.onkeyrelease(stopev_car1, "w")
        screen.onkeypress(move_car1_down, "s")
        screen.onkeyrelease(stopev_car1, "s")
    if not enable_ia2:
        screen.onkeypress(move_car2_up, "Up")
        screen.onkeyrelease(stopev_car2, "Up")
        screen.onkeypress(move_car2_down, "Down")
        screen.onkeyrelease(stopev_car2, "Down")
    screen.listen()


main()

turtle.done()
