from turtle import Turtle, Screen
import random


class Pelota(Turtle):
    def __init__(self, partida, velocidad=3):
        Turtle.__init__(self)
        self.shape('circle')
        self.fillcolor('green')
        self.pencolor('black')
        self.up()
        self.partida = partida
        self.velocidad = velocidad
        self.moviendose = True

    def mover_pelota(self):
        if self.moviendose:
            self.forward(self.velocidad)
            self.check_canvas()
            self.check_bate()
            if self.partida.jugador1.ia:
                self.partida.jugador1.sety(self.ycor())
            if self.partida.jugador2.ia:
                self.partida.jugador2.sety(self.ycor())

    def check_canvas(self):
        """Comprobamos si el objeto está dentro del canvas"""
        partida.screen.tracer(0)
        if abs(self.xcor()) >= self.partida.screen.window_width() / 2 - 20:
            if self.xcor() < 0:
                self.partida.marcador.sumarpunto(1)
                posneg = 1
            if self.xcor() > 0:
                partida.marcador.sumarpunto(0)
                posneg = -1
            self.home()
            self.right(posneg * random.randint(155, 205))
            self.partida.screen.delay(self.partida.initial_delay)
            self.partida.marcador.refrescar()
        if abs(self.ycor()) >= self.partida.screen.window_height() / 2 - 40:
            self.right(self.heading() * 2)
            self.fd(15)
        partida.screen.tracer(1)

    def check_bate(self):
        """Comprobamos si la pelota toca algún jugador"""
        if self.xcor() < 0:  # Choque con el jugador 1
            if int(self.partida.jugador1.xcor()) - 20 <= int(self.xcor()) <= int(self.partida.jugador1.xcor()) \
                    and (int(self.partida.jugador1.ycor()) - 50 <= int(self.ycor()) - 10 and int(
                        self.ycor()) + 10 <= int(self.partida.jugador1.ycor()) + 50):
                self.partida.jugador1.setx(self.partida.jugador1.xcor() - 1)
                self.partida.jugador1.setx(self.partida.jugador1.xcor() - 3)
                self.partida.screen.tracer(0)
                if self.partida.screen.delay() > 0:
                    if self.partida.jugador1.ia:
                        self.partida.screen.delay(self.partida.screen.delay() - 1)
                    else:
                        self.partida.screen.delay(self.partida.screen.delay() - .5)
                angle = self.distance(self.partida.jugador1.xcor(), self.partida.jugador1.ycor()) + random.randint(1,
                                                                                                                   25)
                if self.ycor() <= self.partida.jugador1.ycor():
                    angle = -angle
                self.right(180 + angle)
                self.partida.screen.tracer(1)
                self.fd(15)
                self.partida.jugador1.setx(self.partida.jugador1.xcor() + 3)
                self.partida.jugador1.setx(self.partida.jugador1.xcor() + 1)
        else:  # Choque con el jugador 2
            if int(self.partida.jugador2.xcor()) - 20 <= int(self.xcor()) <= int(self.partida.jugador2.xcor()) \
                    and (int(self.partida.jugador2.ycor()) - 50 <= int(self.ycor()) - 10 and int(
                        self.ycor()) + 10 <= int(self.partida.jugador2.ycor()) + 50):
                self.partida.jugador2.setx(self.partida.jugador2.xcor() + 1)
                self.partida.jugador2.setx(self.partida.jugador2.xcor() + 3)
                self.partida.screen.tracer(0)
                if self.partida.screen.delay() > 0:
                    if self.partida.jugador2.ia:
                        self.partida.screen.delay(self.partida.screen.delay() - 1)
                    else:
                        self.partida.screen.delay(self.partida.screen.delay() - .5)
                angle = self.distance(self.partida.jugador2.xcor(), self.partida.jugador2.ycor()) + random.randint(1,
                                                                                                                   25)
                if self.ycor() <= self.partida.jugador2.ycor():
                    angle = -angle
                self.right(180 + angle)
                self.partida.screen.tracer(1)
                self.fd(15)
                self.partida.jugador2.setx(self.partida.jugador2.xcor() - 3)
                self.partida.jugador2.setx(self.partida.jugador2.xcor() - 1)


