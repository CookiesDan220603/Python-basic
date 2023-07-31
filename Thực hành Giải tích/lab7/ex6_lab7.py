import sympy as sp 
import numpy as np
x,y=sp.symbols("x,y")
def daoham(f):
	fx2y3 = sp.diff(sp.diff(f,x,2),y,3)
	print(fx2y3)
#cau a
fa = (y**2)*(x**4)*sp.exp(x) + 2
print("Cau a")
daoham(fa)
#cau b
fb = y**4 + y*(sp.sin(x)-x**4)
print("Cau b")
daoham(fb)
#cau c
fc = x**5 + 5*(x**5)*(y**5) + sp.sin(x) + 7*sp.exp(x)
print("Cau c")
daoham(fc)
#cau d
fd = (x**3)*sp.exp((y**4)/2)
print("Cau d")
daoham(fd) 
