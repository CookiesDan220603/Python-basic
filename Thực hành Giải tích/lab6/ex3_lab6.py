import math 
import sympy as sp
x = sp.symbols('x')
#Ex3a
fx = sp.cos(x)
taylor_poly = fx.series(x,sp.pi/3,6)
print("Taylor series of f(x) at x = pi/3 is:\n", taylor_poly)
print("--------------------------------------------------")
#Ex3b
fx = sp.log(x)
taylor_poly = fx.series(x, 2, 10)
print("Taylor series of f(x) at x = 2 is:", taylor_poly)
print("--------------------------------------------------")

#Ex3c
fx = sp.exp(x)
taylor_poly = fx.series(x, 3, 12)
print("Taylor series of f(x) at x = 3 is:", taylor_poly,"\n")

'''
def Tay (t,fx,x,k):
	fc =0
	for i in range (1,t+1,1):
		fc = fc + ((sp.diff(fx,x,i).subs(x,k))*((x-k)**i))/sp.factorial(i)
	print(fc)
	print("-------------------------------------------------------------")
print("Ex3a")
Tay (6,sp.cos(x),x,sp.pi/3)
print("Ex3b")
Tay(10,sp.log(x),x,2)
print("Ex3c")
Tay(12,sp.exp(x),x,3)
'''
