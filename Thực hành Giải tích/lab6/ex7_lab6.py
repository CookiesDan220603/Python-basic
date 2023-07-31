import math
import sympy as sp
import numpy as np
n = sp.symbols('n')
#Ex_7a
fn = 1 - pow(0.2,n)
f_a = []
for i in range (1,6,1):
	f_a.append(fn.subs(n,i))
print("Ex_7a :\n",f_a)
#Ex_7b
fn = 2*n /(n**2 + 1)
f_b =[]
for i in range (1,6,1):
	f_b.append(fn.subs(n,i))
print("Ex_7b :\n",f_b)
#Ex_7c
fn = pow(-1,n-1)/(5**n)
f_c = []
for i in range (1,6,1):
	f_c.append(fn.subs(n,i))
print("Ex_7c :\n",f_c)
#Ex_7d
fn = 1/sp.factorial(n+1)
f_d =[]
for i in range (1,6,1):
	f_d.append(fn.subs(n,i))
print("Ex_7d :\n",f_d)

#Ex_7e
a1 =[]
a1.append(1)
for i in range (1,5,1):
  	a1.append(a1[i-1]*5-3)
print("Ex_7e :\n",a1)

#Ex_7f
a2 =[]
a2.append(2) 
for i in range (1,5,1):
	a2.append(a2[i-1]/(a2[i-1]+1))
print("Ex_7f :\n",a2)
