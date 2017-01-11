"""
    Escribir un programa que lea un texto y devuelva un diccionario conteniendo en cada valor todas
    las palabras de una longitud determinada, siendo esta longitud la clave de dicho diccionario.
"""

textoTest = "Al pan, pan. Al vino, vino. Y en tu culo, mi pepino."


def contador(texto):
    diccionario = dict()
    texto = texto.lower().replace(",", "").replace(".", "")
    for word in texto.split(" "):
        letras = len(word)
        if letras in diccionario:
            if word not in diccionario[letras]:
                diccionario[letras].append(word)
        else:
            diccionario[letras] = [word]
    return diccionario


print(contador(textoTest))
