import matplotlib.pyplot as plt
import numpy as np
from funcs import count_tomatoes, count_mushrooms, read_pizza

""" Function takes a slice and returns ratio of the rarer ingredient to 
    the more abundant ingredient

    Eg. If the array contains 5 tomatoes and 3 mushrooms, will return 3/5
    If 2 tomatoes and 7 mushrooms, will return 2/7

    Input argument is an array, output is a float
"""

def ratio(A):
    toms = count_tomatoes(A)
    mush = count_mushrooms(A)
    
    print('toms = ', toms)
    print('mush = ', mush)
        
    if(toms > mush):
        returnval = mush/toms
    elif(mush > toms):
        returnval = toms/mush
    else:
        returnval = 1.0

    return returnval

""" TEST CASE """
R,C,L,H,A = read_pizza('../pizzas/big.in')

print(ratio(A))
plt.imshow(A,interpolation='nearest')
plt.grid()
plt.show()



