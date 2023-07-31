import math
import numpy as np
from sympy import*
x=symbols('x')
#cau 1_a
fx_1a = abs(x**2-x-7)
lim_fx1a= limit(fx_1a,x,3)
print ("Ex_1a. The limit of f(x) then x tends to 3 is :  "+str(lim_fx1a))
#cau 1_b
fx_1b = (abs(x-1))/(x**2-1)
lim_fx1b= limit(fx_1b,x,1)
print ("Ex_1b. The limit of f(x) then x tends to 1 is :  "+str(lim_fx1b))
#cau 1_c
fx_1c = pow(math.e,1/x)
lim_fx1c= limit(fx_1c,x,1)
print ("Ex_1c. The limit of f(x) then x tends to 1 is :  "+str(lim_fx1c))
#cau 1_d
fx_1d = (x**4 -16)/(x-2)
lim_fx1d= limit(fx_1d,x,2)
print ("Ex_1d. The limit of f(x) then x tends to 2 is :  "+str(lim_fx1d))
#cau 1_e
fx_1e = (x**3 - x**2 -5*x -3)/((x+1)**2)
lim_fx1e= limit(fx_1e,x,-1)
print ("Ex_1e. The limit of f(x) then x tends to 1 is :  "+str(lim_fx1e))
#cau 1_f
fx_1f = (x**2 -9)/(sqrt(x**2+7)-4)
lim_fx1f= limit(fx_1f,x,3)
print ("Ex_1f. The limit of f(x) then x tends to 3 is :  "+str(lim_fx1f))
#cau 1_g
fx_1g = (abs(x))/(sin(x))
lim_fx1g= limit(fx_1g,x,1)
print ("Ex_1g. The limit of f(x) then x tends to 1 is :  "+str(lim_fx1g))
#cau 1_h
fx_1h = (1-cos(x))/(x*sin(x))
lim_fx1h= limit(fx_1h,x,0)
print ("Ex_1h. The limit of f(x) then x tends to 0 is :  "+str(lim_fx1h))
#cau 1_i
fx_1i = (2*(x**2))/(3-3*cos(x))
lim_fx1i= limit(fx_1i,x,0)
print ("Ex_1i. The limit of f(x) then x tends to 0 is :  "+str(lim_fx1i))
#cau 1_j
fx_1j = ((3+x)/(-1+x))**x
lim_fx1j= limit(fx_1j,x,math.inf)
print ("Ex_1j The limit of f(x) then x tends to oo is :  "+str(lim_fx1j))
#cau 1_k
fx_1k = (1-(2/(3+x)))**x
lim_fx1k= limit(fx_1k,x,math.inf)
print ("Ex_1k. The limit of f(x) then x tends to oo is :  "+str(lim_fx1k))
#cau 1_l
fx_1l = (1/x)**(1/x)
lim_fx1l= limit(fx_1l,x,math.inf)
print ("Ex_1l. The limit of f(x) then x tends oo is :  "+str(lim_fx1l))
#cau 1_m
fx_1m = ((x**(-1/3))+((1+x)**(1/3)))/(-sqrt(x)+sqrt(1+x))
lim_fx1m= limit(fx_1m,x,math.inf)
print ("Ex_1m. The limit of f(x) then x tends oo is :  "+str(lim_fx1m))
#cau 1_n
fx_1n = factorial(x)/(x**x)
lim_fx1n= limit(fx_1n,x,math.inf)
print ("Ex_1n. The limit of f(x) then x tends to oo is :  "+str(lim_fx1n))