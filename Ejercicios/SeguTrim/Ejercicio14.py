"""
    Crear un lector/editor de texto desde consola, a lo bonito.
"""


def que_hacer():
    do = input('¿Qué quieres hacer?\n')
    while do != "nada" and do != "":
        if do == "abrir":
            abrir()
            do = input('¿Qué quieres hacer?\n')
        elif do == "escribir":
            escribir()
            do = input('¿Qué quieres hacer?\n')
    print("Enga, hasta logo.\n")


def abrir():
    strf = input("¿Qué fichero quieres abrir?\n")
    try:
        fichero = open(strf)
        return fichero
    except FileNotFoundError as Error:
        print("El fichero no existe, te va a tocar hacer otra cosita.\n")


def escribir():
    strf = input("¿En qué fichero quieres escribir?\n")
    fichero = open(strf, 'w')
    return fichero


que_hacer()
