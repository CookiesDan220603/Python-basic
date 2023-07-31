import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt

x, y, = sp.symbols('x, y')

#Ex3a
fa = 2 * x*x - 3*y - 4 
dfa_x = sp.diff(fa, x)
dfa_y = sp.diff(fa, y)
print("Exercise 3a:")
print("The first order partial derivative of f with regard to x:", dfa_x)
print("The first order partial derivative of f with regard to y:", dfa_y)
print("----------------------------")

"""
z_func = lambda x, y: 2 * x*x - 3 * y - 4
x0 = np.arange(-6, 6, 0.1)
y0 = x0.copy()
X, Y = np.meshgrid(x0, y0)
Z = z_func(X, Y)
ax = plt.axes(projection = '3d')
ax.plot_surface(X, Y, Z, cmap = 'cool', linewidth = 0)
ax.set_title('Surface plot')
plt.show()
"""

#Ex3b
fb = (x*x -1) * (y + 2)
dfb_x = sp.diff(fb, x)
dfb_y = sp.diff(fb, y)
print("Exercise 3b:")
print("The first order partial derivative of f with regard to x:", dfb_x)
print("The first order partial derivative of f with regard to y:", dfb_y)
print("----------------------------")

"""
z_func = lambda x, y: (x*x - 1) * (y + 2)
Z = z_func(X, Y)
ax = plt.axes(projection = '3d')
ax.plot_surface(X, Y, Z, cmap = 'winter', linewidth = 0)
ax.set_title('Surface plot')
plt.show()
"""

#Ex3c
fc = x*x - x * y + y*y 
dfc_x = sp.diff(fc, x)
dfc_y = sp.diff(fc, y)
print("Exercise 3c:")
print("The first order partial derivative of f with regard to x:", dfc_x)
print("The first order partial derivative of f with regard to y:", dfc_y)
print("----------------------------")

"""
z_func = lambda x, y: x*x - x * y + y*y 
Z = z_func(X, Y)
ax = plt.axes(projection = '3d')
ax.plot_surface(X, Y, Z, cmap = 'summer', linewidth = 0)
ax.set_title('Surface plot')
plt.show()
"""

#Ex3d
fd = 5 * x * y - 7 * x*x - y*y + 3 * x - 6 * y + 2
dfd_x = sp.diff(fd, x)
dfd_y = sp.diff(fd, y)
print("Exercise 3d:")
print("The first order partial derivative of f with regard to x:", dfd_x)
print("The first order partial derivative of f with regard to y:", dfd_y)
print("----------------------------")

#Ex3e
fe = (x * y - 1) ** 2
dfe_x = sp.diff(fe, x)
dfe_y = sp.diff(fe, y)
print("Exercise 3e:")
print("The first order partial derivative of f with regard to x:", dfe_x)
print("The firse order partial derivative of f with regard to y:", dfe_y)
print("----------------------------")

#Ex3f
ff = (2 * x - 3 * y) ** 3
dff_x = sp.diff(ff, x)
dff_y = sp.diff(ff, y)
print("Exercise 3f:")
print("The first order partial derivative of f with regard to x:", dff_x)
print("The first order partial derivative of f with regard to y:", dff_y)
print("----------------------------")

#Ex3g
fg = sp.sqrt(x*x + y*y)
dfg_x = sp.diff(fg, x)
dfg_y = sp.diff(fg, y)
print("Exercise 3g:")
print("The first order partial derivative of f with regard to x:", dfg_x)
print("The first order partial derivative of f with regard to y:", dfg_y)
print("----------------------------")

#Ex3h
fh = (x**3 + y / 2) ** (2/3)
dfh_x = sp.diff(fh, x)
dfh_y = sp.diff(fh, y)
print("Exercise 3h:")
print("The first order partial derivative of f with regard to x:", dfh_x)
print("The first order partial derivative of f with regard to y:", dfh_y)
print("----------------------------")

#Ex3i
fi = 1 / (x + y)
dfi_x = sp.diff(fi, x)
dfi_y = sp.diff(fi, y)
print("Exercise 3i:")
print("The first order partial derivative of f with regard to x:", dfi_x)
print("The first order partial derivative of f with regard to y:", dfi_y)
print("----------------------------")

#Ex3j
fj = x / (x*x + y*y)
dfj_x = sp.diff(fj, x)
dfj_y = sp.diff(fj, y)
print("Exercise 3j:")
print("The first order partial derivative of f with regard to x:", dfj_x)
print("The first order partial derivative of f with regard to y:", dfj_y)
print("----------------------------")

#E3k
fk = (x + y) / (x * y - 1)
dfk_x = sp.diff(fk, x)
dfk_y = sp.diff(fk, y)
print("Exercise 3k:")
print("The first order partial derivative of f with regard to x:", dfk_x)
print("The first order partial derivative of f with regard to y:", dfk_y)
print("----------------------------")

#Ex3l
fl = 1 / sp.tan(y / x)
dfl_x = sp.diff(fl, x)
dfl_y = sp.diff(fl, y)
print("Exercise 3l:")
print("The first order partial derivative of f with regard to x:", dfl_x)
print("The first order partial derivative of f with regard to y:", dfl_y)
print("----------------------------")

#Ex3m
fm = np.e ** (x + y + 1)
dfm_x = sp.diff(fm, x)
dfm_y = sp.diff(fm, y)
print("Exercise 3m:")
print("The first order partial derivative of f with regard to x:", dfm_x)
print("The first order partial derivative of f with regard to y:", dfm_y)
print("----------------------------")

#Ex3n
fn = (np.e ** (- x)) * sp.sin(x + y)
dfn_x = sp.diff(fn, x)
dfn_y = sp.diff(fn, y)
print("Exercise 3n:")
print("The first order partial derivative of f with regard to x:", dfn_x)
print("The first order partial derivative of f with regard to y:", dfn_y)
print("----------------------------")

#Ex3o
fo = sp.log(x + y)
dfo_x = sp.diff(fo, x)
dfo_y = sp.diff(fo, y)
print("Exercise 3o:")
print("The first order partial derivative of f with regard to x:", dfo_x)
print("The first order partial derivative of f with regard to y:", dfo_y)
print("---------- End ----------")