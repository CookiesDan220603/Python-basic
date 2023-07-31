import numpy as np
import sympy as sp
from sympy import *
import matplotlib.pyplot as plt
#cau1lap10
def Eigenvalues(Matrix):
    eigenvalues = np.linalg.eigvals(Matrix)
    return eigenvalues

def Determinant(Matrix):
    eigenvalues = Eigenvalues(Matrix)
    det = 1
    for i in range(len(eigenvalues)):
        det *= eigenvalues[i]
    return det

A=np.array([[-1, 3.5, 14],
            [0, 5,-26],
            [0,0,2]])
B=np.array([[-2, 0, 0],
            [99, 0, 0],
            [10,-4.5,10]])
print("Eigenvalues of A:",Eigenvalues(A))
print("Det(A):",Determinant(A))
print("Eigenvalues of B:",Eigenvalues(B))
print("Det(B):",Determinant(B))
A=np.array([[5, 5, 0, 2],
            [0, 2, -3, 6],
            [0,0,3,-2],
            [0,0,0,5]])
B=np.array([[3, 0, 0, 0],
            [6, 2, 0, 0],
            [0, 3, 6, 0],
            [2,3,3,-5]])
C=np.array([[3, 0, 0 ,0, 0],
            [-5, 1, 0, 0, 0],
            [3, 8, 0, 0, 0],
            [0, -7, 2, 1, 0],
            [-4, 1, 9, -2, 3]])
print('cau1 lap10')
print("Eigenvalues of A:",Eigenvalues(A))
print("Det(A):",Determinant(A))
print("Eigenvalues of B:",Eigenvalues(B))
print("Det(B):",Determinant(B))
print("Eigenvalues of C:",Eigenvalues(C))
print("Det(C):",Determinant(C))

#cau2lap10
x,y=symbols('x,y')
def ma_tran_con(mt, i, j):
    mtc = mt.copy()
    mtc = np.delete(mtc, i, 0);
    mtc = np.delete(mtc, j, 1); 
    return mtc

def dinh_thuc(mt):
    so_chieu = mt.shape[1]
    if so_chieu == 1==mt.shape[0]:
        return mt[0][0]
    elif mt.shape[0] != so_chieu:
        return None
    
    ket_qua = 0
    j = 0
    for i in range(so_chieu):
        pds = ma_tran_con(mt, 0, j)
        ket_qua += ((-1) ** j) * mt[0][j] * dinh_thuc(pds)
        j = j + 1
    return ket_qua  

def Eigenvalues(Matrix):
    list_set=[32, 31.9, 31.8, 32.1, 32.2]
    for element in list_set:
        eigenvalues = np.linalg.eigvals(Matrix)
        print("Eigenvalues of A:",eigenvalues)
def characteristic(Matrix):
    list_set=[32, 31.9, 31.8, 32.1, 32.2]
    for element in list_set:
        Matrix[2][1]=element
        M=(Matrix-x*np.identity(len(Matrix)))
        print("Characteristic of A:",dinh_thuc(M))

A=np.array([[-6,28,21],
            [4,-15,-12],
            [8,y,25]])
print("Cau 2 lap 10",characteristic(A))

#cau3 lap 10

M=np.array([[-3,-5,-7],
            [-2,1,0],
            [1,5,5]])
values,vectors=np.linalg.eig(M)

x,y,z=symbols('x,y,z')
for k in values:
    m=M-k*np.eye(3) 
    print("the solution of the equation",np.linalg.solve(m,[0,0,0]))
P=vectors.T
D=np.linalg.inv(P)@M@P
print("cau3 lap 10")
print(D)
print(M)

#cau 4 lap 10
A=np.array([[-2,2,-3],
            [2,1,-6],
            [-1,-2,0]])
print("cau4 lap10")
# A
values,vectors=np.linalg.eig(A)
print("the eigenvalues of A\n",values)
print("the eigenvectors of A\n",vectors)
# A.T
values,vectors=np.linalg.eig(A.T)
print("the eigenvalues of A.T\n",values)
print("the eigenvectors of A.T\n",vectors)
# A^-1
values,vectors=np.linalg.eig(np.linalg.inv(A))
print("the eigenvalues of A^-1\n",values)
print("the eigenvectors of A^-1\n",vectors)

#cau5 lap 10

def isDiagonalMatrix(mat) :
    for i in range(0, len(mat)):
        for j in range(0,len(mat)) :
            if ((i != j) and (mat[i][j] != 0)) :
                return False
    return True

A1=np.array([[4,-5],
            [2,-3]])
A2=np.array([[0,2],
            [0,1]])
A3=np.array([[2,3],
            [1,4]])
A4=np.array([[1,2,-2],
            [-2,5,-2],
            [-6,6,-3]])
A5=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]])
print("cau5 lap 10")
if (isDiagonalMatrix(A1)) :
    print("A1 is diagonal")
else :
    print("A1 is not diagonal")
if (isDiagonalMatrix(A2)) :
    print("A2 is diagonal")
else :
    print("A2 is not diagonal")
if (isDiagonalMatrix(A3)) :
    print("A3 is diagonal")
else :
    print("A3 is not diagonal")
if (isDiagonalMatrix(A4)) :
    print("A4 is diagonal")
else :
    print("A4 is not diagonal")
if (isDiagonalMatrix(A5)) :
    print("A5 is diagonal")
else :
    print("A5 is not diagonal")
    
#cau6 lap 10
A=np.array([[2,0,0],
            [1,2,1],
            [-1,0,1]])
values,vectors=np.linalg.eig(A)
print("the eigenvalues of A\n",values)
print("the eigenvectors of A\n",vectors)

P=np.zeros((3,3))
for i in range(3):
    P[i,i]=np.diag(A)[i]

D=np.linalg.inv(P)@A@P
print("cau 6 lap 10")
print("Solve\n",D)

#cau7 lap 10
A1=np.array([[1,0],
            [0,-3]])
A2=np.array([[-5,0],
            [0,0]])
A3=np.array([[np.sqrt(6),1],
            [0,np.sqrt(6)]])
A4=np.array([[np.sqrt(3),2],
            [0,np.sqrt(3)]])
print('cau 7 lap 10')
print("singular values of the matrices A1:",np.linalg.svd(A1,compute_uv=False))
print("singular values of the matrices A2:",np.linalg.svd(A2,compute_uv=False))
print("singular values of the matrices A3:",np.linalg.svd(A3,compute_uv=False))
print("singular values of the matrices A4:",np.linalg.svd(A4,compute_uv=False))

#cau 8 lap 10
A1=np.array([[-18,13,-4,4],
            [2,29,-4,12],
            [-14,11,-12,8],
            [-2,21,4,8]])
A2=np.array([[6 ,-8 ,-4, 5, -4],
            [2, 7, -5, -6, 4],
            [0, -1,-8, 2,2],
            [-1, -2, 4, 4, -8]])

print('cau 8 lap 10')
print("singular values of the matrices A1:",np.linalg.svd(A1,compute_uv=False))
print("singular values of the matrices A2:",np.linalg.svd(A2,compute_uv=False))

