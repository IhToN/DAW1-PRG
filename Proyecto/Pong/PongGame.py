from turtle import Turtle, Screen
import random
import pyglet
import os

import time


class Pelota(Turtle):
    """ Clase Pelota
            Atributos:
                partida - Clase Partida
                velocidad - Float
            Metodos:
                mover_pelota()
                comprobar_canvas()
                comprobar_bate()
    """

    def __init__(self, partida, velocidad=3):
        Turtle.__init__(self)

        self.shape('circle')
        self.fillcolor('green')
        self.pencolor('black')
        self.shapesize(2, 2, 2)
        # self.shape(partida.images['ball'])
        self.up()
        self.partida = partida
        self.velocidad_inicial = velocidad
        self.velocidad = velocidad
        self.moviendose = True

        self.rebote = False

    def mover_pelota(self):
        """ Si la pelota está en 'movimiento' la movemos en pantalla y comprobamos
        si no se ha salido del área o rebota en algún bate
        """
        if self.moviendose:
            self.forward(5 * self.velocidad / 2)
            self.check_bate()
            self.check_canvas()
            if self.partida.jugador1.ia:
                self.partida.jugador1.sety(self.ycor())
            if self.partida.jugador2.ia:
                self.partida.jugador2.sety(self.ycor())
            self.rebote = False

    def check_canvas(self):
        """Comprobamos si el objeto está dentro del canvas
        """
        self.partida.screen.tracer(0)
        if abs(self.xcor()) >= self.partida.screen.window_width() / 2 - 20:
            if self.xcor() < 0:
                self.partida.marcador.sumar_punto(1)
                posneg = -1
            if self.xcor() > 0:
                partida.marcador.sumar_punto(0)
                posneg = 1
            self.home()
            self.setheading(90)
            self.right(posneg * random.randint(45, 75))
            self.velocidad = self.velocidad_inicial
            song = pyglet.media.load(partida.songs['inicioronda'])
            song.play()
        if abs(self.ycor()) >= self.partida.screen.window_height() / 2 - 40 and not self.rebote:
            self.rebote = True
            song = pyglet.media.load(partida.songs['rebote'])
            song.play()
            self.right(self.heading() * 2)
            self.fd(5 * self.velocidad / 2)
            self.rebote = False
        self.partida.screen.tracer(1)

    def check_bate(self):
        """ Comprobamos si la pelota toca algún jugador
        """
        if self.xcor() < 0 and not self.rebote:  # Choque con el jugador 1
            if int(self.xcor()) <= int(self.partida.jugador1.xcor()) + 32 \
                    and (int(self.partida.jugador1.ycor()) - 140 <= int(self.ycor()) - 10 and int(
                        self.ycor()) + 10 <= int(self.partida.jugador1.ycor()) + 140):
                self.partida.jugador1.shape(self.partida.images['redhover'])
                self.partida.screen.tracer(0)
                self.rebote = True
                if 0 < self.velocidad < 15:
                    if self.partida.jugador1.ia:
                        self.velocidad += 2
                    else:
                        self.velocidad += 1
                    self.speed(self.speed() + 1)

                angle = self.distance(self.partida.jugador1.xcor(),
                                      self.partida.jugador1.ycor()) + random.randint(1, 25)
                if self.ycor() >= self.partida.jugador1.ycor():
                    angle = -angle
                self.setheading(-angle)

                song = pyglet.media.load(partida.songs['rebotebate'])
                song.play()
                self.fd(25)
                self.partida.screen.tracer(15)
                self.partida.jugador1.shape(self.partida.images['red'])
        elif self.xcor() > 0 and not self.rebote:  # Choque con el jugador 2
            if int(self.partida.jugador2.xcor()) - 32 <= int(self.xcor()) \
                    and (int(self.partida.jugador2.ycor()) - 140 <= int(self.ycor()) - 10 and int(
                        self.ycor()) + 10 <= int(self.partida.jugador2.ycor()) + 140):
                self.partida.jugador2.shape(self.partida.images['bluehover'])
                self.partida.screen.tracer(0)
                self.rebote = True
                if 0 < self.velocidad < 15:
                    if self.partida.jugador1.ia:
                        self.velocidad += 2
                    else:
                        self.velocidad += 1
                    self.speed(self.speed() + 1)

                angle = self.distance(self.partida.jugador2.xcor(),
                                      self.partida.jugador2.ycor()) + random.randint(1, 25)
                if self.ycor() <= self.partida.jugador2.ycor():
                    angle = -angle
                self.setheading(180 - angle)

                song = pyglet.media.load(partida.songs['rebotebate'])
                song.play()
                self.fd(25)
                self.partida.screen.tracer(15)
                self.partida.jugador2.shape(self.partida.images['blue'])


