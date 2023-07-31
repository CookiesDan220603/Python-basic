import numpy as np
A = np.array([[2,7,9,7],[3,1,5,6],[8,1,2,5]])
print(A)
print("*****************")
B = np.array(A[:,::2])
print(B)
print("*****************")
C = np.array(A[1::2,:])
print(C)
AT2 = A.T
print(AT2)