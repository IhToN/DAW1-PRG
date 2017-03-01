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

    def desemparejar(self):
        if self.pareja:
            pareja = self.pareja
            self.pareja, pareja.pareja = None, None

    def emparejar(self, nueva_pareja):
        if isinstance(nueva_pareja, Persona):
            if nueva_pareja.pareja:
                nueva_pareja.pareja.desemparejar()
            self.pareja, nueva_pareja.pareja = nueva_pareja, self
        else:
            print("¡{0} no es una persona!".format(nueva_pareja))


class Contacto(Persona):
    contador = 0

    def __init__(self, nombre, edad, telefono):
        Persona.__init__(self, nombre, edad)
        Contacto.contador += 1
        self.numero = Contacto.contador
        self.telefono = telefono

    def __str__(self):
        return "Alumno({0}, {1}, {2}, {3})".format(self.numero, repr(self.nombre), self.edad, self.telefono)
