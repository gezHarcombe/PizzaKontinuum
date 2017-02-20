import numpy as np

def read_pizza(filename):

    f = open(filename, 'r')

    info = f.readline().split()
    R = int(info[0])
    C = int(info[1])
    L = int(info[2])
    H = int(info[3])

    A = np.empty((R, C), dtype=float)
    for i in range(R):
        row = f.readline()
        for j in range(C):
            if row[j] == 'T':
                A[i,j] = 1.0
            else:
                A[i,j] = 0.0
    f.close()

    return R, C, L, H, A

def remove_slice_copy( pizza, rows, cols):
    result = np.copy(pizza)
    result[ rows[0]:rows[1]+1, cols[0]:cols[1]+1 ]= -1e-50
    return result

def remove_slice(pizza,rows,cols):
    pizza[ rows[0]:rows[1]+1, cols[0]:cols[1]+1 ]= -1e-50
    return result

def count_tomatoes(arr):
    return np.sum(arr)

def count_mushrooms(arr):
    return arr.size - count_tomatoes(arr)

def is_valid(arr, L, H):

    if count_tomatoes(arr) < L:
        return False

    if count_mushrooms(arr) < L:
        return False

    if np.size(arr) > H:
        return False

    return True
