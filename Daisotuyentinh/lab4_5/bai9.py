import numpy as np
from sympy import *
X=symbols('X')
Y=symbols('Y')
Z=symbols('Z')
A=np.array([[0.61,0.29,0.15],[0.35,0.59,0.063],[0.04,0.12,0.787]])
B=np.array([[X],[Y],[Z]])
root = np.linalg.inv(A)@B
print("(R,G,B)=({},{},{})".format(root[0],root[1],root[2]))