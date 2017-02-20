import numpy as np
from funcs import *
from splitting import *

R, C, L, H, A = read_pizza('../pizzas/example.in')

print(A)
B = remove_slice_copy(A,[0,1],[0,1])
print(B)
print(count_tomatoes(A))
print(count_tomatoes(B))

L,R,L_pos,R_pos = slice(A, [[0,0],[2,4]] ,1)
print(L)
print(R)
print(L_pos)
print(R_pos)
