"""
    Escribir un programa que lea una serie de números y los imprima en orden inverso,
    dándonos también su media aritmética.
"""

promptMsg = 'Introduce a number:\n'
origList = []
invList = []
totalSum = 0

inNum = float(input(promptMsg))

while inNum != 0:
    origList.append(inNum)  # Agregar el elemento a la lista
    totalSum += inNum
    inNum = float(input(promptMsg))

print('Original list: \n', origList)
print('Inverted list: \n', origList[::-1])  # Cosita graciosa que tiene Python para ahorrarnos hacer un for a la lista
print('Arithmetic average: \n', totalSum / len(origList))
