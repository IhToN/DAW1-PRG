"""
    Escribe un programa que compruebe si la última letra de una cadena es una A que suelte un mensaje
"""
while True:
    inputString = input('Would you please intruduce a phrase?\n')

    if str(inputString[-1]).casefold() == 'a':  # Forzamos la conversión a str y le hacemos casefold (tó a minúsculas)
        print('I like that phrase, you must be a nice guy.')
    else:
        print('I don\'t like you, neither your way of thinking.')
    print('Introduced phrase:', inputString)
    print('Length of the phrase:', len(inputString))
