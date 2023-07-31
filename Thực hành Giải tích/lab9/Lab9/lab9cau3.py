from math import sqrt
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
x, y = sp.symbols('x, y')
#ex3a
f = x**2 -1
fin = sp.integrate(f,(x,0,3**(1/3)))
print("Definite integral of f(x) from 0 to 3**1/3:", fin.evalf())
val = np.arange(0, 3**(1/3), 0.001)
fx_val = sp.lambdify(x, f, "numpy")(val)
plt.plot(val, fx_val, color = 'pink', label = 'f(x)')
plt.title("Function f(x)")
plt.grid()
plt.legend()
plt.show()
print("The average value over given integral : {}".format(fin*(1/(3**(1/3)))))
print("-----------------------")
#Ex3b
f = -3*x**2 -1
fin = sp.integrate(f,(x,0,1))
print("Definite integral of f(x) from 0 to 1:", fin.evalf())
val = np.arange(0, 1, 0.001)
fx_val = sp.lambdify(x, f, "numpy")(val)
plt.plot(val, fx_val, color = 'pink', label = 'f(x)')
plt.title("Function f(x)")
plt.grid()
plt.legend()
plt.show()
print("The average value over given integral : {}".format(fin*(1/(1))))
print("-----------------------")
#Ex3c
f = (x**2)/2
fin = sp.integrate(f,(x,0,3))
print("Definite integral of f(x) from 0 to 3:", fin.evalf())
val = np.arange(0, 3, 0.001)
fx_val = sp.lambdify(x, f, "numpy")(val)
plt.plot(val, fx_val, color = 'pink', label = 'f(x)')
plt.title("Function f(x)")
plt.grid()
plt.legend()
plt.show()
print("The average value over given integral : {}".format(fin*(1/(3-0))))
print("-----------------------")
#Ex3d
f = x**2 - x
fin = sp.integrate(f,(x,-2,1))
print("Definite integral of f(x) from -2 to 1:", fin.evalf())
val = np.arange(-2, 1, 0.001)
fx_val = sp.lambdify(x, f, "numpy")(val)
plt.plot(val, fx_val, color = 'pink', label = 'f(x)')
plt.title("Function f(x)")
plt.grid()
plt.legend()
plt.show()
print("The average value over given integral : {}".format(fin*(1/(1+2))))
print("-----------------------")

