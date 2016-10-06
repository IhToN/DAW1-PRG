"""
    Definir una función codifica a la que se le pasa una cadena de caracteres (mensaje) y un número.
    La función desplazará el carácter tanto como el número diga dentro de la tabla ASCII.
        a. Definir la función codifica
        b. Definir la función decodifica
"""

solution = 'b'


def codifica(message, jump):
    ret = ''
    for c in message:
        ret += chr(ord(c) + jump)
    return ret


def decodifica(message, jump):
    ret = ''
    for c in message:
        ret += chr(ord(c) - jump)
    return ret


if solution == 'a':
    msg = input('What do you want to encode?\n')
    jmp = int(input('How long will the jumper be?\n'))
    print(codifica(msg, jmp))
elif solution == 'b':
    msg = input('What do you want to decode?\n')
    jmp = int(input('How long will the jumper be?\n'))
    print(decodifica(msg, jmp))
