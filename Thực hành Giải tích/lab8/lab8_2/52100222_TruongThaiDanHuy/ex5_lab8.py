import sympy as sp

x = sp.symbols('x')

def Golden_Search(fx, a, b, tol):
    d = b - a 
    while ((b - a) > tol):
        d = 0.618 * d 
        x1 = b - d
        x2 = a + d
        if (fx.subs(x, x1) <= fx.subs(x, x2)):
            b = x2
        else:
            a = x1
    fx1 = fx.subs(x, x1)
    fx2 = fx.subs(x, x2)
    return a, b, fx1, fx2

print("Exercise 5:")
fx = pow(x, 2)
(a, b, fx1, fx2) = Golden_Search(fx, -2, 1, 0.3)
print("a =", a)
print("b =", b)
print("f(x1) =", fx1)
print("f(x2) =", fx2)
print("Minimum value of f(x):", (fx1 + fx2) / 2)