"""
    Animal
        Estado (moviendose/parado)

        Met:
            Mover / Parar

    Perro
        Met:
            Ladrar
"""


class Animal:
    def __init__(self):
        self.moviendose = False

    def mover(self):
        self.moviendose = True

    def parar(self):
        self.moviendose = False


class Mascota(Animal):
    def __init__(self, nombre):
        self.nombre = nombre


class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)

    def ladrar(self):
        print('¡Guau!')


class PerroDomestico(Perro, Mascota):
    def __init__(self, nombre):
        Perro.__init__(self)
        Animal.__init__(self, nombre)
