"""
    Crear un generador infinito de números pares.
"""


def numeros_pares():
    i = 0
    while True:
        i += 2
        yield i


# a = numeros_pares()
# for e in a:
#    print(e)


"""
    Generador de potencias sucesivas de un número.
"""


def potencia(n, t=5):
    i = 0
    while i < t:
        i += 1
        yield n ** i


b = potencia(5, 10)
for e in b:
    print(e)
