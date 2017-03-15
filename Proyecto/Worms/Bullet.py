import turtle
from math import pi, atan

x0, y0 = -180, -100  # initial location

vx, vy = 50.0, 88.0  # initial velocity in units per second

travel_time = 16  # seconds

g = 11.0  # acceleration due to gravity in units per second squared

turtellini = turtle.Turtle(shape='turtle', visible=False)

turtellini.penup()
turtellini.radians()  # to make turtle compatible with math.atan()
turtellini.setheading(pi / 2)  # straight up
turtellini.goto(x0, y0)
turtellini.pendown()
turtellini.showturtle()
turtellini.stamp()

for t in range(1, travel_time + 1):

    x = x0 + vx * t
    y = y0 + vy * t - g / 2 * t**2

    turtellini.goto(x, y)

    print(x, y)

    angle = atan((vy * t - g * t**2) / (vx * t))  # a guess!
    turtellini.setheading(angle)

    #turtellini.stamp()

turtle.exitonclick()