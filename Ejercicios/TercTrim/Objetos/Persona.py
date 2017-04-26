"""
    Clase Persona
        Nombre
        Edad
        Pareja
"""
import sqlite3


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
    def __init__(self, id, nombre, edad, telefono, email):
        super().__init__(nombre, edad)
        self.id = id
        self.telefono = telefono
        self.email = email

    def __repr__(self):
        return "Contacto({0}, {1}, {2}, {3}, {4})" \
            .format(self.id, repr(self.nombre), self.edad, self.telefono, self.email)

    def serialize(self):
        return self.id, self.nombre, self.edad, self.telefono, self.email


class Agenda:
    def __init__(self, *contactos):
        self.contactos = {}
        self.i = -1
        for contacto in contactos:
            if isinstance(contacto, Contacto):
                self.contactos[contacto.id] = contacto
            else:
                raise ValueError(contacto, "no es un contacto.")

    def __next__(self):
        self.i += 1
        if self.i < len(self.contactos):
            return self.contactos[self.i]
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def cargar_contacto(self, id=-1, nombre=None):
        """ Devuelve un contacto según su ID o su Nombre.
        La función da preferencia a la ID.
        """
        conn = sqlite3.connect('contacto.db')
        cursor = conn.cursor()

        if id > 0:
            cursor.execute('''SELECT * FROM contactos WHERE id = {}'''.format(id))
        elif nombre:
            cursor.execute('''SELECT * FROM contactos WHERE nombre = {}'''.format(nombre))

        result = cursor.fetchall()

        conn.close()
        return result

    def cargar_agenda(self):
        self.contactos = {}
        self.i = -1

        conn = sqlite3.connect('contacto.db')
        cursor = conn.cursor()

        for contacto in cursor.execute('SELECT * FROM contactos'):
            self.contactos[contacto[0]] = Contacto(*contacto)

        conn.close()

    def guardar_contacto(self, contacto):
        conn = sqlite3.connect('contacto.db')
        cursor = conn.cursor()

        cursor.execute('INSERT INTO contactos VALUES (?, ?, ?, ?, ?)', contacto.serialize())

        conn.commit()
        conn.close()

    def nuevo_contacto(self, nombre, edad, telefono, email, en_db=False):
        id_contacto = 0
        if len(self.contactos):
            id_contacto = list(self.contactos.keys())[-1] + 1
        self.contactos[id_contacto] = Contacto(id_contacto, nombre, edad, telefono, email)

        if en_db:
            self.guardar_contacto(self.contactos[id_contacto])


if __name__ == '__main__':
    c1 = Contacto('Antonio', 24, 111222333, 'trolo@lolo.com')
    c2 = Contacto('Fran', 24, 111222333, 'trolo@lolo.com')
    c3 = Contacto('Joan', 24, 111222333, 'trolo@lolo.com')

    agenda = Agenda(c1, c2, c3)

    for cont in agenda:
        print(cont)
