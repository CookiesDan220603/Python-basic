import sympy as sp
import numpy as np
x = sp.symbols('x')
print("Exe 2")
def E2(f):
  ct = []
  cd = []
  f1 = sp.diff(f,x,1)
  sol = sp.solve(f1,x)
  f2 = sp.diff(f,x,2)
  for i in sol:
   f3 = sp.lambdify(x, f2)(i)
   if f3 ==0:
    print("Day khong phai la cuc tri")
   if f3>0:
     ct.append(i)
   if f3<0:
     cd.append(i)
  return ct,cd
print("a)", E2(18*x**2-9))
print("b)", E2((x+2)/(2*x**2)))
print("c)", E2((-x**2/3)+x**2+3*x+4))
print("d)", E2((5*x**2+5)/x))