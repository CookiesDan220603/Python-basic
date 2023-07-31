import sympy as sp

t = sp.symbols('t')

v = 160 - 32 * t
s = sp.integrate(v, (t, 0, 8))
print("Displacement of the rock during the time period from 0 to 8 second:",s, "ft")
print("---------")