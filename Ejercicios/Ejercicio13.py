"""
    El usuario introduce una serie indefinida de números hasta que se introduzca un cero. El programa ha de imprimir
    cuántos números se han introducido, la suma de todos los números, cuántos de esos números son múltiplos de dos,
    cuántos son múltiplos de tres y cuántos son múltiplos de dos y de tres.
"""

# Inicializamos las variables
promptMsg = 'Introduce a number:\n'
totalTwo = 0
totalThree = 0
totalBoth = 0
totalSum = 0
totalCount = 0

inNum = float(input(promptMsg))

# Usamos el loop para preguntar cuantos números queremos, usamos float para admitir decimales
while inNum != 0:
    # Solución A
    """
    if inNum % 2 == 0:  # Comprobamos los múltiplos de dos
        totalTwo += 1
    if inNum % 3 == 0:  # Comprobamos los múltiplos de tres
        totalThree += 1
    if inNum % 2 == 0 and inNum % 3 == 0:  # Comprobamos los múltiplos de los dos
        totalBoth += 1
    """
    # Solución B
    if inNum % 2 == 0:  # Comprobamos los múltiplos de dos
        totalTwo += 1
        if inNum % 3 == 0:  # Comprobamos los múltiplos de tres
            totalBoth += 1
    if inNum % 3 == 0:  # Comprobamos los múltiplos de tres
        totalThree += 1

    totalSum += inNum  # Sumamos el número al total
    totalCount += 1  # Aumentamos en un el total de cuentas
    inNum = float(input(promptMsg))

print('Total numbers: \n', totalCount)
print('Total sum: \n', totalSum)
print('Multiples of Two: \n', int(totalTwo))
print('Multiples of Three: \n', int(totalThree))
print('Multiples of Two & Three: \n', int(totalBoth))

"""
    Solución usando Listas, así mostramos los números en sí y no las cantidades


# Inicializamos las variables
promptMsg = 'Introduce a number:\n'
repeat = True
numList = []

# Usamos el loop para preguntar cuantos números queremos, usamos float para admitir decimales
while repeat:
    inNum = float(input(promptMsg))
    if inNum == 0:
        repeat = False
    else:
        numList.append(inNum)

# Inicializamos las listas a devolver
twoNum = []
threeNum = []
bothNum = []
sumNum = 0

# Tratamos cada elemento de la lista total de números
for num in numList:
    if num % 2 == 0:  # Comprobamos los múltiplos de dos
        twoNum.append(num)
    if num % 3 == 0:  # Comprobamos los múltiplos de tres
        threeNum.append(num)
    if num % 2 == 0 and num % 3 == 0:  # Comprobamos los múltiplos de los dos
        bothNum.append(num)
    sumNum += num  # Sumamos el número al total

# Imprimimos los números pedidos
print('Total numbers: \n', len(numList))
print('Total sum: \n', sumNum)
print('Multiples of Two: \n', twoNum)
print('Multiples of Three: \n', threeNum)
print('Multiples of Two & Three: \n', bothNum)
"""
