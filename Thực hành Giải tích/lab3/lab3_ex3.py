import math
import numpy as np
from sympy import*
import matplotlib.pyplot as plt
x = symbols('x')
#Ex3.1
fx_3a = 1/(1+(2**(1/x)))
lim_fx_3a = limit(fx_3a,x,0)
lim_fx_3a_left = limit (fx_3a,x,0,'-')
lim_fx_3a_right = limit (fx_3a,x,0,'+')
print("Ex_3a - The limit of f(x) when x tends to 0: ",lim_fx_3a)
print("Ex_3a - The limit of f(x) when x tends to 0-: ",lim_fx_3a_left)
print("Ex_3a - The limit of f(x) when x tends to 0+: ",lim_fx_3a_right)
#Ex3.2
fx_3b = ((x**2)+x)/(sqrt((x**3)+(x**2)))
lim_fx_3b = limit(fx_3b,x,0)
lim_fx_3b_left = limit (fx_3b,x,0,'-')
lim_fx_3b_right = limit (fx_3b,x,0,'+')
print("Ex_3b - The limit of f(x) when x tends to 0: ",lim_fx_3b)
print("Ex_3b - The limit of f(x) when x tends to 0-: ",lim_fx_3b_left)
print("Ex_3b - The limit of f(x) when x tends to 0+: ",lim_fx_3b_right)