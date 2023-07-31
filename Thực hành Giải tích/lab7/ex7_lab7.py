import sympy as sp 
import numpy as np
import math

# def daoham(f,x,y,z,a):
#   ft = diff(f,x,1)*diff(x,t,1) + diff(f,y,1)*diff(y,t,1) +diff(f,z,1)*diff(z,t,1)
#   ft1 = ft.subs(t,a)
#   return ft
x,y,z,t=sp.symbols("x,y,z,t")
def ex7xyz(w,f1,f2,f3,a):
	fxyz = w.subs([(x,f1),(y,f2),(z,f3)])
	kq=sp.diff(fxyz,t,1).subs(t,a)
	return kq
#a
f = x**2 + y**2 
f1 = sp.cos(t)
f2 = sp.sin(t)
f3 =0
a = math.pi
print("Cau a")
print(ex7xyz(f,f1,f2,f3,a))
#b
f = x**2 + y**2 
f1 = sp.cos(t) + sp.sin(t)
f2 = sp.cos(t)- sp.sin(t)
f3 =0
a = 0
print("Cau b")
print(ex7xyz(f,f1,f2,f3,a))
#c
f = (x/z) + (y/z)
f1 = pow(sp.cos(t),2)
f2 = pow(sp.sin(t),2)
f3 = 1/t
a = 3
print("Cau c")
print(ex7xyz(f,f1,f2,f3,a))
#d
f = 2*y*sp.exp(x) - sp.log(z)
f1 = sp.log(t**2 + 1)
f2 = pow(sp.tan(t),-1)
f3 = sp.exp(t)
print("Cau d")
print(ex7xyz(f,f1,f2,f3,a))
#e
f= z- (sp.sin(x))*y
f1 = t
f2 = sp.log(t)
f3 = sp.exp(t-1)
print("Cau e")
print(ex7xyz(f,f1,f2,f3,a))