"""
    Crear una clase Persona con un método __str__ de tal forma que devuelva una cadena
    que nos permita visualizar a dicha persona.
"""
from Ejercicios.SeguTrim.Objetos.Persona import Persona

p1 = Persona('Melchor', 42)
p2 = Persona('Gaspar', 65)
p3 = Persona('Basaltar', 38)

lista_personas = [p1, p2, p3]
for p in lista_personas:
    print(p)

x = p1
print(x, p1)

rave = [Persona('Flipi' + str(i), i) for i in range(1000)]
for p in rave:
    print(p)
