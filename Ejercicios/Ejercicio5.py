"""
    Escribe un programa que reconozca la entrada de un número y nos diga si es positivo o negativo. Que pregunte constantemente hasta que el usuario introduzca un Cero.
"""
while True:     # Hacemos que el while esté SIEMPRE ejecutándose
    x = float(input('Which number would you like to check? \n'))
    if x > 0:       # Miramos si es positivo
        print(x, '- It\'s a positive number.')
    elif x < 0:     # Si no es positivo, miramos si es negativo
        print(x, '- It\'s negative.')
    else:           # Si no es ni uno ni otro, es cero, por lo tanto acabamos el while
        break       # Lanzamos el mágico break para que ROMPA el while
