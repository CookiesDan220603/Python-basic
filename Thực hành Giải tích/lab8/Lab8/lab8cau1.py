import sympy as sp

x = sp.symbols('x')

#Ex 1a
fx = 3 * pow(x, 4) - 16 * pow(x, 3) + 18 * pow(x, 2) - 9
dfx = sp.diff(fx, x)
c_val = sp.solve(dfx, x)
print("Exercise 1a:")
print("Critical values:", c_val)
print("-------------")

#Ex 1b
fx = (x + 2) / (2 * pow(x, 2))
dfx = sp.diff(fx, x)
c_val = sp.solve(dfx, x)
print("Exercise 1b:")
print("Critical values:", c_val)
print("-------------")

#Ex1c
fx = (- pow(x, 2) / 3) + pow(x, 2) + 3 * x + 4
dfx = sp.diff(fx, x)
c_val = sp.solve(dfx, x)
print("Exercise 1c:")
print("Critical values:", c_val)
print("-------------")

#Ex1d
fx = (5 * pow(x, 2) + 5) / x
dfx = sp.diff(fx, x)
c_val = sp.solve(dfx, x)
print("Exercise 1d:")
print("Critical values:", c_val)
print("-------------")