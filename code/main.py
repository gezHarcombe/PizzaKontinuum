import numpy as np
from funcs import *

R, C, L, H, A = read_pizza('../pizzas/example.in')

print(A)
B = remove_slice_copy(A,[0,1],[0,1])
print(B)
print(count_tomatoes(A))
print(count_tomatoes(B))
