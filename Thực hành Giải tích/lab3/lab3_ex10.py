import sympy as sp 
import numpy as np
x = sp.symbols('x')
#Ex10a
fx_10a = sp.sin(x)/x
lim_fx10a_x_0 = sp.limit(fx_10a,x,0)
print("Ex10a: Limit of function when x tends to 2: ", lim_fx10a_x_0)
print("The function is continuous when L = ", lim_fx10a_x_0)
#Ex10b
fx_10b = (x*x + x - 6) / (x*x - 4)
lim_fx10b_x_2 = sp.limit(fx_10b, x, 2)
print("Ex10b: Limit of function when x tends to 2: ", lim_fx10b_x_2)
print("The function is continuous when L = ", lim_fx10b_x_2)
