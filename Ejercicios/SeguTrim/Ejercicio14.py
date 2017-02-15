"""
    Crear un lector/editor de texto desde consola, a lo bonito.
"""


def abrir():
    """ Preguntamos al usuario qué fichero abrir y mostramos su contenido línea a línea
    """
    strf = input("¿Qué fichero quieres abrir?\n")
    try:
        fichero = open(strf)
        for linea in fichero:
            print(linea)
        fichero.close()
    except FileNotFoundError as Error:
        print("El fichero no existe, te va a tocar hacer otra cosita.\n")


def escribir(reemplazar=True):
    """ Abrimos un archivo en modo escritura o modo append según el argumento y se escribe en el archivo
    que el usuario especifique
    """
    strf = input("¿En qué fichero quieres escribir?\n")
    fichero = open(strf, 'w' if reemplazar else 'a')
    aescribir = input("Dime una línea que quieras escribir en el fichero:\n")
    while aescribir != '':
        fichero.write(aescribir + "\n")
        aescribir = input("Dime una línea que quieras escribir en el fichero:\n")
    fichero.close()


def que_hacer():
    """ Se pregunta al usuario qué quiere hacer: abrir, escribir o agregar
    """
    do = input('¿Qué quieres hacer?\n')
    while do != "nada" and do != "":
        if do == "abrir":
            abrir()
            do = input('¿Qué quieres hacer?\n')
        elif do == "escribir":
            escribir()
            do = input('¿Qué quieres hacer?\n')
        elif do == "agregar":
            escribir(False)
            do = input('¿Qué quieres hacer?\n')
    print("Enga, hasta logo.\n")


que_hacer()
