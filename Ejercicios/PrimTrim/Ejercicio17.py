"""
    Escribir una función que lea una cadena desde teclado hasta que se introduzca una cadena vacía.
    Dicha función se llamará leer. Esta función quitará los blancos e invertirá la cadena, imprimiendo el resultado.
"""


# Función de Valor
def sin_blancos(string):
    ret = ''
    for c in string:
        if c != ' ':
            ret += c
    return ret


# Función de Valor
def invierte(string):
    ret = ''
    for c in string:
        ret = c + ret
    return ret


# Función Procedimental
def leer():
    string = input('Introduce a phrase to test:\n')
    while string != '':
        print('Modified string:\n', invierte(sin_blancos(string)))
        string = input('Introduce a phrase to test:\n')
    print('*** Task finished ***')


leer()
