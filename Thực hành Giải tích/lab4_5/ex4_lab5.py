import sympy as sp
# -2*x**2/3
x = sp.symbols('x')
fx = -2*(x**2)/3
f1= fx.subs(x,0)
f2 = fx.subs(x,0+x)
f= (f2-f1)/x
lim = sp.limit(f,x,0)
print("derivative of function is {}".format(lim))