class Bate(Turtle):
    """ Clase Pelota
            Atributos:
                partida - Clase Partida
                minimalista - Boolean
                fillcolor - String
                izquierda - Boolean
                IA - Boolean
                velocidad - Float
            Metodos:
                mover(arriba)
                arriba()
                abajo()
                parar()
                comprobar_canvas()
    """

    def __init__(self, partida, minimalista=False, fillcolor='white', izquierda=True, ia=False, velocidad=4):
        Turtle.__init__(self)
        self.up()
        if minimalista:
            self.shape('square')
            self.shapesize(2, 5, 2)
            self.fillcolor(fillcolor)
            self.pencolor('black')
        else:
            if izquierda:
                self.shape(partida.images['red'])
                self.setpos(-partida.screen.window_width() / 2 + 32, 0)
            else:
                self.shape(partida.images['blue'])
                self.setpos(partida.screen.window_width() / 2 - 32, 0)

        self.left(90)

        self.partida = partida
        self.ia = ia
        self.velocidad = velocidad
        self.moviendose = False
        self.direccion = None

    def mover(self, arriba=True):
        """ Activamos el movimineto del bate bien hacia arriba o hacia abajo
        """
        self.moviendose = True
        if arriba:
            self.direccion = "arriba"
        else:
            self.direccion = "abajo"

    def arriba(self):
        """ Activamos el movimiento del bate hacia arriba
        """
        self.mover(True)

    def abajo(self):
        """ Activamos el movimiento del bate hacia abajo
        """
        self.mover(False)

    def parar(self):
        """ Paramos el movimiento del bate
        """
        self.moviendose = False
        self.direccion = None

    def check_canvas(self):
        """ Comprobamos que el bate no se sale de la pantalla
        """
        partida.screen.tracer(0)
        if self.direccion:
            if self.direccion == "abajo":
                return self.ycor() <= -self.partida.screen.window_height() / 2 + 140
            elif self.direccion == "arriba":
                return self.ycor() >= self.partida.screen.window_height() / 2 - 140
        partida.screen.tracer(1)


class Marcador(Turtle):
    """ Clase Pelota
            Atributos:
                partida - Clase Partida
                puntuacion - Lista de Enteros
            Metodos:
                comprobar_ganador()
                sumar_punto()
                refrescar()
    """

    def __init__(self, partida):
        Turtle.__init__(self)
        self.hideturtle()
        self.up()
        self.color('white')
        self.partida = partida
        self.posicion = (0, self.partida.screen.window_height() / 2 - 160)
        self.setpos(self.posicion)
        self.puntuacion = [0, 0]
        self.refrescar()

    def __str__(self):
        return str(self.puntuacion[0]) + " | " + str(self.puntuacion[1])

    def comprobar_ganador(self):
        """ Comprobamos si existe un ganador, siendo este aquel que tenga mayor puntuación
        con una diferencia de dos y a un mínimo de 5 puntos
        """
        dif = abs(self.puntuacion[0] - self.puntuacion[1])
        ganador = None
        if self.puntuacion[0] >= 5 and self.puntuacion[0] > self.puntuacion[1] and dif >= 2:
            ganador = "Jugador 1"
        if self.puntuacion[1] >= 5 and self.puntuacion[1] > self.puntuacion[0] and dif >= 2:
            ganador = "Jugador 2"
        if ganador:
            self.partida.acabar_partida(ganador)

    def sumar_punto(self, jugador=0):
        """ Sumamos un punto al marcador del jugador
        """
        self.puntuacion[jugador] += 1
        self.partida.marcador.refrescar()
        self.comprobar_ganador()

    def refrescar(self):
        """ Actualizamos el marcador en pantalla
        """
        self.clear()
        # print(str(self).replace('|', "        "))
        self.write(str(self).replace('|', "        "), align="center",
                   font=("Helvetica", 80, "normal"))


