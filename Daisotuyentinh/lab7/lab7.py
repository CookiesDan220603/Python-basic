import numpy as np
u1=np.array([3,1,1])
u2=np.array([-1,2,1])
u3=np.array([-1/2,2,7/2])
if sum(u1*u2)==0:
  print("orthogonal set")
else:
  print("No")
if sum(u1*u3)==0:
  print("orthogonal set")
else:
  print("No")
if sum(u2*u3)==0:
  print("orthogonal set")
else:
  print("No")



#Ex2
y=np.array([3,1,1])
u=np.array([-1,2,1])
proj=(sum(y*u)/(sum(u*u)))*u
print(proj)

#ex3
l_m = np.array([[-1/2 , 2 , 7/2] , [3 , 1, 1] , [-1  ,2  , 1]])

def Ex3(x):
    u = np.linalg.matrix_rank(x)
    g = np.eye(u)
    x = x.T * x
    if(x.all() == g.all()):
        print("orth colums")
    else:
        print("not orth colums")
        
g = np.eye(3)
Ex3(l_m)

#ex4
def orthogonalProjection(y, u):
  if np.sum(u * u) == 0:
    return None
  return np.sum(y * u) / np.sum(u * u) * u
x = np.array([[-10, 13, 7, -11],
              [2, 1, -5, 3],
              [-6, 3, 13, -3],
              [16, -16, -2, 5],
              [2, 1, -5, -7]])
print(x)
print()
x = x.T
v = []
v.append(x[0])
for i in range(1, len(x)):
  v.append(x[i])
  for j in range(i):
    v[i] = v[i] - orthogonalProjection(x[i], x[j])
for i in range(1, len(x)):
  v.append(x[i])
  for j in range(i):
    v[i] = v[i] - orthogonalProjection(x[i], x[j])
print(np.array(v).T)

#Ex5
from sympy import*
A=Matrix(np.array([[1,2,3],[3,2,1],[1,1,1]]))
C,pivot=Matrix.rref(A)
print(np.array(C))
print(pivot)

#Ex6
#a
v1=np.array([1,2,3,4])
v2=np.array([-1,0,1,3])
v3=np.array([0,5,-6,8])
w=np.array([3,-6,17,11])
v=np.array(np.vstack((v1,v2,v3)))
p=np.array(np.vstack((v1,v2,v3,w)))
if np.linalg.matrix_rank(v)==np.linalg.matrix_rank(p):
  print("OK")
else:
  print("None")
#b
v1=np.array([1,1,2,2])
v2=np.array([2,3,5,6])
v3=np.array([2,-1,3,6])
w=np.array([0,5,3,0])
v=np.array(np.vstack((v1,v2,v3)))
p=np.array(np.vstack((v1,v2,v3,w)))
if np.linalg.matrix_rank(v)==np.linalg.matrix_rank(p):
  print("OK")
else:
  print("None")  
#c
v1=np.array([1,1,2,2])
v2=np.array([2,3,5,6])
v3=np.array([2,-1,3,6])
w=np.array([-1,6,1,-4])
v=np.array(np.vstack((v1,v2,v3)))
p=np.array(np.vstack((v1,v2,v3,w)))
if np.linalg.matrix_rank(v)==np.linalg.matrix_rank(p):
  print("OK")
else:
  print("None")  
#d
v1=np.array([1,2,3,4])
v2=np.array([-1,0,1,3])
v3=np.array([0,5,-6,8])
v4=np.array([1,15,-12,8])
w=np.array([3,-6,17,11])
v=np.array(np.vstack((v1,v2,v3,v4)))
p=np.array(np.vstack((v1,v2,v3,v4,w)))
if np.linalg.matrix_rank(v)==np.linalg.matrix_rank(p):
  print("OK")
else:
  print("None")