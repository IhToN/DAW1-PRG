"""
    Escribir una función que lea una cadena desde teclado hasta que se introduzca una cadena vacía.
    Dicha función se llamará leer. Esta función quitará los blancos e invertirá la cadena, imprimiendo el resultado.
"""


def sin_blancos(string):
    ret = ''
    for c in string:
        if c != ' ':
            ret += c
    return ret


def invierte(string):
    ret = ''
    for c in string:
        ret = c + ret
    return ret


def leer():
    string = input('Introduce a phrase to test:\n')
    if string == '':
        print('*** Task finished ***')
        return
    string = sin_blancos(string)
    string = invierte(string)
    print('Modified string:\n', string)
    leer()


leer()
