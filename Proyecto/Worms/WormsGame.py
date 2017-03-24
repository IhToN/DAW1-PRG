from enum import Enum
from turtle import Turtle, Screen
import glob
import os
import sys
import math
import random

import Proyecto.Worms.Utilidades as Utilidades
import Proyecto.Worms.Excepciones as Excepciones

_ARCHIVO_RANKING = 'ranking.txt'
_RESFOLDERS = 'Resources'
_FUENTE = ("Helvetica", 10, "bold")
_TUMBAS = 0, 10

_MAXMOVIMIENTO = 1500
_TIEMPOMISIL = 5000
_GRAVEDAD = 9.8

_SCREENCOORDS = -10, -10, 3100, 1100
_JUGADORES = 2
if len(sys.argv) == 2:
    _JUGADORES = int(sys.argv[1])

_ALTURA_MAPA = 60
_POSICIONES = Utilidades.posiciones_aleatorias(_SCREENCOORDS[0], _SCREENCOORDS[2], _JUGADORES)
print("Posiciones: {}".format(_POSICIONES))


class Direccion(Enum):
    NINGUNO = 0
    ARRIBA = 1
    DERECHA = 2
    ABAJO = 3
    IZQUIERDA = 4


class Gusano(Turtle):
    def __init__(self, nombre, partida):
        if len(nombre) <= 0:
            raise Excepciones.GusanoDebeTenerNombre()

        # Iniciar la parte de la tortuga
        Turtle.__init__(self, shape=partida.shapes['walk_right_1.gif'])
        self.up()

        self.partida = partida

        self.setpos(self.xpos_inicial(), _ALTURA_MAPA)
        self.barra_vida = Turtle()
        self.posicionar_barra_vida()

        self.nombre = nombre.title()
        self.vida = 100
        self.movimiento = _MAXMOVIMIENTO
        self.bazooka = Bazooka(partida)
        self.bazooka.setpos(self.xcor() + 5, self.ycor() - 5)

        self.moviendose = False
        self.apuntando = False
        self.dir_movimiento = Direccion.NINGUNO
        self.dir_apunt = Direccion.NINGUNO

    def __str__(self):
        return "Gusano({})".format(self.nombre)

    def __repr__(self):
        return "Gusano({})".format(self.nombre)

    def xpos_inicial(self):
        if len(_POSICIONES) - 1 >= 1:
            randpos = random.randint(0, len(_POSICIONES) - 1)
        else:
            randpos = 0
        xpos = _POSICIONES.pop(randpos) + random.randint(-350, 350)
        if xpos >= _SCREENCOORDS[2] - _ALTURA_MAPA:
            xpos -= random.randint(100, 500)
        elif xpos <= _SCREENCOORDS[2] + _ALTURA_MAPA:
            xpos += random.randint(100, 500)
        return xpos

    def esta_vivo(self):
        return self.vida > 0

    def posicionar_barra_vida(self):
        self.barra_vida.up()
        self.barra_vida.shape('square')
        self.barra_vida.shapesize(.25, 1, 1)
        self.barra_vida.fillcolor('pink')
        self.barra_vida.pencolor('black')
        self.barra_vida.setpos(self.xcor(), self.ycor() + 30)

    def hide(self):
        self.clear()
        self.barra_vida.clear()
        self.bazooka.clear()
        self.bazooka.misil.clear()

        self.hideturtle()
        self.barra_vida.hideturtle()
        self.bazooka.hideturtle()
        self.bazooka.misil.hideturtle()

    def morir(self):
        self.barra_vida.hideturtle()
        self.bazooka.hideturtle()
        self.partida.jugadores.remove(self)
        tumba_aleatoria = str(random.randint(*_TUMBAS))
        self.shape(self.partida.shapes['Gravestone_' + tumba_aleatoria + '.gif'])
        if self.partida.jugador_actual == self:
            self.partida.actualizar_jugador()
        self.partida.actualizar_ranking(self)

    def recibir_damage(self, damage):
        self.vida -= damage
        if self.vida >= 1:
            alto, ancho, borde = self.barra_vida.shapesize()
            ancho = self.vida / 100
            self.barra_vida.shapesize(alto, ancho, borde)
            if self.vida >= 75:
                self.barra_vida.fillcolor('pink')
            elif self.vida >= 50:
                self.barra_vida.fillcolor('orange')
            elif self.vida >= 25:
                self.barra_vida.fillcolor('tomato')
            elif self.vida >= 1:
                self.barra_vida.fillcolor('red')
        else:
            self.morir()

    def comprobar_canvas_derecho(self):
        return self.xcor() >= _SCREENCOORDS[2] - _ALTURA_MAPA

    def comprobar_canvas_izquierdo(self):
        return self.xcor() <= _SCREENCOORDS[2] + _ALTURA_MAPA

    def comprobar_canvas(self):
        return self.comprobar_canvas_derecho() or self.comprobar_canvas_izquierdo()

    def mover_derecha(self):
        if not self.comprobar_canvas_derecho():
            self.dir_movimiento = Direccion.DERECHA
            self.animar_andar()

    def mover_izquierda(self):
        if not self.comprobar_canvas_izquierdo():
            self.dir_movimiento = Direccion.IZQUIERDA
            self.animar_andar()

    def puede_moverse(self):
        return self.movimiento >= 1 and not self.moviendose and not self.bazooka.misil.moviendose and self.esta_vivo()

    def direccion_animacion(self):
        self.partida.pantalla.tracer(0)
        if self.dir_movimiento == Direccion.IZQUIERDA:
            anim = 'walk_left_'
            vel = -1
        elif self.dir_movimiento == Direccion.DERECHA:
            anim = 'walk_right_'
            vel = 1

        self.bazooka.cambiar_direccion(self.dir_movimiento)
        self.partida.pantalla.tracer(self.partida.tracer_speed)
        return anim, vel

    def animar_andar(self):
        if self.puede_moverse():

            self.moviendose = True
            self.movimiento -= 1

            anim, vel = self.direccion_animacion()
            for i in range(1, 16):
                self.fd(vel)
                self.bazooka.setx(self.bazooka.xcor() + vel)
                self.barra_vida.setx(self.barra_vida.xcor() + vel)
                self.shape(self.partida.shapes[anim + str(i) + '.gif'])
                self.partida.actualizar_pos_marcador()
            self.parar()

    def apuntar(self, dir_apunt):
        self.dir_apunt = dir_apunt
        if dir_apunt == Direccion.ARRIBA:
            self.bazooka.cambiar_angulo(0.1)
        elif dir_apunt == Direccion.ABAJO:
            self.bazooka.cambiar_angulo(-0.1)

    def apuntar_arriba(self):
        if self.puede_moverse():
            self.apuntar(Direccion.ARRIBA)

    def apuntar_abajo(self):
        if self.puede_moverse():
            self.apuntar(Direccion.ABAJO)

    def subir_potencia(self):
        if self.puede_moverse():
            self.bazooka.cambiar_potencia(5)

    def bajar_potencia(self):
        if self.puede_moverse():
            self.bazooka.cambiar_potencia(-5)

    def parar(self):
        self.moviendose = False
        self.apuntando = False
        self.dir_movimiento = Direccion.NINGUNO
        self.dir_apunt = Direccion.NINGUNO

    def disparar(self):
        if self.puede_moverse():
            self.bazooka.lanzar_misil()


