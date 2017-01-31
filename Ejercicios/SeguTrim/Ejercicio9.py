"""
    Hacer una función de conversión de tipos que trate los errores, recuperándolo y volviendo a pedir el dato.
"""


def input_a_int():
    """Pide dos números al usuario y devuelve su división."""
    inp1 = input("Introduce un dividendo, gachón de la capa:\n")
    inp2 = input("Introduce un divisor, gachón de la capa:\n")
    try:
        val1 = int(inp1)
        val2 = int(inp2)
        res = val1 / val2
    except ZeroDivisionError as error:
        print("Toma pete guapo que ha cascao:", error)
        input_a_int()
    except Exception as error:
        print("Toma pete guapo y desconocido que se ha cascao.", error)
        input_a_int()
    else:
        print("Mira qué numerito más bonito", res)
        return res


input_a_int()
