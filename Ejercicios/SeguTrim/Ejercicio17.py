"""
    Descargar y recorrer http://olea.org/proyectos/lemarios/nombres-propios-2003-08-28.txt
        Buscar todos los nombres propios que no contengan ninguna letra de 'Carlos'
"""

_DICNOMBRES = 'nombrespropios_20030828.txt'


def acertijo_carlos():
    """ Devuelve una lista de nombres propios que no contienen las letras de 'carlos'
    """
    ret = []
    carlos = set('carlos')
    try:
        fichero = open(_DICNOMBRES, encoding="utf-8")
        for nombre in fichero:
            nombre_formateado = nombre.strip().lower().replace('á', 'a').replace('ó', 'o')
            if not any(letra in carlos for letra in nombre_formateado):
                ret.append(nombre.strip())
        fichero.close()
    except FileNotFoundError as error:
        print('¿Te has descargao el archivo bien? Porque no tengo cojones de encontrarlo.')

    return ret


print(acertijo_carlos())