class Bazooka(Turtle):
    def __init__(self, partida):
        Turtle.__init__(self, shape=partida.shapes['Bazooka_0.gif'])
        self.up()
        self.radians()

        self.partida = partida

        self.setheading(math.pi / 2)
        self.direccion = Direccion.DERECHA

        self.potencia = 100
        self.misil = Misil(self.posicion_misil(), partida)

    def cambiar_potencia(self, potencia):
        """ Cambiamos la potencia de disparo
        """
        self.potencia += potencia
        self.partida.actualizar_marcador()

    def cambiar_angulo(self, angulo):
        """ Cambiar el ángulo de disparo
        """
        if self.direccion == Direccion.DERECHA:
            if math.pi / 2 - angulo <= self.heading() <= math.pi - angulo:
                self.left(angulo)
        elif self.direccion == Direccion.IZQUIERDA:
            if math.pi + angulo <= self.heading() <= math.pi * 3 / 2 + angulo:
                self.right(angulo)
        new_shape = 'Bazooka_{}.gif'.format(int(Utilidades.rad_a_deg(self.heading() - math.pi / 2)))
        self.shape(self.partida.shapes[new_shape])

    def cambiar_direccion(self, direccion):
        corx = self.xcor()
        cambio = False
        if direccion == Direccion.DERECHA and direccion != self.direccion:
            self.direccion = Direccion.DERECHA
            corx += + 10
            cambio = True
        elif direccion == Direccion.IZQUIERDA and direccion != self.direccion:
            self.direccion = Direccion.IZQUIERDA
            corx += - 10
            cambio = True
        self.setx(corx)
        if cambio:
            self.setheading(-self.heading())
            new_shape = 'Bazooka_{}.gif'.format(int(Utilidades.rad_a_deg(self.heading() - math.pi / 2)))
            self.shape(self.partida.shapes[new_shape])

    def lanzar_misil(self):
        self.misil.lanzar(self.posicion_misil())

    def posicion_misil(self):
        return self.xcor(), self.ycor(), self.direccion, self.heading() - (math.pi / 2), self.potencia


