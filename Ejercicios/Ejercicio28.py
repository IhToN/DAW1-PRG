"""
    Queremos construir una lista por comprensión que contenga, de un texto dado, guarde los caracteres de la cadena según su posición
    a. Primera solución
        'Hola Pepe' => ['H', 'Ho', 'Hol', …, 'Hola Pepe']
    b. Invertir las cadenas
            'Hola Pepe' => ['H', 'oH', 'loH', …, 'epeP olaH']
"""


def concat_text(cadena):
    """
    Devuelve una lista que contiene una cadena por concatenación de caracteres:
    sol a = 'Hola Pepe' => ['H', 'Ho', 'Hol', …, 'Hola Pepe']
    sol b = sol a = 'Hola Pepe' => ['Hola Pepe', 'Hola Pep', 'Hola Pe', …, 'H']
    :param cadena:
    :return:
    """
    return [cadena[:i] for i in range(1, len(cadena) + 1)]


def invert_concat_text(cadena):
    return [x[::-1] for x in concat_text(cadena)]


test_cadena = 'hijo de puta, hay que decirlo más... hijo de puta más...'

print(concat_text(test_cadena))
print(invert_concat_text(test_cadena))
