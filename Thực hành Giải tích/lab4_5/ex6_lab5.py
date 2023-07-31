import sympy as sp
x=sp.symbols('x')
z = sp.symbols('z')
#ex6_a
fx_a = 1/(x+2)
df_a = (fx_a.subs(x,z)-fx_a.subs(x,x))/(z-x)
print (" By limit -Derivative of f(x)_a :", sp.limit(df_a,z,x),"\n")
#ex6_b
fx_b = x**2 - 3*x +4
df_b = (fx_b.subs(x,z)-fx_b.subs(x,x))/(z-x)
print (" By limit -Derivative of f(x)_b :", sp.limit(df_b,z,x),"\n")
#ex6_c
fx_c = x/(x-1)
df_c = (fx_c.subs(x,z)-fx_c.subs(x,x))/(z-x)
print (" By limit -Derivative of f(x)_c :", sp.limit(df_c,z,x),"\n")
#ex6_d
fx_d = 1/(x+2)
df_d = (fx_d.subs(x,z)-fx_d.subs(x,x))/(z-x)
print (" By limit -Derivative of f(x)_d :", sp.limit(df_d,z,x),"\n")