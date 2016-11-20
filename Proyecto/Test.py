""" Test del Sudoku"""
from Proyecto.Sudoku import *
from Proyecto.SudokuSolver import *

sudoku1 = Sudoku()
sudoku1.set_numero(1, 2, 8).set_numero(1, 4, 5).set_numero(1, 5, 7).set_numero(1, 6, 6).set_numero(1, 7, 2) \
    .set_numero(2, 4, 4).set_numero(2, 6, 2) \
    .set_numero(3, 5, 3).set_numero(3, 6, 9).set_numero(3, 7, 5).set_numero(3, 8, 4).set_numero(3, 9, 8) \
    .set_numero(4, 1, 6).set_numero(4, 2, 3).set_numero(4, 4, 9).set_numero(4, 7, 8) \
    .set_numero(4, 8, 5).set_numero(4, 9, 2) \
    .set_numero(5, 2, 9).set_numero(5, 4, 2).set_numero(5, 7, 3).set_numero(5, 8, 7) \
    .set_numero(6, 1, 8).set_numero(6, 5, 5).set_numero(6, 7, 6).set_numero(6, 8, 9).set_numero(6, 9, 4) \
    .set_numero(7, 1, 2).set_numero(7, 2, 5).set_numero(7, 3, 7).set_numero(7, 4, 6).set_numero(7, 6, 3) \
    .set_numero(7, 7, 4).set_numero(7, 8, 8).set_numero(7, 9, 9) \
    .set_numero(8, 1, 3).set_numero(8, 3, 8).set_numero(8, 4, 7).set_numero(8, 8, 2).set_numero(8, 9, 5) \
    .set_numero(9, 2, 4).set_numero(9, 9, 6)
print("\nSudoku Original:", *sudoku1.get_nums_filas(), sep='\n    ')
print("\nSudoku Resuelto:", *sudoku1.get_solucion_algX(), sep='\n    ')
print("\nSoluciones del sudoku:", *code_gold_solver(sudoku1.get_nums_string()))

grid = [[0, 0, 0, 0, 7, 6, 4, 0, 0],
        [0, 1, 4, 0, 0, 3, 0, 0, 7],
        [0, 3, 0, 5, 0, 0, 0, 1, 6],
        [2, 0, 0, 0, 9, 7, 0, 0, 0],
        [8, 6, 9, 0, 0, 0, 3, 0, 4],
        [0, 0, 0, 0, 0, 4, 8, 0, 2],
        [5, 8, 0, 7, 0, 0, 0, 0, 3],
        [0, 2, 0, 0, 0, 0, 5, 8, 0],
        [4, 0, 0, 0, 0, 0, 0, 2, 0]]
sudoku2 = Sudoku(grid)
print("\nSudoku Original:", *sudoku2.get_nums_filas(), sep='\n    ')
print("\nSudoku Resuelto:")
for solucion in solve_sudoku((3, 3), sudoku2.get_nums_filas()):
    print("", *solucion, sep='\n    ')
print("\nSoluciones del sudoku:", *code_gold_solver(sudoku2.get_nums_string()))

sudoku3 = Sudoku("027800061000030008910005420500016030000970200070000096700000080006027000030480007")
print("\nSudoku Original:", *sudoku3.get_nums_filas(), sep='\n    ')
print("\nSudoku Resuelto:", *sudoku3.get_solucion_algX(), sep='\n    ')
print("\nSoluciones del sudoku:", *sudoku3.get_soluciones(), sep='\n    ')
