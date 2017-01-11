"""
    El usuario introduce una cadena y un carácter, produciendo el programa como salida la cadena de entrada
    quitando los caracteres coincidentes con el introducido.
"""
string = input('Introduce the String to modify:\n')
charac = input('Introduce the Character to delete:\n')
res = '\033[33m'  # Cadena resultado, la que trataremos al final, la inicializamos con un color

for c in string:
    if c != charac:
        res += c
print('The new string is:\n' + res)
