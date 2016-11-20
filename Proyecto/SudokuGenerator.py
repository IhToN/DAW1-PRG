"""
    Vamos a hacer un generador de Sudokus aleatorio, el sistema NO valorará la dificultad de un Sudoku
    ya que no hay forma empírica de poder valorar la dificultad. La única forma de "calcular" dicha dificultad
    es contando el número de métodos necesarios para poder resolver el Sudoku.
    A lo sumo podemos ver el número de valores estáticos y las posibles soluciones del Sudoku y con esos datos
    presuponer una dificultad para dicho Sudoku.
"""
import random

from Proyecto.Sudoku import *


def make_board(num_ceros = 17):
    """Return a random filled m**2 x m**2 Sudoku board."""
    n = 3 ** 2
    board = [[None for _ in range(n)] for _ in range(n)]

    def search(c=0):
        i, j = divmod(c, n)
        i0, j0 = i - i % 3, j - j % 3  # Origin of mxm block
        numbers = list(range(1, n + 1))
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]  # row
                and all(row[j] != x for row in board)  # column
                and all(x not in row[j0:j0 + 3]  # block
                        for row in board[i0:i])):
                board[i][j] = x
                if c + 1 >= n ** 2 or search(c + 1):
                    return board
        else:
            board[i][j] = None
            return None

    search()
    for _ in range(num_ceros):
        fil, col = random.randint(0, 8), random.randint(0, 8)
        board[fil][col] = 0
    return board


sudoku = Sudoku(make_board(70))
print("Cuadrícula Sudoku", *sudoku.get_nums_filas(), sep="\n    ")
print("Soluciones Sudoku", *sudoku.get_soluciones(), sep="\n    ")
