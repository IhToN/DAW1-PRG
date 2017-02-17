"""
    Clase Persona
        Nombre
        Edad
        Pareja
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.pareja = None

    def __str__(self):
        return "Persona({0}, {1})".format(repr(self.nombre), self.edad)

    def presentate(self, a_quien=None):
        if a_quien:
            output = "Hola {0}, ".format(a_quien)
        else:
            output = "Hola, "
        output += "soy {0} y tengo {1} años".format(self.nombre, self.edad)
        print(output)

    def emparejar(self, pareja):
        if isinstance(pareja, Persona):
            if pareja.pareja:
                pareja.pareja.desemparejar()
            self.pareja, pareja.pareja = pareja, self
        else:
            print("¡{0} no es una persona!".format(pareja))

    def desemparejar(self):
        if self.pareja:
            pareja = self.pareja
            self.pareja, pareja.pareja = None, None
