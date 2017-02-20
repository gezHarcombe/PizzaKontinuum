import numpy as np
import sys
from data import R, C

pizza = str(sys.argv[1])
filename = pizza + '.out'
data = np.loadtxt(filename, skiprows=1)
score = np.sum((data[:,2]+1-data[:,0]) * (data[:,3]+1-data[:,1]))
print(score / (R * C))

