"""
    Clase Punto
        coord x
        coord y
        suma(punto)
        resta(punto)

    Clase Traza
        instancias Punto en una Lista
        añadir punto
        comparar dos trazas (dos trazas serán iguales si sus puntos son iguales)
"""

import math
import turtle


class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "Punto({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def suma(self, punto):
        """ Devuelve la suma vectorial del punto con otro
        """
        return Punto(self.x + punto.x, self.y + punto.y)

    def resta(self, punto):
        """ Devuelve la resta vectorial del punto con otro
        """
        return self.suma(-punto)

    def distancia(self, punto):
        """ Devuelve la distancia que hay entre un punto y otro
        """
        return math.hypot(self.x - punto.x, self.y - punto.y)


class Traza:
    def __init__(self, *args):
        self.trazado = []
        for arg in args:
            if isinstance(arg, Punto):
                self.trazado.append(arg)
            else:
                raise ValueError(arg, "no es un punto.")

    def __str__(self):
        out = ""
        for punto in self.trazado:
            out += str(punto) + " "
        return out

    def __eq__(self, other):
        return self.trazado == other.trazado

    def add_punto(self, punto):
        """ Añade un punto nuevo a la Traza
        """
        if isinstance(punto, Punto):
            self.trazado.append(punto)
        else:
            raise ValueError("¡Ioputa, que en las trazas sólo puede haber puntos y no cosas raras!")

    def longitud_traza(self):
        """ Devuelve la suma de la distancia entre todos los puntos de la traza
        """
        ret = 0
        for p in range(len(self.trazado) - 1):
            ret += self.trazado[p].distancia(self.trazado[p + 1])
        return ret

    def dump_traza(self, fichero):
        """ Guardamos la traza en un fichero de trazas
        """
        fichero = open(fichero, 'w', encoding="utf-8")
        for punto in self.trazado:
            fichero.write("{},{}\n".format(punto.x, punto.y))
        fichero.close()

    def load_traza(self, fichero):
        try:
            fichero = open(fichero, encoding="utf-8")
            self.trazado = []
            for linea in fichero:
                if linea != "":
                    punto = linea.split(",")
                    self.add_punto(Punto(punto[0].strip(), punto[1].strip()))
        except FileNotFoundError:
            print("No existe el fichero.")

    def dibuja(self, ):
        tortuga = self.turtle
        tortuga.down()
        for punto in self.trazado:
            tortuga.setpos(punto.x, punto.y)
        tortuga.up()

    def toggle_capture(self):
        """Activamos o desactivamos el modo captura, según toque"""
        self.capture_mode = not self.capture_mode
        if not self.capture_mode:
            self.turtle.clear()
            self.dibuja()

    def toggle_pen(self):
        """Cambiar estado del lapiz de la tortuga"""
        tortuga = self.turtle
        if tortuga.isdown():
            tortuga.up()
        else:
            tortuga.down()

    def move_turtle(self, x, y):
        """Si estamos en modo captura, movemos la tortuga y vamos guardando los puntos"""
        tortuga = self.turtle
        if self.capture_mode:
            tortuga.setheading(tortuga.towards(x, y))
            tortuga.setpos(x, y)
            self.add_punto(Punto(x, y))


def test():
    p = Punto(3, 0)
    k = Punto(0, 4)
    tr = Traza(p, k)
    print(tr)
    tr.dump_traza("traza.txt")
    tr.load_traza("traza.txt")
    print(tr)

    s = turtle.Screen()
    t = turtle.Turtle()
    tr.turtle = t
    tr.capture_mode = False

    s.onkey(tr.toggle_capture, 'space')
    t.onclick(tr.toggle_pen, btn=1)
    s.onclick(tr.move_turtle)
    s.listen()

    tr.dibuja()

    turtle.done()
