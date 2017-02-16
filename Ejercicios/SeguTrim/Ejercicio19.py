"""
    Crear una clase Persona con un método __str__ de tal forma que devuelva una cadena
    que nos permita visualizar a dicha persona.
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Persona({0}, {1})".format(repr(self.nombre), self.edad)


print(Persona("Antonio", 24))
