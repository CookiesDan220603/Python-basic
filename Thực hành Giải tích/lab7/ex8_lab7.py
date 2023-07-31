import sympy as sp 
import numpy as np
import math
x,y=sp.symbols("x,y")
def daoham(f,a,b):
	fx = sp.limit((f.subs(y,b)-f.subs([(x,a),(y,b)]))/(x-a),x,a)
	fy = sp.limit((f.subs(x,a)-f.subs([(x,a),(y,b)]))/(y-b),y,b)
	print("Fx = {} , Fy = {}".format(fx,fy))
	print("--------------------------------")
#a
f = 1 -x + y - 3*x**2
a=1
b=2
print("Cau a")
daoham(f,a,b)
#b
f = 4 + 2*x + 3*y -3*x*y**2
a=-2
b=1
print("Cau b")
daoham(f,a,b)
