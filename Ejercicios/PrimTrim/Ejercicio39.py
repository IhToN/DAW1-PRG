"""
    Definir los siguientes conjuntos (profesores de Bilingüe, FOL e Informática):
        B = {'Ramón', 'Paco', 'Tessa'}
        F = {'José Manuel'}
        I = {'Paco', 'Belén', 'Blas', 'Manolo', 'Jose', 'Paqui', 'Ramón'}
        Definir dos más que sean Profesores y Profesoras.
    A través de operaciones con conjuntos obtener
        a. Todos los profesores NO Bilingües
        b. Profesores que sean de informática O de FOL
        c. Todos los profesores (que no profesoras) que NO sean de Bilingüe
        d. Todas las profesoras Bilingües
        e. Todos los profesores de Bilingüe o Informática, pero no incluídos
        f. Todos los profesores que NO sean Bilingües NI de FOL NI Mujeres
"""

B = {'Ramón', 'Paco', 'Tessa'}
F = {'José Manuel'}
I = {'Paco', 'Belén', 'Blas', 'Manolo', 'Jose', 'Paqui', 'Ramón'}

H = {'Ramón', 'Paco', 'Jose Manuel', 'Blas', 'Manolo', 'Jose'}
M = {'Tessa', 'Belén', 'Paqui'}

a = F | I - B
b = F | B
c = H - B
d = M & B
e = B ^ I
f = H - B - F

print("Apartado a", a)
print("Apartado b", b)
print("Apartado c", c)
print("Apartado d", d)
print("Apartado e", e)
print("Apartado f", f)
