
from sympy import * ## KHONG XOA
import numpy as np ## KHONG XOA 

global x, y, z, t ## KHONG XOA
x, y, z, t = symbols("x, y, z, t") ## KHONG XOA     
f = 24*x/(225 -5*x)
fx = integrate(f,x)

print(fx)
kq = fx.subs(x,1)
kq = kq.subs(y,0)


print(kq)
# fxy = fx.subs(x,1)
# fxy = fxy.subs(y,0)
# print(fxy)