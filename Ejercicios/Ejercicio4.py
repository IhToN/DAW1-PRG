"""
    Escribe un programa que reconozca una entrada de un número y nos diga si es negativo, positivo o cero.
"""
x = int(input('Introduce un número: '))
if x > 0:       # La condición puede ir entre paréntesis (x > 0) aunque es desaconsejable (en Python)
    print(x, 'es positivo.')
elif x == 0:
    print(x, 'es cero.')
else:
    print(x, 'es negativo.')