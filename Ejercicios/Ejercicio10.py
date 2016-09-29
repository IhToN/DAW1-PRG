"""
    El usuario introduce dos números. El programa produce una serie de múltiplos del
    primer número de longitud al segundo. Ejemplo: 3,10 => 3, 6, 9, …. 30
"""
# Número a comprobar
x = int(input('Of which number do you want to check its multiples?\n'))
# Cuántos múltiplos vamos a ver
y = int(input('How many multiples do you want to see?\n'))

for i in range(x, x*y + 1, x):
    print(i)
