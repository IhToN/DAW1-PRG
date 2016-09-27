"""
    Escribe un programa que reconozca una entrada de un número y nos diga si es negativo, positivo o cero.
"""
x = float(input('Introduce un número: '))  # Si usas int() en vez de float() sólo reconoce enteros y no decimales.
if x > 0:  # La condición puede ir entre paréntesis (x > 0) aunque es desaconsejable (en Python)
    print(x, 'es positivo.')
elif x == 0:
    print(x, 'es cero.')
else:
    print(x, 'es negativo.')
