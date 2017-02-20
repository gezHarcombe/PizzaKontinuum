import matplotlib.pyplot as plt
import numpy as np
from funcs import count_tomatoes, count_mushrooms
from data import L

def ratio(arr):
""" Function takes a slice and returns ratio of the rarer ingredient to 
    the more abundant ingredient

    Eg. If the array contains 5 tomatoes and 3 mushrooms, will return 3/5
    If 2 tomatoes and 7 mushrooms, will return 2/7

    Input argument is an array, output is a float
"""
    toms = count_tomatoes(arr)
    mush = count_mushrooms(arr)

    if(toms > mush):
        returnval = mush/toms
    elif(mush > toms):
        returnval = toms/mush
    else:
        returnval = 1.0

    return returnval


def is_too_small(arr):
""" Determine if a slice is too small, so that recursive searching can be
    terminated

    The pizza is deemed too small if there are either too few tomatoes or too
    few mushrooms

    Function returns True if the pizza is too small, and False otherwise
"""
    if count_tomatoes(arr) < L:
        return True
    elif count_mushrooms(arr) < L:
        return True
    else:
        return False
