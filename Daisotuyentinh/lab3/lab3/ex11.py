import numpy as np

A = np.array([[2,4,1],[6,7,2],[3,5,9]])
print(A)
print("*****************")
print(A.shape)
C = (A.shape)[0]
D = (A.shape)[1]
print(C)
print(D)
if (C == D):
    print("The magic is square")
else:
    print("The magic is not square")
print("*****************")
check = A.T
if (check.all == A.all):
    print("The magic is a matrix symmertric")
else:
    print("The magic is not a maxtrix symmertric")
print("*****************")
check = -A.T
if (check.all == A.all):
    print("The magic is a matrix skew-symmertric")
else:
    print("The magic is not a maxtrix skew-symmertric")
print("*****************")
print("Upper")
print(np.triu(A,k=1))
print("*****************")
print("Lower")
print(np.tril(A,k=-1))



