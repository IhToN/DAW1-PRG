"""
    Dada una lista, queremos insertar detrás de cada elemento de dicha lista,
    el mismo elemento que estamos recorriendo.
    [1, 2, 3, 4] -> [1, 1, 2, 2, 3, 3, 4, 4]
"""


def duplicList(list1):
    """
    Duplica los elementos de una lista en su posición correspondiente
    :param list1:
    :return:
    """
    idx = 0
    for elem in list1.copy():
        list1.insert(idx, elem)
        idx += 2


testList = [1, 4, 3, 4]
duplicList(testList)
print(testList)
