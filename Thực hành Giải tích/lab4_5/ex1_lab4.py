import sympy as sp
import math
x = sp.symbols('x')
t = sp.symbols('t')
z = sp.symbols('z')

#1a
fx_a = 4 - x**2
df_a = sp.diff(fx_a,x)
print("1a - Derivative of f(x) = ",df_a)
#1b
fx_b = (x-1)**2 +1
df_b = sp.diff(fx_b,x)
print("1b - Derivative of f(x) = ",df_b)
#1c
fx_c = 1/t**2
df_c = sp.diff(fx_c,t)
print("1c - Derivative of f(x) = ",df_c)
#1d
fx_d = (1-z)/(2*z)
df_d = sp.diff(fx_d,z)
print("1d - Derivative of f(x) = ",df_d)
#1e
fx_e = sp.sqrt(3*z)
df_e = sp.diff(fx_e,z)
print("1e - Derivative of f(x) = ",df_e)
#1f
fx_f = sp.sqrt(2*z + 1)
df_f = sp.diff(fx_f,z)
print("1f - Derivative of f(x) = ",df_f)

