"""
    Clase Persona
        Nombre
        Edad
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Persona({0}, {1})".format(repr(self.nombre), self.edad)
