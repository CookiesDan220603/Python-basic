import numpy as np
from sympy import *
t=symbols('t')
A=np.array([[2,-4,4],[0,-2,2],[2,-2,0]])
B=np.array([[3.86-0.077*t],[-3.47+0.056*t],[0]])
root=np.linalg.inv(A)@B
print("(x,y,z)= ({},{},{})".format(root[0],root[1],root[2]))