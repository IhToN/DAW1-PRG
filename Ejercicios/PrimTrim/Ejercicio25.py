"""
    Vamos a hacer una inserción ordenada en lista. Es decir, cada vez que se introduce un número en la lista,
    éste se insertará en la posición que le corresponda manteniendo el criterio de ordenación de la lista,
    de tal forma que la lista siempre está ordenada.
        a. El programa va a contener una lista de números indefinida, el cierre de función
            la hará la introducción de un 0 por parte del usuario.
        b. Definir la función inserta_ordenado(lista, elemento). Esta función NO devuelve nada.
"""


def inserta_ordenado(lista, elemento):
    """ Inserta el elemento dentro de la lista en la posición ordenada que le toca
    """
    pos = 0
    if not lista:
        lista.append(elemento)
    else:
        while pos < len(lista) and elemento > lista[pos]:
            pos += 1
        lista.insert(pos, elemento)


testlist = []
loop = True
elem = int(input("Introduce a number:\n"))
if elem == 0:
    loop = False
while loop:
    inserta_ordenado(testlist, elem)
    elem = int(input("Introduce a number:\n"))
    if elem == 0:
        loop = False
print(testlist)
