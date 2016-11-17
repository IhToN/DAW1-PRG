"""
    Clase Sudoku. Contendrá la cuadrícula con sus subsecciones vacías.
    Será el propio generador quien se encargue de rellenarlo con la solución.
"""
from random import randint


class Sudoku:
    def __init__(self):
        self.cuadricula = tuple([[0] * 9 for _ in range(9)])

    def gen_cuadricula(self):
        """
        Regenera el Sudoku con todos los elementos a 0
        """
        self.cuadricula = tuple([[0] * 9 for _ in range(9)])

    def check_solucion(self):
        """
        Devuelve si el Sudoku está bien resuelto o no
        """
        return self.check_regiones() and self.check_horizontales() and self.check_verticales()

    def get_regiones(self):
        """ Devuelve una lista con todas las regiones de 3x3 del Sudoku
        """
        return [self.create_region(column, row) for row in range(3) for column in range(3)]

    def create_region(self, column, row):
        """ Devuelve la región según la columna y la fila especificada
        """
        """
        first_region = [item for sublist in range(0, 3) for item in self.cuadricula[sublist][0:3]]
        second_region = [item for sublist in range(0, 3) for item in self.cuadricula[sublist][3:6]]
        third_region = [item for sublist in range(0, 3) for item in self.cuadricula[sublist][6:9]]
        fourth_region = [item for sublist in range(3, 6) for item in self.cuadricula[sublist][0:3]]
        fifth_region = [item for sublist in range(3, 6) for item in self.cuadricula[sublist][3:6]]
        sixth_region = [item for sublist in range(3, 6) for item in self.cuadricula[sublist][6:9]]
        seventh_region = [item for sublist in range(6, 9) for item in self.cuadricula[sublist][0:3]]
        eighth_region = [item for sublist in range(6, 9) for item in self.cuadricula[sublist][3:6]]
        nineth_region = [item for sublist in range(6, 9) for item in self.cuadricula[sublist][6:9]]

        total_regions = [first_region, second_region, third_region, fourth_region, fifth_region, sixth_region,
                         seventh_region, eighth_region, nineth_region]
        """
        return [item for sublist in range(0 + 3 * row, 3 + 3 * row) for item in
                self.cuadricula[sublist][0 + 3 * column: 3 + 3 * column]]

    def check_regiones(self):
        """
        Comprueba que todas las regiones están bien resueltas
        """
        for region in self.get_regiones():
            if not self.check_numbers(region):
                return False
        return True

    def get_verticales(self):
        """
        Devuelve una lista con todas las columnas de la cuadrícula
        """
        return [list(tuple(zip(*self.cuadricula))[_]) for _ in range(9)]

    def check_verticales(self):
        """
        Comprueba que las columnas están bien resueltas
        """
        for vertical in self.get_verticales():
            if not self.check_numbers(vertical):
                return False
        return True

    def check_horizontales(self):
        """
        Comprueba que las filas están bien resueltas
        """
        for horizontal in self.cuadricula:
            if not self.check_numbers(horizontal):
                return False
        return True

    def check_numbers(self, numberlist):
        """
        Comprueba que la cada lista de números están correctas y no hay números repetidos
        """
        if 0 in numberlist:
            return False
        return 1 in numberlist and 2 in numberlist and 3 in numberlist and 4 in numberlist and \
               5 in numberlist and 6 in numberlist and 7 in numberlist and 8 in numberlist and 9 in numberlist


Sudo = Sudoku()

print(" ==== Cuadrícula Base ====")
for elem in Sudo.cuadricula:
    print(elem)

print(" ==== Cuadrícula Aleatoria (No Solucionada) ====")
for reg in range(9):
    for elem in range(9):
        Sudo.cuadricula[reg][elem] = randint(1, 9)
    print(Sudo.cuadricula[reg])

print(" ==== Regiones de Cuadrícula ====")
for elem in Sudo.get_regiones():
    print(elem)

print(" ==== Números Verticales ====")
for elem in Sudo.get_verticales():
    print(elem)
