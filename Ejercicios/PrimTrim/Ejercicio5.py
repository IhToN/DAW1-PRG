"""
    Escribe un programa que reconozca la entrada de un número y nos diga si es positivo o negativo. Que pregunte constantemente hasta que el usuario introduzca un Cero.
"""
while True:  # Hacemos que el while esté SIEMPRE ejecutándose
    x = float(input('Which number would you like to check? \n'))
    if x > 0:  # Miramos si es positivo
        print(x, '- It\'s a positive number.')
    elif x < 0:  # Si no es positivo, miramos si es negativo
        print(x, '- It\'s a negative number.')
    else:  # Si no es ni uno ni otro, es cero, por lo tanto acabamos el while
        print('Okay, I\'ll stop making questions.')
        break  # Lanzamos el mágico break para que ROMPA el while
print('\033[93m*** IA has stopped working.')  # La cosa esa del \033[93m es para darle colorcito amarillo al texto

"""
    - Modo estructurado -
    x = 1
    while x != 0:
        x = float(input('Number? ')
        if x > 0:
            print('Positive')
        if x < 0:
            print('Negative')
    print('EOP')
"""