from enum import Enum
from turtle import Turtle, Screen
import math
import random

_MAXMOVIMIENTO = 30
_TIEMPOMISIL = 16


class Direccion(Enum):
    NINGUNO = 0
    ARRIBA = 1
    DERECHA = 2
    ABAJO = 3
    IZQUIERDA = 4


class Gusano(Turtle):
    def __init__(self, nombre):
        # Iniciar la parte de la tortuga
        Turtle.__init__(self)
        self.up()

        self.nombre = nombre
        self.vida = 100
        self.movimiento = _MAXMOVIMIENTO
        self.bazooka = Bazooka()

        self.movimiento = False
        self.apuntando = False
        self.dir_movimiento = Direccion.NINGUNO
        self.dir_apunt = Direccion.NINGUNO

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


class Bazooka(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.up()

        self.misil = Misil()
        self.velx = 0
        self.vely = 0

    def cambiar_potencia(self, velx):
        """ Cambiamos la velocidad inicial de X
        """
        self.velx += velx

    def cambiar_angulo(self, vely):
        """ Cambiamos la velocidad inicial de y
        """
        self.vely += vely


class Misil(Turtle):
    def __init__(self):
        Turtle.__init__(self, shape='misil.gif', visible=False)
        self.up()


class Partida():
    def __init__(self, num_jugadores=2):
        self.iniciar_pantalla()

        self.iniciar_jugadores(num_jugadores)
        self.jugador_actual = self.jugadores[0]

        self.iniciar_teclas()

    def iniciar_pantalla(self):
        self.pantalla = Screen()
        self.pantalla.setup(0.8, 0.8)

    def iniciar_jugadores(self, num_jugadores):
        self.jugadores = []
        for i in range(num_jugadores):
            self.jugadores.append(self.crear_gusano(i))

    def crear_gusano(self, num):
        nombre = self.pantalla.textinput("Nombre del Jugador", "¿Cómo se va a llamar el Jugador {}?".format(num + 1))
        return Gusano(nombre)

    def iniciar_teclas(self):
        # Press
        self.pantalla.onkeypress(self.jugador_actual.mover_derecha, "Right")
        self.pantalla.onkeypress(self.jugador_actual.mover_izquierda, "Left")

        # Release
        self.pantalla.onkeyrelease(self.jugador_actual.parar, "Right")
        self.pantalla.onkeyrelease(self.jugador_actual.parar, "Left")

        # Listen
        self.pantalla.listen()


if __name__ == "__main__":
    partida = Partida(1)
    pantalla = partida.pantalla
    print(partida.jugadores)
    pantalla.mainloop()
