import sympy as sp 
import numpy as np

x = sp.symbols('x')

#Ex7a
fx_7a = (x*x - x - 2) / (x - 2)
for x_0 in np.arange(-100, 100, 1):
	lim_fx7a = sp.limit(fx_7a, x, x_0)
	if (lim_fx7a != fx_7a.subs(x, x_0)):
		print("Ex7a: The function isn't continuous at x = ", x_0)
print("----")

#Ex7b
fx_7b = (x*x - 2*x - 3) / (2*x - 6)
for x_0 in np.arange(-100, 100, 1):
	lim_fx7b = sp.limit(fx_7b, x, x_0)
	if (lim_fx7b != fx_7b.subs(x, x_0)):
		print("Ex7b: The function isn't continuous at x =", x_0)