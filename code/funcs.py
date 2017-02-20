import numpy as np

def read_pizza(filename):

    f = open(filename, 'r')

    info = f.readline().split()
    R = int(info[0])
    C = int(info[1])
    L = int(info[2])
    H = int(info[3])

    A = np.empty((R, C), dtype=int)
    for i in range(R):
        row = f.readline()
        for j in range(C):
            if row[j] == 'T':
                A[i,j] = 1
            else:
                A[i,j] = 0
    f.close()

    return R, C, L, H, A

def count_tomatoes(arr):
    return sum(arr)

def count_mushrooms(arr):
    return arr.size - sum(arr)

def is_valid(arr, L, H):

    if count_tomatoes(arr) < L:
        return False

    if count_mushrooms(arr) < L:
        return False

    if np.size(arr) > H:
        return False

    return True
