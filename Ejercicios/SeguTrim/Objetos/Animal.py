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
        self.estado = False

    def mover(self):
        self.estado = True

    def parar(self):
        self.estado = False


class Perro(Animal):
    def __init__(self):
        pass

    def ladrar(self):
        print('¡Guau!')
