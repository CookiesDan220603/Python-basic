import sympy as sp

x = sp.symbols('x')

#Ex 2a
fx = 3 * pow(x, 4) - 16 * pow(x, 3) + 18 * pow(x, 2) - 9
dfx = sp.diff(fx, x)
dfxx = sp.diff(fx, x, 2)
c_val = sp.solve(dfx, x)
print("Exercise 2a:")
for i in c_val:
    if (i.is_real):
        if (dfxx.subs(x, i) > 0):
            print("f(x) has a local minimum at:", i)
            print("f(", i, ") =", fx.subs(x, i))
        if (dfxx.subs(x, i) < 0):
            print("f(x) has a local maximum at:", i)
            print("f(", i, ") =", fx.subs(x, i))
print("--------------")

#Ex 2b
fx = (x + 2) / (2 * pow(x, 2))
dfx = sp.diff(fx, x)
dfxx = sp.diff(fx, x, 2)
c_val = sp.solve(dfx, x)
print("Exercise 2b:")
for i in c_val:
    if (i.is_real):
        if (dfxx.subs(x, i) > 0):
            print("f(x) has a local minimum at:", i)
            print("f(", i, ") =", fx.subs(x, i))
        if (dfxx.subs(x, i) < 0):
            print("f(x) has a local maximum at:", i)
            print("f(", i, ") =", fx.subs(x, i))
print("--------------")

#Ex 2c
fx = (- (x*x) / 3) + x*x + 3 * x + 4
dfx = sp.diff(fx, x)
dfxx = sp.diff(fx, x, 2)
c_val = sp.solve(dfx, x)
print("Exercise 2c:")
for i in c_val:
    if (i.is_real):
        if (dfxx.subs(x, i) > 0):
            print("f(x) has a local minimum at:", i)
            print("f(", i, ") =", fx.subs(x, i))
        if (dfxx.subs(x, i) < 0):
            print("f(x) has a local maximum at:", i)
            print("f(", i, ") =", fx.subs(x, i))
print("--------------")

#Ex 2d
fx = (5 * pow(x, 2) + 5) / x
dfx = sp.diff(fx, x)
dfxx = sp.diff(fx, x, 2)
c_val = sp.solve(dfx, x)
print("Exercise 2d:")
for i in c_val:
    if (i.is_real):
        if (dfxx.subs(x, i) > 0):
            print("f(x) has a local minimum at:", i)
            print("f(", i, ") =", fx.subs(x, i))
        if (dfxx.subs(x, i) < 0):
            print("f(x) has a local maximum at:", i)
            print("f(", i, ") =", fx.subs(x, i))
print("--------------")