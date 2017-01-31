"""
    Hacer una función de conversión de tipos que trate los errores, recuperándolo y volviendo a pedir el dato.
"""


def input_a_int():
    """Pide un número al usuario y casca si no lo introduce."""
    inp = input("Introduce un número, gachón de la capa:\n")
    try:
        inp = int(inp)
    except:
        print("Toma pete guapo que ha cascao")
        input_a_int()
    else:
        print("Mira qué numerito más bonito", inp)
        return inp


input_a_int()
