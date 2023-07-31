import math 
import numpy as np
import sympy as sp

x = sp.symbols('x')

#Ex5_a
fx_5a = x*x - 7
la = sp.limit(fx_5a, x, 1)
print("Ex5a: f(c) = ", 1*1 - 7)
print("Limit of F(x) 5a when x tend to 1: ", lim_fx_5a)
if (lim_fx_5a == 1*1 - 7):
	print("The function 5a is continuous at c")
else:
	print("The function 5a isn't continuous at c")

#Ex_5b
fx_5b = pow(2*x - 3, 1/2)
lim_fx_5b = sp.limit(fx_5b, x, 2)
print("Ex5b: f(c) = ", pow(1, 1/2))
print("Limit of F(x) 5b when x tend to 2: ", lim_fx_5b)
if (lim_fx_5b == pow(1, 1/2)):
	print("The function 5b is continuous at c")
else:
	print("The function 5b is continuous at c")