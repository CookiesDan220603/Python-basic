import sympy as sp 
import numpy as np
def sosanh(f):
	fxy = sp.diff(sp.diff(f,x,1),y,1)
	fyx = sp.diff(sp.diff(f,y,1),x,1)
	if fyx == fxy:
		print("Fxy = Fyx")
	else:
		print("Fxy is not equal Fyx")
x,y = sp.symbols('x,y')
#a
f_a= x*sp.sin(x) + y*sp.sin(x) + x*y

print("Cau a")
sosanh(f_a)
#b
f_b = sp.log(2*x + 3*y)
print("Cau b")
sosanh(f_b)
#c
f_c = x*y**2 + (x**2)*y**3 + (x**3)*y**4
print("Cau c")
sosanh(f_c)
#d
f_d = sp.exp(x)+x*sp.log(y)+y*sp.log(x)
print("Cau d")
sosanh(f_d)
