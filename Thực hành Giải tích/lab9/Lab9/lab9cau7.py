import sympy as sp

t = sp.symbols('t')

#Ex7a
h = sp.sqrt(t + 1) + 5 * pow(t, 1/3)
print("Exercise 7a:")
print("Tree's height when t = 0:", h.subs(t, 0).evalf(), "ft")
print("Tree's height when t = 4:", h.subs(t, 4).evalf(), "ft")
print("Tree's height when t = 8:", h.subs(t, 8).evalf(), "ft")
print("---------")

#Ex7b
avg = (1 / 8) * sp.integrate(h, (t, 0, 8))
print("Exercise 7b:")
print("Tree's average height for 0 <= t <= 8:", avg.evalf(), "ft")
print("---------")
