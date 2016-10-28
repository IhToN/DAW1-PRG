"""
    Hacer un conversor de gradación
    a. De Celsius a Fahrenheit y de Fahrenheit a Celsius
    b. Escribir una función que genere aleatoriamente valores de temperatura entre -5 y 40ºC
    c. Escribir una función que genere una tupla con 1200 valores de temperatura
    d. Considerar que cada 100 datos del apartado C es un mes. Dar una media de temperaturas por meses
    e. Definir una función que traduzca la tupla de Celsius a Fahrenheit y viceversa
"""
from random import randint


def conversor(grados, de_f_a_c=False):
    """ Conversor de grados. Por defecto convierte de Celsius a Fahrenheit.
    Si el segundo parámetro es True convertirá de Fahrenheit a Celsius
    """
    if de_f_a_c:
        return (grados - 32) / 1.8
    else:
        return grados * 1.8 + 32


def rand_temp(mes=0):
    """ Genera un número aleatorio entre distintos rangos según el mes.
    Diciembre, Enero y Febrero [-10, 10]
    Marzo, Abril y Mayo o Octubre y Noviembre [3, 25]
    Junio, Julio, Agosto y Septiembre [20, 40]
    """
    if mes <= 2 or mes >= 12:
        return randint(-10, 10)
    if 3 <= mes <= 5 or 10 <= mes <= 11:
        return randint(3, 25)
    if 6 <= mes <= 9:
        return randint(20, 40)
    else:
        return randint(-5, 40)


def gen_tem():
    ret = ()
    for i in range(1200):
        ret += rand_temp(i // 100 + 1),
    return ret


def subdivide_gen():
    return [gen_tem()[100 * x + 0: 100 * x + 100] for x in range(len(gen_tem()) // 100)]


def media_mes():
    ret = ()
    for element in subdivide_gen():
        ret += sum(element) / len(element),
    return ret


def con_tuple(tupla, de_f_a_c=False):
    ret = ()
    for elem in tupla:
        ret += conversor(elem, de_f_a_c)
    return ret


print(media_mes())
