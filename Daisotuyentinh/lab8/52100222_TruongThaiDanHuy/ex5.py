import numpy as np
from math import *
def solve(A,b):
    return np.linalg.solve(A.T@A,A.T@b)
A=np.array([[cos(1),sin(1)],
            [cos(2),sin(2)],
            [cos(3),sin(3)]
])
b=np.array([[7.9],[5.4],[-9]])
print(solve(A,b))