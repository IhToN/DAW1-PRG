"""
    Mostrar una cadena por líneas mostrando en la primera línea el primer carácter,
    en la segunda línea el primer y segundo carácter, y así hasta la cadena final donde muestra la cadena completa.
"""
# Declaramos las variables principales que vamos a usar, aquí si debemos repetir el loop y los mensajes estáticos
repeatLoop = True
askMsg = 'Would you please intruduce a phrase?\n'
bypassMsg = 'no me da la gana'
stopMsg = 'Ok, don\'t hit me, I won\'t ask you anymore.'
solucion = 'a'  # Puede ser 'a', 'b' y 'r'

# Pedimos la String, comprobamos si es el bypass message y si no inicializamos contador
inputString = input(askMsg)
if str(inputString).casefold() == bypassMsg:
    print(stopMsg)
    repeatLoop = False
i = 0

# Entramos en el loop, procesamos los caracteres y luego preguntamos de nuevo al usuario por otra frase
while repeatLoop:
    while i < len(inputString):
        # Solución A
        if solucion == 'a':
            print(inputString[0:i + 1])  # Usamos Slicing
        # Solución B
        if solucion == 'b':
            print(inputString[0:len(inputString) - i])
        # Solución Random, mostrarlo tipo árbol de navidad
        if solucion == 'r':
            print(' ' * ((len(inputString) - i) // 2), inputString[0:i + 1])
        i += 1
    print('The String has', len(inputString), 'elements.')

    inputString = input(askMsg)
    if str(inputString).casefold() == bypassMsg:
        print(stopMsg)
        repeatLoop = False
