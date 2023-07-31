import numpy as np
# I = np.eye(5)
# I = I*3
# np.random.seed(1)
# B =np.random.randint(-3,5 ,size=(5,5))
# print(B)
# print(I)
# print(B + I)
A = np.array([[1,0,1],[1,-1,1]])
B = np.array([[1,0,1],[2,1,0]])
B2 = np.transpose(B)
C = np.dot(A,B2)
C = A@B.T
# D = A*B.T
print(C)
# print(D)
# Det |A|
# det_A = np.linalg.det(A)
# #Inverse A
# inv_A = np.linalg.inv(A)
