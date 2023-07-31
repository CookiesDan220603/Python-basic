import sympy as sp 
import numpy as np

x = sp.symbols('x')

#Ex10b
fx_10b = (x*x + x - 6) / (x*x - 4)
lim_fx10b_x_2 = sp.limit(fx_10b, x, 2)
print("Ex10b: Limit of function when x tends to 2: ", lim_fx10b_x_2)
print("The function is continuous when L = ", lim_fx10b_x_2)
