"""
    Modificar el ejercicio 20 para que el desplazamiento tome por defecto el valor por omisión 1.
"""

solution = 'b'


def codifica(message, jump=1):
    ret = ''
    for c in message:
        ret += chr(ord(c) + jump)
    return ret


def decodifica(message, jump=1):
    return codifica(message, -jump)


if solution == 'a':
    msg = input('What do you want to encode?\n')
    jmp = int(input('How long will the jumper be?\n'))
    print(codifica(msg, jmp))
elif solution == 'b':
    msg = input('What do you want to decode?\n')
    jmp = int(input('How long will the jumper be?\n'))
    print(decodifica(msg, jmp))
