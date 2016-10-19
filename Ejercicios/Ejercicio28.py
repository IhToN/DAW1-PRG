"""
    Queremos construir una lista por comprensión que contenga, de un texto dado,
    guarde los caracteres de la cadena según su posición
    'Hola Pepe' => ['H', 'Ho', 'Hol', …, 'Hola Pepe']
"""


def concat_text(cadena):
    """
    Devuelve una lista que contiene una cadena por concatenación de caracteres:
    'Hola Pepe' => ['H', 'Ho', 'Hol', …, 'Hola Pepe']
    :param cadena:
    :return:
    """
    return [cadena[0:i] for i in range(1, len(cadena) + 1)]


print(concat_text('hijo de puta, hay que decirlo más... hijo de puta más...'))
