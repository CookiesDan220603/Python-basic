import sympy as sp 
import numpy as np
import math
x,y=sp.symbols("x,y")
a = 2
b = -1
f = 2*x + 3*y + 4
fx = sp.diff(f,x)
fy = sp.diff(f,y)
sf =  f.subs([(x,a),(y,b)])
sx =  fx.subs([(x,a),(y,b)])
sy =  fy.subs([(x,a),(y,b)])
z = sf + sx*(x-a) + sy*(y-b)
print(z)