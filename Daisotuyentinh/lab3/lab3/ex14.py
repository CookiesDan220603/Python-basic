import numpy as np
I = np.eye(5)
I = I*3
np.random.seed(1)
A =np.random.randint(-3,5 ,size=(5,5))
B =np.random.randint(-3,5 ,size=(5,5))
# print(A)
# print(B)
C = np.linalg.det(A*B)
D = (np.linalg.det(A)) * (np.linalg.det(B))
print(C)
print(D)
if (C == D):
    print("Det(AB) = Det(A).Det(B)")
else:
    print("Det(AB) # Det(A).Det(B)")

