from math import sqrt
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x, y = sp.symbols('x, y')
#Ex 2a
fx = x**3 - 3*(sp.sin(x))*(sp.cos(x))
fin = sp.integrate(fx, (x, 0, (sp.pi)/2))
print("Exercise 2a:")
print("Definite integral of f(x) from 0 to pi/2:", fin.evalf())
val = np.arange(0, np.pi/2, 0.001)
fx_val = sp.lambdify(x, fx, "numpy")(val)
plt.plot(val, fx_val, color = 'pink', label = 'f(x)')
plt.title("Function f(x)")
plt.grid()
plt.legend()
plt.show()
print("---------") 
#Ex 2b
f = pow(sp.sin(x**2),2)
fin = sp.integrate(f, (x, 0, 1))
print("Exercise 2b:")
print("Definite integral of f(x) from 0 to 1:", fin.evalf())
val = np.arange(0, 1, 0.001)
fx_val = sp.lambdify(x, f, "numpy")(val)
plt.plot(val, fx_val, color = 'pink', label = 'f(x)')
plt.title("Function f(x)")
plt.grid()
plt.legend()
plt.show()
print("---------")
#Ex 2c
g = x + 1
f = sp.sqrt(1 + g.subs(x, x*x) + pow(g, 2))
fin = sp.integrate(f, (x, 0, 3))
print("Exercise 2c:")
print("Definite integral of f(x) from 0 to 3:", fin.evalf())
val = np.arange(0,3, 0.001)
fx_val = sp.lambdify(x, f, "numpy")(val)
plt.plot(val, fx_val, color = 'pink', label = 'f(x)')
plt.title("Function f(x)")
plt.grid()
plt.legend()
plt.show()
print("---------")

#Ex 2d
fxy = x*x * y
fin = sp.integrate(f, (x, 1, 2), (y, 0, 3))
print("Exercise 2d:")
print("Definite integral of f(x, y):", fin.evalf())
print("---------")