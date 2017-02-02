"""
    Hacer tres funciones llamándola en tres niveles y a capturar errores de la función
    más pequeñita en errores superiores.
"""


def func1():
    try:
        func2()
    except:
        print("Error desconocido")


def func2():
    try:
        func3()
    except ZeroDivisionError as error:
        print("No se puede dividir entre cero")
        func2()


def func3():
    try:
        res = 500 / int(input("Dame un numerito\n"))
    except ValueError as error:
        print("Eso no es un numerito")
    else:
        print(res)


func1()
