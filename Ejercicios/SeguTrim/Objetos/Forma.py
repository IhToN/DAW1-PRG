"""
    Clase Forma
        Met:
            area
            perimetro

    Clase Círculo
        Atrib:
            radio

    Clase Rectángulo
        Atrib:
            base
            altura

    Clase Cuadrado - hijo de Rectángulo
        Atrib:
            lado
"""

from math import pi


class Forma:
    def __init__(self):
        pass

    def perimetro(self):
        return None

    def area(self):
        return None


class Circulo(Forma):
    def __init__(self, radio=1):
        self.radio = radio

    def perimetro(self):
        return 2 * pi * self.radio

    def area(self):
        return pi * self.radio ** 2


class Rectangulo(Forma):
    def __init__(self, base=1, altura=1):
        self.base = base
        self.altura = altura

    def perimetro(self):
        return 2 * self.base + 2 * self.altura

    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):
    def __init__(self, lado=1):
        Rectangulo.__init__(self, lado, lado)
