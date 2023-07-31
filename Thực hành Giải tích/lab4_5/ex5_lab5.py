import sympy as sp
x=sp.symbols('x')
dx = sp.symbols('dx')
#ex5_a
fx_a=4-x*x
df_a = ( fx_a.subs(x,-3 + dx) - fx_a.subs(x,-3))/dx
print (" By limit -Derivative of f(x) at x = -3:", sp.limit(df_a,dx,0))
df_a = ( fx_a.subs(x,0 + dx) - fx_a.subs(x,0))/dx
print (" By limit -Derivative of f(x) at x = 0: ", sp.limit(df_a,dx,0))
df_a = ( fx_a.subs(x,1 + dx) - fx_a.subs(x,1))/dx
print (" By limit -Derivative of f(x) at x = 1: ", sp.limit(df_a,dx,0),"\n")
 #ex5_b
fx_b = (x-1)**2
df_b = (fx_b.subs(x,-1+dx)-fx_b.subs(x,-1))/dx
print("By limit -Derivative of f(x) at x = -1: ",sp.limit(df_b,dx,0))
df_b = (fx_b.subs(x,0+dx)-fx_b.subs(x,0))/dx
print("By limit -Derivative of f(x) at x = 0: ",sp.limit(df_b,dx,0))
df_b = (fx_b.subs(x,2+dx)-fx_b.subs(x,2))/dx
print("By limit -Derivative of f(x) at x = 2: ",sp.limit(df_b,dx,0),'\n')
#ex5_c
fx_c = (1/(x**2))
df_c = (fx_c.subs(x,-1+dx)-fx_c.subs(x,-1))/dx
print("By limit -Derivative of f(x) at x = -1: ",sp.limit(df_c,dx,0))
df_c = (fx_c.subs(x,2+dx)-fx_c.subs(x,2))/dx
print("By limit -Derivative of f(x) at x = 2: ",sp.limit(df_c,dx,0))
df_c = (fx_c.subs(x,sp.sqrt(3)+dx)-fx_c.subs(x,sp.sqrt(3)))/dx
print("By limit -Derivative of f(x) at x = sqrt(3): ",sp.limit(df_c,dx,0),"\n")
#ex5_d
fx_d= (1-x)/(2*x)
df_d = (fx_d.subs(x,-1+dx)-fx_d.subs(x,-1))/dx
print("By limit -Derivative of f(x) at x = -1: ",sp.limit(df_d,dx,0))
df_d = (fx_d.subs(x,1+dx)-fx_d.subs(x,1))/dx
print("By limit -Derivative of f(x) at x = 1: ",sp.limit(df_d,dx,0))
df_d = (fx_d.subs(x,sp.sqrt(2)+dx)-fx_d.subs(x,sp.sqrt(2)))/dx
print("By limit -Derivative of f(x) at x = sqrt(2): ",sp.limit(df_d,dx,0),"\n")
