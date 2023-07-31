import sympy as sp
import numpy as np
import math

from sympy.solvers.solvers import solve

x, m = sp.symbols('x, m')
fx = x**3 - 3 * m * x*x + 3 * (m*m - 1) * x - (m*m - 1)
dfx = sp.diff(fx, x)
dfx0 = dfx.subs(x, 1)
vals_m = sp.solve(dfx0, m)
print(vals_m)
dfxx = sp.diff(fx, x, 2).subs(x, 1)
for i in range(0, 2):
    if dfxx.subs(m, vals_m[i]) < 0:
        print("Function y maximize at x0 = 1 when m =", vals_m[i])
print("----- End -----")