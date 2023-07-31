import sympy as sp 
import math

x = sp.symbols('x') #Tạo ra biến x biểu tượng

#cau1_a
fx_1a = abs(x*x - x - 7)
lim_fx1a = sp.limit(fx_1a, x, 3)
print("Ex_1a - The limit of f(x) when x tends to 3: " + str(lim_fx1a))

#cau1_b
fx_1b = abs(x - 1) / (x*x - 1) 
lim_fx1b = sp.limit(fx_1b, x, 1)
print("Ex_1b - The limit of f(x) when x tends to 1: " + str(lim_fx1b))

#cau1_c
fx_1c = pow(math.e, 1/x)
lim_fx1c = sp.limit(fx_1c, x, 1)
print("Ex_1c - The limit of f(x) when x tends to 1: " + str(lim_fx1c))

#cau1d
fx_1d = (pow(x, 4) - 16) / (x - 2)
lim_fx1d = sp.limit(fx_1d, x, 2)
print("Ex_1d - The limit of f(x) when x tends to 2: " + str(lim_fx1d))

#cau1e
fx_1e = (x**3 - x**2 - 5*x - 3) / pow(x + 1, 2)
lim_fx1e = sp.limit(fx_1e, x, -1)
print("Ex_1e - The limit of f(x) when x tends to -1: " + str(lim_fx1e))

#cau1f
fx_1f = (x**2 - 9) / (sp.sqrt(x**2 + 7) - 4)
lim_fx1f = sp.limit(fx_1f, x, 3)
print("Ex_1f - The limit of f(x) when x tends to 3: " + str(lim_fx1f))

#cau1g
fx_1g = abs(x) / sp.sin(x)
lim_fx1g = sp.limit(fx_1g, x, 1)
print("Ex_1g - The limit of f(x) when x tends to 1: " + str(lim_fx1g))

#cau1h
fx_1h = (1 - sp.cos(x)) / (x * sp.sin(x))
lim_fx1h = sp.limit(fx_1h, x, 0)
print("Ex_1h - The limit of f(x) when x tends to 0: " + str(lim_fx1h))

#cau1i
fx_1i = (2 * x*x) / (3 - 3 * sp.cos(x))
lim_fx1i = sp.limit(fx_1i, x, 0)
print("Ex_1i - The limit of f(x) when x tends to 0: " + str(lim_fx1i))

#cau1j 
fx_1j = pow((3 + x) / (-1 + x), x)
lim_fx1j = sp.limit(fx_1j , x, sp.oo)
print("Ex_1j - The limit of f(x) when x tends to oo: " + str(lim_fx1j))

#cau1k
fx_1k = pow(1 - 2 / (3 + x), x)
lim_fx1k = sp.limit(fx_1k, x, sp.oo)
print("Ex_1k - The limit of f(x) when x tends to oo:", lim_fx1k)

#cau1l
fx_1l = pow(1 / x, 1 / x)
lim_fx1l = sp.limit(fx_1l, x, sp.oo)
print("Ex_1l - The limit of f(x) when x tends to oo:", lim_fx1l)
 
"""
cau1m
fx_1m = (- pow(x, 1/3) + pow(1 + x, 1/3)) / (- pow(x, 1/2) + pow(1 + x, 1/2))
lim_fx1m = sp.limit(fx_1m, x, sp.oo)
"""
print("Ex_1m - There is no limit of f(x) when x tends to oo")

#cau1n
fx_1n = sp.factorial(x) / pow(x, x)
lim_fx1n = sp.limit(fx_1n, x, sp.oo)
print("Ex_1n - The limit of f(x) when x tends to oo:", lim_fx1n)
