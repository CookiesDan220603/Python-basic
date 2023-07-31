from sympy import*
x = symbols('x')
f = x**2
f1 = 2
f2 = 3
a = -2
b = 1
n = 2
while b-a>=0.3:
  d = b - a
  x1 = b - d*(f1/f2)
  x2 = a + d*(f1/f2)
  if f.subs(x,x1)<=f.subs(x,x2):
    b = x2
  else:
    a = x1
  n = n + 1
  f3 = f2 + f1
print([a,b])