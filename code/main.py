import numpy as np
from data import R, C, L, H, A
from knut import divide 

pizza = A.copy()
pos = [0,0,R-1,C-1]
slices = []
divide(pizza, pos, slices)

print(len(slices))
for s in slices: 
    print(s[0], s[1], s[2], s[3])
