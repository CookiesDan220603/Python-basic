import sympy as sp 
x = sp.symbols('x')
dx = sp.symbols('dx')
#Ex10a x=1
fx = (x-1)**(1/3)
d_fx = (fx.subs(x, 1 + dx) - fx.subs(x, 1)) / dx
lim1 = sp.limit(d_fx, dx, 0, '+')
lim2 = sp.limit(d_fx, dx, 0, '-')
print("lim1 =", lim1)
print("lim2 =", lim2)
if (lim1 == lim2):
	print("Ham so f(x) kha vi tai 1")
else:
	print("Ham so f(x) khong kha vi tai 1")


#Ex10b

fx = - (x + 2)
fx_1 = x + 2
d_fx = (fx.subs(x, -2 + dx) - fx.subs(x, -2)) / dx
d_fx1 = (fx_1.subs(x, -2 + dx) - fx.subs(x, -2)) / dx
lim1 = sp.limit(d_fx1, dx, 0, '+')
lim2 = sp.limit(d_fx, dx, 0, '-')
print("lim1 =", lim1)
print("lim2 =", lim2)
if (lim1 == lim2):
	print("Ham so f(x) kha vi tai -2")
else:
	print("Ham so f(x) khong kha vi tai -2")

#Ex10c
fx = x*x 
fx_1 = 0 
d_fx = (fx.subs(x, 0 + dx) - fx.subs(x, 0)) / dx
d_fx1 = 0 / dx
lim1 = sp.limit(d_fx, dx, 0, '+')
lim2 = sp.limit(d_fx1, dx, 0, '-')
print("lim1 =", lim1)
print("lim2 =", lim2)
if (lim1 == lim2):
	print("Ham so f(x) kha vi tai x = 0")
else:
	print("Ham so f(x) khong kha vi tai x = 0")