import math 
import sympy as sp
x = sp.symbols('x')
def mac (t,fx,x):
	fc =0
	for i in range (0,t+1,1):
		fc = fc + (((sp.diff(fx,x,i)).subs(x,0))*(x**i))/sp.factorial(i)
	print(fc)
print("maclaurin of 1a :")
mac (6,sp.cos(x),x)
print("--------------------------------------------------")
print("maclaurin of 1b :")
mac (12,sp.exp(x),x)
print("--------------------------------------------------")
print("maclaurrin of 1c :")
mac (12,1/(1-x),x)
print("--------------------------------------------------")
print("maclaurin of 1d :")
mac (12,pow(sp.tan(x),-1),x)
print("--------------------------------------------------")
