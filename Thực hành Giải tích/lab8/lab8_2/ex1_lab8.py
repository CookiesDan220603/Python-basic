import sympy as sp 
import numpy as np
import math
x= sp.symbols('x')
def solve (f):
	df = sp.diff(f,x)
	k = sp.solve(df,x)
	print(k)
#a
f = 18*x**2 -19
print("cau a")
solve(f)
#b
f = (x+2)/(x*x**2)
print("Cau b")
solve(f)
#c
f = -(x**2)/3 + x**2 + 3*x + 4
print("Cau c")
solve(f)
#d
f = (5*x**2 + 5)/x
print("Cau d")
solve(f)