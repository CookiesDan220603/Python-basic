import numpy as np
from sympy import *
x1 = symbols('x1')
A=np.array([[0,-1,0],[2,-3,-1],[0,0,-2]])
B=np.array([[-3*x1],[0],[-8*x1]])
root=np.linalg.inv(A)@B
print("(x2,x3,x4) = ({},{},{})".format(root[0],root[1],root[2]))
