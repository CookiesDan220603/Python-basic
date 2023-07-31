import math
import numpy as np
import sympy as sp
def factorial(num):
	if num ==1: return 1
	return num*factorial(num-1)
n = sp.symbols('x')
def check(lim):
	if lim != math.inf:
		print("The sequence is converges at : ",lim)
	else:
		print("The sequence is diverges !")
#Ex_6a
fn = 1 - pow(0.2,n)
lim_6a = sp.limit(fn,n,math.inf)
print("Ex_6a ")
check(lim_6a)
#Ex_6b
fn = (n**3)/(n**3+1)
lim_6b = sp.limit(fn,n,math.inf)
print("Ex_6b")
check(lim_6b)

#Ex_6c
fn = (3 + 5*n**2)/(n+n**2)
lim_6c = sp.limit(fn,n,math.inf)
print("Ex_6c")
check(lim_6c)

#Ex_6d
fn = (n**3)/(n+1)
lim_6d = sp.limit(fn,n,math.inf)
print("Ex_6d :")
check(lim_6d)

#Ex_6e
fn = sp.exp(1/n)
lim_6e = sp.limit(fn,n,math.inf)
print("Ex_6e")
check(lim_6e)
#Ex_6f
fn = sp.sqrt((n+1)/(9*n+1))
lim_6f = sp.limit(fn,n,math.inf)
print("Ex_6f")
check(lim_6f)

#Ex_6g
fn_1 = (n)/(n+sp.sqrt(n))
fn_2 = -(n)/(n+sp.sqrt(n))
lim_6g_1 = sp.limit(fn_1,n,math.inf)
lim_6g_2 = sp.limit(fn_2,n,math.inf)
print("Ex_6g when n + 1 = 2k")
check(lim_6g_1)
print("Ex_6g when n + 1 = 2k+1")
check(lim_6g_2)

#Ex_6h
fn = sp.tan((2*n*sp.pi)/(1+8*n))
lim_6h = sp.limit(fn,n,math.inf)
print("Ex_6h")
check(lim_6h)
#Ex_6i
fn = (sp.factorial(2*n-1))/(sp.factorial(2*n+1))
lim_6i = sp.limit(fn,n,math.inf)
print("Ex_6i")
check(lim_6i)
#Ex_6j
fn = sp.log(2*n**2 + 1) - sp.log(n**2 + 1)
lim_6j = sp.limit(fn,n,math.inf)
print("Ex_6j")
check(lim_6j)