class Misil(Turtle):
    def __init__(self, posicion, partida):
        Turtle.__init__(self, shape=partida.shapes['Missile_0.gif'], visible=False)
        # Turtle.__init__(self, shape='circle', visible=False)
        self.up()
        self.radians()

        self.partida = partida

        self.moviendose = False
        self.x0, self.y0, self.direccion, self.angulo0, self.potencia = posicion
        if self.direccion == Direccion.IZQUIERDA:
            self.angulo0 = -self.angulo0

    def iniciar_lanzamiento(self, posicion):
        self.moviendose = True
        self.x0, self.y0, self.direccion, self.angulo0, self.potencia = posicion
        if self.direccion == Direccion.IZQUIERDA:
            self.angulo0 = -self.angulo0

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
        self.showturtle()
        self.down()

        self.partida.pantalla.tracer(0)

        posy = Utilidades.tiro_parabolico(self.x0, self.y0, posx, self.angulo0, self.potencia, _GRAVEDAD)
        # print(self.x0, self.y0, posx, self.angulo0, self.potencia, _GRAVEDAD)
        # print("X e Y: {} {}".format(posx, posy))
        if self.direccion == Direccion.IZQUIERDA:
            posx = self.x0 - (posx - self.x0)

        self.setheading(self.towards(posx, posy) - math.pi / 2)
        self.goto(posx, posy)
        new_shape = 'Missile_{}.gif'.format(int(Utilidades.rad_a_deg(self.heading())))
        self.shape(self.partida.shapes[new_shape])
        # Utilidades.followobject(self.partida.pantalla, _SCREENCOORDS, self)
        self.partida.pantalla.tracer(self.partida.tracer_speed)

    def lanzar(self, posicion):
        if not self.moviendose:
            self.iniciar_lanzamiento(posicion)

            tupla_movimiento = int(self.x0), int(self.x0) + _TIEMPOMISIL + 1, 10
            for posx in range(*tupla_movimiento):
                self.mover_parabola(posx)
                if self.comprobar_colision():
                    self.colision()
                    return
            self.limpiar()

    def colision(self):
        print("------------/ Lista de Daños \\------------")
        for jugador in self.partida.jugadores:
            distancia = self.distance(jugador.xcor(), jugador.ycor())
            damage = math.ceil(Utilidades.calcular_damage(250, distancia, 50))
            print("Daño para", jugador, "--", damage, "para la distancia", distancia)
            if damage > 0:
                jugador.recibir_damage(damage)
        print("--------------------\\/--------------------\n")
        self.limpiar()

    def comprobar_colision(self):
        """Comprobamos si el misil ha chocado con algo
        """
        return self.comprobar_bordes() or self.comprobar_enemigos()

    def comprobar_enemigos(self):
        """ Comprobamos si el misil ha chocado con algún enemigo
        """
        for enemigo in self.partida.jugadores:
            if enemigo != self.partida.jugador_actual:
                if self.distance(enemigo.xcor(), enemigo.ycor()) <= 35:
                    return True
        return False

    def comprobar_bordes(self):
        """Comprobamos si el misil está dentro de la pantalla
        """
        llx, lly, urx, ury = _SCREENCOORDS
        return self.xcor() <= llx + _ALTURA_MAPA or self.xcor() >= urx - _ALTURA_MAPA or self.ycor() <= lly + _ALTURA_MAPA

    def limpiar(self):
        Utilidades.setworldcoordinates(self.partida.pantalla, *_SCREENCOORDS)
        self.partida.pantalla.tracer(0)
        self.up()
        self.hideturtle()
        self.home()
        self.clear()
        self.shape(self.partida.shapes['Missile_0.gif'])
        self.moviendose = False
        self.partida.actualizar_jugador()
        self.partida.pantalla.tracer(self.partida.tracer_speed)


