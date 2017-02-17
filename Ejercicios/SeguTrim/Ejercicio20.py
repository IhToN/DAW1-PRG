"""
    Crear tantas personas como nombres del fichero de nombres propios.
"""

from Ejercicios.SeguTrim.Objetos.Persona import Persona
import random


def main():
    fichero = open('nombrespropios_20030828.txt', encoding="utf-8")
    personas = []
    for nombre in fichero:
        personas.append(Persona(nombre.strip(), random.randint(0, 125)))
    fichero.close()
    return personas


for persona in main():
    persona.presentate()
