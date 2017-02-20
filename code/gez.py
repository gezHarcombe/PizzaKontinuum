import matplotlib.pyplot as plt
import numpy as np
from funcs import count_tomatoes, count_mushrooms
from data import L

class Pos:
    """ position data struction - r1, c1, r2, c2
        Usage:
        test = pos(0,0,1,2)
        a = test.r1
    """
    def __init__(self, r1a, c1a, r2a, c2a):
        self.r1 = r1a
        self.c1 = c1a
        self.r2 = r2a
        self.c2 = c2a

    def write(self):
        print(self.r1,self.c1,self.r2,self.c2)

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
