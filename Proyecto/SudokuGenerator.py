"""
    Proyecto Personal - Vamos a hacer un generador de Sudokus intentando usar el algoritmo de Backtracking.
    Este algoritmo lo que hace es generar el Sudoku por pasos reasignando valores anteriores en lugar de
     desechar todo el proceso en caso de llegar a un Sudoku irresoluble.
"""

from Proyecto.Sudoku import *
from itertools import product


def solve_sudoku(size, grid):
    """ An efficient Sudoku solver using Algorithm X.
    """

    row, column = size
    num_regiones = row * column
    X = ([("rc", rc) for rc in product(range(num_regiones), range(num_regiones))] +
         [("rn", rn) for rn in product(range(num_regiones), range(1, num_regiones + 1))] +
         [("cn", cn) for cn in product(range(num_regiones), range(1, num_regiones + 1))] +
         [("bn", bn) for bn in product(range(num_regiones), range(1, num_regiones + 1))])
    Y = dict()
    for r, c, n in product(range(num_regiones), range(num_regiones), range(1, num_regiones + 1)):
        b = (r // row) * row + (c // column)  # Box number
        Y[(r, c, n)] = [
            ("rc", (r, c)),
            ("rn", (r, n)),
            ("cn", (c, n)),
            ("bn", (b, n))]
    X, Y = exact_cover(X, Y)
    for i, row in enumerate(grid):
        for j, n in enumerate(row):
            if n:
                select(X, Y, (i, j, n))
    for solution in solve(X, Y, []):
        for (r, c, n) in solution:
            grid[r][c] = n
        yield grid


def exact_cover(X, Y):
    X = {j: set() for j in X}
    for i, row in Y.items():
        for j in row:
            X[j].add(i)
    return X, Y


def solve(X, Y, solution):
    if not X:
        yield list(solution)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for r in list(X[c]):
            solution.append(r)
            cols = select(X, Y, r)
            for s in solve(X, Y, solution):
                yield s
            deselect(X, Y, r, cols)
            solution.pop()


def select(X, Y, r):
    cols = []
    for j in Y[r]:
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].remove(i)
        cols.append(X.pop(j))
    return cols


def deselect(X, Y, r, cols):
    for j in reversed(Y[r]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)


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
print("\nSudoku original:\n")
for elem in sudoku1.get_nums_filas():
    print("   ", elem)
print("\nSudoku Solucionado:")
for solution in solve_sudoku((3, 3), sudoku1.get_nums_filas()):
    print("", *solution, sep='\n    ')

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
print("\nSudoku original:\n")
for elem in sudoku2.get_nums_filas():
    print("   ", elem)

print("\nSudoku Solucionado:")
for solution in solve_sudoku((3, 3), sudoku2.get_nums_filas()):
    print("", *solution, sep='\n    ')
