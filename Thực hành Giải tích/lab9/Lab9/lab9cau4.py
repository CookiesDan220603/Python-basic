from numpy.core.fromnumeric import ptp
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')

#Ex4a
fx = x*x * sp.cos(x)
val = np.arange(-4, 9.01, 0.01)
fin = sp.integrate(abs(fx), (x, -4, 9))
print("Exercise 4a:")
print("Area under curve of function f(x):", fin.evalf())
print("---------")

fx_val = sp.lambdify(x, fx, "numpy")(val)
plt.plot(val, fx_val, color = 'cyan', label = 'f(x)')
plt.title("Function f(x)")
plt.grid()
plt.legend()
plt.show()

#Ex 4b
fx = pow(np.e, -0.5 * x*x)
fin = sp.integrate(abs(fx), (x, -sp.oo, sp.oo))
print("Exercise 4b:")
print("Area under curve of function f(x):", fin.evalf())
print("---------")

val = np.arange(-100, 100, 0.01)
fx_val = sp.lambdify(x, fx, "numpy")(val)
plt.plot(val, fx_val, color = 'pink', label = 'f(x)')
plt.title("Function f(x)")
plt.grid()
plt.legend()
plt.show()