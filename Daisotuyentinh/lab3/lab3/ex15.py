import numpy as np
A = np.array([[2,4,5/2],[-3/4,2,1/4],[1/4,1/2,2]])
B = np.array([[1,-1/2,3/4],[3/2,1/2,-2],[1/4,1,1/2]])
# print(A)
# print(B)
#a
print((np.linalg.inv(A))*(np.linalg.inv(B)))
print("*****************")
print(np.linalg.inv(A*B))
print("*****************")
print(np.linalg.inv(B*A))
print("-------------------------------")
#b
print((np.linalg.inv(A)).T)
print("*****************")
print(np.linalg.inv(A.T))

