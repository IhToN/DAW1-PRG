"""
    Coger una cadena e imprimir todos los caracteres uno a uno de la cadena.
"""
# Declaramos las variables principales que vamos a usar, aquí si debemos repetir el loop y los mensajes estáticos
repeatLoop = True
askMsg = 'Would you please intruduce a phrase?\n'
bypassMsg = 'no me da la gana'
stopMsg = 'Ok, don\'t hit me, I won\'t ask you anymore.'

# Pedimos la String, comprobamos si es el bypass message y si no inicializamos contador
inputString = input(askMsg)
if str(inputString).casefold() == bypassMsg:
    print(stopMsg)
    repeatLoop = False
upCounter = 0

# Entramos en el loop, procesamos los caracteres y luego preguntamos de nuevo al usuario por otra frase
while repeatLoop:
    while upCounter < len(inputString):
        print('The element', upCounter, 'of the String is "', inputString[upCounter], '"')
        upCounter += 1

    print('The String has', len(inputString), 'elements.')

    inputString = input(askMsg)
    if str(inputString).casefold() == bypassMsg:
        print(stopMsg)
        repeatLoop = False