class Bate(Turtle):
    def __init__(self, partida, fillcolor='white', izquierda=True, ia=False, velocidad=2):
        Turtle.__init__(self)
        self.up()
        self.shape('square')
        self.fillcolor(fillcolor)
        self.pencolor('black')
        self.shapesize(1, 5, 2)
        self.left(90)
        if izquierda:
            self.setpos(-partida.screen.window_width() / 2 + 30, 0)
        else:
            self.setpos(partida.screen.window_width() / 2 - 30, 0)

        self.partida = partida
        self.ia = ia
        self.velocidad = velocidad
        self.moviendose = False
        self.direccion = None

    def mover(self, arriba=True):
        self.moviendose = True
        if arriba:
            self.direccion = "arriba"
        else:
            self.direccion = "abajo"

    def arriba(self):
        self.mover(True)

    def abajo(self):
        self.mover(False)

    def parar(self):
        self.moviendose = False
        self.direccion = None

    def check_canvas(self):
        partida.screen.tracer(0)
        if self.direccion:
            if self.direccion == "abajo":
                return self.ycor() <= -self.partida.screen.window_height() / 2 + (20 * (self.shapesize()[1] - 1))
            elif self.direccion == "arriba":
                return self.ycor() >= self.partida.screen.window_height() / 2 - (20 * (self.shapesize()[1] - 1))
        partida.screen.tracer(1)


class Marcador(Turtle):
    def __init__(self, partida):
        Turtle.__init__(self)
        self.hideturtle()
        self.up()
        self.color('white')
        self.partida = partida
        self.position = (0, self.partida.screen.window_height() / 2 - 160)
        self.setpos(self.position)
        self.score = [0, 0]
        self.refrescar()

    def sumarpunto(self, jugador=0):
        self.score[jugador] += 1

    def refrescar(self):
        self.clear()
        self.write(str(self.score[0]) + "          " + str(self.score[1]), align="center",
                   font=("Helvetica", 80, "normal"))


class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor('#0f0f0f')

        self.jugando = True
        self.activar_ia1, self.activar_ia2 = True, False
        self.initial_delay = 3

        self.marcador = Marcador(self)
        self.pelota = Pelota(self)

        self.pintar_campo()

        self.jugador1 = Bate(self, 'red', True, self.activar_ia1)
        self.jugador2 = Bate(self, 'blue', False, self.activar_ia2)

    def pintar_campo(self):
        self.pelota.clear()
        self.pelota.pensize(3)
        oldcolor = self.pelota.pencolor()
        self.pelota.pencolor('white')
        self.pelota.speed(0)
        self.pelota.down()
        self.pelota.setpos(0, -self.screen.window_height() // 2 + 30)
        self.pelota.setpos(0, self.screen.window_height() // 2 - 30)
        self.pelota.fd(self.screen.window_width() // 2 - 30)
        self.pelota.right(90)
        self.pelota.fd(self.screen.window_height() // 2 - 30)
        self.pelota.fd(self.screen.window_height() // 2 - 30)
        self.pelota.right(90)
        self.pelota.fd(self.screen.window_width() // 2 - 30)
        self.pelota.fd(self.screen.window_width() // 2 - 30)
        self.pelota.right(90)
        self.pelota.fd(self.screen.window_height() // 2 - 30)
        self.pelota.fd(self.screen.window_height() // 2 - 30)
        self.pelota.right(90)
        self.pelota.fd(self.screen.window_width() // 2 - 30)
        self.pelota.pencolor(oldcolor)
        self.pelota.up()
        self.pelota.home()
        posneg = random.choice([-1, 1])
        self.pelota.right(posneg * random.randint(155, 205))
        self.pelota.speed(self.pelota.velocidad)


if __name__ == "__main__":
    partida = Game()

    partida.screen.delay(partida.initial_delay)

    if not partida.jugador1.ia:
        partida.screen.onkeypress(partida.jugador1.arriba, "w")
        partida.screen.onkeyrelease(partida.jugador1.parar, "w")
        partida.screen.onkeypress(partida.jugador1.abajo, "s")
        partida.screen.onkeyrelease(partida.jugador1.parar, "s")
    if not partida.jugador2.ia:
        partida.screen.onkeypress(partida.jugador2.arriba, "Up")
        partida.screen.onkeyrelease(partida.jugador2.parar, "Up")
        partida.screen.onkeypress(partida.jugador2.abajo, "Down")
        partida.screen.onkeyrelease(partida.jugador2.parar, "Down")
    partida.screen.listen()

    while partida.jugando:
        partida.screen.tracer(1)
        partida.pelota.mover_pelota()
        if partida.jugador1.moviendose:
            if not partida.jugador1.check_canvas():
                if partida.jugador1.direccion == "arriba":
                    posneg = 1
                else:
                    posneg = -1
                partida.jugador1.fd(posneg * partida.jugador1.velocidad)
        if partida.jugador2.moviendose:
            if not partida.jugador2.check_canvas():
                if partida.jugador2.direccion == "arriba":
                    posneg = 1
                else:
                    posneg = -1
                partida.jugador2.fd(posneg * partida.jugador2.velocidad)

    partida.screen.mainloop()
