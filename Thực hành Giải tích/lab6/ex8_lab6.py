import math 
import sympy as sp
x = sp.symbols('x')
k = [0,1,2,3]
def series(fx,a):
	for i in range (0,4):
		taylor_poly = fx.series(x,a,i)
		print("Taylor series of f(x) at x = ",a," and order is ",i," is:\n", taylor_poly)
		print("************************")
#a
fx = sp.exp(x)
a =0
print("Ex:8_a")
series(fx,a)
print("--------------------------------------------------")
#b
fx = sp.sin(x)
a =0
print("Ex:8_b")
series(fx,a)
print("--------------------------------------------------")
#c
fx = sp.log(x)
a =1
print("Ex:8_c")
series(fx,a)
print("--------------------------------------------------")
#d
fx = 1/x
a =2
print("Ex:8_d")
series(fx,a)