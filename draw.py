import matplotlib.pyplot as plt
import numpy as np
from funcs import read_pizza

R, C, L, H, A = read_pizza('medium.in')

plt.imshow(A,interpolation='nearest')
plt.grid()
plt.show()
