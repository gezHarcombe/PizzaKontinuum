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
                A[i,j] = 2
    f.close()

    return R, C, L, H, A

def remove_slice( pizza, rows, cols):
    result = np.copy(pizza)
    result[ rows[0]:rows[1], cols[0]:cols[1]] = 0
    return result
