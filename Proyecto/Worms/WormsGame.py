from enum import Enum
from turtle import Turtle, Screen, Vec2D
import glob
import os
import math
import random

_RESFOLDERS = 'Resources'

_MAXMOVIMIENTO = 30
_TIEMPOMISIL = 18
_GRAVEDAD = 11.0

_SCREENCOORDS = -10, -10, 2110, 910


class Direccion(Enum):
    NINGUNO = 0
    ARRIBA = 1
    DERECHA = 2
    ABAJO = 3
    IZQUIERDA = 4


class Gusano(Turtle):
    def __init__(self, nombre):
        # Iniciar la parte de la tortuga
        Turtle.__init__(self, shape=Partida.shapes['walk_left_1.gif'])
        self.up()

        self.nombre = nombre
        self.vida = 100
        self.movimiento = _MAXMOVIMIENTO
        self.bazooka = Bazooka()

        self.movimiento = False
        self.apuntando = False
        self.dir_movimiento = Direccion.NINGUNO
        self.dir_apunt = Direccion.NINGUNO
        self.pot_disparo = 0

    def __str__(self):
        return "Gusano({})".format(self.nombre)

    def __repr__(self):
        return "Gusano({})".format(self.nombre)

    def mover(self):
        if self.movimiento:
            self.movimiento = True
            self.fd(1)
            self.movimiento -= 1
        elif self.movimiento:
            self.parar()

    def mover_derecha(self):
        self.setheading(0)
        self.dir_movimiento = Direccion.DERECHA

    def mover_izquierda(self):
        self.setheading(180)
        self.dir_movimiento = Direccion.IZQUIERDA

    def apuntar(self, dir_apunt):
        self.apuntando = True
        self.dir_apunt = dir_apunt

    def apuntar_arriba(self):
        self.apuntar(Direccion.ARRIBA)

    def apuntar_abajo(self):
        self.apuntar(Direccion.ABAJO)

    def parar(self):
        self.movimiento = False
        self.apuntando = False
        self.dir_movimiento = Direccion.NINGUNO
        self.dir_apunt = Direccion.NINGUNO

    def disparar(self):
        self.bazooka.lanzar_misil()


class Bazooka(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.up()

        self.misil = Misil()
        self.velx = 55.0
        self.vely = 32.0

    def cambiar_potencia(self, velx):
        """ Cambiamos la velocidad inicial de X
        """
        self.velx += velx

    def cambiar_angulo(self, vely):
        """ Cambiamos la velocidad inicial de y
        """
        self.vely += vely

    def lanzar_misil(self):
        self.misil.lanzar((self.xcor(), self.ycor()), (self.velx, self.vely))


class Misil(Turtle):
    def __init__(self):
        # Turtle.__init__(self, shape=Partida.shapes['missile.gif'], visible=False)
        Turtle.__init__(self, shape='circle', visible=False)
        self.up()
        self.radians()
        self.moviendose = False

    def lanzar(self, posicion, velocidad):
        if not self.moviendose:
            self.moviendose = True
            x, y = posicion
            vx, vy = velocidad
            speed = self.speed()
            self.speed(0)
            self.goto(x, y)

            self.showturtle()
            self.speed(speed)
            for t in range(1, _TIEMPOMISIL + 1):
                x = x + vx * t
                y = y + vy * t - _GRAVEDAD / 2 * t ** 2

                self.goto(x, y)
                print(x, y)
                angle = math.atan((vy * t - _GRAVEDAD * t ** 2) / (vx * t))
                self.setheading(angle)
                self.stamp()
                if self.comprobar_colision():
                    self.colision()
                    return

            self.limpiar()

    def colision(self):
        print("Ha chocao con un borde")
        self.limpiar()

    def comprobar_colision(self):
        """Comprobamos si el objeto está dentro del canvas
        """
        if abs(self.xcor()) >= Partida.pantalla.window_width() / 2 - 20 \
                or abs(self.ycor()) >= Partida.pantalla.window_height() / 2 - 20:
            return True
        return False

    def limpiar(self):
        setworldcoordinates(Partida.pantalla, *_SCREENCOORDS)
        self.hideturtle()
        self.clear()
        self.moviendose = False


class Partida:
    pantalla = Screen()
    shapes = {}

    def __init__(self, num_jugadores=2):
        self.iniciar_pantalla()
        self.iniciar_sprites()

        self.iniciar_jugadores(num_jugadores)
        self.jugador_actual = self.jugadores[0]

        self.iniciar_teclas()

    def iniciar_pantalla(self):
        Partida.pantalla.setup(0.8, 0.8)
        Partida.pantalla.setworldcoordinates(*_SCREENCOORDS)

    def iniciar_jugadores(self, num_jugadores):
        self.jugadores = []
        for i in range(num_jugadores):
            self.jugadores.append(self.crear_gusano(i))

    def crear_gusano(self, num):
        nombre = self.pantalla.textinput("Nombre del Jugador", "¿Cómo se va a llamar el Jugador {}?".format(num + 1))
        return Gusano(nombre)

    def iniciar_sprites(self):
        # Walk Animation
        walk_images = os.path.join(_RESFOLDERS, 'Walk', '*.gif')
        walk_list = glob.glob(walk_images)
        for sprite_path in walk_list:
            self.guardar_sprite(sprite_path)

        # Weapons
        weapon_images = os.path.join(_RESFOLDERS, 'Weapons', '*.gif')
        weapon_list = glob.glob(weapon_images)
        for sprite_path in weapon_list:
            self.guardar_sprite(sprite_path)

    def guardar_sprite(self, path):
        nombre_sprite = path.split('\\')[-1]
        self.pantalla.register_shape(path)
        Partida.shapes[nombre_sprite] = path

    def iniciar_teclas(self):
        # Press
        self.pantalla.onkeypress(self.jugador_actual.mover_derecha, "Right")
        self.pantalla.onkeypress(self.jugador_actual.mover_izquierda, "Left")
        self.pantalla.onkeypress(self.jugador_actual.apuntar_arriba, "Up")
        self.pantalla.onkeypress(self.jugador_actual.apuntar_abajo, "Down")
        self.pantalla.onkeypress(self.jugador_actual.disparar, 'space')

        # Release
        self.pantalla.onkeyrelease(self.jugador_actual.parar, "Right")
        self.pantalla.onkeyrelease(self.jugador_actual.parar, "Left")
        self.pantalla.onkeyrelease(self.jugador_actual.parar, "Up")
        self.pantalla.onkeyrelease(self.jugador_actual.parar, "Down")

        # Listen
        self.pantalla.listen()


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


def followobject(screen, turtobj):
    slx, sly, srx, sry = _SCREENCOORDS

    llx = (-screen.window_width() / 4) + turtobj.xcor()
    lly = (-screen.window_height() / 4) + turtobj.ycor()
    urx = (screen.window_width() / 4) + turtobj.xcor()
    ury = (+screen.window_height() / 4) + turtobj.ycor()

    setworldcoordinates(Partida.pantalla, llx, lly, urx, ury)


if __name__ == "__main__":
    partida = Partida(1)
    print(partida.jugadores)
    Partida.pantalla.mainloop()
