"""
    Una persona puede o no tener una sóla pareja. Por defecto la persona se crea sin pareja
    sin embargo se podrá crear una pareja.
"""
from Ejercicios.SeguTrim.Objetos.Persona import Persona

persona1 = Persona('Alberto', 24)
persona2 = Persona('Marta', 23)
persona3 = Persona('Chuloplaya', 25)

# Emparejar
persona1.emparejar(persona2)
print("P1: {} \n P2: {} \n P3: {}".format(persona1.pareja, persona2.pareja, persona3.pareja))

# Emparejar
persona3.emparejar(persona2)
print("P1: {} \n P2: {} \n P3: {}".format(persona1.pareja, persona2.pareja, persona3.pareja))

# Desemparejar
persona1.desemparejar()
print("P1: {} \n P2: {} \n P3: {}".format(persona1.pareja, persona2.pareja, persona3.pareja))
