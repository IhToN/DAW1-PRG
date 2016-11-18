"""
    Crear un diccionario de palabras:
        a. Un diccionario Español - Inglés, necesitará una función para añadir traducciones a dicho diccionario.
        b. Crear una lista de tuplas con los pares del diccionario, pudiendo pasar dicha tupla a la traducción.
    Usar los días de la semana como ejemplos.
"""


def traduce(diccionario, palabra):
    """ Devuelve la traducción de la palabra Español-Inglés
    """
    if palabra in diccionario.keys():
        return diccionario[palabra]
    elif palabra in diccionario.values():
        return list(diccionario.keys())[list(diccionario.values()).index(palabra)]
    else:
        print("No me la vas a colar, esa palabra no está en el diccionario")


def aprende(diccionario, castellano, ingles):
    """ Enseña al diccionario una nueva palabra con su traducción
    """
    diccionario[castellano] = ingles


def aprende_tupla(diccionario, lista_tuplas):
    """ Enseña al diccionario una lista de tuplas pares de
    (palabra, traducción)
    """
    [aprende(diccionario, *par_trad) for par_trad in lista_tuplas]


insiclopidia = dict()

palabras = [("Lunes", "Monday"), ("Martes", "Tuesday"), ("Miércoles", "Wednesday"),
            ("Jueves", "Thursday"), ("Viernes", "Friday"), ("Sábado", "Saturday"), ("Domingo", "Sunday")]
aprende_tupla(insiclopidia, palabras)
print(insiclopidia)
print(traduce(insiclopidia, "Tuesday"))
