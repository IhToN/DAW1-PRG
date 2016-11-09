"""
    Comprobar las Leyes de Demorgan
        a. not (AUB) = not A or not B
        b. not(AorB) = not A and not B
"""
A, B = {1, 2, 3}, {2, 3, 4}
Universal = {x for x in range(100)}

aleft = Universal - (A | B)
aright = Universal - A & Universal - B
print('Primera ley de Demorgan: ', aleft == aright)

bleft = Universal - (A & B)
bright = Universal - A | Universal - B
print('Segunda ley de Demorgan: ', bleft == bright)
