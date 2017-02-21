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


class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def suma(self, punto):
        """ Devuelve la suma vectorial del punto con otro.
        """
        return Punto(self.x + punto.x, self.y + punto.y)

    def resta(self, punto):
        """ Devuelve la resta vectorial del punto con otro.
        """
        return self.suma(-punto)


class Traza:
    def __init__(self, *args):
        self.trazado = []
        for arg in args:
            if isinstance(arg, Punto):
                self.trazado.append(arg)

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
