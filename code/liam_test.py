import numpy as np
from funcs import *
from liam import *

R, C, L, H, A = read_pizza('../pizzas/example.in')

print("remove slice, count, etc:")
print(A)
B = remove_slice_copy(A,[0,1],[0,1])
print(B)
print(count_tomatoes(A))
print(count_tomatoes(B))

print("row slice:")
L,R,L_pos,R_pos = slice_pizza(A, [[0,0],[2,4]] ,1)
print("L: ", L)
print("R: ", R)
print("L_pos: ", L_pos)
print("R_pos: ", R_pos)

print("col slice:")
L,R,L_pos,R_pos = slice_pizza(A, [[0,0],[2,4]] ,1, is_rows=False)
print("L: ", L)
print("R: ", R)
print("L_pos: ", L_pos)
print("R_pos: ", R_pos)
