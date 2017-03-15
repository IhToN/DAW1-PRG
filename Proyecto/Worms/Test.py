from time import sleep
from turtle import *


def parabolaY(x, a=-1, b=5, c=0):
    return a * x ** 2 + b * x + c


screen = Screen()
screen.setworldcoordinates(-10, -10, 310, 110)
pen = Turtle()
pen.up()

pen.down()
pen.setpos(0, -10)
pen.setheading(90)
pen.fd(110)
pen.up()
pen.setpos(-10, 0)
pen.down()
pen.setheading(0)
pen.fd(310)
pen.up()

for x in range(-10, 10):
    pen.goto(x, parabolaY(x))
    pen.down()
pen.up()

pen.goto(-10, -10)
pen.color('green')
pen.write("Listo")
screen.exitonclick()
