"""
    Hacer un jueguecillo de un coche.
    a. Buscar en la documentación una forma de ver el tamaño del canvas.
    b. Comprobar una colisión entre dos coches, en caso de colisión cambiarles el color.
    c. Colocar una pelota que rebote, añadiendo un ángulo de corrección. Se colocarán dos porterías y
        cuando la pelota entra por alguno de ellos se aumenta el valor de un contador.
"""
import threading
import turtle

screen = turtle.Screen()
car1 = turtle.Turtle()
car1.shape('square')
car2 = turtle.Turtle()
car2.shape('square')
ball = turtle.Turtle()
ball.shape('circle')

stop_car = threading.Event()


def initialize_game():
    """Inicializa los objetos principales, orientándolos y posicionándolos"""
    car1.fillcolor('red')
    car2.fillcolor('blue')
    ball.fillcolor('green')

    car1.setheading(0)
    car2.setheading(180)
    ball.setheading(90)

    car1.up()
    car2.up()
    ball.up()

    car1.setpos(-400, 0)
    car2.setpos(400, 0)

    move_car1 = threading.Thread(target=move_object, args=[car1, 0, stop_car])
    move_car2 = threading.Thread(target=move_object, args=[car2, 0, stop_car])
    move_ball = threading.Thread(target=move_object, args=[ball, -10])

    move_car1.start()
    move_car2.start()
    move_ball.start()


def move_object(object, initial_angle=0, stop=threading.Event()):
    """Movemos el objeto en pasos de 5"""
    if initial_angle:
        object.right(initial_angle)
    while not stop.is_set():
        object.forward(5)
        if not check_canvas(object):
            object.right(180 + initial_angle)
        if object == car1 or object == car2:
            check_collision(car1, car2)


def check_canvas(object):
    """Comprobamos si el objeto está dentro del canvas"""
    width = screen.window_width() // 2 - (object.turtlesize()[0] * 2)
    height = screen.window_height() // 2 - (object.turtlesize()[1] * 2)
    xcor = object.xcor()
    ycor = object.ycor()
    return not (width < xcor or -width > xcor or height < ycor or -height > ycor)


def check_collision(obj1, obj2):
    """Comprobamos si los objetos han colisionado entre sí"""
    if obj1.distance(obj2.pos()) < 30:
        print("Puuuum, y explotó")
        stop_car.set()


initialize_game()

screen.exitonclick()
