"""
    El usuario introduce una cadena y un carácter, produciendo el programa como salida la cadena de entrada invertida
    quitando los caracteres coincidentes con el introducido.
"""
string = input('Introduce the String to modify:\n')
charac = input('Introduce the Character to delete:\n')

res = ''  # Cadena resultado, la que trataremos al final, la inicializamos con un color
color = '\033[33m'  # Opcional, esta cositas es para dar color a la cadena de salida

for c in string:
    if c != charac:
        res = c + res
print('The new string is:\n' + color + res)
