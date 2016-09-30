"""
    El usuario introduce una serie indefinida de números hasta que se introduzca un cero. El programa ha de imprimir
    cuántos números se han introducido, la suma de todos los números, cuántos de esos números son múltiplos de dos,
    cuántos son múltiplos de tres y cuántos son múltiplos de dos y de tres.
"""

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
parNum = []
threeNum = []
bothNum = []
sumNum = 0

# Tratamos cada elemento de la lista total de números
for num in numList:
    if num % 2 == 0:  # Comprobamos los múltiplos de dos
        parNum.append(num)
    if num % 3 == 0:  # Comprobamos los múltiplos de tres
        threeNum.append(num)
    if num % 2 == 0 and num % 3 == 0:  # Comprobamos los múltiplos de los dos
        bothNum.append(num)
    sumNum += num  # Sumamos el número al total

# Imprimimos los números pedidos
print('Total numbers: \n', len(numList))
print('Total sum: \n', sumNum)
print('Multiples of Two: \n', parNum)
print('Multiples of Three: \n', threeNum)
print('Multiples of Two & Three: \n', bothNum)
