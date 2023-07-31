import sympy as sp
import math

x, y = sp.symbols('x, y')

def Find_minima_maxima(fxy):
    minima = []
    maxima = []
    dfx = sp.diff(fxy, x)
    dfy = sp.diff(fxy, y)
    dfxx = sp.diff(fxy, x, 2)
    dfyy = sp.diff(fxy, y, 2)
    dfxy = sp.diff(dfx, y)
    vals = sp.solve((dfx, dfy), dict = True)
    for i in vals:
        if (i[x].is_real and i[y].is_real):
            fxx = (dfxx.subs(x, i[x])).subs(y, i[y])
            fyy = (dfyy.subs(x, i[x])).subs(y, i[y])
            fxy_val = (dfxy.subs(x, i[x])).subs(y, i[y])
            D = fxx * fyy - (fxy_val * fxy_val)
            if D > 0 and fxx > 0:
                minima.append((i[x], i[y]))
            elif D > 0 and fxx < 0:
                maxima.append((i[x], i[y]))
    return minima, maxima

#Ex 9a
fxy = x*x + y*y - 4 * x - 4 * y
minima = []
maxima = []
(minima, maxima) = Find_minima_maxima(fxy)
print("Exercise 9a:")
print("Local minimum of f(x, y):", minima)
print("Local maximum of f(x, y):", maxima)
print("-------------")

#Ex 9b
fxy = 3 * x*x + 2 * y**4 - x*x + y*y + 1
minima = []
maxima = []
(minima, maxima) = Find_minima_maxima(fxy)
print("Exercise 9b:")
print("Local minimum of f(x, y):", minima)
print("Local maximum of f(x, y)", maxima)
print("-------------")

#Ex 9c
fxy = pow(math.e, x*x) + y*y - 3 + 2 * y
minima = []
maxima = []
(minima, maxima) = Find_minima_maxima(fxy)
print("Exercise 9c:")
print("Local minimum of f(x, y):", minima)
print("Local maximum of f(x, y)", maxima)
print("-------------")

#Ex 9d
fxy = (x*x - 1) ** 2 + y*y - 3 * y + 1
minima = []
maxima = []
(minima, maxima) = Find_minima_maxima(fxy)
print("Exercise 9d:")
print("Local minimum of f(x, y):", minima)
print("Local maximum of f(x, y):", maxima)
print("-------------")

#Ex 9e
fxy = x*x * pow(math.e, x) + 51 * y + pow(y, 4) + 3
minima = []
maxima = []
print("Exercise 9e:")
print("Local minimum of f(x, y):", minima)
print("Local maximum of f(x, y):", maxima)
print("-------------")

#Ex 9f
fxy = pow(math.e, x*x - 3) + y*y - 3 * y
minima = []
maxima = []
print("Exercise 9f:")
print("Local minimum of f(x, y)", minima)
print("Local maximum of f(x, y)", maxima)
print("-------------")

#Ex 9g
fxy = x * pow(y, 3) + 2 * pow(x, 2) + 2 * pow(y, 4) - 5
minima = []
maxima = []
print("Exercise 9g:")
print("Local minimum of f(x, y):", minima)
print("Local maximum of f(x, y):", maxima)
print("------- End ------")