from enum import Enum
from turtle import Turtle, Screen, Vec2D
import glob
import os
import math
import random

_RESFOLDERS = 'Resources'

_MAXMOVIMIENTO = 15
_TIEMPOMISIL = 5000
_GRAVEDAD = 9.8

_SCREENCOORDS = -10, -10, 3100, 1100


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

        self.moviendose = False
        self.apuntando = False
        self.dir_movimiento = Direccion.NINGUNO
        self.dir_apunt = Direccion.NINGUNO
        self.pot_disparo = 0

    def __str__(self):
        return "Gusano({})".format(self.nombre)

    def __repr__(self):
        return "Gusano({})".format(self.nombre)

    def mover_derecha(self):
        self.dir_movimiento = Direccion.DERECHA
        self.animar_andar()

    def mover_izquierda(self):
        self.dir_movimiento = Direccion.IZQUIERDA
        self.animar_andar()

    def animar_andar(self):
        if self.movimiento <= 0 or self.moviendose or self.bazooka.misil.moviendose:
            self.parar()
            return

        self.moviendose = True
        self.movimiento -= 1

        if self.dir_movimiento == Direccion.IZQUIERDA:
            anim = 'walk_left_'
            vel = -1
        else:
            anim = 'walk_right_'
            vel = 1

        for i in range(1, 16):
            self.fd(vel)
            self.bazooka.setx(self.bazooka.xcor() + vel)
            self.shape(Partida.shapes[anim + str(i) + '.gif'])

    def apuntar(self, dir_apunt):
        self.apuntando = True
        self.dir_apunt = dir_apunt

    def apuntar_arriba(self):
        self.apuntar(Direccion.ARRIBA)
        self.bazooka.cambiar_angulo(0.1)

    def apuntar_abajo(self):
        self.apuntar(Direccion.ABAJO)
        self.bazooka.cambiar_angulo(-0.1)

    def parar(self):
        self.moviendose = False
        self.apuntando = False
        self.dir_movimiento = Direccion.NINGUNO
        self.dir_apunt = Direccion.NINGUNO

    def disparar(self):
        self.bazooka.lanzar_misil()


class Bazooka(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.up()
        self.radians()

        self.setheading(math.pi / 2)
        print(self.heading())

        self.misil = Misil()
        self.potencia = 100

    def cambiar_potencia(self, velx):
        """ Cambiamos la velocidad inicial de X
        """
        self.velx += velx

    def cambiar_angulo(self, angulo):
        """ Cambiamos la velocidad inicial de y
        """
        if math.pi / 2 - angulo < self.heading() < math.pi - angulo:
            self.left(angulo)

    def lanzar_misil(self):
        self.misil.lanzar((self.xcor(), self.ycor(), self.heading() - (math.pi / 2), self.potencia))


class Misil(Turtle):
    def __init__(self):
        Turtle.__init__(self, shape=Partida.shapes['missile_0.gif'], visible=False)
        # Turtle.__init__(self, shape='circle', visible=False)
        self.up()
        self.radians()
        self.moviendose = False

    def iniciar_lanzamiento(self, posicion):
        self.moviendose = True
        self.x0, self.y0, self.angulo0, self.potencia = posicion

        speed = self.speed()
        self.speed(0)
        self.goto(self.x0, self.y0)
        self.speed(speed)

    def calc_velocidades(self, potencia):
        vel_inicial = potencia
        vx = vel_inicial * math.cos(self.angulo0)
        vy = vel_inicial * math.sin(self.angulo0)
        return vx, vy

    def mover_parabola(self, posx):
        tracerspeed = Partida.pantalla.tracer()
        Partida.pantalla.tracer(0)
        self.showturtle()
        self.down()

        posy = Utilidades.tiro_parabolico(self.x0, self.y0, posx, self.angulo0, self.potencia)
        print("X e Y: {} {}".format(posx, posy))

        self.setheading(self.towards(posx, posy) - math.pi / 2)
        new_shape = 'missile_{}.gif'.format(int(Utilidades.rad_a_deg(self.heading())))
        self.shape(Partida.shapes[new_shape])
        Partida.pantalla.tracer(tracerspeed)
        self.goto(posx, posy)

    def lanzar(self, posicion):
        if not self.moviendose:
            self.iniciar_lanzamiento(posicion)

            for posx in range(int(self.x0), int(self.x0) + _TIEMPOMISIL + 1, 10):
                self.mover_parabola(posx)

                if self.ycor() < 0:
                    self.limpiar()
                    return
                    # self.stamp()
                    # if self.comprobar_colision():
                    #    self.colision()
                    #    return
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
        Utilidades.setworldcoordinates(Partida.pantalla, *_SCREENCOORDS)
        self.up()
        self.hideturtle()
        self.home()
        self.clear()
        self.shape(Partida.shapes['missile_0.gif'])

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
        weapon_images = os.path.join(_RESFOLDERS, 'Weapons', '*', '*.gif')
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


class Utilidades:
    # Utilidades de Turtle
    @staticmethod
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

    @staticmethod
    def followobject(screen, turtobj):
        slx, sly, srx, sry = _SCREENCOORDS

        llx = (-screen.window_width() / 4) + turtobj.xcor()
        lly = (-screen.window_height() / 4) + turtobj.ycor()
        urx = (screen.window_width() / 4) + turtobj.xcor()
        ury = (+screen.window_height() / 4) + turtobj.ycor()

        Utilidades.setworldcoordinates(Partida.pantalla, llx, lly, urx, ury)

    # Utilidades Matemáticas
    @staticmethod
    def rad_a_deg(angle_rads):
        return (math.degrees(angle_rads) + 360) % 360

    @staticmethod
    def tiro_parabolico(x0, y0, posx, angulo, potencia):
        vel_inicial = potencia
        vx = vel_inicial * math.cos(angulo)
        vy = vel_inicial * math.sin(angulo)
        posy = y0 + vy * ((posx - x0) / vx) - 1 / 2 * _GRAVEDAD * ((posx - x0) / vx) ** 2
        """posy = y0 + posx * math.tan(angulo) - (_GRAVEDAD * (posx + x0) ** 2) / \
                                              (2 * vel_inicial ** 2 * math.cos(angulo) ** 2)"""
        return posy

    @staticmethod
    def tiro_parabolico_tiempo(x0, y0, vx, vy, t):
        posx = x0 + vx * t
        posy = y0 + vy * t - _GRAVEDAD * t ** 2 / 2
        return posx, posy


if __name__ == "__main__":
    partida = Partida(1)
    print(partida.jugadores)
    Partida.pantalla.mainloop()
