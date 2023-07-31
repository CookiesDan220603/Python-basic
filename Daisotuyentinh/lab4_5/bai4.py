import numpy as np
A=np.array([[1,1,2],[3,6,-5],[2,4,-3]])
B=np.array([[1],[-1],[0]])
#a) 
detA=np.linalg.det(A)
print("(a) Determinant of A: {}".format(detA))
if (detA!=0):
	print("(a) Invertible")
else:
	print("(a) Not invertible")
C=np.linalg.inv(A)
root = np.dot(C,B)
x=float(root[0])
y=float(root[1])
z=float(root[2])
print("(b) (x,y,z) = ({},{},{})".format(x,y,z))