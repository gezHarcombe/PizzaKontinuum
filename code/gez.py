import matplotlib.pyplot as plt
import numpy as np
from funcs import count_tomatoes, count_mushrooms, read_pizza

""" Function takes a slice and returns ratio of the rarer ingredient to 
    the more abundant ingredient

    Eg. If the array contains 5 tomatoes and 3 mushrooms, will return 3/5
    If 2 tomatoes and 7 mushrooms, will return 2/7

    Input argument is an array, output is a float
"""

def ratio(arr):
    toms = count_tomatoes(arr)
    mush = count_mushrooms(arr)
        
    if(toms > mush):
        returnval = mush/toms
    elif(mush > toms):
        returnval = toms/mush
    else:
        returnval = 1.0

    return returnval

""" Determine if a slice is too small, so that recursive searching can be
    terminated
        
    The pizza is deemed too small if there are either too few tomatoes or too
    few mushrooms

    Function returns True if the pizza is too small, and False otherwise
"""

def is_too_small(arr):
        
    if count_tomatoes(arr) < L:
        return True
    elif count_mushrooms(arr) < L:
        return True
    else:
        return False


""" TEST CASE FOR ratio(arr)

print(ratio(A)) """

""" TEST CASE FOR is_too_small(arr)

print(is_too_small(A))

small_slice = np.array([0, 0, 1])
print(is_too_small(small_slice));

"""
