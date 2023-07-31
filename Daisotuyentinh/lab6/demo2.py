import numpy as np
A = np.array([[-1,1,0],[-2,1,3],[1,-1,0]])
##L1
##option 1
print(np.linalg.norm(A,1))
print(A)
print(max(sum(abs(A))))
print("--------------")
##L2
##option 1
print(np.linalg.norm(A,'fro'))
##option 2
print(np.sqrt(np.sum(A**2)))
print("-----------------")
##Loo
##option 1
print(np.linalg.norm(A,np.inf))
##option 2
print(max(sum(abs(A.T))))
print(max(np.sum(abs(A),axis=1)))