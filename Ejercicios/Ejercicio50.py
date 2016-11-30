"""
    Crear una agenda de teléfono donde la clave sea el nombre del contacto y el valor sea su teléfono.
    a. Solución Original
    b. Crear una funcionalidad para añadir contactos
    c. Se tendrán tres agendas: Amigos, Familia y Trabajo. Crear una función para fundir las tres agendas.
    Esta función debe detectar si existen duplicados, en caso de detectar usuarios duplicados con distinto
    nombre se generará un diccionario inverso cuya clave será el teléfono y como valor la lista de usuario
    que contenía anteriormente
    d. Generar contactos aleatorios usando un diccionario por comprensión,
    siendo el nombre 4 letras aleatorias y un teléfono móvil.
"""
import random, string


def add_contacto(agenda, contacto):
    """ Contacto ha de ser una tupla del tipo ("Nombre", Telefono)
    """
    agenda[contacto[0]] = contacto[1]


def fuse_agendas(lista_agendas):
    """ Devuelve una agenda nueva en base a una lista de agendas.
    La nueva agenda contendrá todos los valores de las agendas de la lista.
    """
    ret = dict()
    for elem in lista_agendas:
        ret.update(elem)
    return ret


def contactos_duplicados(agenda):
    """ Devuelve una agenda cuya clave será el teléfono y su valor los nombres de los contactos
    con dicho teléfono.
    """
    ret = dict()
    for clave, valor in agenda.items():
        if valor in ret.keys():
            ret[valor].append(clave)
        else:
            ret[valor] = [clave]
    return ret


def generar_lista_contacto(cantidad):
    """ Genera y devuelve una lista de tuplas de contactos.
    """
    ret = []
    for i in range(cantidad):
        nombre = ""
        for pos_letra in range(4):
            nombre += random.choice(string.ascii_lowercase)
        numero = 600000000
        for pot_diez in range(8):
            numero += random.randint(0, 9) * (10 ** pot_diez)
        ret.append((nombre.capitalize(), numero))
    return ret


def agregar_contactos_random(agenda, cantidad):
    """ Agrega cantidad contactos aleatorios a la agenda especificada
    """
    for nombre, telefono in generar_lista_contacto(cantidad):
        agenda[nombre] = telefono


amigos, familia, trabajo = dict(), dict(), dict()
add_contacto(amigos, ('Lonchas', 952361245))
add_contacto(familia, ('Oboe', 612452365))
add_contacto(trabajo, ('Zippi', 612452365))
print(fuse_agendas([amigos, familia, trabajo]))
print(contactos_duplicados(fuse_agendas([amigos, familia, trabajo])))

agregar_contactos_random(amigos, 10)
print(amigos)
