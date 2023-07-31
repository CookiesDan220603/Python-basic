from sympy import * ## KHONG XOA
import numpy as np ## KHONG XOA 
import math
global x, y, z, t ## KHONG XOA
x, y, z, t = symbols("x, y, z, t")
f = (x/x**2)**2
lim = limit(f,x,oo)
print(lim)
