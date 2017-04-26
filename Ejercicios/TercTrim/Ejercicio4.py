"""
    Crear una tabla para la clase Contacto y gestionar la agenda.
    Ha de contener métodos para
        insertar contactos
        Agenda - 'cargar_contacto' a través de su identificador
        Agenda - 'cargar_contacto' a través de su nombre
        Agenda - 'cargar_agenda' que lea todos los contactos
        Agenda - 'nuevo_contacto' que cree y guarde un contacto nuevo
    Detectar errores
        qué error produce cuando se pide un identificador no existente
"""

from Ejercicios.TercTrim.Objetos import Persona
import sqlite3


def initDB():
    print('Creamos la base de datos')
    conn = sqlite3.connect('contacto.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS contactos
    (id INT PRIMARY KEY, nombre VARCHAR(255), edad INT, telefono INT, email VARCHAR(255))''')

    conn.commit()
    conn.close()


def insertar_datos(lista_contactos):
    print('Insertamos los datos en la DB')
    conn = sqlite3.connect('contacto.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO contactos VALUES (?, ?, ?, ?)', lista_contactos)
    conn.commit()
    conn.close()


def obtener_datos():
    print('Obtenemos y mostramos los datos')
    conn = sqlite3.connect('contacto.db')
    cursor = conn.cursor()
    for row in cursor.execute('SELECT * FROM contactos'):
        print(row)
    conn.close()


def ejemplo():
    agenda = Persona.Agenda()
    initDB()
    lista_contactos = [('Antonio', 24, 666555444, 'asd@fgh.jkl'),
                       ('Francisco', 29, 666555444, 'asd@fgh.jkl'),
                       ('Joan', 28, 666555444, 'asd@fgh.jkl')]
    print(lista_contactos)
    for contacto in lista_contactos:
        agenda.nuevo_contacto(contacto[0], contacto[1], contacto[2], contacto[3], True)
    obtener_datos()


try:
    ejemplo()
except sqlite3.DatabaseError as e:
    print('Error con la base de datos: {}'.format(e))
except sqlite3.OperationalError as e:
    print('Error de operación: {}'.format(e))