class Partida:
    def __init__(self, num_jugadores=2):
        if num_jugadores < 2:
            raise Excepciones.FinalizarPartida("No se puede iniciar la partida con menos de dos jugadores.")

        self.pantalla = Screen()
        self.tracer_speed = self.pantalla.tracer()
        self.pantalla.tracer(0)
        self.shapes = {}
        self.jugadores = []
        self.ranking = []

        self.iniciar_pantalla()
        self.iniciar_sprites()

        self.iniciar_jugadores(num_jugadores)

        self.jugador_actual_index = random.randint(0, _JUGADORES - 1)
        self.jugador_actual = self.jugadores[self.jugador_actual_index]

        self.iniciar_marcador()
        self.actualizar_marcador()

        self.iniciar_teclas()
        self.pantalla.tracer(self.tracer_speed)

    def iniciar_pantalla(self):
        self.pantalla.title("Tankworms Wars")
        self.pantalla._root.resizable(0, 0)
        self.pantalla.setup(0.8, 0.8)
        self.pantalla.setworldcoordinates(*_SCREENCOORDS)
        self.pantalla.bgpic(os.path.join(_RESFOLDERS, 'background.gif'))

    def iniciar_jugadores(self, num_jugadores):
        self.jugadores.clear()
        for i in range(num_jugadores):
            nuevo_gusano = self.crear_gusano(i)
            self.jugadores.append(nuevo_gusano)

    def crear_gusano(self, num):
        nombre = self.pantalla.textinput("Nombre del Jugador", "¿Cómo se va a llamar el Jugador {}?".format(num + 1))
        try:
            nuevo_gusano = Gusano(nombre, self)
        except Excepciones.GusanoDebeTenerNombre:
            print("Ponle un nombre al shiquillo anda.")
            return self.crear_gusano(num)
        else:
            return nuevo_gusano

    def iniciar_sprites(self):
        """
        # Walk Animation
        walk_images = os.path.join(_RESFOLDERS, 'Walk', '*.gif')
        walk_list = glob.glob(walk_images)
        for sprite_path in walk_list:
            self.guardar_sprite(sprite_path)

        # Weapons
        weapon_images = os.path.join(_RESFOLDERS, 'Weapons', '*', '*.gif')
        weapon_list = glob.glob(weapon_images)
        for sprite_path in weapon_list:
            self.guardar_sprite(sprite_path)"""

        res_gifs = os.path.join(_RESFOLDERS, '**', '*.gif')
        gifs_list = glob.glob(res_gifs, recursive=True)
        for gif in gifs_list:
            self.guardar_sprite(gif)

    def guardar_sprite(self, path):
        nombre_sprite = path.split('\\')[-1]
        self.pantalla.register_shape(path)
        self.shapes[nombre_sprite] = path

    def iniciar_marcador(cls):
        cls.marcador = Turtle()
        cls.marcador.up()
        cls.marcador.radians()
        cls.marcador.speed(0)
        cls.marcador.color('white')
        cls.marcador.setheading(0)

    def actualizar_marcador(cls):
        nombre_jugador, potencia_bazooka = cls.jugador_actual.nombre, cls.jugador_actual.bazooka.potencia
        cls.marcador.clear()
        cls.marcador.setpos(2460, 925)
        cls.marcador.write('Turno de {}'.format(nombre_jugador), align='center', font=_FUENTE)
        cls.marcador.setpos(2300, 890)
        cls.marcador.write('Potencia del Bazooka: {}'.format(potencia_bazooka), font=_FUENTE)
        cls.marcador.setpos(cls.jugador_actual.xcor(), cls.jugador_actual.ycor() + 40)

    def actualizar_pos_marcador(self):
        self.marcador.setpos(self.jugador_actual.xcor(), self.jugador_actual.ycor() + 40)

    def actualizar_jugador(self):
        self.jugador_actual_index += 1
        if self.jugador_actual_index >= len(self.jugadores):
            self.jugador_actual_index = 0
        self.jugador_actual = self.jugadores[self.jugador_actual_index]
        self.iniciar_teclas()
        self.actualizar_marcador()

    def actualizar_ranking(self, jugador):
        self.ranking.insert(0, jugador)
        if len(self.jugadores) <= 1:
            self.finalizar_partida()

    def iniciar_teclas(self):
        # Press
        self.pantalla.onkeypress(self.jugador_actual.mover_derecha, 'Right')
        self.pantalla.onkeypress(self.jugador_actual.mover_izquierda, 'Left')
        self.pantalla.onkeypress(self.jugador_actual.apuntar_arriba, 'Up')
        self.pantalla.onkeypress(self.jugador_actual.apuntar_abajo, 'Down')
        self.pantalla.onkeypress(self.jugador_actual.disparar, 'space')
        self.pantalla.onkeypress(self.jugador_actual.subir_potencia, 'x')
        self.pantalla.onkeypress(self.jugador_actual.bajar_potencia, 'z')

        # Release
        # cls.pantalla.onkeyrelease(cls.jugador_actual.parar, 'Right')
        # cls.pantalla.onkeyrelease(cls.jugador_actual.parar, 'Left')
        # cls.pantalla.onkeyrelease(cls.jugador_actual.parar, 'Up')
        # cls.pantalla.onkeyrelease(cls.jugador_actual.parar, 'Down')

        # Generales
        # cls.pantalla.onkeypress(cls.jugador_actual.subir_potencia, 'x')
        # cls.pantalla.onkeypress(cls.jugador_actual.bajar_potencia, 'z')

        # Listen
        self.pantalla.listen()

    def ranking_mensaje(self):
        mensaje = '/***********************************\\' + '\n'
        mensaje += '     1. {}\n'.format(self.jugador_actual)
        for pos in range(len(self.ranking)):
            mensaje += '     {}. {}\n'.format(pos + 2, self.ranking[pos])
        mensaje += '\\***********************************/' + '\n\n'
        return mensaje

    def mensaje_finalizar(self):
        self.pantalla.tracer(0)
        jugadores = self.ranking[:]
        jugadores.append(self.jugador_actual)
        for j in jugadores:
            # Limpiar y Ocultar Jugadores
            j.hide()
            # Colocar Marcador
            # self.marcador.clear()
            self.marcador.shape(self.shapes['ranking.gif'])
        llx, lly, urx, ury = _SCREENCOORDS
        posicion = (llx + urx) / 2, (lly + ury) / 2
        self.marcador.setpos(*posicion)
        self.marcador.color('black')
        self.marcador.write(self.ranking_mensaje(), align='center', font=_FUENTE)
        self.pantalla.tracer(self.tracer_speed)

    def finalizar_partida(self):
        historial = open(_ARCHIVO_RANKING, 'a', encoding='UTF-8')
        output = self.ranking_mensaje()
        historial.write(output)
        historial.close()
        print(output)
        self.mensaje_finalizar()
        Utilidades.cerrar_programa(self.pantalla)


if __name__ == "__main__":
    try:
        partida = Partida(_JUGADORES)
        print("Jugadores: {}".format(partida.jugadores))
        partida.pantalla.mainloop()
    except Excepciones.FinalizarPartida as error:
        print("Ha habido un error curiosete: {}".format(error))
        Utilidades.cerrar_programa()
