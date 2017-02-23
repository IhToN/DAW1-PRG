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


class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

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
            out += str(punto)
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
            fichero.write(str(punto) + "\n")
        fichero.close()

    def load_traza(self, fichero):
        try:
            fichero = open(fichero, encoding="utf-8")
            self.trazado = []
            for linea in fichero:
                if linea != "":
                    punto = linea.replace("(", "").replace(")", "").split(",")
                    self.add_punto(Punto(punto[0].strip(), punto[1].strip()))
        except FileNotFoundError:
            print("No existe el fichero.")

    """ Cosa mágica para cargar una lista de trazas
    def load_traza(self, numlinea):
        try:
            fichero = open('trazas.txt', encoding="utf-8")
            fichero.seek(numlinea)
            linea = fichero.readline()
            if linea != "":
                print(linea)
                puntos = linea.replace(")(", "//").replace("(", "").replace(")", "").split("//")
                for punto in puntos:
                    punto = punto.split(",")
                    self.trazado = []
                    self.add_punto(Punto(punto[0].strip(), punto[1].strip()))
            else:
                raise ValueError
        except FileNotFoundError:
            print("No existe el fichero de trazas.")
        except ValueError:
            print("No existe esa traza en el fichero de trazas.")
    """


def test():
    p = Punto(3, 0)
    k = Punto(0, 4)
    tr = Traza(p, k)
    print(tr)
    tr.dump_traza("traza.txt")
    tr.load_traza("traza.txt")
    print(tr)
