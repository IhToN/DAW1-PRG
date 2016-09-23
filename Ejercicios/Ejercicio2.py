"""
    Escribir un programa que pida un número al usuario
    y el programa imprima los 100 primeros múltiplos de ese número.
"""

print('100 first multiples of X')
count = 1
num = int(input('Introduce a number: '))
while count <= 100:
    # Solución a
    # print(count, ' ', num*count)

    # Solución b
    print(num, '*', count, ' = ', (num * count))  # 2*3 = 6
    count += 1  # El puñetero Python no tiene x++ ni x--
print('Those are the first 100 multiples of', num)
