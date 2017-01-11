"""
    Escribe la función invierte. Al cual se le pasa una cadena y devuelve dicha cadena de forma invertida.
"""


def invierte(string):
    ret = ''
    for c in string:
        ret = c + ret
    return ret


testString = "Frase a probar en la función 'invierte'"
print(invierte(testString))
