"""
    Escribir un programa en la cual al usuario se le pida dos números, siendo estos
    el primero el número del que quiere saber la tabla de multiplicar y el segundo
    cuántos valores de dicha tabla quiere.
    La salida ha de ser del tipo "7*1=7"
"""

print('Y first multiples of X')
count = 1
num = int(input('Introduce el número a calcular: '))
cant = int(input('Indica el total de cálculos: '))
while count <= cant:
    print(num, '*', count, ' = ', (num * count))  # 2*3 = 6
    count += 1
print('Those are the first', cant, 'multiples of', num)
