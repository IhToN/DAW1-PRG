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
    """ Conversor de grados. Por defecto convierte de Celsius a Fahrenheit
    Si el segundo parámetro es True convertirá de Fahrenheit a Celsius
    """
    if de_f_a_c:
        return (grados - 32) / 1.8
    else:
        return grados * 1.8 + 32


def rand_temp(mes=0):
    """ Genera un número aleatorio entre distintos rangos según el mes
    Diciembre (12), Enero (1) y Febrero (2) [-10, 10]
    Marzo (3), Abril (4) y Mayo (5) o Octubre (10) y Noviembre (11) [3, 25]
    Junio (6), Julio (7), Agosto (8) y Septiembre (9) [20, 40]
    En cualquier otro caso [-5, 40]
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
    """ Genera y devuelve una tupla de 1200 temperaturas aleatorias a 100 temperaturas por mes
    """
    ret = ()
    for i in range(1200):
        ret += rand_temp(i // 100 + 1),
    return ret


def subdivide_gen():
    """ Devuelve una lista con las temperaturas divididas de 100 en 100
    """
    return [gen_tem()[100 * x + 0: 100 * x + 100] for x in range(len(gen_tem()) // 100)]


def media_mes():
    """ Devuelve la media de temperaturas de cada mes
    """
    ret = ()
    for element in subdivide_gen():
        ret += sum(element) / len(element),
    return ret


def con_tuple(tupla, de_f_a_c=False):
    """ Convierte y devuelve los grados de una tupla
    Por defecto convierte de Celsius a Fahrenheit
    Si de_f_a_c = True convertirá de Fahrenheit a Celsius
    """
    ret = ()
    for elem in tupla:
        ret += conversor(elem, de_f_a_c)
    return ret


print(media_mes())
