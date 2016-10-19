"""
    Queremos construir una lista por comprensión que contenga, de un texto dado, guarde los caracteres de la cadena según su posición
    a. Primera solución
        'Hola Pepe' => ['H', 'Ho', 'Hol', …, 'Hola Pepe']
    b. Invertir las cadenas
        'Hola Pepe' => ['Hola Pepe', 'Hola Pep', 'Hola Pe', …, 'H']
"""

solucion = 'b'

def concat_text(cadena):
    """
    Devuelve una lista que contiene una cadena por concatenación de caracteres:
    sol a = 'Hola Pepe' => ['H', 'Ho', 'Hol', …, 'Hola Pepe']
    sol b = sol a = 'Hola Pepe' => ['Hola Pepe', 'Hola Pep', 'Hola Pe', …, 'H']
    :param cadena:
    :return:
    """
    if solucion == 'a':
        return [cadena[:i] for i in range(1, len(cadena) + 1)]
    elif solucion == 'b':
        return [cadena[:i] for i in range(len(cadena), 0, -1)]
    else:
        return 'Solución Inválida'


print(concat_text('hijo de puta, hay que decirlo más... hijo de puta más...'))