class Partida:
    def __init__(self):
        self.screen = Screen()
        self.screen.screensize()
        self.screen.setup(width=0.8, height=0.8)
        self.screen.bgcolor('#0f0f0f')

        self.jugando = True
        self.activar_ia1, self.activar_ia2 = False, True

        self.images = dict()
        self.images['ball'] = os.path.join('Resources', 'ball.gif')
        self.images['red'] = os.path.join('Resources', 'red.gif')
        self.images['redhover'] = os.path.join('Resources', 'redhover.gif')
        self.images['blue'] = os.path.join('Resources', 'blue.gif')
        self.images['bluehover'] = os.path.join('Resources', 'bluehover.gif')
        self.registrar_shapes()

        self.songs = dict()
        self.songs['musica'] = os.path.join('Resources', 'bgmusic.wav')
        self.songs['rebote'] = os.path.join('Resources', 'boing.wav')
        self.songs['rebotebate'] = os.path.join('Resources', 'boing.wav')
        self.songs['inicioronda'] = os.path.join('Resources', 'startround.wav')

        self.marcador = Marcador(self)
        self.pelota = Pelota(self)

        self.pintar_campo()

        # def __init__(self, partida, minimalista=False, fillcolor='white', izquierda=True, ia=False, velocidad=4):
        self.jugador1 = Bate(self, False, 'red', True, self.activar_ia1)
        self.jugador2 = Bate(self, False, 'blue', False, self.activar_ia2)

    def registrar_shapes(self):
        for image in self.images.values():
            self.screen.register_shape(image)

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
        self.pelota.setheading(90)
        self.pelota.right(random.choice([-1, 1]) * random.randint(45, 75))
        self.pelota.speed(0)

    def acabar_partida(self, ganador):
        output = '/=================================\\' + "\n" + \
                 '|    Ganador: {}'.format(ganador) + "\n" + \
                 '|    Resultado: {}'.format(str(self.marcador)) + "\n" + \
                 '\\=================================/' + "\n"
        fichero = open('historial.txt', 'a', encoding="utf-8")
        fichero.write(output)
        fichero.close()
        print(output)
        self.jugando = False


def followobject(screen, turtobj):
    llx = (-screen.window_width() / 2) + turtobj.xcor()
    lly = (-screen.window_height() / 2) + turtobj.ycor()
    urx = (screen.window_width() / 2) + turtobj.xcor()
    ury = (+screen.window_height() / 2) + turtobj.ycor()

    setworldcoordinates(partida.screen, llx, lly, urx, ury)


def setworldcoordinates(screen, llx, lly, urx, ury):
    """Set up a user defined coordinate-system.

    Arguments:
    llx -- coordenada X de la esquina inferior izquierda
    lly -- coordenada Y de la esquina inferior izquierda
    urx -- coordenada X de la esquina superior derecha
    ury -- coordenada Y de la esquina superior derecha
    """
    xspan = float(urx - llx)
    yspan = float(ury - lly)
    wx, wy = screen._window_size()
    screen.screensize(wx - 20, wy - 20)
    oldxscale, oldyscale = screen.xscale, screen.yscale
    screen.xscale = screen.canvwidth / xspan
    screen.yscale = screen.canvheight / yspan
    srx1 = llx * screen.xscale
    sry1 = -ury * screen.yscale
    srx2 = screen.canvwidth + srx1
    sry2 = screen.canvheight + sry1
    screen._setscrollregion(srx1, sry1, srx2, sry2)
    screen._rescale(screen.xscale / oldxscale, screen.yscale / oldyscale)
    screen.update()


if __name__ == "__main__":
    partida = Partida()

    song = pyglet.media.load(partida.songs['musica'])
    looper = pyglet.media.SourceGroup(song.audio_format, None)
    looper.loop = True
    looper.queue(song)
    p = pyglet.media.Player()
    p.queue(looper)
    p.play()

    # pyglet.app.run()

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

        # followobject(partida.screen, partida.pelota)

        # canvas.place(height=partida.screen.window_height(), width=partida.screen.window_width(), x=150, y=0)

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

    partida.screen.bye()
    p.delete()
    time.sleep(5)
