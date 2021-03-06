import numpy as np
from data import R, C, L, H, A
from gez import Pos
from knut import divide 

pizza = A.copy()
init_pos = Pos(0, 0, R-1, C-1)
slices = divide(pizza, init_pos)

print(len(slices))
for s in slices: 
    s.write()
