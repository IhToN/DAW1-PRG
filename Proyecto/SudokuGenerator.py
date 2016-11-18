"""
    Proyecto Personal - Vamos a hacer un generador de Sudokus intentando usar el algoritmo de Backtracking.
    Este algoritmo lo que hace es generar el Sudoku por pasos reasignando valores anteriores en lugar de
     desechar todo el proceso en caso de llegar a un Sudoku irresoluble.
"""

from Proyecto.Sudoku import *
import time


def findNextCellToFill(sudoku, fila, columna):
    for x in range(fila, 10):
        for y in range(columna, 10):
            if sudoku.get_numero(x, y) == 0:
                return x, y
    for x in range(1, 10):
        for y in range(1, 10):
            if sudoku.get_numero(x, y) == 0:
                return x, y
    return -1, -1


def isValid(sudoku, i, j, e):
    rowOk = sudoku.check_duplicated(sudoku.get_nums_filas()[i - 1], e)
    # rowOk = all([e != sudoku.get_numero(i, x) for x in range(0, 7)])
    if rowOk:
        columnOk = sudoku.check_duplicated(sudoku.get_nums_columnas()[j - 1], e)
        # columnOk = all([e != sudoku.get_numero(x, j) for x in range(0, 7)])
        if columnOk:
            numRegion = 0
            if 1 <= i <= 3:
                if 1 <= j <= 3:
                    numRegion = 1
                elif 4 <= j <= 6:
                    numRegion = 2
                elif 7 <= j <= 9:
                    numRegion = 3
            elif 4 <= i <= 6:
                if 1 <= j <= 3:
                    numRegion = 4
                elif 4 <= j <= 6:
                    numRegion = 5
                elif 7 <= j <= 9:
                    numRegion = 6
            elif 7 <= i <= 9:
                if 1 <= j <= 3:
                    numRegion = 7
                elif 4 <= j <= 6:
                    numRegion = 8
                elif 7 <= j <= 9:
                    numRegion = 9
            for elem in sudoku.get_nums_filas():
                print(elem)
            print("----")
            print(i, sudoku.get_nums_filas()[i - 1], rowOk)
            print(j, sudoku.get_nums_columnas()[j - 1], columnOk)
            print(numRegion, sudoku.get_nums_regiones()[numRegion - 1],
                  sudoku.check_duplicated(sudoku.get_nums_regiones()[numRegion - 1], e))
            print(e)
            print("----")
            return sudoku.check_duplicated(sudoku.get_nums_regiones()[numRegion - 1], e)
            """# finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = int(3 * (i / 3)), int(3 * (j / 3))
            print(secTopX, ",", secTopX + 3, "---", secTopY, ",", secTopY + 3)
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if sudoku.get_numero(x, y) == e:
                        return False
            return True"""
    return False


def solveSudoku(sudoku, fila=1, columna=1):
    fila, columna = findNextCellToFill(sudoku, fila, columna)
    if fila == -1:
        return True
    for e in range(1, 10):
        if isValid(sudoku, fila, columna, e):
            sudoku.set_numero(fila, columna, e)
            # time.sleep(2)
            if solveSudoku(sudoku, fila, columna):
                return True
            sudoku.set_numero(fila, columna, 0)
    return False


test_sudoku = Sudoku()
test_sudoku.set_numero(1, 2, 8).set_numero(1, 4, 5).set_numero(1, 5, 7).set_numero(1, 6, 6).set_numero(1, 7, 2) \
    .set_numero(2, 4, 4).set_numero(2, 6, 2) \
    .set_numero(3, 5, 3).set_numero(3, 6, 9).set_numero(3, 7, 5).set_numero(1, 8, 4).set_numero(3, 9, 8) \
    .set_numero(4, 1, 6).set_numero(4, 2, 3).set_numero(4, 4, 9).set_numero(4, 7, 8) \
    .set_numero(4, 8, 5).set_numero(4, 9, 2) \
    .set_numero(5, 2, 9).set_numero(5, 4, 2).set_numero(5, 7, 3).set_numero(5, 8, 7) \
    .set_numero(6, 1, 8).set_numero(6, 5, 5).set_numero(6, 7, 6).set_numero(6, 8, 9).set_numero(6, 9, 4) \
    .set_numero(7, 1, 2).set_numero(7, 2, 5).set_numero(7, 3, 7).set_numero(7, 4, 6).set_numero(7, 6, 3) \
    .set_numero(7, 7, 4).set_numero(7, 8, 8).set_numero(7, 8, 9) \
    .set_numero(8, 1, 3).set_numero(8, 3, 8).set_numero(8, 4, 7).set_numero(8, 8, 2).set_numero(8, 9, 5) \
    .set_numero(9, 2, 4).set_numero(9, 9, 6)
solveSudoku(test_sudoku)
# test_sudoku.set_numero(5, 3, 8)
for elem in test_sudoku.get_nums_filas():
    print(elem)
