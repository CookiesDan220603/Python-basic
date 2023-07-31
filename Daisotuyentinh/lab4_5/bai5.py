import numpy as np
from sympy import *
A=np.array([[1,2,1],[2,2,2],[2,4,1]])
B=np.array([[1],[1],[2]])
#option1
root1=np.linalg.solve(A,B)
x=float(root1[0])
y=float(root1[1])
z=float(root1[2])
print("option1: (x,y,z) = ({},{},{})".format(x,y,z))
#option2
root2=np.dot(np.linalg.inv(A),B)
x=float(root2[0])
y=float(root2[1])
z=float(root2[2])
print("option2: (x,y,z) = ({},{},{})".format(x,y,z))
#option3
M=Matrix([[1,2,1,1],[2,2,2,1],[2,4,1,2]])
Mr,pivot = M.rref()
root3 = np.array(Mr)[:,3]
x=float(root3[0])
y=float(root3[1])
z=float(root3[2])
print("option3: (x,y,z) = ({},{},{})".format(x,y,z))