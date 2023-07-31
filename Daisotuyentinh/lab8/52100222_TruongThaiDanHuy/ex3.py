import numpy as np

#Ex3
# y = a0 + a1x
A = np.array([[1,1],
              [1,1],
              [1,2],
              [1,3]])
b = np.array([1,1,2,2])
w = np.linalg.inv(A.T@A)@A.T@b.T
print(w)
print("------------------------")
A = np.array([[1,1],
              [1,2],
              [1,4],
              [1,5]])
b = np.array([0,1,2,3])
w = np.linalg.inv(A.T@A)@A.T@b.T
print(w)
print("------------------------")
A = np.array([[1,-1],
              [1,0],
              [1,1],
              [1,2]])
b = np.array([0,1,2,4])
w = np.linalg.inv(A.T@A)@A.T@b.T
print(w)
print("------------------------")
A = np.array([[1,2],
              [1,3],
              [1,5],
              [1,6]])
b = np.array([3,2,1,0])
w = np.linalg.inv(A.T@A)@A.T@b.T
print(w)
print("------------------------")

