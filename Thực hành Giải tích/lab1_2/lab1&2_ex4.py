import sympy as sp
import math
x= sp.symbols('x')
f = x**2 + 2*x -1
print(f)
root = sp.solve(f)
print("Answer of f(x): {}".format(root))
print("Answer of f(x): x1 = {:.3f}, x2 = {:.3f}".format(root[0].evalf(),root[1].evalf()))