import numpy as np
A = np.array([[2,2],[2,3]])
b = np.array([4,6])
w = np.linalg.inv(A.T@A)@A.T@b
print(w)