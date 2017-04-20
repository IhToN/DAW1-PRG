"""
    Crear un generador finito con la sucesión de Fibonacci de los 100 primeros elementos.
"""


def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        yield x
        x, y = y, x + y
    yield y


test = fibonacci(100)
for elem in test:
    print(elem)
