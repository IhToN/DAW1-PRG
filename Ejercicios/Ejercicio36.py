"""
    Modificar el ejercicio 20 para que el desplazamiento tome por defecto el valor por omisión 1 en el,
    además para la cadena se le pasará una sucesión indefinida de cadenas a codificar.
    La función devuelve una lista todas las cadenas codificadas.
"""
solution = 'a'


def codifica(*message, jump=1):
    """ Devuelve una lista de mensajes codificados por desplazamiento jump
    """
    ret = []
    for elem in message:
        ret.append(cod_msg(elem, jump))
    return ret


def cod_msg(message, jump):
    ret = ''
    for c in message:
        ret += chr(ord(c) + jump)
    return ret


def decodifica(*message, jump=1):
    """ Devuelve una lista de mensajes decodificados por desplazamiento jump
    """
    return codifica(*message, jump=-jump)


if solution == 'a':
    msg = input('What do you want to encode?\n')
    jmp = int(input('How long will the jumper be?\n'))
    print(codifica(msg, jump=jmp))
elif solution == 'b':
    msg = input('What do you want to decode?\n')
    jmp = int(input('How long will the jumper be?\n'))
    print(decodifica(msg, jump=jmp))
