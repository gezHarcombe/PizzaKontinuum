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

R,C,L,H,A = read_pizza('../pizzas/example.in')

""" 
    At the top of your file, write:
    from data import R,C,L,H
"""
