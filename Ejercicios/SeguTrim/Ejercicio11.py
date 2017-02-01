"""
    Realizar un conversor de ºC a ºK con su excepción boñica de que no haya temperatura por debajo de los 0ºK
"""


def celsius_a_kelvin(grados):
    res = grados + 273.15
    try:
        if res < 0:
            raise ValueError('peperoni')
    except ValueError as error:
        print('Mongolo, no se puede abajá del cero absoluto (-273.15ºC),', error)
    else:
        return res


print(celsius_a_kelvin(-273.16))
print(celsius_a_kelvin(-273.15))
print(celsius_a_kelvin(9273.15))
