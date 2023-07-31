import math
import numpy as np
import sympy as sp

n = sp.symbols('n')
#Ex_5a
fn = (4*n**2 + 1)/(3*n**2 + 2)
lim_5a = sp.limit(fn,n,math.inf)
print("Limit of sequence 5a is :  {}".format(lim_5a))
#Ex_5b
fn = sp.sqrt(n**2 + 1)-n
lim_5b = sp.limit(fn,n,math.inf)
print("Limit of sequence 5b is :  {}".format(lim_5b))
#Ex_5c
fn = (sp.sqrt(2*n + sp.sqrt(n))-sp.sqrt(2*n + 1))
lim_5c = sp.limit(fn,n,math.inf)
print("Limit of sequence 5c is :  {}".format(lim_5c))
#Ex_5d
fn = (3*pow(5,n)-pow(2,n))/(pow(4,n)+pow(2.5,n))
lim_5d = sp.limit(fn,n,math.inf)
print("Limit of sequence 5d is :  {}".format(lim_5d))
#Ex_5e
fn = (n*sp.sin(sp.sqrt(n)))/(n**2 + n -1)
lim_5e = sp.limit(fn,n,math.inf)
print("Limit of sequence 5e is :  {}".format(lim_5e))




