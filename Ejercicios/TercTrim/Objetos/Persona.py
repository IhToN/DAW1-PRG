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

    def __init__(self, nombre, edad, telefono, email):
        super().__init__(nombre, edad)
        Contacto.contador += 1
        self.numero = Contacto.contador
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return "Contacto({0}, {1}, {2}, {3}, {4})" \
            .format(self.numero, repr(self.nombre), self.edad, self.telefono, self.email)


class Agenda:
    def __init__(self, *contactos):
        self.contactos = {}
        self.i = -1
        for contacto in contactos:
            if isinstance(contacto, Contacto):
                self.contactos[contacto.nombre] = contacto
            else:
                raise ValueError(contacto, "no es un contacto.")

    def __next__(self):
        self.i += 1
        if self.i < len(self.contactos):
            cont_name = sorted(list(self.contactos))[self.i]
            return self.contactos[cont_name]
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    c1 = Contacto('Antonio', 24, 111222333, 'trolo@lolo.com')
    c2 = Contacto('Fran', 24, 111222333, 'trolo@lolo.com')
    c3 = Contacto('Joan', 24, 111222333, 'trolo@lolo.com')

    agenda = Agenda(c1, c2, c3)

    for cont in agenda:
        print(cont)
