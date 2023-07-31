import numpy as np
from sympy import * 

#a) 
A=np.array([[1,2,1],[2,-1,1],[2,1,0]])
B=np.array([[0],[0],[0]])
root = np.linalg.solve(A,B)
root1= np.linalg.inv(A)@B
print("(a) (x,y,z) = ({},{},{})".format(root[0],root[1],root[2]))
#print(root1)
##option 2: LU
M=Matrix([[1,2,1,0],[2,-1,1,0],[2,1,0,0]])
Mr,pivot = M.rref()
print(Mr)

#b)
C=np.array([[2,1,1,1],[1,2,1,1],[1,1,2,2],[1,1,1,2]])
D=np.array([[1],[1],[1],[1]])
root = np.linalg.solve(C,D)
print("(b) (x,y,z,t) = ({},{},{},{})".format(root[0],root[1],root[2],root[3]))
M=Matrix([[2,1,1,1,1],[1,2,1,1,1],[1,1,2,2,1],[1,1,1,2,1]])
Mr,pivot = M.rref()
print(Mr)