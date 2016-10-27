"""
    Escribir una función a la que se le da como parámetro una tupla de números enteros
    y devuelva la suma de todos los elementos de dicha tupla.
    a. Solución Original
    b. Hacer otra función resumen(notas) a la que dada la tupla nos devuelva otra tupla
    que conste de tres elementos internos: cantidad de elementos, la suma de ellos y la media aritmética
    c. Generar entre 10 y 20 notas al azar para 40 alumnos distintos.
"""
from random import randint


def suma_numeros(lista_numeros):
    """ Devuelve la suma de todos los elementos de 'lista_numeros'
    """
    ret = 0
    for elem in lista_numeros:
        ret += elem
    return ret
    # Otra posible solución es con la función sum(iterable)
    # return sum(lista_numeros)


def resumen(notas):
    """ Devuelve una tupla de tres elementos:
        Cantidad de elementos de notas
        Suma de todos los elementos de notas
        Media aritmética de notas
    """
    return len(notas), suma_numeros(notas), suma_numeros(notas) / len(notas)


def gen_notas():
    ret = ()
    for i in range(randint(10, 20)):
        ret += (randint(0, 10),)
    return ret


def gen_alumnos():
    ret = ()
    for i in range(40):
        ret += (gen_notas(),)
    return ret


test = 1, 2, 3, 4, 5, 6, 7
print('Contador notas:', resumen(test)[0])
print('Total notas:', resumen(test)[1])
print('Media notas:', resumen(test)[2])

print('-----')
id = 1
for i in gen_alumnos():
    print('Notas del alumno ', id)
    print(i, resumen(i))
    id += 1
