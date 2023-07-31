from numbers import Real
from numpy.lib.type_check import real
import sympy as sp
import numpy as np
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.matrices.expressions.determinant import per

x = sp.symbols('x', real = True)

def Calculate_Integrate(f, a, b):
    fin = sp.integrate(f, (x, a, b))
    return fin.evalf()

#Ex 1a
fx = x**3 + 2 * x*x + 3
print("Exercise 1a:")
print("Definite integral of f(x) from 1 to 2:", Calculate_Integrate(fx, 1, 2))
print("---------")

#Ex 1b
fx = 1 / x**3 + 1 / x*x + x*pow(x, 1/2)
print("Exercise 1b:")
print("Definite integral of f(x) from 1 to 4:", Calculate_Integrate(fx, 1, 4))
print("---------")

#Ex 1c
fx = (x**3 + x * pow(x, 1/2) + x) / (x*x)
print("Exercise 1c:")
print("Definite integral of f(x) from 1 to 4:", Calculate_Integrate(fx, 1, 4))
print("---------")

#Ex 1d
fx = 2 / x + x**3
print("Exercise 1d:")
print("Definite integral of f(x) from 1 to 2:", Calculate_Integrate(fx, 1, 2))
print("---------")

#Ex 1e
fx = x*x * (1 / x + 2 * x)
print("Exercise 1e:")
print("Definite integral of f(x) from 1 to 2:", Calculate_Integrate(fx, 1, 2))
print("---------")

#Ex 1f
fx = (pow(x, 1/2) - 1) * (x + pow(x, 1/2) + 1)
print("Exercise 1f:")
print("Definite integral of f(x) from 0 to 1:", Calculate_Integrate(fx, 0, 1))
print("---------")

#Ex 1g
fx = (1 - 2 / pow(sp.sin(x), 2))
print("Exercise 1g:")
print("Definite integral of f(x) from pi/4 to pi/2:", Calculate_Integrate(fx, sp.pi / 4, sp.pi / 2))
print("---------")

#Ex 1h
fx = 1 / (pow(sp.sin(x), 2) * pow(sp.cos(x), 2))
print("Exercise 1h:")
print("Definite integral of f(x) from pi/6 to pi/4", Calculate_Integrate(fx, sp.pi / 6, sp.pi / 4))
print("---------")

#Ex 1i
fx = pow(np.e, x) * (1 - pow(np.e, -x) / (pow(sp.cos(x), 2)))
print("Exercise 1i:")
print("Definite integral of f(x) from 0 to pi/4:", Calculate_Integrate(fx, 0, sp.pi / 4))
print("---------")

#Ex 1j
fx = pow(np.e, x) * (2 + pow(np.e, -x) / pow(np.e, x))
print("Exercise 1j:")
print("Definite integral of f(x) from 0 to ln2:", Calculate_Integrate(fx, 0, sp.log(2)))
print("---------")

#Ex 1k
fx = (pow(2, x) + 2 / x)
print("Exercise 1k:")
print("Definite integral of f(x) from 1 to 2:", Calculate_Integrate(fx, 1, 2))
print("---------")

#Ex 1l
fx = pow(x, 2) * pow(x - 1, 2)
print("Exercise 1l:")
print("Definite integral of f(x) from 0 to 1:", Calculate_Integrate(fx, 0, 1))
print("---------")

#Ex 1m
fx = 1 / (x * (x + 1))
print("Exercise 1m:")
print("Definite integral of f(x) from 1 to 2:", Calculate_Integrate(fx, 1, 2))
print("---------")

#Ex 1n
fx = abs(1 - x)
print("Exercise 1n:")
print("Definite integral of f(x) from 0 to 2:", Calculate_Integrate(fx, 0, 2))
print("---------")

#Ex 1o
fx = abs(2 * x - x * x)
print("Exercise 1o:")
print("Definite integral of f(x) from 0 to 3:", Calculate_Integrate(fx, 0, 3))
print("---------")

#Ex 1p
fx = sp.sqrt(x*x - 3 * x + 2)
print("Exercise 1p:")
print("Definite integral of f(x) from 2 to 4:", Calculate_Integrate(fx, 2, 4))
print("---------")

#Ex 1q
fx = pow(1 + (1 - 2 * pow(sp.sin(x), 2)), 1/2)
print("Exercise 1q:")
print("Definite integral of f(x) from 0 to pi:", Calculate_Integrate(fx, 0, sp.pi))
print("----- End -----")