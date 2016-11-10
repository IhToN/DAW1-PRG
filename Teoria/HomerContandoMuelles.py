"""
    Me aburro un huevo y parte del otro así que voy a poner a homer contando muelles que se traga el retrete.
"""


def homer_muellin(numero_muelles=1000):
    for i in range(1, numero_muelles + 1):
        estrin = 'un', 'es', 'muelle el'
        if i > 1:
            estrin = 'otro', 'son', 'muelles los'
        print('Cojo', estrin[0], 'muelle, lo tiro por el retrete y ya', estrin[1], i, estrin[2],
              'que el retrete se ha tragado.')


homer_muellin(999999999)
