"""
    Crear un generador infinito de números pares.
"""


def numeros_pares():
    i = 0
    while True:
        i += 2
        yield i


a = numeros_pares()
for e in a:
    print(e)
