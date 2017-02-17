"""
    Calse Punto
        coord x
        coord y
"""


class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def suma(self, punto):
        return Punto(self.x + punto.x, self.y + punto.y)

    def resta(self, punto):
        return Punto(self.x - punto.x, self.y - punto.y)
