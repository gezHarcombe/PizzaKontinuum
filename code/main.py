import numpy as np
from data import R, C, L, H, A
from knut import divide 

pizza = A.copy()
pos = [[0,0],[R,C]]
slices = []
divide(pizza, pos, slices)

for s in slices: 
    print(s)
