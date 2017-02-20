import numpy as np
from data import L, H


def count_tomatoes(arr):
    return np.sum(arr)

def count_mushrooms(arr):
    return np.size(arr) - count_tomatoes(arr)

def is_valid(arr):

    if count_tomatoes(arr) < L:
        return False

    if count_mushrooms(arr) < L:
        return False

    if np.size(arr) > H:
        return False

    return True
