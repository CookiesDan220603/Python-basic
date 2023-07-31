import numpy as np
x = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5,6])
c = np.arange(1,31)
d = np.arange(1,26)
A = np.repeat(x,5,axis=0)
A = A.reshape(5,5)
print(A)
B = np.repeat(b,6,axis=0)
B = (B.reshape(6,6)).T
print(B)
C = ((np.array(c)).reshape(6,5)).T
print(C)
D = (np.array(d)).reshape(5,5)
print(D)
