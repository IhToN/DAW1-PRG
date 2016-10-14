"""
    Vamos a hacer una inserción ordenada en lista. Es decir, cada vez que se introduce un número en la lista,
    éste se insertará en la posición que le corresponda manteniendo el criterio de ordenación de la lista,
    de tal forma que la lista siempre está ordenada.
        a. El programa va a contener una lista de números indefinida, el cierre de función
            la hará la introducción de un 0 por parte del usuario.
        b. Definir la función inserta_ordenado(lista, elemento). Esta función NO devuelve nada.
"""


def inserta_ordenado(lista, elemento):
    numcheck = True
    if len(lista) == 0:
        lista.insert(0, elemento)
    else:
        for num in lista.copy():
            if elemento <= num and numcheck:
                lista.insert(lista.index(num), elemento)
                numcheck = False


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
