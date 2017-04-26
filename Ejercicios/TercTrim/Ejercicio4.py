"""
    Crear una tabla para la clase Contacto.
"""

from Ejercicios.TercTrim.Objetos import Persona
import sqlite3


def initDB():
    print('Creamos la base de datos')
    conn = sqlite3.connect('contacto.db')

    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS contactos
    (nombre VARCHAR(255) PRIMARY KEY, edad NUMBER, telefono NUMBER, email VARCHAR(255))''')

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
    initDB()
    lista_contactos = [Persona.Contacto('Antonio', 24, 666555444, 'asd@fgh.jkl').serialize(),
                       Persona.Contacto('Francisco', 29, 666555444, 'asd@fgh.jkl').serialize(),
                       Persona.Contacto('Joan', 28, 666555444, 'asd@fgh.jkl').serialize()]
    print(lista_contactos)
    insertar_datos(lista_contactos)
    obtener_datos()


ejemplo()
