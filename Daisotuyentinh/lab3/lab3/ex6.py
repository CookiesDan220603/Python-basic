import numpy as np
A = np.array([[2,4,1],[6,7,2],[3,5,9]])
print(A)
X1 = np.array(A[0,::])
print(X1)
print("***********")
Y = np.array(A[-2:,::])
print(Y)
