"""
    Clase Sudoku. Contendrá la cuadrícula con sus subsecciones vacías.
    Será el propio generador quien se encargue de rellenarlo con la solución.
"""
from math import ceil, sqrt
from random import randint
from tkinter import Tk

from Proyecto import SudokuGenerator
from Proyecto.SudokuSolver import *
import textwrap

from Proyecto.SudokuUI import SudokuUI


class Sudoku:
    def __init__(self, grid=None):
        """ Inicializa el sudoku con 9 filas a [0, False] o con el grid introducido,
        el grid ha de ser del tipo:
                [[0, 0, 0, 0, 7, 6, 4, 0, 0],
                 [0, 1, 4, 0, 0, 3, 0, 0, 7],
                 [0, 3, 0, 5, 0, 0, 0, 1, 6],
                 [2, 0, 0, 0, 9, 7, 0, 0, 0],
                 [8, 6, 9, 0, 0, 0, 3, 0, 4],
                 [0, 0, 0, 0, 0, 4, 8, 0, 2],
                 [5, 8, 0, 7, 0, 0, 0, 0, 3],
                 [0, 2, 0, 0, 0, 0, 5, 8, 0],
                 [4, 0, 0, 0, 0, 0, 0, 2, 0]]
        """
        self.game_over = False
        if not grid:
            self.cuadricula = [[[0, False]] * 9 for _ in range(9)]
        elif type(grid) == list:
            self.cuadricula = [[[number, False if number == 0 else True] for number in elem] for elem in grid]
        elif type(grid) == str:
            self.cuadricula = [[[int(number), False if number == 0 else True] for number in elem] for elem in
                               textwrap.wrap(grid, int(sqrt(len(grid))))]

    # Puzzle Starter
    def start(self, num_ceros=17, is_clear=False):
        if is_clear:
            for elem in self.cuadricula:
                for num in elem:
                    if not num[1]:
                        num[0] = 0
        else:
            self.__init__(SudokuGenerator.make_board(num_ceros))

    # Getters
    def get_cuadricula(self):
        """ Devuelve la cuadrícula generada
        """
        return self.get_nums_filas()

    def get_regiones(self):
        """ Devuelve una lista con todas las regiones de 3x3 del Sudoku
        """
        return [self.get_region(row, column) for row in range(1, 10, 3) for column in range(1, 10, 3)]

    def get_columnas(self):
        """ Devuelve una lista con todas las columnas de la cuadrícula
        """
        return [list(tuple(zip(*self.cuadricula))[_]) for _ in range(9)]

    def get_filas(self):
        """ Devuelve una lista con todas las columnas de la cuadrícula
        """
        return self.cuadricula

    def get_nums_regiones(self):
        """ Devuelve una lista con los números de cada region de la cuadrícula
        """
        return [list(tuple(zip(*elem))[0]) for elem in self.get_regiones()]

    def get_nums_columnas(self):
        """ Devuelve una lista con los números de cada columna de la cuadrícula
        """
        return [list(tuple(zip(*elem))[0]) for elem in self.get_columnas()]

    def get_nums_filas(self):
        """ Devuelve una lista con los números de cada fila de la cuadrícula
        """
        return [list(tuple(zip(*elem))[0]) for elem in self.get_filas()]

    def get_numero(self, row, column):
        return self.cuadricula[row - 1][column - 1][0]

    def get_region(self, row, column):
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
        row_reg = ceil((row - 1) // 3)
        column_reg = ceil((column - 1) // 3)
        return [item for sublist in range(0 + 3 * row_reg, 3 + 3 * row_reg) for item in
                self.cuadricula[sublist][0 + 3 * column_reg: 3 + 3 * column_reg]]

    def get_nums_region(self, row, column):
        return [item[0] for item in self.get_region(row, column)]

    def get_nums_string(self):
        acum = ""
        for fila in self.get_nums_filas():
            for numero in fila:
                acum += str(numero)
        return acum

    def get_solucion_algX(self):
        for solucion in solve_sudoku((len(self.get_nums_filas()) // 3, len(self.get_nums_columnas()) // 3),
                                     self.get_nums_filas()):
            return solucion

    def get_soluciones(self):
        soluciones = []
        for sol in code_gold_solver(self.get_nums_string()):
            soluciones.append(sol)
        return soluciones

    # Setters
    def set_numero(self, row, column, numero):
        """ Cambia el número de la columna y la fila especificada,
        numeradas desde 1 hasta 9.
        """
        if not self.cuadricula[row - 1][column - 1][1]:
            self.cuadricula[row - 1][column - 1] = [numero, False]
        else:
            print("¡Ese número no es modificable!", row, column, self.cuadricula[row - 1][column - 1])
        return self

    def set_solucion_algX(self):
        i = 0
        solucion = self.get_solucion_algX()
        for fila in solucion:
            i += 1
            j = 0
            for num in fila:
                j += 1
                if not self.cuadricula[i - 1][j - 1][1]:
                    self.set_numero(i, j, num)

    # Generators
    def gen_cuadricula(self):
        """ Regenera el Sudoku con todos los elementos a 0
        """
        self.cuadricula = [[[0, False]] * 9 for _ in range(9)]
        return self

    # Checkers
    def check_solucion(self):
        """ Devuelve si el Sudoku está bien resuelto o no
        """
        self.game_over = self.check_regiones() and self.check_filas() and self.check_columnas()
        return self.game_over

    def check_regiones(self):
        """ Comprueba que todas las regiones están bien resueltas
        """
        for region in self.get_nums_regiones():
            if not self.check_numbers(region):
                return False
        return True

    def check_columnas(self):
        """ Comprueba que las columnas están bien resueltas
        """
        for columna in self.get_nums_columnas():
            if not self.check_numbers(columna):
                return False
        return True

    def check_filas(self):
        """ Comprueba que las filas están bien resueltas
        """
        for fila in self.get_nums_filas():
            if not self.check_numbers(fila):
                return False
        return True

    def check_numbers(self, numberlist):
        """ Comprueba que la cada lista de números están correctas y no hay números repetidos
        """
        if 0 in numberlist:
            return False
        return 1 in numberlist and 2 in numberlist and 3 in numberlist and 4 in numberlist and \
               5 in numberlist and 6 in numberlist and 7 in numberlist and 8 in numberlist and 9 in numberlist

    def check_duplicated(self, numberlist, number):
        return not number in numberlist


if __name__ == '__main__':
    sudoku = Sudoku(SudokuGenerator.make_board(randint(5, 70)))
    root = Tk()
    SudokuUI(root, sudoku)
    root.geometry("%dx%d" % (SudokuUI.WIDTH, SudokuUI.HEIGHT + 60))
    root.mainloop()
