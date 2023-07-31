import numpy as np
A = np.array([[-1,4,8],[-9,1,2]])
B = np.array([[5,8],[0,-6],[5,6]])
C = np.array([[-4,1],[6,5]])
D = np.array([[-6,3,1],[8,9,-2],[6,-1,5]])
# print(A)
# print(B)
# print(C)
# print(D)
a = A*B.T
print(a)
print("*****************")
# b = (B*C).T
# print(b)
# print("*****************")
c = C - C.T
print(c)
print("*****************")
d = D - D.T
print(d)
print("*****************")
e = (D.T).T
print(e)
print("*****************")
f = 2*(C.T)
print(f)
print("*****************")
g = A.T + B
print(g)
print("*****************")
h = (A.T + B).T
print(h)
print("*****************")
i = (2*A.T - 5*B).T
print(i)
print("*****************")
j = (-D).T 
print(j)
print("*****************")
k = -(D.T)
print(k)
print("*****************")
l = (C*C).T
print(l)
print("*****************")
m = (C.T)*(C.T)
print(m)
