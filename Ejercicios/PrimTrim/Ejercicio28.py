"""
    Queremos construir una lista por comprensión que contenga, de un texto dado, guarde los caracteres
    de la cadena según su posición
    a. Primera solución
        'Hola Pepe' => ['H', 'Ho', 'Hol', …, 'Hola Pepe']
    b. Invertir las cadenas
            'Hola Pepe' => ['H', 'oH', 'loH', …, 'epeP olaH']
    c. Construir una lista que contenga el tamaño de cada elemento de la lista de la solución a
"""


def concat_text(cadena):
    """
    Devuelve una lista que contiene una cadena por concatenación de caracteres:
    'Hola Pepe' => ['H', 'Ho', 'Hol', …, 'Hola Pepe']
    :param cadena:
    :return:
    """
    return [cadena[:i] for i in range(1, len(cadena) + 1)]


def invert_concat_text(cadena):
    """
    Devuelve una lista que contiene una cadena por concatenación de caracteres invertida:
    'Hola Pepe' => ['H', 'oH', 'loH', …, 'epeP olaH']
    :param cadena:
    :return:
    """
    return [elem[::-1] for elem in concat_text(cadena)]


def len_concat_text(cadena):
    """
    Devuelve la longitud de cada elemento de concat_text(cadena)
    :param cadena:
    :return:
    """
    return [len(elem) for elem in concat_text(cadena)]


test_cadena = 'hijo de puta, hay que decirlo más... hijo de puta más...'

print('-------------- Solución A --------------')
print(concat_text(test_cadena))
print('-------------- Solución B --------------')
print(invert_concat_text(test_cadena))
print('-------------- Solución C --------------')
print(len_concat_text(test_cadena))
