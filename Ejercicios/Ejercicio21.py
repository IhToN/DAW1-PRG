"""
    Definir una función rotar a la que se le introduzca una cadena y un número.
    Esta función devuelve una cadena la cual es la rotación a la derecha N veces de la cadena de entrada.ABC
"""


def rotar(message, nrots):
    """
    Devuelve una cadena rotada a la derecha nrots veces.
    :param message - cadena a rotar:
    :param nrots - numero de veces:
    :return - cadena rotada:
    """
    lenrot = (len(message) - nrots) % len(message)  # Miramos en qué punto tenemos que cortar la cadena
    subMsg = message[0:lenrot]  # Subdividimos la parte izquierda de la cadena
    shifted = message[lenrot:]  # Subdividimos la parte derecha de la cadena
    return shifted + subMsg  # Invertimos la posición izquierda y la derecha y la devolvemos


testmsg = input('Introduce a message to test:\n')
testnr = int(input('Introduce how many rotations:\n'))
print(rotar(testmsg, testnr))
