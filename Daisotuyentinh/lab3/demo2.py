import numpy as np
x = np.arange(1,6)
P = np.repeat(x,5,axis=0)
P = P.reshape(5,5)
#Ex3 
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.flip(A,axis=1))
# print(np.fliplr(A))
# print(A[:,::-1])
#Ex4
B = np.flip(A,axis=0)
# print(B)
# print(A[::-1,:])
#Ex5
Y = np.array([[1,2,16,31,22],[2,8,12,21,23],[4,9,11,14,25],[3,6,10,16,34]])
# print(np.sum(np.diag(Y)))
# print(np.trace(Y))
# K = np.diag(Y)
# print(len(K[K%2==0]))
F = Y
F[0,:] = -1
F[-1:,:] = -1
F[:,0] = -1
F[:,-1:] = -1
J = Y
J[[0,-1],:] = 0
J[:,[0,-1]] = 0
# print(J)
print(F)
