"""
    Me aburro un huevo y parte del otro así que voy a poner a homer contando muelles que se traga el retrete.
"""


def homer_muellin(numero_muelles=1000):
    for i in range(1, numero_muelles + 1):
        estrin = 'un', 'muelle'
        if i > 1:
            estrin = 'otro', 'muelles'
        print('Cojo', estrin[0], 'muelle, lo tiro por el retrete y ya son', i, estrin[1],
              'los que el retrete se ha tragado.')


homer_muellin(2000)
