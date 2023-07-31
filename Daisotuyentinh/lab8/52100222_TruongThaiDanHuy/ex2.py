import numpy as np
A = np.array([[0,0,1],
              [0,1,1],
              [1,2,1],
              [1,0,1],
              [4,1,1],
              [4,2,1]])
b = np.array([0.5,1.6,2.8,0.8,5.1,5.9])
w = np.linalg.inv(A.T@A)@A.T@b.T
print(w)