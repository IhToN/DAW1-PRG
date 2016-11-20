"""
    Proyecto Personal - Vamos a hacer un generador de Sudokus intentando usar el algoritmo de Donald Knuth - Algorithm X
            https://en.wikipedia.org/wiki/Dancing_Links
            http://es.slideshare.net/ljsking/dancing-links-11376810
"""
from itertools import product


def solve_sudoku(tamanyo, grid):
    """ Solucionar el Grid, devuelve un Generator con las soluciones
        Tamanyo = (#reg x, #reg y)
        Grid = Lista de listas de numeros
    """

    fila, columna = tamanyo
    num_regiones = fila * columna

    # X e Y serán nuestros "double-linked lists", para recorrer de forma más rápida tanto filas como columnas.
    X = ([("fc", fc) for fc in product(range(num_regiones), range(num_regiones))] +
         [("fn", fn) for fn in product(range(num_regiones), range(1, num_regiones + 1))] +
         [("cn", cn) for cn in product(range(num_regiones), range(1, num_regiones + 1))] +
         [("bn", bn) for bn in product(range(num_regiones), range(1, num_regiones + 1))])
    Y = dict()
    for f, c, n in product(range(num_regiones), range(num_regiones), range(1, num_regiones + 1)):
        b = (f // fila) * fila + (c // columna)  # Box number
        Y[(f, c, n)] = [
            ("fc", (f, c)),
            ("fn", (f, n)),
            ("cn", (c, n)),
            ("bn", (b, n))]
    X, Y = exact_cover(X, Y)
    for i, fila in enumerate(grid):
        for j, n in enumerate(fila):
            if n:
                select(X, Y, (i, j, n))
    for solucion in solve(X, Y, []):
        for (f, c, n) in solucion:
            grid[f][c] = n
        yield grid


def exact_cover(X, Y):
    X = {j: set() for j in X}
    for i, row in Y.items():
        for j in row:
            X[j].add(i)
    return X, Y


def solve(X, Y, solucion):
    if not X:
        yield list(solucion)
    else:
        c = min(X, key=lambda c: len(X[c]))
        for row in list(X[c]):
            solucion.append(row)
            cols = select(X, Y, row)
            for sol in solve(X, Y, solucion):
                yield sol
            deselect(X, Y, row, cols)
            solucion.pop()


def select(X, Y, row):
    try:
        cols = []
        for j in Y[row]:
            for i in X[j]:
                for k in Y[i]:
                    if k != j:
                        X[k].remove(i)
            cols.append(X.pop(j))
        return cols
    except KeyError:
        print('¡El sudoku no tiene solución!')


def deselect(X, Y, row, cols):
    for j in reversed(Y[row]):
        X[j] = cols.pop()
        for i in X[j]:
            for k in Y[i]:
                if k != j:
                    X[k].add(i)
