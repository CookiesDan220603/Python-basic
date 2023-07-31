import sympy as sp

x = sp.symbols('x')

f = 1 / (2 * sp.sqrt(x))
cost = sp.integrate(f, (x, 1, 100))
print("The cost of printing poster 2-100:", cost, "dollars")
print("---------")