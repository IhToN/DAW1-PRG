"""
    Escribe un programa que reconozca la entrada de un número y nos diga si es positivo o negativo. Que pregunte constantemente hasta que el usuario introduzca un Cero.
"""
loopCondition = True
while loopCondition:
    x = float(input('Which number would you like to check? \n'))
    if x > 0:
        print(x, '- It\'s a positive number.')
    elif x < 0:
        print(x, '- It\'s negative.')
    else:
        loopCondition = False
